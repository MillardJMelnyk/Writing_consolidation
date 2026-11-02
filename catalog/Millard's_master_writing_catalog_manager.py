"""Catalog manager: run this to set up search and open the catalog, instead of opening Millard's_master_writing_catalog.html directly.

It serves the catalog folder on this computer, opens the catalog page in your browser, and does the search
fingerprinting and saving the page asks for while it sets up search. The window closes by itself once the page
is open and search is ready, unless there were errors.

Put this file in the same folder as Millard's_master_writing_catalog.html. Needs Python 3.9 or newer.
"""
import os, sys, json, base64, threading, time, webbrowser, subprocess, importlib, importlib.util, urllib.request, urllib.parse, socket
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = 8765
FILES = os.path.join(HERE, 'catalog_search_files')
SRC = 'https://raw.githubusercontent.com/MillardJMelnyk/Writing_consolidation/main/catalog/tools/search_build/'
NEEDED = ['model_quantized.onnx', 'tokenizer.json', 'projection.json']
PAGE = os.path.basename(os.path.abspath(__file__)).replace("_manager.py", ".html")  # page name = this script's name without "_manager"
INDEX = 'catalog_search_index.js'


ERRORS = []
SERVER = None


def say(msg):
    print(time.strftime('%H:%M:%S'), msg, flush=True)


def error(msg):
    ERRORS.append(msg); say('ERROR: ' + msg)


def ensure_packages():
    missing = [m for m in ('numpy', 'onnxruntime', 'tokenizers') if importlib.util.find_spec(m) is None]
    if missing:
        say('First run: installing Python parts the search needs (%s)…' % ', '.join(missing))
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', '--quiet'] + missing)
        importlib.invalidate_caches()


def ensure_files():
    os.makedirs(FILES, exist_ok=True)
    for f in NEEDED:
        dst = os.path.join(FILES, f)
        if not os.path.exists(dst):
            say('First run: downloading %s…' % f)
            tmp = dst + '.part'
            urllib.request.urlretrieve(SRC + f, tmp)
            os.replace(tmp, dst)


class Fingerprinter:
    """Same fingerprints as the page makes for queries: model output, mean pooling, unit length,
    projection to a smaller size, unit length again, times scale, rounded to whole numbers."""
    def __init__(self):
        import numpy as np, onnxruntime as ort
        from tokenizers import Tokenizer
        self.np = np
        self.tok = Tokenizer.from_file(os.path.join(FILES, 'tokenizer.json'))
        self.tok.no_padding(); self.tok.enable_truncation(max_length=256)
        opts = ort.SessionOptions(); opts.intra_op_num_threads = os.cpu_count() or 1
        self.sess = ort.InferenceSession(os.path.join(FILES, 'model_quantized.onnx'), opts)
        p = json.load(open(os.path.join(FILES, 'projection.json')))
        self.mean = np.array(p['mean'], np.float32); self.W = np.array(p['W'], np.float32)
        self.scale = float(p['scale'])
        self.lock = threading.Lock()

    def run(self, texts):
        np = self.np
        out = []
        with self.lock:
            for b in range(0, len(texts), 64):
                enc = [e.ids for e in self.tok.encode_batch(texts[b:b + 64])]
                L = max(len(e) for e in enc)
                ids = np.zeros((len(enc), L), np.int64); mask = np.zeros_like(ids)
                for i, e in enumerate(enc): ids[i, :len(e)] = e; mask[i, :len(e)] = 1
                h = self.sess.run(None, {'input_ids': ids, 'attention_mask': mask, 'token_type_ids': np.zeros_like(ids)})[0]
                m = mask[:, :, None].astype(np.float32)
                v = (h * m).sum(1) / m.sum(1)
                v /= np.linalg.norm(v, axis=1, keepdims=True)
                p = (v - self.mean) @ self.W
                p /= np.linalg.norm(p, axis=1, keepdims=True)
                out.append(np.clip(np.round(p * self.scale), -127, 127).astype(np.int8))
        return np.concatenate(out).tobytes()


FP = None


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=HERE, **k)

    def log_message(self, fmt, *args):
        pass

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def do_POST(self):
        global FP
        try:
            body = self.rfile.read(int(self.headers.get('Content-Length', 0)))
            if self.path == '/api/embed':
                if FP is None:
                    say('Search setup: loading the meaning model…'); FP = Fingerprinter()
                data = FP.run(json.loads(body)['texts'])
                self.send_response(200); self.send_header('Content-Type', 'application/octet-stream')
                self.send_header('Content-Length', str(len(data))); self.end_headers(); self.wfile.write(data)
            elif self.path == '/api/save':
                tmp = os.path.join(HERE, INDEX + '.part')
                with open(tmp, 'wb') as fh:
                    fh.write(b'window.CATALOG_SEARCH_INDEX="'); fh.write(base64.b64encode(body)); fh.write(b'";\n')
                os.replace(tmp, os.path.join(HERE, INDEX))
                say('Search setup finished: saved %s (%.0f MB).' % (INDEX, os.path.getsize(os.path.join(HERE, INDEX)) / 1e6))
                self.send_response(200); self.send_header('Content-Length', '0'); self.end_headers()
            elif self.path == '/api/done':
                self.send_response(200); self.send_header('Content-Length', '0'); self.end_headers()
                threading.Thread(target=finish, daemon=True).start()
            else:
                self.send_response(404); self.send_header('Content-Length', '0'); self.end_headers()
        except Exception as e:
            error(str(e))
            msg = str(e).encode('utf-8')
            self.send_response(500); self.send_header('Content-Length', str(len(msg))); self.end_headers(); self.wfile.write(msg)


def finish():
    time.sleep(1.5)
    if ERRORS:
        say('The catalog is open, but there were errors (shown above). This window stays open so you can see them.')
        return
    say('Search is ready. This window will now close.')
    time.sleep(2)
    os._exit(0)


def port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0


def main():
    url = 'http://localhost:%d/%s' % (PORT, urllib.parse.quote(PAGE))
    if not os.path.exists(os.path.join(HERE, PAGE)):
        say("%s is not in this folder. This script must sit next to it, with the same name plus _manager." % PAGE); input('Press Enter to close.'); return
    if port_in_use(PORT):
        say('The catalog manager is already running. Opening the catalog…'); webbrowser.open(url); return
    try:
        ensure_packages(); ensure_files()
    except Exception as e:
        say('Could not get the search parts ready: %s' % e); input('Press Enter to close.'); return
    server = ThreadingHTTPServer(('127.0.0.1', PORT), Handler)
    say('Catalog manager running. Opening %s' % url)
    say('Leave this window open until the search index is built. It will close by itself.')
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

# Search index format

[← How to update the catalog](How_to_update_the_catalog.md)

`catalog_search_index.js` is created the first time the catalog is started with Millard's_master_writing_catalog_manager.py, and is saved next to Millard's_master_writing_catalog.html on your computer. Other programs can read it.

## File layout

The file is one line:

```
window.CATALOG_SEARCH_INDEX="<base64>";
```

To read it from another program: drop the text before the first `"` and from the last `"` onward, then base64-decode. The decoded bytes are:

| Bytes | Content |
|---|---|
| 0–3 | the letters `CSI1` |
| 4–7 | header length in bytes (unsigned 32-bit, little-endian) |
| 8 … | header: JSON text (UTF-8) |
| padded to a multiple of 8 | the data arrays, one after another, each starting on a multiple of 8 bytes |

The header lists every array under `arrays`: its `name`, `type` (Int8Array, Uint8Array, Uint16Array, Uint32Array, Float32Array — all little-endian), `offset` (from the start of the data section) and `length` (number of values).

## Header fields

- `items` — catalog item IDs, in order. Item number *n* below means `items[n]`; its page is `catalog/items/<id>.md`.
- `terms` — every distinct word (lowercase), sorted; used by the word index.
- `dim`, `scale` — fingerprint size and the multiplier used to store fingerprints as whole numbers.
- `model` — how fingerprints were made (see below).
- `text_source` — where the item text is read from.
- `created` — when the index was built.

## Text positions

All `start`/`end` values are character positions in the item's **plain text**, which is produced from the item page by the rules in `search_build/core.js` (`parseItem`): the text after the header block, with Markdown formatting removed, one paragraph per line.

## Arrays

| Name | One value per | Meaning |
|---|---|---|
| `proj` | — | 384 + 384×dim numbers: the mean vector, then the projection matrix (row-major) |
| `item_words` | item | word count |
| `sec_item`, `sec_start`, `sec_end` | passage / section | item number, text range |
| `par_sec`, `par_start`, `par_end`, `par_author` | paragraph | section number, text range, author (0 = Millard, 1 = Claude, 2 = someone else) |
| `sen_par`, `sen_start`, `sen_end`, `sen_words`, `sen_vec` | sentence | paragraph number, text range, word count, fingerprint (dim values each) |
| `phr_sen`, `phr_start`, `phr_end`, `phr_words`, `phr_w0`, `phr_vec` | phrase | sentence number, text range, word count, position of its first word in the sentence, fingerprint |
| `term_off` | term (+1) | where each term's entries start in `post_sen`/`post_pos` |
| `post_sen`, `post_pos` | word occurrence | sentence number, word position within the sentence |

Sentences of 12 words or fewer have no separate phrases; the sentence is its own phrase.

## Fingerprints

Model: all-MiniLM-L6-v2 (`search_build/model_quantized.onnx`, tokenizer `search_build/tokenizer.json`, max 256 tokens). For a piece of text:

1. Run the model; average the token outputs (mean pooling); scale to length 1.
2. Subtract the `proj` mean, multiply by the `proj` matrix (giving `dim` numbers), scale to length 1 again.
3. Multiply by `scale`, round, and limit to −127…127.

The similarity of two fingerprints is their dot product divided by `scale`².

# Running DeepSeek models locally

| | |
|---|---|
| Date | 2025-12-02 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-393` |
| Links | [Original](https://claude.ai/chat/496037c5-b008-467b-9ef1-ce6539fa11f4) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/393-2025-12-02-running-deepseek-models-locally.html) |

**Summary:** Confirms DeepSeek V3.2 models can be run locally, noting their 685-billion-parameter size and hardware requirements.

**Topics:** AI chatbots and working with Claude > Local LLMs and AI document search

**Index terms:** DeepSeek V3.2; Hugging Face; MIT License; local LLM; vLLM; GPU requirements

[← Catalog home](../Master_catalog.md)

---

### Millard · 2025-12-02 17:33

DeepSeek's new models be installed and run locally?

[File attached: Screenshot\_2025120211323717\_e307a3f9df9f380ebaf106e1dc980bb6.jpg — contents not included in export]

### Claude · 2025-12-02 17:34

I'll search for information about DeepSeek V3.2's local installation capabilities.

**Yes.** DeepSeek V3.2 and V3.2-Speciale can be installed and run locally.

**Key facts (as of December 1, 2025):**

* **Model availability**: Both models are released on Hugging Face under the MIT License with full model weights, training code, and documentation
* **Size**: Both are 685 billion parameters, approximately 690GB
* **Local deployment documentation**: The Hugging Face page directs users to the DeepSeek-V3.2-Exp repository for local deployment instructions
* **Deployment methods**: SGlang, vLLM, and native inference code are supported

**Hardware requirements** (based on similar DeepSeek models):

* Full model requires approximately 715GB disk space; quantized versions can reduce to 245GB (2-bit) or 170GB (1-bit dynamic)
* Recommended minimum 226GB combined RAM+VRAM for 2-bit quantized version

**Local setup process** involves:

1. Converting Hugging Face model weights to the required format
2. Launching via SGlang, vLLM, or native inference scripts

from langchain.llms import LlamaCpp

# Path to your locally downloaded Llama 3.2 1B model
MODEL_PATH = "/Users/divyarajput/.cache/lm-studio/models/hugging-quants/Llama-3.2-1B-Instruct-Q8_0-GGUF/llama-3.2-1b-instruct-q8_0.gguf"
#MODEL_PATH = "/Users/divyarajput/.cache/lm-studio/models/hugging-quants/Llama-3.2-1B-Instruct-Q8_0-GGUF"

# llm = LlamaCpp(
#     model_path=MODEL_PATH,
#     temperature=0.7,
#     max_tokens=512,
#     verbose=True
# )

# llm = LlamaCpp(
#         model_path=MODEL_PATH,
#         temperature=0.7,
#         max_tokens=512,
#         n_ctx=2048,
#         n_batch=512,
#         verbose=True,
#         stop=["###"]
# )


def initialize_llm():
    return LlamaCpp(
        model_path=MODEL_PATH,
        temperature=0.7,
        max_tokens=512,
        n_ctx=2048,
        n_batch=512,
        verbose=True,
        stop=["###"]
    )

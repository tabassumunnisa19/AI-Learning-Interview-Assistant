from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

_model = None
_tokenizer = None

def load_model():
    global _model, _tokenizer

    if _model is None or _tokenizer is None:
        model_name = "google/flan-t5-small"

        _tokenizer = AutoTokenizer.from_pretrained(model_name)
        _model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    return _model, _tokenizer

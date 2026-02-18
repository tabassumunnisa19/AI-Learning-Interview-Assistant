import torch

def generate_response(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=600,
            temperature=0.3
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

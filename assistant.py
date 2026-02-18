import torch

def generate_response(model, tokenizer, prompt):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    inputs = {key: value.to(device) for key, value in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=800,
            temperature=0.3,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return decoded_output

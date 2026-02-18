import torch

def generate_response(model, tokenizer, prompt):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    ).to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=600,
            do_sample=False,        # IMPORTANT for T5
            num_beams=4,            # better structured output
            early_stopping=True
        )

    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return decoded_output

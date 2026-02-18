import torch

def generate_response(model, tokenizer, prompt):

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=600,
            num_beams=4,
            do_sample=False,
            early_stopping=True
        )

    decoded_output = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return decoded_output

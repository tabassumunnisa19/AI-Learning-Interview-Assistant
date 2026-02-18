import torch

def generate_response(model, tokenizer, prompt):

    # Encode input (T5 max input length is 512)
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    # Generate output (deterministic for structured JSON)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=600,
            num_beams=4,          # improves structure
            do_sample=False,      # IMPORTANT for JSON stability
            early_stopping=True
        )

    # Decode output
    decoded_output = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return decoded_output

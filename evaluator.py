def extract_json(text):
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON found in model output")

    json_str = match.group()

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {e}")

    missing_keys = [key for key in REQUIRED_KEYS if key not in data]
    if missing_keys:
        raise ValueError(f"Missing keys in JSON: {missing_keys}")

    return data

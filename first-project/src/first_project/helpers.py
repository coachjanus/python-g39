def normalize(name: str):
    return name.strip().lower()

def get_field(field):
    """Gets non-empty field from user."""
    while True:
        result = input(f"Enter {field}: ")
        if result:
            return normalize(result)
        print(f"❌ {field.title()} cannot be empty.")

def get_optional_field(field):
    """Gets optional field from user."""
    result = input(f"Enter {field} (optional): ")
    return normalize(result) or None

def get_updated_field(field, current, optional=False):
    prompt = f"{field} [{current}]: "
    value = input(prompt).strip()
    if not value:
        return current
    normalized = normalize(value)
    return normalized if normalized else None if optional else normalized

def is_valid_row(row):
    required_fields = ["chicken_breed", "breed", "age", "birthday"]
    for field in required_fields:
        if field not in row or not row(field).strip():
            return False
    try:
        int(row["age"])
    except ValueError:
        return False
    return True

def transform_data(data):
    cleaned_data = []
    for row in data:
        if is_valid_row(row):
            cleaned_row = {
                "chicken": row["chicken"],
                "breed": row["breed"],
                "age": int(row["age"]),
                "birthday": row["birthday"]
            }
            cleaned_data.append(cleaned_row)
    return cleaned_data
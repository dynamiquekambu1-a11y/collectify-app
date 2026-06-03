def load_template(path, data):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    return content.format(**data)

from os import path


def open_file(file_path: str) -> str:

    if path.exists(file_path):
        with open(file_path, 'r') as text_file:
            text = text_file.read()
    else:
        raise FileNotFoundError("File not found.")

    return text

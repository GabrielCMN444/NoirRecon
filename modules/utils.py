import os


def create_output_folder():
    """Cria a pasta output se não existir"""
    if not os.path.exists("output"):
        os.mkdir("output")


def save_list(filename, data):
    """Salva uma lista em arquivo txt"""
    with open(filename, "w") as f:
        for item in data:
            f.write(item + "\n")

import json
from pathlib import Path


CONFIG_FILE = Path("config.json")


def load_config():
    if not CONFIG_FILE.exists():
        raise FileNotFoundError("config.json nu a fost găsit.")

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
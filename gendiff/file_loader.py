import json
import yaml
import os


def parse_content(content, ext):
    """Parse file content based on its extension"""
    if ext == '.json':
        return json.loads(content)
    elif ext in ['.yml', '.yaml']:
        return yaml.safe_load(content)
    else:
        raise ValueError("Unsupported file format")


def load_file(file_path):
    """Load and parse a file based on its extension"""
    _, ext = os.path.splitext(file_path)
    with open(file_path, 'r') as file:
        content = file.read()
        return parse_content(content, ext)

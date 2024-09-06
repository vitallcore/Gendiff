import json


def format_json(diff):
    """Formatting the output of the diff in JSON format."""
    return json.dumps(diff, indent=4)

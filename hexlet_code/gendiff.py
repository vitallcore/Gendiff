import json


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1, open(file_path2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    diff = []

    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))

    for key in all_keys:
        if key not in data2:
            diff.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1:
            diff.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] != data2[key]:
            diff.append(f"  - {key}: {format_value(data1[key])}")
            diff.append(f"  + {key}: {format_value(data2[key])}")
        else:
            diff.append(f"    {key}: {format_value(data1[key])}")

    return f"{{\n{'\n'.join(diff)}\n}}" if diff else "{}"

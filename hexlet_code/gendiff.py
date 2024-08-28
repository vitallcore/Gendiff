import json


def bool_to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1, open(file_path2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff = []

    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f"    {key}: {bool_to_str(data1[key])}")
            else:
                diff.append(f"  - {key}: {bool_to_str(data1[key])}")
                diff.append(f"  + {key}: {bool_to_str(data2[key])}")
        elif key in data1:
            diff.append(f"  - {key}: {bool_to_str(data1[key])}")
        else:
            diff.append(f"  + {key}: {bool_to_str(data2[key])}")

    return "{\n" + "\n".join(diff) + "\n}"

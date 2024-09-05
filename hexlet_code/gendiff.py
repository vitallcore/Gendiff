from hexlet_code.file_loader import load_file


# Getting the difference between two files
def build_diff(data1, data2):
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    diff = {}

    for key in all_keys:
        if key not in data2:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        elif key not in data1:
            diff[key] = {'status': 'added', 'value': data2[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'status': 'unchanged',
                'children': build_diff(data1[key], data2[key])
            }
        elif data1[key] != data2[key]:
            diff[key] = {
                'status': 'changed',
                'value_before': data1[key],
                'value_after': data2[key]
            }
        else:
            diff[key] = {'status': 'unchanged', 'value': data1[key]}

    return diff


# Helper function to process unchanged keys
def handle_unchanged(result, key, info, indent, depth):
    if 'children' in info:
        result.append(f"{indent}    {key}: {{")
        result.append(format_stylish(info['children'], depth + 1))
        result.append(f"{indent}    }}")
    else:
        result.append(f"{indent}    {key}: {format_value(info['value'])}")


# Formatting the output of the diff with formatter
def format_stylish(diff, depth=0):
    indent = '    ' * depth
    result = []

    for key, info in diff.items():
        if info['status'] == 'unchanged':
            handle_unchanged(result, key, info, indent, depth)
        elif info['status'] == 'added':
            result.append(f"{indent}  + {key}: {format_value(info['value'])}")
        elif info['status'] == 'removed':
            result.append(f"{indent}  - {key}: {format_value(info['value'])}")
        elif info['status'] == 'changed':
            result.append(
                f"{indent}  - {key}: {format_value(info['value_before'])}"
            )
            result.append(
                f"{indent}  + {key}: {format_value(info['value_after'])}"
            )

    return '\n'.join(result)


# Formatting the output of the diff
def format_value(value, depth=0):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        indent = '    ' * (depth + 1)
        lines = []
        for k, v in value.items():
            formatted_value = format_value(v, depth + 1)
            lines.append(f"{indent}{k}: {formatted_value}")
        return f"{{\n{'\n'.join(lines)}\n{'    ' * depth}}}"
    return str(value)


# Generating the diff between two files with the specified format
def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return f"{{\n{format_stylish(diff)}\n}}"
    else:
        raise ValueError(f"Unknown format: {format_name}")

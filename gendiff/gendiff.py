from gendiff.file_loader import load_file
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.json import format_json


def build_diff(data1, data2):
    """Getting the difference between two files"""
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    diff = {}

    for key in all_keys:
        if key not in data2:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        elif key not in data1:
            diff[key] = {'status': 'added', 'value': data2[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'status': 'nested',
                'children': build_diff(data1[key], data2[key])
            }
        elif data1[key] != data2[key]:
            diff[key] = {
                'status': 'updated',
                'value_before': data1[key],
                'value_after': data2[key]
            }
        else:
            diff[key] = {'status': 'unchanged', 'value': data1[key]}

    return diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Generating the diff between two files with the specified format"""
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return f"{{\n{format_stylish(diff)}\n}}"
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")

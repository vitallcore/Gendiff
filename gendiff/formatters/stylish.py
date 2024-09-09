def format_value(value, depth=0):
    """Formatting the output of the diff"""
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
        closing_indent = '    ' * depth
        return f"{{\n{'\n'.join(lines)}\n{closing_indent}}}"
    return str(value)


def handle_unchanged(result, key, info, indent, depth):
    """Helper function to process unchanged keys"""
    if 'children' in info:
        result.append(f"{indent}    {key}: {{")
        result.append(format_stylish(info['children'], depth + 1))
        result.append(f"{indent}    }}")
    else:
        result.append(
            f"{indent}    {key}: {format_value(info['value'], depth)}")


def handle_added(result, key, info, indent, depth):
    """Helper function to process added keys"""
    result.append(
        f"{indent}  + {key}: {format_value(info['value'], depth)}")


def handle_removed(result, key, info, indent, depth):
    """Helper function to process removed keys"""
    result.append(
        f"{indent}  - {key}: {format_value(info['value'], depth)}")


def handle_updated(result, key, info, indent, depth):
    """Helper function to process updated keys"""
    result.append(
        f"{indent}  - {key}: {format_value(info['value_before'], depth)}")
    result.append(
        f"{indent}  + {key}: {format_value(info['value_after'], depth)}")


def handle_nested(result, key, info, indent, depth):
    """Helper function to process nested nodes (children)"""
    result.append(f"{indent}    {key}: {{")
    result.append(format_stylish(info['children'], depth + 1))
    result.append(f"{indent}    }}")


def format_stylish(diff, depth=0):
    """Formatting the output of the diff with stylish formatter"""
    indent = '    ' * depth
    result = []

    for key, info in diff.items():
        status_handlers = {
            'unchanged': handle_unchanged,
            'added': handle_added,
            'removed': handle_removed,
            'updated': handle_updated,
            'nested': handle_nested,
        }
        handler = status_handlers.get(info['status'])
        if handler:
            handler(result, key, info, indent, depth)

    # Ensure no extra newlines are added
    return '\n'.join(result)

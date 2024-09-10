def format_value(value):
    """Formatting the output of the diff"""
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def format_plain(diff, parent=''):
    """Formatting the output of the diff with plain formatter"""
    result = []

    for key, info in diff.items():
        path = f"{parent}.{key}" if parent else key
        status = info.get('status')

        if status == 'added':
            value = format_value(info['value'])
            result.append(f"Property '{path}' was added with value: {value}")

        elif status == 'removed':
            result.append(f"Property '{path}' was removed")

        elif status == 'updated':
            old_value = format_value(info['value_before'])
            new_value = format_value(info['value_after'])
            result.append(
                f"Property '{path}' was updated. "
                f"From {old_value} to {new_value}"
            )

        elif status == 'nested_unchanged':
            nested_lines = format_plain(info['children'], path)
            result.append(nested_lines)

        elif status == 'unchanged':
            continue

        else:
            raise ValueError("Invalid value")

    return '\n'.join(result)

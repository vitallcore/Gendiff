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


def handle_added_plain(result, path, info):
    """Helper function to process added keys"""
    value = format_value(info['value'])
    result.append(f"Property '{path}' was added with value: {value}")


def handle_removed_plain(result, path, info):
    """Helper function to process removed keys"""
    result.append(f"Property '{path}' was removed")


def handle_updated_plain(result, path, info):
    """Helper function to process updated keys"""
    old_value = format_value(info['value_before'])
    new_value = format_value(info['value_after'])
    result.append(
        f"Property '{path}' was updated. From {old_value} to {new_value}"
    )


def handle_nested_plain(result, path, info):
    """Helper function to process nested unchanged keys"""
    nested_lines = format_plain(info['children'], path)
    result.append(nested_lines)


STATUS_HANDLERS_PLAIN = {
    'added': handle_added_plain,
    'removed': handle_removed_plain,
    'updated': handle_updated_plain,
    'nested': handle_nested_plain,
    'unchanged': lambda *args: None
}


def format_plain(diff, parent=''):
    """Formatting the output of the diff with plain formatter"""
    result = []

    for key, info in diff.items():
        path = f"{parent}.{key}" if parent else key
        status = info.get('status')

        handler = STATUS_HANDLERS_PLAIN.get(status)
        if handler:
            handler(result, path, info)
        else:
            raise ValueError("Invalid value")

    return '\n'.join(result)

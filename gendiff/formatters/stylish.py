def calculate_indent(depth, indent_size, left_offset=0, special_symbol=''):
    """
    Вычисляет отступ на основе глубины и смещения влево.

    :param depth: Глубина текущего уровня
    :param indent_size: Количество пробелов на один уровень глубины
    :param left_offset: Смещение влево (включая специальный символ)
    :param special_symbol: Символ, который используется для смещения влево
    :return: Строка, содержащая отступ
    """
    # Общий отступ — это глубина * количество отступов
    base_indent = ' ' * (depth * indent_size)

    # Смещение влево включает специальный символ и пробел после него
    left_shift = special_symbol + ' ' if left_offset > 0 else ''

    # Убираем отступ на смещение влево
    final_indent = base_indent[left_offset:] + left_shift
    return final_indent


def format_value(value, depth=0):
    """Formatting the output of the diff"""
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        indent = calculate_indent(depth + 1, 4)
        lines = []
        for k, v in value.items():
            formatted_value = format_value(v, depth + 1)
            lines.append(f"{indent}{k}: {formatted_value}")
        return f"{{\n{'\n'.join(lines)}\n{calculate_indent(depth, 4)}}}"
    return str(value)


def handle_unchanged(result, key, info, depth):
    """Helper function to process unchanged keys"""
    indent = calculate_indent(depth, 4)
    if 'children' in info:
        result.append(f"{indent}    {key}: {{")
        result.append(format_stylish(info['children'], depth + 1))
        result.append(f"{indent}    }}")
    else:
        result.append(f"{indent}    {key}: {format_value(info['value'])}")


def format_stylish(diff, depth=0):
    """Formatting the output of the diff with stylish formatter"""
    result = []

    for key, info in diff.items():
        if info['status'] == 'unchanged':
            handle_unchanged(result, key, info, depth)
        elif info['status'] == 'added':
            indent = calculate_indent(depth, 4, left_offset=2, special_symbol='+')
            result.append(f"{indent}{key}: {format_value(info['value'])}")
        elif info['status'] == 'removed':
            indent = calculate_indent(depth, 4, left_offset=2, special_symbol='-')
            result.append(f"{indent}{key}: {format_value(info['value'])}")
        elif info['status'] == 'updated':
            indent_removed = calculate_indent(depth, 4, left_offset=2, special_symbol='-')
            indent_added = calculate_indent(depth, 4, left_offset=2, special_symbol='+')
            result.append(f"{indent_removed}{key}: {format_value(info['value_before'])}")
            result.append(f"{indent_added}{key}: {format_value(info['value_after'])}")

    return '\n'.join(result)

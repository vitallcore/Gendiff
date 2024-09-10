import pytest
from gendiff.gendiff import generate_diff
import difflib


def load_expected(file_name):
    with open(f'tests/fixtures/{file_name}', 'r') as file:
        return file.read().strip()


@pytest.mark.parametrize(
    "file1, file2, format, expected_file",
    [
        ('file3.json', 'file4.json', 'stylish', 'result_generate_diff_stylish_2.txt'),
        ('file3.json', 'file3.json', 'stylish', 'result_identical_files_stylish.txt'),
        ('empty.json', 'file3.json', 'stylish', 'result_one_empty_file_stylish.txt'),
        ('empty.json', 'empty.json', 'stylish', 'result_both_empty_files_stylish.txt'),
        ('file1.json', 'file2.json', 'plain', 'result_generate_diff_plain.txt'),
        ('file4.json', 'file4.json', 'plain', 'result_identical_files_plain.txt'),
        ('file1.json', 'empty.json', 'plain', 'result_one_file_empty_plain.txt'),
        ('empty.json', 'empty.json', 'plain', 'result_both_files_empty_plain.txt'),
        ('file1.json', 'file4.json', 'json', 'result_different_files_json.txt'),
        ('empty.json', 'file4.json', 'json', 'result_one_empty_file_json.txt'),
    ]
)
def test_generate_diff(file1, file2, format, expected_file):
    file1_path = f'tests/fixtures/{file1}'
    file2_path = f'tests/fixtures/{file2}'
    expected = load_expected(expected_file).strip()
    actual = generate_diff(file1_path, file2_path, format).strip()

    if not expected and actual:
        assert actual == "", f"Expected an empty result but got:\n{actual}"
    elif expected and not actual:
        assert expected == "", f"Expected:\n{expected}\n\nActual result is empty"
    else:
        assert expected == actual, f"Expected:\n{expected}\n\nActual:\n{actual}"

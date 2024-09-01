import pytest
from hexlet_code.gendiff import generate_diff


@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.yml'


def test_generate_diff(file1_path, file2_path):
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(file1_path, file2_path) == expected


def test_identical_files(file1_path):
    expected = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    assert generate_diff(file1_path, file1_path) == expected


def test_different_files():
    file3_path = 'tests/fixtures/file3.yml'
    file4_path = 'tests/fixtures/file4.yml'
    expected = """{
  - key1: value1
  + key1: value2
  - key2: value3
  + key3: value4
}"""
    assert generate_diff(file3_path, file4_path) == expected


def test_one_empty_file():
    file_empty_path = 'tests/fixtures/empty.yml'
    file_full_path = 'tests/fixtures/file1.yml'
    expected = """{
  + follow: false
  + host: hexlet.io
  + proxy: 123.234.53.22
  + timeout: 50
}"""
    assert generate_diff(file_empty_path, file_full_path) == expected


def test_both_empty_files():
    file_empty_path = 'tests/fixtures/empty.yml'
    expected = """{}"""
    assert generate_diff(file_empty_path, file_empty_path) == expected

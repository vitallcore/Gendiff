import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def file3_path():
    return 'tests/fixtures/file3.json'


@pytest.fixture
def file4_path():
    return 'tests/fixtures/file4.json'


def test_generate_diff_stylish(file1_path, file2_path):
    expected = """    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
    key5: value5
}
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
    key: value
}
      + nest: str
    }
  - group2: {
    abc: 12345
    deep: {
        id: 45
    }
}
  + group3: {
    deep: {
        id: {
            number: 45
        }
    }
    fee: 100500
}"""
    assert generate_diff(file1_path, file2_path) == expected


def test_generate_diff(file3_path, file4_path):
    expected = """  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true"""
    assert generate_diff(file3_path, file4_path) == expected


def test_identical_files(file3_path):
    expected = """    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50"""
    assert generate_diff(file3_path, file3_path) == expected


def test_different_files():
    file5_path = 'tests/fixtures/file5.json'
    file6_path = 'tests/fixtures/file6.json'
    expected = """  - key1: value1
  + key1: value2
  - key2: value3
  + key3: value4"""
    assert generate_diff(file5_path, file6_path) == expected


def test_one_empty_file():
    file_empty_path = 'tests/fixtures/empty.json'
    file_full_path = 'tests/fixtures/file3.json'
    expected = """  + follow: false
  + host: hexlet.io
  + proxy: 123.234.53.22
  + timeout: 50"""
    assert generate_diff(file_empty_path, file_full_path) == expected


def test_both_empty_files():
    file_empty_path = 'tests/fixtures/empty.json'
    expected = """"""
    assert generate_diff(file_empty_path, file_empty_path) == expected


def test_generate_diff_plain(file1_path, file2_path):
    expected = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    assert generate_diff(file1_path, file2_path, 'plain') == expected


def test_identical_files_plain():
    first_file_path = 'tests/fixtures/file6.json'
    second_file_path = 'tests/fixtures/file6.json'
    expected = """"""
    assert generate_diff(first_file_path, second_file_path, 'plain') == expected


def test_one_file_empty_plain(file1_path, file2_path):
    file_empty_path = 'tests/fixtures/empty.json'
    expected = """Property 'common' was removed
Property 'group1' was removed
Property 'group2' was removed"""
    assert generate_diff(file1_path, file_empty_path, 'plain') == expected


def test_both_files_empty_plain():
    file_empty_path = 'tests/fixtures/empty.json'
    expected = """"""
    assert generate_diff(file_empty_path, file_empty_path, 'plain') == expected


def test_generate_diff_json():
    file5_path = 'tests/fixtures/file5.json'
    file6_path = 'tests/fixtures/file6.json'
    expected = """{
    "key1": {
        "status": "updated",
        "value_before": "value1",
        "value_after": "value2"
    },
    "key2": {
        "status": "removed",
        "value": "value3"
    },
    "key3": {
        "status": "added",
        "value": "value4"
    }
}"""
    assert generate_diff(file5_path, file6_path, 'json') == expected


def test_different_files_json():
    file1_path = 'tests/fixtures/file1.json'
    file5_path = 'tests/fixtures/file5.json'
    expected = """{
    "common": {
        "status": "removed",
        "value": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": true,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        }
    },
    "group1": {
        "status": "removed",
        "value": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        }
    },
    "group2": {
        "status": "removed",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    "key1": {
        "status": "added",
        "value": "value1"
    },
    "key2": {
        "status": "added",
        "value": "value3"
    }
}"""
    assert generate_diff(file1_path, file5_path, 'json') == expected


def test_one_empy_file_json():
    file_empty_path = 'tests/fixtures/empty.json'
    file5_path = 'tests/fixtures/file5.json'
    expected = """{
    "key1": {
        "status": "added",
        "value": "value1"
    },
    "key2": {
        "status": "added",
        "value": "value3"
    }
}"""
    assert generate_diff(file_empty_path, file5_path, 'json') == expected

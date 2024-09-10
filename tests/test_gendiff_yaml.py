import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.yml'


@pytest.fixture
def file3_path():
    return 'tests/fixtures/file3.yml'


@pytest.fixture
def file4_path():
    return 'tests/fixtures/file4.yml'


def test_generate_diff_stylish(file1_path, file2_path):
    expected = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: {
        key: value
    }
      + setting4: blah blah
      + setting5: {
        key5: value5
    }
        setting6: {
            doge: {
              - wow: too much
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
}
    group4: {
      - default: null
      + default: 
      - foo: 0
      + foo: null
      - isNested: false
      + isNested: none
      + key: false
        nest: {
          - bar: 
          + bar: 0
          - isNested: true
        }
      + someKey: true
      - type: bas
      + type: bar
    }
}"""
    assert generate_diff(file1_path, file2_path) == expected


def test_generate_diff(file3_path, file4_path):
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(file3_path, file4_path) == expected


def test_identical_files(file3_path):
    expected = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    assert generate_diff(file3_path, file3_path) == expected


def test_one_empty_file(file3_path):
    file_empty_path = 'tests/fixtures/empty.yml'
    expected = """{
  + follow: false
  + host: hexlet.io
  + proxy: 123.234.53.22
  + timeout: 50
}"""
    assert generate_diff(file_empty_path, file3_path) == expected


def test_both_empty_files():
    file_empty_path = 'tests/fixtures/empty.yml'
    expected = """{

}"""
    assert generate_diff(file_empty_path, file_empty_path) == expected


def test_generate_diff_plain(file1_path, file2_path):
    expected = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to [complex value]
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From 'too much' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
Property 'group4.default' was updated. From null to ''
Property 'group4.foo' was updated. From 0 to null
Property 'group4.isNested' was updated. From false to 'none'
Property 'group4.key' was added with value: false
Property 'group4.nest.bar' was updated. From '' to 0
Property 'group4.nest.isNested' was removed
Property 'group4.someKey' was added with value: true
Property 'group4.type' was updated. From 'bas' to 'bar'"""
    assert generate_diff(file1_path, file2_path, 'plain') == expected


def test_identical_files_plain(file4_path):
    expected = """"""
    assert generate_diff(file4_path, file4_path, 'plain') == expected


def test_one_file_empty_plain(file1_path):
    file_empty_path = 'tests/fixtures/empty.yml'
    expected = """Property 'common' was removed
Property 'group1' was removed
Property 'group2' was removed
Property 'group4' was removed"""
    assert generate_diff(file1_path, file_empty_path, 'plain') == expected


def test_both_files_empty_plain():
    file_empty_path = 'tests/fixtures/empty.yml'
    expected = """"""
    assert generate_diff(file_empty_path, file_empty_path, 'plain') == expected


from string_calculator import add

def test_add_one_number():
    assert add("1") == 1

def test_add_two_numbers():
    assert add("1,2") == 3

def test_empty_string():
    assert add("") == 0

def test_multiple_numbers():
    assert add("1,2,3,4") == 10

def test_new_line_as_delimiter():
    assert string_calculator.add('1\n2,3') == 6

def test_different_delimiters():
    assert string_calculator.add('//;\n1;2') == 3

def test_negative_numbers_exception():
    with pytest.raises(Exception, match = r'negatives not allowed \[-1, -2, -3\]'):
        string_calculator.add('-1, -2, -3, 1, 2, 3')

def test_delimiters_any_length():
    assert string_calculator.add('//[***]\n1***2***3') == 6

def test_multiple_delimiters():
    assert string_calculator.add('//[*][%]\n1*2%3') == 6

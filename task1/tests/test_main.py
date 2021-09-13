from task1 import main
import pytest


# Task 1.1
def test_for_calculate_string_length_positive():
    actual_result = main.string_length('rtryrtetg')
    assert actual_result == len('rtryrtetg')


def test_for_calculate_string_length_negative():
    with pytest.raises(ValueError):
        main.string_length(12345)


# Task 1.2
def test_character_frequency_positive():
    actual_result = main.count_character_frequency('Oh, it is python')
    assert actual_result == {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}


def test_character_frequency_negative():
    with pytest.raises(TypeError):
        main.count_character_frequency(type(1))


# Task 1.3
def test_set_of_unique_words():
    actual_result = main.unique_words(['red', 'white', 'black', 'red', 'green', 'black'])
    assert actual_result == ['black', 'green', 'red', 'white']


# Task 1.4
def test_divisors_of_number_positive():
    actual_result = main.divisors_of_number(60)
    assert actual_result == {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}


def test_divisors_of_number_negative():
    with pytest.raises(TypeError):
        main.count_character_frequency(type('Red'))


# Task 1.5
def test_sorted_dictionary_positive():
    actual_result = main.sorted_dictionary({2: 3, 1: 89, 4: 5, 3: '0', 7: 3, 5: 76, 9: '17', 6: 45, 8: [2, 3]})
    assert actual_result == {1: 89, 2: 3, 3: '0', 4: 5, 5: 76, 6: 45, 7: 3, 8: [2, 3], 9: '17'}


def test_sorted_dictionary_negative():
    with pytest.raises(TypeError):
        main.sorted_dictionary(type('Yellow'))


# Task 1.6
def test_unique_values_from_dict_positive():
    actual_res = main.unique_values([
        {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}])
    assert actual_res == {'S005', 'S002', 'S007', 'S001', 'S009'}


def test_unique_values_from_dict_negative():
    with pytest.raises(TypeError):
        main.sorted_dictionary(type('Blue'))


# Task 1.7
def test_from_tuple_into_integer_positive():
    actual_result = main.tuple_to_an_integer((1, 2, 3, 4))
    assert actual_result == 1234


def test_from_tuple_into_integer_negative():
    with pytest.raises(TypeError):
        main.tuple_to_an_integer(type('Green'))


# Task 1.8
def test_multiplication_table_positive():
    actual_result = main.multiplication_table(2, 4, 3, 7)
    assert actual_result == """\t 3	 4	 5	 6	 7
2	 6	 8	 10	 12	 14
3	 9	 12	 15	 18	 21
4	 12	 16	 20	 24	 28"""
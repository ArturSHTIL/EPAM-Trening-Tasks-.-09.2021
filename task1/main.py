# Task 1.1
def string_length(string: str) -> int:
    """
    Write a Python program to calculate the length of a string without using the `len` function.

    :param: string
    :return: 35
    """
    if isinstance(string, str):
        length = sum([1 for _ in string])
        return length
    else:
        raise ValueError


# Task 1.2
def count_character_frequency(string_for_dict: str) -> dict:
    """
    Write a Python program to count the number of characters (character frequency)
        in a string (ignore case of letters).

    :param string_for_dict: 'Oh, it is python'
    :return: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
    """
    if not isinstance(string_for_dict, str):
        raise TypeError
    else:
        string_for_dict = string_for_dict.lower()
        count_character_symbol = {i: string_for_dict.count(i) for i in string_for_dict}
        return count_character_symbol


# Task 1.3
def unique_words(words: list) -> list:
    """
    Write a Python program that accepts a comma separated sequence of words as input and
    prints the unique words in sorted form.

    :param words: ['red', 'white', 'black', 'red', 'green', 'black']
    :return: ['black', 'green', 'red', 'white']
    """
    set_unique_words = sorted(set(words))
    return set_unique_words


# Task 1.4
def divisors_of_number(number: int) -> set:
    """
    Create a program that asks the user for a number and then prints out a list of all the [divisors] of that number.

    :param number: 60
    :return: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
    """
    if not isinstance(number, int):
        raise TypeError

    else:
        divisors = {i for i in range(1, number + 1) if number % i == 0}
        return divisors


# Task 1.5
def sorted_dictionary(dictionary: dict) -> dict:
    """
    Write a Python program to sort a dictionary by key.

    :param dictionary: {2: 3, 1: 89, 4: 5, 3: '0', 7: 3}
    :return: {1: 89, 2: 3, 3: '0', 4: 5, 7: 3}
    """
    if not isinstance(dictionary, dict):
        raise TypeError
    else:
        return dict(sorted(dictionary.items()))


# Task 1.6
def unique_values(dictionary: list) -> set:
    """
    Write a Python program to print all unique values of all dictionaries in a list.

    :param dictionary: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                                        {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    :return: {'S005', 'S002', 'S007', 'S001', 'S009'}
    """
    if not isinstance(dictionary, list):
        raise TypeError
    else:
        unique_val = set([val for i in dictionary for key, val in i.items()])
        return unique_val


# Task 1.7
def tuple_to_an_integer(tuple_int: tuple) -> int:
    """
    Write a Python program to convert a given tuple of positive integers into an integer.

    :param tuple_int: (1, 2, 3, 4)
    :return: 1234
    """
    int_number = int(''.join(map(str, tuple_int)))
    return int_number


# Task 1.8
def multiplication_table(a: int, b: int, c: int, d: int):
    """
    # Write a program which makes a pretty print of a part of the multiplication table.

    :param a: 2
    :param b: 4
    :param c: 3
    :param d: 7
    :print:     3	4	5	6	7
            2	6	8	10	12	14
            3	9	12	15	18	21
            4	12	16	20	24	28
    """
    table_str = ""
    for i in range(c, d + 1):
        table_str += f"\t {i}"
    table_str += '\n'
    for j in range(a, b + 1):
        table_str += f"{j}"
        for k in range(c, d + 1):
            table_str += f"\t {j * k}"
        table_str += '\n'
    table_str = table_str.rstrip('\n')
    return table_str


if __name__ == '__main__':
    print(string_length('qwertycheckthelenwithoutlenfunction'))
    print(count_character_frequency('Oh, it is python'))
    print(unique_words(['red', 'white', 'black', 'red', 'green', 'black']))
    print(divisors_of_number(60))
    print(sorted_dictionary({2: 3, 1: 89, 4: 5, 3: '0', 7: 3, 5: 76, 9: '17', 6: 45, 8: [2, 3]}))
    print(unique_values([{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                         {"VIII": "S007"}]))
    print(tuple_to_an_integer((1, 2, 3, 4)))
    print(multiplication_table(2, 4, 3, 7))

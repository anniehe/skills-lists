"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """

    odd_list = [number for number in number_list if number % 2 != 0]

    # Alternative solution using for loops:

    # odd_list = []
    # for number in number_list:
    #     if number % 2 != 0:
    #         odd_list.append(number)

    return odd_list


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    even_list = [number for number in number_list if number % 2 == 0]

    # Alternative solution using for loops:

    # even_list = []
    # for number in number_list:
    #     if number % 2 == 0:
    #         even_list.append(number)

    return even_list


def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """

    for i in range(len(my_list)):
        print i, my_list[i]


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """

    long_words_list = [word for word in word_list if len(word) > 4]

    # Alternative solution using for loops:

    # long_words_list = []
    # for word in word_list:
    #     if len(word) > 4:
    #         long_words_list.append(word)

    return long_words_list


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """

    sorted_number_list = sorted(number_list)
    if number_list:
        return sorted_number_list[0]


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    sorted_number_list = sorted(number_list)
    if number_list:
        return sorted_number_list[-1]


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """

    halved_number_list = [number/2.0 for number in number_list]

    # Alternative solution using for loops:

    # halved_number_list = []
    # for number in number_list:
    #     halved_number = number/2.0
    #     halved_number_list.append(halved_number)

    return halved_number_list


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    word_lengths_list = [len(word) for word in word_list]

    # Alternative solution using for loops:

    # word_lengths_list = []
    # for word in word_list:
    #     word_length = len(word)
    #     word_lengths_list.append(word_length)

    return word_lengths_list


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """

    total = 0
    for number in number_list:
        total += number

    return total


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """

    result = 1
    for number in number_list:
        result *= number

    return result


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """

    joined_string = ""
    for word in word_list:
        for ch in word:
            joined_string += ch

    return joined_string


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    total = 0.0
    for number in number_list:
        total += number

    return total/len(number_list)


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """

    joined_string_with_commas = ""

    if len(list_of_words) > 1:
        for i in range(len(list_of_words)-1):
            joined_string_with_commas += list_of_words[i] + ", "
        joined_string_with_commas += list_of_words[-1]

    else:
        for word in list_of_words:
            joined_string_with_commas += word

    # Alternative solution:

    # joined_string_with_commas = ", ".join(list_of_words)

    return joined_string_with_commas


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print

import re

def valid_numbers(numbers):
    if numbers == '':
        return [0], []

    numbers = list(map(int, re.findall(r"-?\d+", numbers)))
    negative_numbers = list(filter(lambda x: x < 0, numbers))

    return numbers, negative_numbers


def add(numbers):

    numbers = valid_numbers(numbers)

    if numbers[1]:
        raise Exception('negatives not allowed ' + str(numbers[1]))

    elif numbers[0]:
        return (sum(numbers[0]))

def add_diff(numbers):
    numbers = valid_numbers(numbers)

    if numbers[1]:
        raise Exception('negatives not allowed ' + str(numbers[1]))

    elif numbers[0]:
        even_sum = 0
        odd_sum = 0

        for i, n in enumerate(numbers[0]):
            if i % 2 == 0:
                even_sum += n
            else:
                odd_sum += n

        return odd_sum - even_sum


# print(add(""))
# print(add("1,2"))
# print(add("1"))
# print(add("1,2,3,4"))
# print(add('1\n2,3'))
# print(add('//;\n1;2'))
# print(add('//[***]\n1***2***3'))
# print(add('//[*][%]\n1*2%3'))
# print(add('-1, -2, -3, 1, 2, 3'))

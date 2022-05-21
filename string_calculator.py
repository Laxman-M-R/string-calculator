import re

def add(numbers):
    if numbers == '':
        return 0

    numbers = list(map(int, re.findall(r"-?\d+", numbers)))
    negative_numbers = list(filter(lambda x: x < 0, numbers))


    if negative_numbers:
        raise Exception('negatives not allowed ' + str(negative_numbers))

    return (sum(numbers))


print(add(""))
print(add("1,2"))
print(add("1"))
print(add("1,2,3,4"))
print(add('1\n2,3'))
print(add('//;\n1;2'))
print(add('//[***]\n1***2***3'))
print(add('//[*][%]\n1*2%3'))
# print(add('-1, -2, -3, 1, 2, 3'))
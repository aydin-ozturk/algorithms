# Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(array):
    for i in array:
        if i % 2 != 0:
            array.remove(i)
            array.append(i)
    return array


""" Does this solution meet "solve it without allocating additional storage" requirement? """

print(even_first([7, 3, 5, 6, 4, 10, 3, 2]))
print(even_first([6, 0, 4, 2]))
print(even_first([3, 1, 5]))
print(even_first([5, 0, 0, 0, 0, 0]))
print(even_first([0, 0, 0, 0, 0, 5]))
print(even_first([5, 2]))
print(even_first([2, 5]))


# Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and
# updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def increment_number(array):
    increase = 1
    carry = 0
    for i in reversed(range(0, len(array))):
        array[i], carry = (increase + array[i] + carry) % 10, (increase + array[i] + carry) // 10
        increase = 0
    if carry > 0:
        return [carry] + array
    else:
        return array


print(increment_number([1, 1, 1]))
print(increment_number([1, 2, 9]))
print(increment_number([1, 9, 9]))
print(increment_number([9, 9, 9]))
print(increment_number([1, 9, 1, 9]))


def increment_number2(array):
    n = int("".join(str(i) for i in array))
    n += 1
    return [int(i) for i in str(n)]


print(increment_number2([1, 1, 1]))
print(increment_number2([1, 2, 9]))
print(increment_number2([1, 9, 9]))
print(increment_number2([9, 9, 9]))
print(increment_number([1, 9, 1, 9]))

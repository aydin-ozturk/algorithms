# Compute the sum of digits in all numbers from 1 to n. When a function gets a number n,
# find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
#
def sum_numbers(n:int):
    return int((1+n)/2*n)


print(sum_numbers(5))
#
#
# # Find max number from 3 values.
# # Example: 124, 21, 32. Result = 124.
#
def find_max(a:int, b:int, c:int):
    if a > b and a > c: return a
    if b > a and b > c: return b
    if c > b and c > a: return c


print(find_max(124, 21, 32))
#
#
# # Count odd and even numbers. Count odd and even digits of the whole number.
# # Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
#
def count_odd_even(n:int):
    odd = 0
    even = 0
    for i in str(n):
        if int(i) % 2 == 0:
            odd += 1
        else:
            even += 1
    return f"Number of odd digits: {odd} \nNumber of even digits: {even}"


print(count_odd_even(34560))
#Task 1
def max_multiplication(s):
    # Helper function to calculate the product of a list of numbers
    def product(numbers):
        result = 1
        for num in numbers:
            result *= num
        return result

    if not isinstance(s, str):
        return None

    max_product = 0
    max_sequence = None

    for i in range(len(s) - 3):

        chunk = s[i:i + 4]
        if chunk.isdigit():
            numbers = [int(digit) for digit in chunk]
            current_product = product(numbers)
            if current_product > max_product:
                max_product = current_product
                max_sequence = numbers

    if max_sequence is not None:
        return max_product
    else:
        return None

# Test cases
print(max_multiplication('abc12345def'))  # Output: 120 (2*3*4*5)
print(max_multiplication('a1b2c3d4e'))    # Output: None (No combinations found)

#Task 2
"""There is 2 functions counting ones in binary , 
first one is using defauly function in python library, 
second is just by taking reminder"""

def count_ones_in_binary(num):
    # Helper function to count the number of '1's in the binary representation of a number
    return bin(num).count('1')

def count_ones_manually_in_binary(num):
    # Helper function to count the number of '1's in the binary representation of a number
    count = 0
    while num > 0:
        if num % 2 == 1:
            count += 1
        num //= 2
    return count
def custom_sort(numbers):
    # Sort the numbers based on the number of '1's in their binary representation and then by decimal value
    return sorted(numbers, key=lambda x: (count_ones_manually_in_binary(x), x))

# Test case
print(custom_sort([3, 7, 8, 9]))  # Output: [8, 3, 9, 7] (1000, 11, 1001, 111)

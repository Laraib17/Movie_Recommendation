def check_sum_even(numbers):
    for i in numbers:
        if i % 2 != 0:
            return False
    return True
def sum_of_squares(numbers):
    return sum(i**2 for i in numbers)
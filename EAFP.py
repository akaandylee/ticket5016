# Exception1.py
#
# @ author: A. N. Other
# date: September 2016

def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Error, cannot divide by zero!"


print(divide_numbers(3, 0))
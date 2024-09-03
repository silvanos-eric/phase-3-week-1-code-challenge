def add_numbers(num1, num2):
  return num1 + num2

def is_even(number):
  return True if number % 2 == 0 else False

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

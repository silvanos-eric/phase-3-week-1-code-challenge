# Phase 3 Week 1 Code Challenge

## Table of Contents

- [Phase 3 Week 1 Code Challenge](#phase-3-week-1-code-challenge)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Modules](#modules)
    - [decorators.py](#decoratorspy)
    - [dicts.py](#dictspy)
    - [numbers.py](#numberspy)
    - [oop.py](#ooppy)
    - [sequences.py](#sequencespy)
    - [strings.py](#stringspy)
  - [License](#license)

## Project Overview

This project contains a collection of Python modules with various functions and classes demonstrating different programming concepts. The modules include decorators, dictionary operations, number manipulations, object-oriented programming, sequence handling, and string operations.

## Installation

To install the project dependencies, ensure you have Python 3.12 installed, and then use the `Pipfile` to set up the environment:

```bash
pipenv install
```

## Usage

To work within the virtual environment created by pipenv, you can use the following command to activate the shell:
```bash
pipenv shell
```

Import the relevant modules into your Python scripts to use the provided functions and classes. For example:

```python
from modules.strings import reverse_string, count_vowels
from modules.numbers import add_numbers
from modules.oop import Car

# Example usage
print(reverse_string("hello"))  # Output: "olleh"
print(count_vowels("hello"))    # Output: 2

car = Car("Toyota", "Corolla", 2021)
car.display_info()
```

## Modules

### decorators.py

Contains the `decorator_func` decorator which prints "Decorator Applied" before calling the decorated function.

### dicts.py

Includes the `merge_dicts` function which merges two dictionaries and sums the values of common keys.

### numbers.py

Provides functions for:
- `add_numbers(num1, num2)`: Adds two numbers.
- `is_even(number)`: Checks if a number is even.
- `calculate_factorial(n)`: Calculates the factorial of a non-negative integer.

### oop.py

Defines the `Car` class with:
- `make`, `model`, and `year` attributes.
- `display_info` method to print the car’s details.

### sequences.py

Includes the `sort_by_age(person_list)` function which sorts a list of tuples by age in ascending order.

### strings.py

Provides functions for:
- `reverse_string(text)`: Reverses the input string.
- `count_vowels(text)`: Counts the number of vowels in the input string.

## License

This project is licensed under the terms of the MIT License.

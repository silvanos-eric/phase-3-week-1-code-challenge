def reverse_string(text):
    return text[::-1]


def count_vowels(text):
    vowels = "aeiou"
    text = text.lower()
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

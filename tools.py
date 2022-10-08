import re


def count_the_number_of_spaces(text: str) -> int:
    return list(text).count(' ')

def count_the_number_of_special_symbols(text: str) -> int:
    return len(re.findall("[^a-zA-ZА-Яa-я0-9 ]", text))# Пробел в конце означает, что пробелы нам не нужны

def count_the_number_of_digits(text: str) -> int:
    return len(re.findall("[0-9]", text))

def count_the_number_of_latin_characters(text: str) -> int:
    return len(re.findall("[a-zA-Z]", text))

def count_the_number_of_curilic_characters(text: str) -> int:
    return len(re.findall("[а-яА-Я]", text))

def count_the_number_of_symbols(text: str) -> int:
    return len(list(text))

def count_the_number_of_symbols_without_spaces(text: str) -> int:
    return len(list(re.sub(" ", "", text.strip())))

def count_the_number_of_words(text: str) -> int:
    """Не совсем правильно работает"""
    return len(re.findall("\w+[^\d] ", text))


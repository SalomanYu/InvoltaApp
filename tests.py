import tools


def test_count_the_number_of_spaces():
    text1 = "Hello World by test module !"
    text2 = "    I    have   a   lot    of   spaces  "
    text3 = "I_don`t_have_spaces"

    assert tools.count_the_number_of_spaces(text1) == 5
    assert tools.count_the_number_of_spaces(text2) == 23
    assert tools.count_the_number_of_spaces(text3) == 0

def test_count_the_number_of_special_symbols():
    text1 = "21;Hello WOrld! &$"
    text2 = "Hello World, I have one special symbol"
    text3 = "Ho do you do, man?"

    assert tools.count_the_number_of_special_symbols(text1) == 4
    assert tools.count_the_number_of_special_symbols(text2) == 1
    assert tools.count_the_number_of_special_symbols(text3) == 2

def test_count_the_number_of_digits():
    text1 = "+7-978-670-68-90"
    text2 = "This text doesnt have digits!"
    text3 = "It`s 2022 now"

    assert tools.count_the_number_of_digits(text1) == 11
    assert tools.count_the_number_of_digits(text2) == 0
    assert tools.count_the_number_of_digits(text3) == 4

def test_count_the_number_of_latin_characters():
    text1 = "Hello, World!"
    text2 = "Меня зовут Ярослав"
    text3 = "Мой ник Rosya"

    assert tools.count_the_number_of_latin_characters(text1) == 10
    assert tools.count_the_number_of_latin_characters(text2) == 0
    assert tools.count_the_number_of_latin_characters(text3) == 5

def test_count_the_number_of_curilic_characters():
    text1 = "Hello, World!"
    text2 = "Меня зовут Ярослав"
    text3 = "Мой ник Rosya"

    assert tools.count_the_number_of_curilic_characters(text1) == 0
    assert tools.count_the_number_of_curilic_characters(text2) == 16
    assert tools.count_the_number_of_curilic_characters(text3) == 6

def test_count_the_number_of_symbols():
    text1 = ""
    text2 = "Просто ,"
    text3 = "Хелло, Много Text !: 21 4"

    assert tools.count_the_number_of_symbols(text1) == 0
    assert tools.count_the_number_of_symbols(text2) == 8
    assert tools.count_the_number_of_symbols(text3) == 25

def test_count_the_number_of_symbols_without_spaces():
    text1 = "             Сначала  пробуем  с про белами   Пото м   без н  и  х    "
    text2 = "СначалапробуемспробеламиПотомбезних"
    
    assert tools.count_the_number_of_symbols_without_spaces(text1) == tools.count_the_number_of_symbols_without_spaces(text2)
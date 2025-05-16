import pytest
from task1.solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def concat_strings(a: str, b: str) -> str:
    return a + b

@strict
def check_bool(value: bool) -> bool:
    return value

@strict
def float_mult(a: float, b: float) -> float:
    return a * b

# 1. Тест корректных аргументов
@pytest.mark.parametrize("func,args,expected", [
    (sum_two, (2, 3), 5),
    (concat_strings, ("hello", "world"), "helloworld"),
    (check_bool, (True,), True),
    (float_mult, (2.5, 2.0), 5.0),
])
def test_correct_arguments(func, args, expected):
    """Проверка работы с корректными типами аргументов"""
    assert func(*args) == expected

# 2. Тест неправильных типов аргументов
@pytest.mark.parametrize("func,args", [
    (sum_two, (1, "2")),
    (concat_strings, (1, "world")),
    (check_bool, (1,)),
    (float_mult, ("2.5", 2.0)),
])
def test_wrong_argument_types(func, args):
    """Проверка вызова TypeError при неверных типах аргументов"""
    with pytest.raises(TypeError):
        func(*args)

# 3. Тест возвращаемых значений
def test_return_types():
    """Проверка соответствия возвращаемых типов"""
    assert isinstance(sum_two(1, 2), int)
    assert isinstance(concat_strings("a", "b"), str)
    assert isinstance(check_bool(True), bool)
    assert isinstance(float_mult(1.0, 2.0), float)

# 4. Граничные случаи
@pytest.mark.parametrize("func,args,expected", [
    (concat_strings, ("", ""), ""),
    (sum_two, (0, 0), 0),
    (check_bool, (False,), False),
])
def test_edge_cases(func, args, expected):
    """Проверка граничных случаев"""
    assert func(*args) == expected

# 5. Проверка количества аргументов
def test_argument_count():
    """Проверка вызова TypeError при неверном количестве аргументов"""
    with pytest.raises(TypeError):
        sum_two(1)
    with pytest.raises(TypeError):
        concat_strings("single")
from solution import concat_strings, sum_two


def test_add_numbers_correct():
    result = sum_two(2, 3)
    assert result == 5, f"Expected 5, but got {result}"


def test_concat_strings_correct():
    result = concat_strings("hello", "world")
    assert result == "helloworld", f"Expected 'helloworld', but got {result}"

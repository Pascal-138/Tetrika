from functools import wraps


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        arg_types = list(annotations.values())[:-1]
        allowed_types = [bool, int, float, str]

        # Проверим, соответствует ли полученные типы параметров требуемым
        for type in arg_types:
            if type not in allowed_types:
                raise TypeError(
                    f"Тип аргумента {type.__name__} не допустим."
                )
        # Проверим, что нет значений параметров, заданных по умолчанию
        if len(arg_types) != len(args):
            raise TypeError(f"Ожидалось {len(args)} типов аргументов, "
                            f"но получено {len(arg_types)}.")

        for arg, expected_type in zip(args, arg_types):
            if not isinstance(arg, expected_type):
                raise TypeError(
                    f"Аргумент {arg} не соответствует "
                    f"типу {expected_type.__name__}."
                )

        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 2))    # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError

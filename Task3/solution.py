def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Функция объединяет пересекающиеся интервалы."""

    intervals.sort()
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def cross_intervals(intervals1: list[tuple[int, int]],
                    intervals2: list[tuple[int, int]]) -> list[
                        tuple[int, int]]:
    """Функция находит пересечения между двумя списками интервалов."""
    result = []
    i, j = 0, 0

    while i < len(intervals1) and j < len(intervals2):
        start1, end1 = intervals1[i]
        start2, end2 = intervals2[j]

        start = max(start1, start2)
        end = min(end1, end2)

        if start < end:
            result.append((start, end))

        if end1 < end2:
            i += 1
        else:
            j += 1

    return result


def full_time(intervals: list[tuple[int, int]]) -> int:
    """Функция считает суммарное время для списка интервалов."""
    summa = 0
    for start, end in intervals:
        summa += end - start
    return summa


def appearance(intervals: dict[str, list[int]]) -> int:
    """Функция считает общее время присутствия ученика и учителя на уроке."""
    lesson = [(intervals["lesson"][0], intervals["lesson"][1])]
    pupil = [(intervals["pupil"][i], intervals["pupil"][i + 1]) for i in range(
        0, len(intervals["pupil"]), 2)]
    tutor = [(intervals["tutor"][i], intervals["tutor"][i + 1]) for i in range(
        0, len(intervals["tutor"]), 2)]

    merged_pupil = merge_intervals(pupil)
    merged_tutor = merge_intervals(tutor)
    lesson_intersection = cross_intervals(lesson, merged_pupil)
    total_intersection = cross_intervals(lesson_intersection, merged_tutor)

    return full_time(total_intersection)


if __name__ == '__main__':
    tests = [
            {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                       1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
             'answer': 3117
             },
            {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                       1594704512, 1594704513, 1594704564, 1594705150,
                       1594704581, 1594704582, 1594704734, 1594705009,
                       1594705095, 1594705096, 1594705106, 1594706480,
                       1594705158, 1594705773, 1594705849, 1594706480,
                       1594706500, 1594706875, 1594706502, 1594706503,
                       1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
                       1594705149, 1594706463]},
             'answer': 3577
             },
            {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
             'answer': 3565
             },
    ]

    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got '
        f'{test_answer}, expected {test["answer"]}'
    print("Время общего присутствия ученика и учителя посчитано верно!")

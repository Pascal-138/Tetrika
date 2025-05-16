from task3.solution import cross_intervals, full_time, merge_intervals


def test_merge_intervals():
    intervals = [(1, 4), (2, 5), (7, 10)]
    result = merge_intervals(intervals)
    expected = [(1, 5), (7, 10)]
    assert result == expected, f"Ожидалось {expected}, но получено {result}"


def test_cross_intervals():
    intervals1 = [(1, 5), (6, 10)]
    intervals2 = [(4, 7), (8, 12)]
    result = cross_intervals(intervals1, intervals2)
    expected = [(4, 5), (6, 7), (8, 10)]
    assert result == expected, f"Ожидалось {expected}, но получено {result}"


def test_full_time():
    intervals = [(1, 3), (5, 7), (8, 10)]
    result = full_time(intervals)
    expected = 6
    assert result == expected, f"Ожидалось {expected}, но получено {result}"

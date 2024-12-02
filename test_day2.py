from day2 import read_reports, report_is_safe, report_is_safe_with_dampener


def test_read_reports():
    assert read_reports(["7 6 4 2 1", "1 2 7 8 9"]) == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
    ]


def test_report_is_safe():
    assert report_is_safe([7, 6, 4, 2, 1])
    assert not report_is_safe([1, 2, 7, 8, 9])
    assert not report_is_safe([9, 7, 6, 2, 1])
    assert not report_is_safe([1, 3, 2, 4, 5])
    assert not report_is_safe([8, 6, 4, 4, 1])
    assert report_is_safe([1, 3, 6, 7, 9])


def test_report_is_safe_with_dampener():
    assert report_is_safe_with_dampener([7, 6, 4, 2, 1])
    assert not report_is_safe_with_dampener([1, 2, 7, 8, 9])
    assert not report_is_safe_with_dampener([9, 7, 6, 2, 1])
    assert report_is_safe_with_dampener([1, 3, 2, 4, 5])
    assert report_is_safe_with_dampener([8, 6, 4, 4, 1])
    assert report_is_safe_with_dampener([1, 3, 6, 7, 9])

    # This one tripped me up on inspecting the diff
    assert not report_is_safe_with_dampener([37, 34, 37, 34, 31])

    # From reddit
    assert report_is_safe_with_dampener([9, 2, 3, 4, 5])
    assert report_is_safe_with_dampener([1, 9, 3, 4, 5])
    assert report_is_safe_with_dampener([1, 2, 9, 4, 5])
    assert report_is_safe_with_dampener([1, 2, 3, 9, 5])
    assert report_is_safe_with_dampener([1, 2, 3, 4, 9])

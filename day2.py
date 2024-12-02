from utils import read_lines_from_file
from itertools import pairwise


def read_reports(lines: list[str]) -> list[list[int]]:
    reports = []
    for line in lines:
        reports.append([int(char) for char in line.split()])
    return reports


def report_is_safe(report: list[int]) -> bool:
    """
    A report is safe if:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """

    ascending: bool | None = None
    for left, right in pairwise(report):
        # Hasn't been set yet
        if ascending is None:
            if left < right:
                ascending = True
            elif left > right:
                ascending = False
            else:
                # is equal
                return False

        # Breaks the first rule
        if (ascending and left > right) or (not ascending and right > left):
            return False

        # Breaks the second rule
        if abs(left - right) > 3 or abs(left - right) < 1:
            return False
    return True


def report_is_safe_with_dampener(report: list[int]) -> bool:
    """
    Now, the same rules apply as before, except if removing a single level
    from an unsafe report would make it safe, the report instead counts as safe.
    """
    if report_is_safe(report):
        return True

    i = 0
    while i < len(report):
        # TIL that python doesnt throw IndexError if slice start is outside of len
        if report_is_safe(report[:i] + report[i + 1 :]):
            return True
        i += 1

    return False


if __name__ == "__main__":
    lines = read_lines_from_file("day2.txt")
    reports = read_reports(lines)

    # Part 1
    part1 = list(filter(report_is_safe, reports))
    print(len(part1))

    # # Part 2
    part2 = list(filter(report_is_safe_with_dampener, reports))
    print(len(part2))

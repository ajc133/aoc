from utils import read_lines_from_string, read_lines_from_file

from day1 import calculate_distance, get_sorted_columns, calculate_similarity_score


def test_solve_part1() -> None:
    lines = read_lines_from_string("""3   4
        4   3
        2   5
        1   3
        3   9
        3   3""")
    column1, column2 = get_sorted_columns(lines)

    assert calculate_distance(column1, column2) == 11


def test_solve_part2() -> None:
    lines = read_lines_from_string("""3   4
        4   3
        2   5
        1   3
        3   9
        3   3""")
    column1, column2 = get_sorted_columns(lines)
    assert calculate_similarity_score(column1, column2) == 31

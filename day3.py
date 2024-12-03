import re
from utils import read_lines_from_file


def extract_instructions(line: str) -> list[tuple[int, int]]:
    pattern = re.compile(
        r"(?P<do>do\(\))|(?P<dont>don't\(\))|mul\((?P<left>\d+),(?P<right>\d+)\)"
    )
    result: list[tuple[int, int]] = []
    do_append = True
    for match in re.finditer(pattern, line):
        if match.group("dont"):
            do_append = False
            continue
        elif match.group("do"):
            do_append = True
            continue

        if do_append:
            left, right = int(match.group("left")), int(match.group("right"))
            result.append((left, right))
    return result


if __name__ == "__main__":
    lines = read_lines_from_file("day3.txt")
    total = 0
    for line in lines:
        for instruction in extract_instructions(line):
            total += instruction[0] * instruction[1]
    print("part 2:", total)

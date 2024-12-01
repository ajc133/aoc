from utils import read_lines_from_file


def get_sorted_columns(lines: list[str]) -> tuple[list[int], list[int]]:
    column1 = []
    column2 = []
    for line in lines:
        column1.append(int(line.split()[0]))
        column2.append(int(line.split()[1]))

    return (sorted(column1), sorted(column2))


def calculate_distance(sorted_column1: list[int], sorted_column2: list[int]) -> int:
    i = 0
    total = 0
    while i < len(sorted_column1):
        total += abs(sorted_column1[i] - sorted_column2[i])
        i += 1
    return total


def calculate_similarity_score(
    sorted_column1: list[int], sorted_column2: list[int]
) -> int:
    similarity_score = 0
    for digit in sorted_column1:
        similarity_score += digit * sorted_column2.count(digit)
    return similarity_score


def main() -> None:
    actual_input = read_lines_from_file("day1.txt")
    # part 1
    print(calculate_distance(*get_sorted_columns(actual_input)))

    # part 2
    print(calculate_similarity_score(*get_sorted_columns((actual_input))))


if __name__ == "__main__":
    main()

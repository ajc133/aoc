def read_lines_from_file(path: str) -> list[str]:
    with open(path) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def read_lines_from_string(s: str) -> list[str]:
    return [line.strip() for line in s.split("\n")]

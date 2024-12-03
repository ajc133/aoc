from day3 import extract_instructions


def test_extract_instructions():
    instructions = extract_instructions(
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    assert instructions == [(2, 4), (8, 5)]
    instructions = extract_instructions("mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 )")
    assert instructions == []

    instructions = extract_instructions("do()don't()do()mul(6,9)")
    assert instructions == [(6, 9)]
    instructions = extract_instructions("do()don't()do()don't()mul(6,9)")
    assert instructions == []
    assert extract_instructions("mul(1,1)") == [(1, 1)]
    instructions = extract_instructions("mul(2,5)don't()mul(2,5),do()mul(1,1)")
    assert instructions == [(2, 5), (1, 1)]

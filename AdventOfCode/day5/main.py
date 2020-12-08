"""--- Day 5: Binary Boarding ---"""
from utils.utils import get_data, clean_new_line_char


def change_code_str_to_binary(code: str, one: str, zero: str) -> bin:
    code = code.replace(one, '1')
    code = code.replace(zero, '0')
    return code


def count_position(code: str) -> int:
    """bin -> int"""
    return int(code, 2)


def count_seat_id(code: str) -> int:
    """seat_id = row_id * 8 + col_id
    code: string, 10 letter code: first 7 letters are B or F representing row position Back or Forward,
    last 3 letters are R or L representing column number Right or Left
    """
    return (
            count_position(change_code_str_to_binary(code[:7], one="B", zero="F")) * 8 +
            count_position(change_code_str_to_binary(code[7:], one="R", zero="L"))
            )


def check_maximum_seat_number(data: list) -> int:
    """Return maximum seat_id in a given seat code list"""
    max_id: int = 0
    for code in data:
        if count_seat_id(code) > max_id:
            max_id = count_seat_id(code)
    return max_id


def check_occupied_seats(data: list):
    return [count_seat_id(code) for code in data]


def find_your_seat(data: list) -> int:
    for i, seat_id in enumerate(s[:-1]):
        if s[i] + 1 != s[i + 1]:
            return s[i] + 1
    else:
        return -1


if __name__ == "__main__":
    path = r'C:\Users\Mateusz\Python\AdventOfCode\day5\day5_input.TXT'
    data = get_data(path)
    data = clean_new_line_char(data)
    print(check_maximum_seat_number(data))
    s = sorted(check_occupied_seats(data))
    print(find_your_seat(s))

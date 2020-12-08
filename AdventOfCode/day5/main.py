"""--- Day 5: Binary Boarding ---"""
from utils.utils import get_data, clean_new_line_char


def change_code_str_to_binary(code: str, one: str, zero: str) -> bin:
    code = code.replace(one, '1')
    code = code.replace(zero, '0')
    return code


def count_position(code: str) -> int:
    return int(code, 2)


def count_seat_id(code: str) -> int:
    return (
            count_position(change_code_str_to_binary(code[:7], one="B", zero="F")) * 8 +
            count_position(change_code_str_to_binary(code[7:], one="R", zero="L"))
            )


def check_maximum_seat_number(data: list):
    max_id: int = 0
    for code in data:
        if count_seat_id(code) > max_id:
            max_id = count_seat_id(code)
    return max_id


if __name__ == "__main__":
    path = r'C:\Users\Mateusz\Python\AdventOfCode\day5\day5_input.TXT'
    data = get_data(path)
    data = clean_new_line_char(data)
    print(check_maximum_seat_number(data))

"""--- Day 9: Encoding Error ---"""
from utils import utils


def is_valid_test(data_number: str, data) -> bool:
    for index, number in enumerate(data):
        for j in data[index + 1:]:
            print(f"number: {number} + {j} ?= {int(number) + int(j)} == {data_number}")
            if int(number) + int(j) == int(data_number):
                return True
    else:
        return False


def check_validity(data: str, shift: int):
    for index, number in enumerate(data[shift:]):
        check = is_valid_test(number, data[index:index + shift])
        print(check)
        if not(check):
            return number


if __name__ == "__main__":
    path = 'input.txt'
    data = utils.get_raw_data(path)
    data = data.split('\n')
    print(data)
    print(check_validity(data, 25))

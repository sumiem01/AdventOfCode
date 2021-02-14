"""--- Day 8: Handheld Halting ---"""
from utils import utils


def boot_instructions(starting_value: int, list_of_values: list):
    index = 0
    while True:
        if list_of_values[index][0] == "nop":
            list_of_values[index][2] += 1
            if list_of_values[index][2] > 1:
                return starting_value
            index += 1
        elif list_of_values[index][0] == "acc":
            list_of_values[index][2] += 1
            if list_of_values[index][2] > 1:
                return starting_value
            starting_value = eval(str(starting_value) + list_of_values[index][1])
            index += 1
        elif list_of_values[index][0] == "jmp":
            list_of_values[index][2] += 1
            if list_of_values[index][2] > 1:
                return starting_value
            index = eval(str(index) + list_of_values[index][1])
        else:
            return ValueError


def add_fixed_value_column(value: int, list_of_values: list) -> list:
    for index in list_of_values:
        index.append(value)
    return list_of_values


if __name__ == "__main__":
    path = "input.txt"
    data = utils.get_raw_data(path).split("\n")
    processed_data = [i.split() for i in data]
    processed_data = add_fixed_value_column(0, processed_data)
    print(boot_instructions(0, processed_data))

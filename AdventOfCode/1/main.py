from utils import utils
PATH = "input1.txt"


def clean_input(data: list) -> list:
    new_input: list = []
    for i in data:
        new_input.append(int(i.replace("\n", "")))
    return new_input


def count_two() -> list:
    new_input = clean_input(utils.get_data(PATH))
    numbers: list = []
    RANGE = len(new_input)
    for i in range(RANGE):
        for j in range(i, RANGE):
            if new_input[i] + new_input[j] == 2020:
                numbers.append(new_input[i] * new_input[j])
    return numbers


def count_three() -> list:
    new_input = clean_input(utils.get_data(PATH))
    numbers: list = []
    RANGE = len(new_input)
    for i in range(RANGE):
        for j in range(i, RANGE):
            for k in range(j, RANGE):
                if new_input[i] + new_input[j] + new_input[k] == 2020:
                    numbers.append(new_input[i] * new_input[j] * new_input[k])
    return numbers


print(count_two())
print(count_three())
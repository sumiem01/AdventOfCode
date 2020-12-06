from utils import utils
PATH = "input1.txt"


def count_two() -> list:
    new_input = utils.clean_input(utils.get_data(PATH))
    numbers: list = []
    RANGE = len(new_input)
    for i in range(RANGE):
        for j in range(i, RANGE):
            if new_input[i] + new_input[j] == 2020:
                numbers.append(new_input[i] * new_input[j])
    return numbers


def count_three() -> list:
    new_input = utils.clean_input(utils.get_data(PATH))
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
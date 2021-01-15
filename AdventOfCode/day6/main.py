from utils import utils
from typing import Callable


def count_group_yes_answers_anyone(answers: str) -> int:
    return len(set(list(answers.replace("\n", ""))))


def count_group_yes_answers_everyone(answers: str) -> int:
    answer_list = answers.split("\n")
    answer_intersection: set = set(list(answer_list[0]))
    for answer in answer_list[1:]:
        answer_intersection = answer_intersection.intersection(answer)
    return len(answer_intersection)


def count_all_groups_yes_answers(data: list, checking_function: Callable[[str], int]) -> int:
    sum: int = 0
    for answers in data:
        sum += checking_function(answers)
    return sum


if __name__ == "__main__":
    path: str = r"C:\Users\Mateusz\Python\AdventOfCode\day6\day6_input.TXT"
    data: str = utils.get_raw_data(path)
    data: list = data.split("\n\n")
    print(count_all_groups_yes_answers(data, count_group_yes_answers_anyone))
    print(count_all_groups_yes_answers(data, count_group_yes_answers_everyone))

"""
--- Day 7: Handy Haversacks ---
input: str, a text describing set of different rules for storing bags

light red bags contain 1 bright white bag, 2 muted yellow bags.

output: int, a number of bags that contain shiny bag (directly and indirectly)
"""
from utils import utils


def contains_shiny(parent_key: str) -> None:
    for bag_info in input_lines:
        if parent_key in bag_info[1]:
            bag_info[2] = True
            contains_shiny(bag_info[0])
        elif bag_info[1] == "no other bags.":
            continue


def count_list(data: list) -> int:
    s: int = 0
    for i in data:
        s += i[2]
    return s


def shiny_have(parent_key: str, counter: int):
    for bag_info in list_p2:
        if parent_key == bag_info[0]:
            for i in bag_info[1]:
                print(counter)
                shiny_have(i[1], counter * i[0])
        elif bag_info[1] == (0, "other"):
            continue


if __name__ == "__main__":
    PATH = "input_test_p2.txt"
    data = utils.get_raw_data(PATH)
    data_p2 = data.replace(" bags contain", ",")
    data_p2 = data_p2.replace(" bag,", ",")
    data_p2 = data_p2.replace(" bags,", ",")
    data_p2 = data_p2.replace(" bags.", "").replace(" bag.", "")
    data_p2 = data_p2.replace("no other", "0 other")
    input_lines_p2 = [i.split(", ") for i in data_p2.split("\n")]
    input_lines_p2.pop()  # to remove [] at the end of list

    list_p2 = []
    for i, j in enumerate(input_lines_p2):
        list_p2.append([j[0], [(int(k[0]), k[2:]) for k in j[1:]]])
    print(list_p2)

    # for i in list_p2:
    #     print(i)
    #     for j in i[1]:
    #         print(j)
    #         i[2] += int(j[0])
    # print(list_p2)

    input_lines = [i.split(" bags contain ") for i in data.split("\n")]
    input_lines.pop()
    input_lines = [[i[0], i[1], 0] for i in input_lines]

    # contains_shiny("shiny gold")
    # print(count_list(input_lines))

    print(shiny_have("shiny gold", 1))
    # print(count_list(list_p2))

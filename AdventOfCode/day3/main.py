from utils import utils
PATH = "input3.TXT"

data = utils.get_lines(PATH)
data = utils.clean_new_line_char(data)


def count_tree(data: list, down_slope: int, right_slope: int):
    """Each tree is represented as # sign in data"""
    no_rows = len(data)
    no_columns = len(data[0])
    counter: int = 0
    for i in range(no_rows):
        if i * down_slope >= no_rows:
            break
        # print(data[i * down_slope][(i * right_slope) % no_columns], i * down_slope, (i * right_slope) % no_columns)
        if data[i * down_slope][(i * right_slope) % no_columns] == "#":
            counter += 1

    return counter


if __name__ == "__main__":
    print(count_tree(data, 1, 1))
    print(count_tree(data, 1, 3))  # correct answer = 216
    print(count_tree(data, 1, 5))
    print(count_tree(data, 1, 7))
    print(count_tree(data, 2, 1))
    multiply = count_tree(data, 1, 1) * count_tree(data, 1, 3) * count_tree(data, 1, 5) * count_tree(data, 1, 7) * count_tree(data, 2, 1)
    print(multiply)

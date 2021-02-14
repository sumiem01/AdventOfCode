from day3.main import count_tree
from utils import utils


TEST_PATH = "input_test.TXT"

data = utils.get_lines(TEST_PATH)
data = utils.clean_new_line_char(data)

assert count_tree(data, 1, 1) == 2, "Wrong value"
assert count_tree(data, 1, 3) == 7, "Wrong value"
assert count_tree(data, 1, 5) == 3, "Wrong value"
assert count_tree(data, 1, 7) == 4, "Wrong value"
assert count_tree(data, 2, 1) == 2, "Wrong value"

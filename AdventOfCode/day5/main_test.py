from day5.main import *

test1 = 'BFFFBBFRRR'  # : row 70, column 7, seat ID 567.
test2 = 'FFFBBBFRRR'  # : row 14, column 7, seat ID 119.
test3 = 'BBFFBBFRLL'  # : row 102, column 4, seat ID 820.

assert count_position(change_code_str_to_binary(test1[:7], one="B", zero="F")) == 70
assert count_position(change_code_str_to_binary(test2[:7], one="B", zero="F")) == 14
assert count_position(change_code_str_to_binary(test3[:7], one="B", zero="F")) == 102

assert count_position(change_code_str_to_binary(test1[7:], one="R", zero="L")) == 7
assert count_position(change_code_str_to_binary(test2[7:], one="R", zero="L")) == 7
assert count_position(change_code_str_to_binary(test3[7:], one="R", zero="L")) == 4

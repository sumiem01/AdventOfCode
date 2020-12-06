from day4.main import *

test_path = "input4_test.TXT"
test_data = read_data(test_path).split("\n\n")

assert validate_passports(test_data) == 2, "Wrong number of valid passports"

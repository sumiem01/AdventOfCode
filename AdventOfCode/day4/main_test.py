from day4.main import *


valid_data = read_data("valid_test.TXT").split("\n\n")
invalid_data = read_data("invalid_test.TXT").split("\n\n")

assert validate_passports(valid_data, is_valid) == 4, "Wrong number of valid passports"
assert validate_passports(invalid_data, is_valid) == 0, "Wrong number of valid passports"
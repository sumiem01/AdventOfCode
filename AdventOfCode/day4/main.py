"""--- Day 4: Passport Processing ---
The automatic passport scanners are slow because they're having trouble detecting
which passports have all required fields.
The expected fields are as follows:
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
import re
PATH = "input4.TXT"


def read_data(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


data = read_data(PATH).split("\n\n")


def find_codes(passport: str) -> list:
    pattern = r"[a-z]{3,3}:"
    return re.findall(pattern, passport)


def is_valid(passport: str) -> bool:
    codes = find_codes(passport)
    if (len(codes) == 7) and ('cid:' not in codes):
        return True
    elif len(codes) == 8:
        return True
    else:
        return False


def validate_passports(data: list) -> int:
    counter: int = 0
    for passport in data:
        if is_valid(passport):
            counter += 1
    return counter


print(validate_passports(data))

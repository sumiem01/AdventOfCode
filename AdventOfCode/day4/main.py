"""--- Day 4: Passport Processing ---
The automatic passport scanners are slow because they're having trouble detecting
which passports have all required fields.
The expected fields are as follows:
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""
import re
from typing import Callable


def read_data(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def extract_codes(passport: str):
    return passport.replace("\n", " ").split()


def prepare_code_values(data: list):
    passports: list = []
    for passport in data:
        passports.append({p.split(":")[0]: p.split(":")[1] for p in extract_codes(passport)})
    return passports


def find_codes(passport: str) -> list:
    pattern = r"[a-z]{3,3}:"
    return re.findall(pattern, passport)


def is_valid_without_cid(passport: str) -> bool:
    codes = find_codes(passport)
    if (len(codes) == 7) and ("cid:" not in codes):
        return True
    elif len(codes) == 8:
        return True
    else:
        return False


def is_valid(passport: str) -> bool:
    pattern_byr = r"byr:19[2-9][0-9]|byr:200[0-2]"  # 1920 <= valid <= 2002
    pattern_iyr = r"iyr:201[0-9]|iyr:2020"  # 2010 <= valid <= 2020
    pattern_eyr = r"eyr:202[0-9]|eyr:2030"  # 2020 <= valid <= 2030
    pattern_hgt = r"hgt:1[5-8][0-9]cm|hgt:19[0-3]cm|hgt:59in|hgt:6[0-9]in|hgt:7[0-6]in"  # 150 < valid(cm) < 193 or 59 < valid(in) < 76
    pattern_hcl = r"hcl:#[0-9a-f]{6}"
    pattern_ecl = r"ecl:amb|ecl:blu|ecl:brn|ecl:gry|ecl:grn|ecl:hzl|ecl:oth"
    pattern_pid = r"pid:\d+"  # all 9 digits numbers
    if re.search(pattern_pid, passport):
        pid_cond = len(re.search(pattern_pid, passport)[0]) == 13  # 9 + len("pid:")
    else:
        pid_cond = False
    pattern_list: list = [pattern_byr, pattern_iyr, pattern_eyr, pattern_hgt, pattern_hcl, pattern_ecl]
    return all([bool(re.search(pattern, passport)) for pattern in pattern_list]) and pid_cond


def validate_passports(data: list, validate_function: Callable[[str], bool]) -> int:
    counter: int = 0
    for passport in data:
        if validate_function(passport):
            counter += 1
    return counter


if __name__ == "__main__":
    PATH = "input4.TXT"
    data = read_data(PATH).split("\n\n")
    print(validate_passports(data, is_valid))

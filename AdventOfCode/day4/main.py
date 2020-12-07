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
PATH = "input4.TXT"


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


def is_valid_byr(passport: dict) -> bool:
    return 1920 < int(passport.get('byr', 0)) < 2002


def is_valid_iyr(passport: dict) -> bool:
    return 2010 < int(passport.get('iyr', 0)) < 2020


def is_valid_eyr(passport: dict) -> bool:
    return 2020 < int(passport.get('eyr', 0)) < 2030


def is_valid_hgt(passport: dict) -> bool:
    if 'cm' in passport.get('hgt', '0'):
        return 150 < int(passport.get('hgt', '0').strip("cm")) < 193
    elif 'in' in passport.get('hgt', '0'):
        return 59 < int(passport.get('hgt', '0').strip("in")) < 76
    else:
        return False


def is_valid_hcl(passport: dict) -> bool:
    pattern = r"^#[1-9a-zA-Z]{6,6}"
    value = passport.get('hcl', '0')
    result = re.match(pattern, value)
    if bool(result) and len(value) == 7:
        return True
    else:
        return False


def is_valid_ecl(passport: dict) -> bool:
    return passport.get('ecl', 0) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_valid_pid(passport: dict) -> bool:
    return passport.get('pid', 0) == 9


def is_valid(passport: dict) -> bool:
    """
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
    function_tuple = (is_valid_byr,
                      is_valid_iyr,
                      is_valid_eyr,
                      is_valid_hgt,
                      is_valid_hcl,
                      is_valid_ecl,
                      is_valid_pid
                      )
    logic_list: list = []
    for fun in function_tuple:
        logic_list.append(fun(passport))
    return all(logic_list)


def validate_passports(data: list, validate_function) -> int:
    counter: int = 0
    for passport in data:
        if validate_function(passport):
            counter += 1
    return counter


data = read_data(PATH).split("\n\n")
print(validate_passports(prepare_code_values(data), is_valid))

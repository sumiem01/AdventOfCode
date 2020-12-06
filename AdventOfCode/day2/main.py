from utils import utils
PATH = "input2.TXT"

data = utils.get_data(PATH)


def extract_info_from_code(code: str) -> tuple:
    policy: str = code.split(":")[0]
    password: str = code.split(":")[1].strip()
    letter: str = policy.split(" ")[1]
    minimum: int = int(policy.split(" ")[0].split("-")[0])
    maximum: int = int(policy.split(" ")[0].split("-")[1])
    return  minimum, maximum, letter, password


def prepare_data(data: list) -> list:
    prep: list = []
    for item in data:
        prep.append(extract_info_from_code(item))
    return prep


def is_valid_old_policy(minimum: int, maximum: int, letter: str, password: str) -> bool:
    count: int = 0
    for s in password:
        if s == letter:
            count += 1
    if minimum <= count <= maximum:
        return True
    else:
        return False


def is_valid_new_policy(minimum: int, maximum: int, letter: str, password: str) -> bool:
    if (password[minimum - 1] == letter and not password[maximum - 1] == letter) or \
       (not password[minimum - 1] == letter and password[maximum - 1] == letter):
        return True
    else:
        return False


def validate_passwords_old_policy(data: list, validate_function) -> int:
    counter: int = 0
    for i in data:
        if validate_function(*i):
            counter += 1
    return counter


data = utils.clean_new_line_char(data)
data = prepare_data(data)
count = validate_passwords_old_policy(data, is_valid_new_policy)
range = len(data)
print(count)
print(range)
print(count / range)

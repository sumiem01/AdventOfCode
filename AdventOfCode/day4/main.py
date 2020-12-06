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
from utils import utils
PATH = "input4.TXT"
with open(PATH, 'r') as f:
    data = f.read()

data = data.split("\n\n")
print(len(data))

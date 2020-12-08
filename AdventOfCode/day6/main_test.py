from day6.main import *


test_input = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""


group1_answer = count_group_yes_answers_anyone("abc")
assert group1_answer == 3, f"{group1_answer} is wrong answer"



group2_answer = count_group_yes_answers_anyone("""a
b
c""".replace("\n", ""))
assert group2_answer == 3, f"{group2_answer} is wrong answer"

group3_answer = count_group_yes_answers_anyone("""ab
ac""".replace("\n", ""))
assert group3_answer == 3, f"{group3_answer} is wrong answer"

group4_answer = count_group_yes_answers_anyone("""a
a
a
a""".replace("\n", ""))
assert group4_answer == 1, f"{group4_answer} is wrong answer"

group5_answer = count_group_yes_answers_anyone("b")
assert group5_answer == 1, f"{group5_answer} is wrong answer"


# part 2

group1 = count_group_yes_answers_everyone("abc")
assert group1 == 3, f"{group1} is wrong answer"

group2 = count_group_yes_answers_everyone("""a
b
c""")
assert group2 == 0, f"{group2} is wrong answer"

group3 = count_group_yes_answers_everyone("""ab
ac""")
assert group3 == 1, f"{group3} is wrong answer"

group4 = count_group_yes_answers_everyone("""a
a
a
a""")
assert group4 == 1, f"{group4} is wrong answer"

group5 = count_group_yes_answers_everyone("b")
assert group5 == 1, f"{group5} is wrong answer"
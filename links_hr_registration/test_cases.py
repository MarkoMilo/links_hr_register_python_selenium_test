import random

from common import random_string, choose_zipcode, months
GENDER = ["gender-male", "gender-female"]
GENDER1 = ["//input[@id='gender-male']", "//input[@id='gender-female']"]

tc_9_1 = ["password", "password1", "tc_9_1"]
tc_10_1 = ["password", "password1", "tc_10_1"]
tc_12_1 = ["email", "email@", "@email.com", random_string()]
tc_13_1 = {"first_name": random_string(10), "last_name": random_string(10),
           "email": "marko87milosavljevi+{}@gmail.com".format(random_string(10)),
           "password": "password",
           "confirm_password": "password"}
tc_13_2 = {"first_name": random_string(10), "last_name": random_string(10),
           "email": "marko87milosavljevi+{}@gmail.com".format(random_string(10)),
           "password": "password1",
           "confirm_password": "password1"}
tc_13_3 = {"first_name": random_string(10), "last_name": random_string(10),
           "email": "marko87milosavljevi+{}@gmail.com".format(random_string(10)),
           "password": "passwordWEF",
           "confirm_password": "passwordWEF"}
tc_13_4 = {"first_name": random_string(10), "last_name": random_string(10),
           "email": "marko87milosavljevi+{}@gmail.com".format(random_string(10)),
           "password": "password1QW",
           "confirm_password": "password1QW"}

tc_14_1 = {"first_name": "", "last_name": random_string(10),
           "email": "marko87milosavljevi+{}@gmail.com".format(random_string(10)),
           "password": "password",
           "confirm_password": "password"}
tc_14_2 = {"first_name": random_string(10), "last_name": "random_string(10)",
           "email": "marko87milosavljevi+{}@gmail.com".format(random_string(10)),
           "password": "password1",
           "confirm_password": "password1"}
tc_14_3 = {"first_name": random_string(10), "last_name": random_string(10),
           "email": "",
           "password": "passwordWEF",
           "confirm_password": "passwordWEF"}
tc_14_4 = {"first_name": random_string(10), "last_name": random_string(10),
           "email": "marko87milosavljevi+{}@gmail.com".format(random_string(10)),
           "password": "",
           "confirm_password": ""}
tc_15_1 = {"gender": random.choice(GENDER),
           "first_name": random_string(10),
           "last_name": random_string(10),
           "birthmonth": random.randint(1, 12),
           "birthday": random.choice(months),
           "birtyear": random.randint(1911, 2021),
           "email": "marko87milosavljevi+{}@gmail.com".format(random_string(10)),
           "adress": random_string(20),
           "zipcode": choose_zipcode()[1],
           "phone": "+38598{}".format(random.randint(1, 10 ** 7)),
           "password": "password",
           "confirm_password": "password"}
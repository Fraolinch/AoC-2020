import re

with open("input4", 'r') as file:
    passports = file.read().split("\n\n")

rgx = re.compile(r"(\w+):")

keys = ["byr:", "iyr:", "eyr:", "hgt:",
        "hcl:", "ecl:", "pid:", "cid:"]

valid = 0
cid = 0

for passport in passports:
    passport = passport.replace(" ", "\n")
    passport = passport.splitlines()
    for pair in passport:
        key = rgx.match(pair)
        for k in keys:
            if key[0] == "cid:":
                cid = 1
    if len(passport) == 8 or (len(passport) == 7 and cid == 0):
            valid = valid + 1
    cid = 0

print(valid)
import re

with open("input4", 'r') as file:
    passports = file.read().split("\n\n")

rgx = re.compile("(\w+):")

keys = ["byr:", "iyr:", "eyr:", "hgt:",
        "hcl:", "ecl:", "pid:", "cid:"]

valid = 0
key_count = 0
cid = 0

for passport in passports:
    passport = passport.replace(" ", "\n")
    passport = passport.splitlines()
    for pair in passport:
        key = rgx.match(pair)
        for k in keys:
            if key[0] == k:
                key_count = key_count + 1
            if key[0] == "cid:":
                cid = 1
    if key_count == 8 or (key_count == 7 and cid == 0):
            valid = valid + 1
    key_count = 0
    cid = 0

print(valid)
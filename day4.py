import re

with open("input4", 'r') as file:
    passports = file.read().split("\n\n")

valid = 0
cid = 0

for passport in passports:
    passport = passport.replace(" ", "\n")
    passport = passport.splitlines()
    for pair in passport:
        if pair[:3] == "cid":
            cid = 1
            break
    if len(passport) == 8 or (len(passport) == 7 and cid == 0):
            valid = valid + 1
    cid = 0

print(valid)
import re

with open("input4", 'r') as file:
    passports = file.read().split("\n\n")

valid = 0
invalid_key = 0
cid = 0

for passport in passports:
    passport = passport.replace(" ", "\n")
    passport = passport.splitlines()
    for pair in passport:
        pair = pair.split(":")
        if pair[0] == "byr":
            pair[1] = int(pair[1])
            if pair[1] < 1920 or pair[1] > 2002:
                invalid_key = 1
                break
        elif pair[0] == "iyr":
            pair[1] = int(pair[1])
            if pair[1] < 2010 or pair[1] > 2020:
                invalid_key = 1
                break
        elif pair[0] == "eyr":
            pair[1] = int(pair[1])
            if pair[1] < 2020 or pair[1] > 2030:
                invalid_key = 1
                break
        elif pair[0] == "hgt":
            metric = ''.join(c for c in pair[1] if c.isalpha())     #get cm or in
            value = int(''.join(c for c in pair[1] if c.isdigit())) #get numbers
            if metric == "cm":
                if value < 150 or value > 193:
                    invalid_key = 1
                    break
            elif metric == "in":
                if value < 59 or value > 76:
                    invalid_key = 1
                    break
            else:
                invalid_key = 1
                break
        elif pair[0] == "hcl":
            if pair[1][0] != "#":
                invalid_key = 1
                break
            for c in pair[1]:
                if (c < '0' and c > '9') and (c < 'a' and c > 'f'):
                    invalid_key = 1
                    break
        elif pair[0] == "ecl":
            if (pair[1] != "amb"
            and pair[1] != "blu"
            and pair[1] != "brn"
            and pair[1] != "gry"
            and pair[1] != "grn"
            and pair[1] != "hzl"
            and pair[1] != "oth"):
                invalid_key = 1
                break
        elif pair[0] == "pid":
            if len(pair[1]) != 9:
                invalid_key = 1
                break
        elif pair[0] == "cid":
            cid = 1
        else:
            print("holy shit wtf")
            quit()
    if invalid_key:
        invalid_key = 0
    elif len(passport) == 8 or (len(passport) == 7 and cid == 0):
            valid = valid + 1
    cid = 0

print(valid)
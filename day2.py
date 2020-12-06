import re

with open("input2.txt", 'r') as file:
    lines = file.read().splitlines()

rgx = re.compile("(.+)-(.+?) (.): (.+)")

countpwd1 = 0
countpwd2 = 0

for i in range(0, len(lines)):
    match = rgx.match(lines[i])
    checkmin = int(match.group(1))
    checkmax = int(match.group(2))
    checkltr = match.group(3)[0]
    checkpwd = match.group(4)
    countltr = 0

    for j in checkpwd:
        if(j == checkltr):
            countltr = countltr + 1
    if(countltr <= checkmax and countltr >= checkmin):
        countpwd1 = countpwd1 + 1

    if((checkpwd[checkmin - 1] == checkltr) ^ (checkpwd[checkmax - 1] == checkltr)):
        countpwd2 = countpwd2 + 1

print(countpwd1)
print(countpwd2)
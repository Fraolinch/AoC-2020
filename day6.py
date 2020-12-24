with open("input6", 'r') as file:
    answers = file.read().split("\n\n")

total = 0

for group in answers:
    hashtable = {}
    for letter in group:
        if letter == '\n':
            continue
        hashtable[letter] = 0
    total = total + len(hashtable)

print(total)
with open("input6", 'r') as file:
    answers = file.read().split("\n\n")

total = 0

for group in answers:
    hashtable = {}
    for letter in group:
        hashtable[letter] = hashtable.get(letter, 0) + 1
    for key in hashtable:
        if key == '\n':
            continue
        elif hashtable[key] == hashtable.get('\n', 0) + 1:
            total = total + 1

print(total)
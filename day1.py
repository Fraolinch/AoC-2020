with open("input.txt", 'r') as file:
    input_text = file.read().splitlines()

answer = 0

for i in range(0, len(input_text)):
    for j in range(i + 1, len(input_text)):
        if(int(input_text[i]) + int(input_text[j]) == 2020):
            print(int(input_text[i]) * int(input_text[j]))
            answer = answer + 1
        if(answer == 2):
            quit()
        for k in range(j + 1, len(input_text)):
            if(int(input_text[i]) + int(input_text[j]) + int(input_text[k]) == 2020):
                print(int(input_text[i]) * int(input_text[j]) * int(input_text[k]))
                answer = answer + 1
            if(answer == 2):
                quit()
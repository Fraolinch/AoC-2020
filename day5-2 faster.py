with open("input5", 'r') as file:
    passes = file.read().splitlines()

def getSeatID(board_pass):
    binary_pass = board_pass

    binary_pass = int(binary_pass.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)

    return(binary_pass)

def getMissing2(pass_list):
    highest_id = 0
    lowest_id = 10000
    total = 0
    missing = 0
    for entry in pass_list:
        seat_id = getSeatID(entry)
        if seat_id > highest_id:
            highest_id = seat_id
        elif seat_id < lowest_id:
            lowest_id = seat_id
        total = total + seat_id
    theory_total = (highest_id * (highest_id + 1) / 2) - (lowest_id) * (lowest_id - 1) / 2
    missing = theory_total - total
    return(missing)

print(int(getMissing2(passes)))
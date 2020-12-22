with open("input5", 'r') as file:
    passes = file.read().splitlines()

def getSeatID(board_pass):
    rows = 128
    cols = 8
    row = [0, 127]
    col = [0, 7]
    for c in board_pass:
        if c == 'F':
            rows = rows / 2
            row[1] = row[1] - rows
        elif c == 'B':
            rows = rows / 2
            row[0] = row[0] + rows
        elif c == 'R':
            cols = cols / 2
            col[0] = col[0] + cols
        elif c == 'L':
            cols = cols / 2
            col[1] = col[1] - cols
    return(int(row[0] * 8 + col[0]))

def getHighestID(pass_list):
    highest_id = 0
    for entry in pass_list:
        seat_id = getSeatID(entry)
        if seat_id > highest_id:
            highest_id = seat_id
    return(highest_id)

def list_passes(pass_list):
    passes_list = []
    for entry in pass_list:
        seat_id = getSeatID(entry)
        passes_list.append(seat_id)
    passes_list.sort()
    return(passes_list)

def check_missing(pass_list):
    previous_entry = 0
    for entry in pass_list:
        if entry != (previous_entry + 1) and previous_entry != 0:
            return(previous_entry + 1)
        previous_entry = entry

print(check_missing(list_passes(passes)))
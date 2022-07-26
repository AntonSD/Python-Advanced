import re

def is_missing_turn(player, counter):
    pass

names = input().split(", ")

size = 6
matrix = []
for row in range(6):
    matrix.append(input().split(" "))

first_player = "Jerry"
second_player = "Tom"

if names[0] == "Tom":
    first_player = "Tom"
    second_player = "Jerry"
counter = 0
first_player_row = 0
first_player_col = 0
second_player_row, second_player_col = 0, 0

while True:
    counter += 1
    row, col = [int(x) for x in re.findall('\d', input())]
    if counter % 2 != 0:
        first_player_row = row
        first_player_col = col
        if matrix[row][col] == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break
        elif matrix[row][col] == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            continue
        elif matrix[row][col] == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
    else:
        second_player_row = row
        second_player_col = col
        if matrix[row][col] == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break
        elif matrix[row][col] == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            continue
        elif matrix[row][col] == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break

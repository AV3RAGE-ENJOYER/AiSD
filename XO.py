import os

from tabulate import tabulate


def display_field(field):
    os.system("cls")
    print(tabulate(field, tablefmt="grid"))


def check_win(field):
    for row in field:
        if len(set(row)) == 1:
            return True

    for column in range(0, 3):
        if field[column][0] == field[column][1] == field[column][2]:
            return True

    if field[0][0] == field[1][1] == field[2][2]:
        return True

    if field[0][2] == field[1][1] == field[2][0]:
        return True

    return False


def game_cycle(field):
    game = True
    while game:
        display_field(field)


if __name__ == "__main__":
    FIELD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    display_field(FIELD)

import os
import random
import numpy as np

from tabulate import tabulate
from pynput.keyboard import Key, Listener


clear = lambda: os.system("cls")


def generate_field():
    field = list(range(0, 16))
    random.shuffle(field)
    field = np.array(field).reshape(-1, 4)

    return field


def check_win(field):
    if list(field.flatten()) == list(range(0, 16)):
        return True

    return False


def locate_zero(field):
    for x in range(0, 4):
        for y in range(0, 4):
            if field[x][y] == 0:
                return x, y


def get_available_moves(field):
    zero_position = locate_zero(field)

    available_moves = []

    if zero_position[1] > 0:
        available_moves.append("right")
    if zero_position[1] < 3:
        available_moves.append("left")
    if zero_position[0] > 0:
        available_moves.append("down")
    if zero_position[0] < 3:
        available_moves.append("up")

    return available_moves


def swap_numbers(z_p: tuple, n_p: tuple):
    global FIELD

    FIELD[z_p[0]][z_p[1]] = FIELD[n_p[0]][n_p[1]]
    FIELD[n_p[0]][n_p[1]] = 0


def display_field(field: np.array):
    print("Управляй числами с помощью стрелок.\n")
    print(tabulate(field, tablefmt="grid"))
    print(f"Сделано {COUNTER} ходов.")


def on_release(key):
    global FIELD
    global COUNTER

    available_moves = get_available_moves(FIELD)
    zero_position = locate_zero(FIELD)

    if key == Key.right and "right" in available_moves:
        number_position = (zero_position[0], zero_position[1] - 1)
        swap_numbers(zero_position, number_position)
        COUNTER += 1

    if key == Key.left and "left" in available_moves:
        number_position = (zero_position[0], zero_position[1] + 1)
        swap_numbers(zero_position, number_position)
        COUNTER += 1

    if key == Key.up and "up" in available_moves:
        number_position = (zero_position[0] + 1, zero_position[1])
        swap_numbers(zero_position, number_position)
        COUNTER += 1

    if key == Key.down and "down" in available_moves:
        number_position = (zero_position[0] - 1, zero_position[1])
        swap_numbers(zero_position, number_position)
        COUNTER += 1

    if key == Key.esc:
        return False

    clear()
    display_field(FIELD)

    if check_win(FIELD):
        print("Победа.")
        return False


def game_cycle():
    with Listener(on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    FIELD = generate_field()
    COUNTER = 0

    display_field(FIELD)
    game_cycle()
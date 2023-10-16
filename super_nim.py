import random


def generate_field():
    FIELD = []

    for _ in range(8):
        pieces = random.randint(0, 5)
        row = ["*"] * pieces + [" "] * (8 - pieces)
        random.shuffle(row)
        FIELD.append(row)

    return FIELD


def check_win(field):
    win = True
    for i in range(8):
        if not (len(set(field[i])) == 1 and field[i][0] == " "):
            win = False

    return win


def display_field(field):
    for i in range(8):
        print(field[i], i)

    print("  a    b    c    d    e    f    g    h")


def make_move(field):
    while True:
        k = input("Введите строку или столбец: ")

        if k.isdigit():
            if len(set(field[int(k)])) > 1:
                field[int(k)] = [" "] * 8
                return field
            else:
                print("Нельзя выбрать пустую строку.")

        else:
            rows = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

            if k in rows.keys() and len(set([el[rows[k]] for el in field])) > 1:
                for i in range(8):
                    field[i][rows[k]] = " "

                return field
            else:
                print("Нельзя выбрать пустой столбец.")


def game_cycle(field):
    game = True
    counter = 0
    while game:
        display_field(field)

        field = make_move(field)

        if check_win(field):
            game = False

            if counter % 2 == 0:
                print("Победа 1 игрока.")
            else:
                print("Победа 2 игрока.")
        else:
            counter += 1


if __name__ == "__main__":
    field = generate_field()
    game_cycle(field)
field = ["|", 1, "|", 2, "|", 3, "|",
         "|", 4, "|", 5, "|", 6, "|",
         "|", 7, "|", 8, "|", 9, "|"]

from time import sleep

print('\033[34m%12s ' %'WELCOME')
sleep(0.6)
print('to the TIC-TAC-TOE')
sleep(0.6)
print('WORLD CHAMPIONSHIP!\033[0m')
print()
sleep(0.8)

winn_combinations = [[1, 3, 5],
                     [8, 10, 12],
                     [15, 17, 19],
                     [1, 8, 15],
                     [3, 10, 17],
                     [1, 10, 19],
                     [5, 12, 19],
                     [5, 10, 15]]

def game_field():
    print(field[0], end=" ")
    print(field[1], end=" ")
    print(field[2], end=" ")
    print(field[3], end=" ")
    print(field[4], end=" ")
    print(field[5], end=" ")
    print(field[6])
    print("-" * 13)

    print(field[7], end=" ")
    print(field[8], end=" ")
    print(field[9], end=" ")
    print(field[10], end=" ")
    print(field[11], end=" ")
    print(field[12], end=" ")
    print(field[13])
    print("-" * 13)

    print(field[14], end=" ")
    print(field[15], end=" ")
    print(field[16], end=" ")
    print(field[17], end=" ")
    print(field[18], end=" ")
    print(field[19], end=" ")
    print(field[20])

def step_field(step, value):
    ind = field.index(step)
    field[ind] = value

def result_check():
    win = ""
    for i in winn_combinations:
        if field[i[0]] == "\033[31mX\033[0m"\
                and field[i[1]] == "\033[31mX\033[0m"\
                and field[i[2]] == "\033[31mX\033[0m":
            win = "X"
        if field[i[0]] == "\033[31m0\033[0m"\
                and field[i[1]] == "\033[31m0\033[0m"\
                and field[i[2]] == "\033[31m0\033[0m":
            win = "0"

    return win

game = True
player1 = True
n = 0
while game:
    game_field()

    if player1:
        value = "\033[31mX\033[0m"
        step = (input("Player №1, you turn: "))
        try:
            step = int(step)
        except:
            print("Wrong input! Enter the number:")
            continue
        if step < 1 or step > 9:
            print("Warning! Enter the number from 1 to 9!")
            continue
        if 1 <= int(step) <= 9:
            n += 1

    else:
        value = "\033[31m0\033[0m"
        step = (input("Player №2, you turn: "))
        try:
            step = int(step)
        except:
            print("Wrong input! Enter the number:")
            continue
        if step < 1 or step > 9:
            print("Warning! Enter the number from 1 to 9!")
            continue

    step_field(step, value)
    win = result_check()
    player1 = not (player1)

    if win == "X" or win == "0":
        print("Winner:", win)
        print("GAME OVER!")
        break
    if n == 5:
        print("Draw!")
        print("GAME OVER!")
        break

    else:
        game = True

game_field()












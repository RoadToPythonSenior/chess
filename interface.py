from figures.figure import Color
from game import Game


def show_menu():
    print('1. Начать новую игру')
    command = int(input())
    if command == 1:
        game = Game()
        while True:
            game.show()
            print('Введите ваш ход')
            move = input()
            pass
            if game.has_mate:
                if game.move_color == Color.white:
                    winner = 'Белые'
                else:
                    winner = 'Чёрные'
                print(f"Игра закончена, победили {winner}")
                break

    else:
        print("Неверная команда")
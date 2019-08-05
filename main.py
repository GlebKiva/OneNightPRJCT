from inbar import inbar
from magaz import magaz
from home import home
from games import games
from gostin import gostin
import sys
import io

print('Добро пожаловать в текстовую игру "Одна Ночь"!')
while True:
    file = io.open('text', 'r')
    x = file.read()
    x = x.split(' ')
    energy = int(x[0])
    money = int(x[1])
    reputation = int(x[2])
    ishome = int(x[3])
    products = int(x[4])
    gostinn = int(x[5])
    if ishome == 1:
        print('\n-Зайти в дом\n-Магазин\n-В Бар\n-В Игровой Зал\n-Гостиная\n-Автор игры\n-Выход из игры')
    else:
        print('\n-Купить дом\n-Магазин\n-В Бар\n-В Игровой Зал\n-Гостиная\n-Автор игры\n-Выход из игры')
    print('Введи номер варианта, чтобы его выбрать:')
    while True:
        try:
            x = int(input())
            break
        except:
            print('Попробуй ещё раз!')
    if x == 1:
        home()
    elif x == 2:
        magaz()
    elif x == 3:
        inbar()
    elif x == 4:
        games()
    elif x == 5:
        gostin()
    elif x == 6:
        print('\n ____  ____  ___   ____   ____          ____           __ \n|     |       |   |    | |    | |\   | |    '
            '|   \  /  |   \n|____ |____   |   |____| |    | | \  | |    |    \/   |__ \n|     |       |   |   |  | '
            '   | |  \ | |    |    /\      |\n|     |____  _|_  |   |  |____| |   \| |____|   /  \  '
            '___|\n__________________________________________________________\nPRESENTS  PRESENTS  PRESENTS  PRESENTS  PRESENTS  PRESENTS\n\n\n                     THE GAME CALLED                     \n                       "ONE NIGHT"                        \n\n')

        x = input('Не хочешь ввести ключ?')
        if x == 'I am from Letovo':
            print('@#$%^&*(\n'*10)
            print('Неплохо! + 1000 Монет / + 1000 Энергии!')
            file = io.open('text', 'r')
            x = file.read()
            x = x.split(' ')
            energy = int(x[0])
            money = int(x[1])
            reputation = int(x[2])
            ishome = int(x[3])
            products = int(x[4])
            gostinn = int(x[5])
            money += 1000
            energy += 1000
            file = io.open('text', 'w')
            file.write(str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(products) + ' ' + str(gostinn))
            file.close()
    elif x == 7:
        sys.exit()

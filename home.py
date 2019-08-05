def home():
    import io
    import time
    import random

    file = io.open('text', 'r')
    x = file.read()
    x = x.split(' ')
    energy = int(x[0])
    money = int(x[1])
    reputation = int(x[2])
    ishome = int(x[3])
    products = int(x[4])
    gostinn = int(x[5])
    file.close()

    def inhome():
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
            print('ВАШ ДОМ')
            print(
                ' _______________________________________________________ \n'
                '|                      |                                |\n'
                '|                      |                                |\n'
                '|                      |                                |\n'
                '|                                                       |\n'
                '|         КУХНЯ                 ГОСТИНАЯ/СПАЛЬНЯ        |\n'
                '|                                                       |\n'
                '|                      |                                |\n'
                '|                      |                                |\n'
                '|________     _________|________________________________|\n'
                '\                      |\n'
                ' \                     |\n'
                '  \                    |\n'
                '   \      ПРИХОЖАЯ     |\n'
                '    \                  |\n'
                '     \_____|   |_______|\n\n')
            print('В какую комнату Вы хотите отправиться?')
            print('-Сохранить игру\n-Прихожая\n-Кухня\n-Гостиная/Спальня\n-Выход')
            print('Введи номер варианта, чтобы его выбрать:')
            while True:
                try:
                    x = int(input())
                    break
                except:
                    print('Попробуй ещё раз!')
            if x == 1:
                file = io.open('text', 'w')
                file.write(str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(
                    products) + ' ' + str(gostinn))
                file.close()
            elif x == 2:
                while True:
                    print('\nПРИХОЖАЯ\n\nТут пока пусто(\n-Выход')
                    print('Введи номер варианта, чтобы его выбрать:')
                    while True:
                        try:
                            x = int(input())
                            break
                        except:
                            print('Попробуй ещё раз!')
                    if x == 1:
                        break
            elif x == 3:
                while True:
                    print('\nКУХНЯ\n\n-Приготовить поесть (+1 Продукт / -1 Монета)\n-Выход')
                    print('Введи номер варианта, чтобы его выбрать:')
                    while True:
                        try:
                            x = int(input())
                            break
                        except:
                            print('Попробуй ещё раз!')
                    if x == 1:
                        if money >= 1:
                            products += 1
                            print('Еда готова! Идите в гостиную, чтобы её съесть')
                            money -= 1
                            file = io.open('text', 'w')
                            file.write(
                                str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(
                                    products) + ' ' + str(gostinn))
                            file.close()
                        else:
                            print('Недостаточно монет! Попробуй заработать монету у мудрого бармена.')
                    if x == 2:
                        break
            elif x == 4:
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
                    print(
                        '\nГОСТИНАЯ/СПАЛЬНЯ\n\n-Есть еду (-1 Продукт / +5 Энергии)\n-Спать (Ждите 10 секунд / + 4 Энергии)\n-Выход')
                    print('Введи номер варианта, чтобы его выбрать:')
                    while True:
                        try:
                            x = int(input())
                            break
                        except:
                            print('Попробуй ещё раз!')
                    if x == 1:
                        if products >= 1:
                            products -= 1
                            energy += 5
                            y = random.randint(1, 5)
                            z = random.randint(1, 2)
                            if y == 1:
                                x = 'Курицу с макаронами'
                            elif y == 2:
                                x = 'Спагетти Болоньезе'
                            elif y == 3:
                                x = 'Говядину'
                            elif y == 4:
                                x = 'Хотдоги'
                            elif y == 5:
                                x = 'Пиццу'
                            if z == 2:
                                print('Ммм... Вкусно! У меня просто превосходно получается готовить ' + x + '!')
                            else:
                                print('Ой! У меня не очень хорошо получается готовить ' + x + '!')
                            file.write(
                                str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(
                                    products) + ' ' + str(gostinn))
                            file.close()
                        else:
                            print('Приготовь еды на кухне!')

                    elif x == 2:
                        print('Засыпаю...')
                        for i in range(10):
                            time.sleep(0.5)
                            print('Zzz...')
                            time.sleep(0.5)
                        energy += 4
                        print('\nЯ снова готов работать!\n')
                    elif x == 3:
                        file = io.open('text', 'w')
                        file.write(
                            str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(
                                products) + ' ' + str(gostinn))
                        file.close()
                        break

            elif x == 5:
                print('Перед выходом рекомендуем сохранить игру.')
                print('Вы готовы?\n-Да\n-Нет')
                print('Введи номер варианта, чтобы его выбрать:')
                while True:
                    try:
                        x = int(input())
                        break
                    except:
                        print('Попробуй ещё раз!')
                if x == 1:
                    break

    if ishome == 1:
        file = io.open('text', 'w')
        file.write(str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(
            products) + ' ' + str(gostinn))
        file.close()
        inhome()
    else:
        while True:
            print('ДОМ, ВЫСТАВЛЕННЫЙ НА ПРОДАЖУ')
            print('\nЗдравствуй, хочешь купить этот дом?\n\nСхема дома:')
            print(
                ' _______________________________________________________ \n'
                '|                      |                                |\n'
                '|                      |                                |\n'
                '|                      |                                |\n'
                '|                                                       |\n'
                '|         КУХНЯ                 ГОСТИНАЯ/СПАЛЬНЯ        |\n'
                '|                                                       |\n'
                '|                      |                                |\n'
                '|                      |                                |\n'
                '|________     _________|________________________________|\n'
                '\                      |\n'
                ' \                     |\n'
                '  \                    |\n'
                '   \      ПРИХОЖАЯ     |\n'
                '    \                  |\n'
                '     \_____|   |_______|\n\n')
            print('-Сохранить игру\n-Купить дом\n-Выход на улицу')
            print('Введи номер варианта, чтобы его выбрать:')
            while True:
                try:
                    x = int(input())
                    break
                except:
                    print('Попробуй ещё раз!')
            if x == 1:
                file = io.open('text', 'w')
                file.write(str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(
                    products) + ' ' + str(gostinn))
                file.close()
            elif x == 2:
                print('Как скажешь! С тебя 10 монет. Ты уверен?\n-Да\n-Нет')
                print('Введи номер варианта, чтобы его выбрать:')
                while True:
                    try:
                        x = int(input())
                        break
                    except:
                        print('Попробуй ещё раз!')
                if x == 1:
                    if money >= 10:
                        money -= 10
                        print('Дом куплен!')
                        ishome = 1
                        file = io.open('text', 'w')
                        file.write(
                            str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(
                                products) + ' ' + str(gostinn))
                        file.close()
                        inhome()
                    else:
                        print('Недостаточно монет! Попробуй заработать монеты у мудрого бармена.')
            elif x == 3:
                print('Перед выходом рекомендуем сохранить игру.')
                print('Вы готовы?\n-Да\n-Нет')
                print('Введи номер варианта, чтобы его выбрать:')
                while True:
                    try:
                        x = int(input())
                        break
                    except:
                        print('Попробуй ещё раз!')
                if x == 1:
                    break

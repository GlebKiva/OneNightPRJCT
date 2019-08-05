def gostin():
    import io
    import time
    import random

    def ingostin():
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
            print('ВАША КОМНАТА')
            print(' _______________________________________________________ \n'
                  '|                      |                                |\n'
                  '|                      |                                |\n'
                  '|                      |                                |\n'
                  '|                                                       |\n'
                  '|         КУХНЯ                 ГОСТИНАЯ/СПАЛЬНЯ        |\n'
                  '|                                                       |\n'
                  '|                      |                                |\n'
                  '|                      |                                |\n'
                  '|______________________|________________________________|\n')
            print('В какую комнату Вы хотите отправиться?')
            print('-Сохранить игру\n-Кухня\n-Гостиная/Спальня\n-Выход')
            print('Введи номер варианта, чтобы его выбрать:')
            while True:
                try:
                    x = int(input())
                    break
                except:
                    print('Попробуй ещё раз!')
            if x == 1:
                file = io.open('text', 'w')
                file.write(str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(products) + ' ' + str(gostinn))
                file.close()
            elif x == 2:
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
            elif x == 3:
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

            elif x == 4:
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
    print('ГОСТИНИЦА "ОДНА НОЧЬ"')
    if gostinn == 0:
        print('Добро Пожаловать в нашу гостиницу! На стене возле стойки висят ключи от комнат: ')
        print(' ______ ______ ______ ______ ______ ______ \n'
              '|      |      |      |      |      |      |\n'
              '|  01  |  02  |  03  |  04  |  05  |  06  |\n'
              '|______|______|______|______|______|______|\n'
              '|      |      |      |      |      |      |\n'
              '|  07  |  08  |  09  |  10  |  11  |  12  |\n'
              '|______|______|______|______|______|______|\n'
              '|      |      |      |      |      |      |\n'
              '|  13  |  14  |  15  |  16  |  17  |  18  |\n'
              '|______|______|______|______|______|______|\n'
              '|      |      |      |      |      |      |\n'
              '|  19  |  20  |  21  |  22  |  23  |  24  |\n'
              '|______|______|______|______|______|______|\n'
              '|      |      |      |      |      |      |\n'
              '|  25  |  26  |  27  |  28  |  29  |  30  |\n'
              '|______|______|______|______|______|______|')
        x = 0
        while 30 < x or x < 1:
            while True:
                try:
                    x = int(input('\nВыбери подходящий тебе номер: '))
                    break
                except:
                    print('\nПопробуй ещё раз!')
        print('Отлично! Номер ' + str(x) + ' забронирован на Ваше имя!')
        gostinn = 1
        if x == 13:
            print('Хотя я бы и не рекомендовал бы там останавливаться...')
        elif x == 7:
            print('Счастливое число! Просто прекрасно!')
        file = io.open('text', 'w')
        file.write(str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(
            products) + ' ' + str(gostinn))
        file.close()
        print('Приходите через несколько минут, Ваш номер убирают.')
    else:
        while True:
            print('Добро Пожаловать в нашу гостиницу!')
            print('Каждый вход в комнату с тебя будет списываться 1 Монета')
            print('-Сохранить игру\n-Войти в комнату\n-Отменить аренду комнаты')
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
                file = io.open('text', 'w')
                file.write(str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(
                    products) + ' ' + str(gostinn))
                file.close()
                ingostin()
                break
            elif x == 3:
                gostinn = 0
                print('Ваша аренда отменена!')
                print('Приходите ещё!')
                file = io.open('text', 'w')
                file.write(str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(
                    products) + ' ' + str(gostinn))
                file.close()
                break


def magaz():
    import io
    import time

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
    print('МАГАЗИН "У БОБА И ЛЮСИ"')
    print('Боб: Привет, я Боб!\nЛюси: А я Люси! У нас ты найдёшь полезные зелья. \nБоб: Ты не маг, поэтому зелье ты сможешь использовать только здесь.')
    while True:
        print('\n-Сохранить игру\n-Купить зелье\n-Выход на улицу')
        while True:
            try:
                x = int(input())
                break
            except:
                print('\nПопробуй ещё раз!')
        if x == 1:
            file = io.open('text', 'w')
            file.write(str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(products) + ' ' + str(gostinn))
            file.close()
        elif x == 2:
            print('\nЛюси: Какое зелье тебе подходит?')
            print('Зелье Сна - 12 Монет [Энергия становиться равна 20]\nЗелье Монет - 20 Энергии [+12 Монет]\nСклянка со смертью - +1 Монета [Вы выходите из игры, перед этим игра автоматически сохраняется]\nВыход')
            while True:
                try:
                    x = int(input())
                    break
                except:
                    print('\nПопробуй ещё раз!')
            if x == 1:
                if money >= 12:
                    print('Боб: Как будто энергетиков напился!')
                    money -= 12
                    energy = 20
            elif x == 2:
                if energy >= 20:
                    print('Люси: Золотые слова!')
                    energy -= 20
                    money += 12
            elif x == 3:
                money += 1
                file = io.open('text', 'w')
                file.write(str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(products) + ' ' + str(gostinn))
                file.close()
                exit()
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



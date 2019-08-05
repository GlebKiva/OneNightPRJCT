def games():
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
    while True:
        print('\nКЛУБ "БЕШЕНОЕ РОДЕО"')
        print('\nПривет! Во что сегодня сыграешь?')
        print(
            '-Сохранить Игру\n-Игровой автомат (+ Выигрыш)\n-Стрельба (-2 Энергии / + Выигрыш)\n-Игра "Угадай где деньги" (-1 Энергия / + Выигрыш)\n-Выход на улицу')
        print('Введи номер варианта, чтобы его выбрать:')
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
        if x == 2:
            print('Автомат крутиться...')
            for i in range(random.randint(3, 7)):
                result = str(random.randint(1, 3)) + str(random.randint(1, 3)) + str(random.randint(1, 3))
                print(result)
            if result[0] == result[1] == result[2]:
                print('\nВы выиграли!')
                money += (random.randint(1, 3))
                print('Деньги: ' + str(money) + '\nЭнергия: ' + str(energy))

            else:
                print('\nБез потерь сложно что-либо заработать...')
        elif x == 3:
            if energy >= 2:
                energy -= 2
                print('Это игра на реакцию! Правила просты:\nЧем больше ты собьёшь сурикатов, нажимая на клавиатуре их номера, тем больше монет ты выиграешь!\nОдин сурикат - 0.5 Монет. В конце игры вы получите округлённое количество монет.\n')
                time.sleep(1)
                print('1')
                time.sleep(1)
                print('2')
                time.sleep(1)
                print('3')
                print('ВПЕРЁД!\n')
                time.sleep(0.5)
                j = 0
                for i in range(10):
                    i = random.randint(1, 4)
                    print('|______|'*(5-i) + ' HERE ' + '|______|'*(i-1))
                    y = time.time()
                    while True:
                        try:
                            x = int(input())
                            break
                        except:
                            print('\nНе стоит тут ошибаться!')
                    z = time.time()
                    y = int(str(int(y))[-1])
                    z = int(str(int(z))[-1])
                    print(y, z)
                    if z-y > 2 or z-y < 0:
                        print('Не успел! Продолжаем!')
                    else:
                        if x == 6-i:
                            print('В точку!')
                            j += 0.5
                        else:
                            print('Вовремя, но не туда!')
                print('Твой выигрыш: ' + str(int(j)))
                money += int(j)
            else:
                print('Недостаточно энергии! Рекомендуем выпить кофе в баре!')
        elif x == 4:
            if energy >= 1:
                energy-=1
                print('В этой игре тебе поможет лишь твоё везение! Угадай где спрятаны монеты и введи номер этой банки!')
                print('   ___         ___         ___   \n  /   \       /   \       /   \  \n /     \     /     \     /     \ \n|       |   |       |   |       |\n|       |   |       |   |       |\n|       |   |       |   |       |\n|       |   |       |   |       |\n|_______|   |_______|   |_______|\n')
                print('Где лежат монеты?')
                while True:
                    try:
                        x = int(input())
                        break
                    except:
                        print('\nВводи лучше цифру!')
                i = random.randint(1,3)
                if x == i:
                    z = random.randint(1, 4)
                    print('Вы угадали! В этой банке лежало ' + str(z) + ' Монет!')
                    money += z

                else:
                    print('Ничего, попробуй ещё раз!')
            else:
                print('Недостаточно энергии! Рекомендуем выпить кофе в баре!')
        elif x== 5:
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

def inbar():
    import random
    import time
    import sys
    import io

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
    print('БАР "3 СОЛНЦА"')
    print('Здравствуй, здесь тебе всегда будут рады! Как ты решил развлечься сегодня?')

    while True:
        timed = str(int(time.time()))
        timen = int(timed[-1])
        if 3 <= timen < 5:
            timed = 'Утро'
        elif 5 <= timen < 8:
            timed = 'День'
        else:
            timed = 'Ночь'
        print('\nВремя: ' + str(timed))
        print('-Сохранить игру\n-Выпить кофе (+3 Энергии / -1 Монета)\n-Зайти в игральную комнату\n-Послушать сплетни (-1 '
              'Энергии / +2 Репутация)\n-Подойти к бармену\n-Проверить свои сбережения\n-Выход на улицу')
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
        if x == 2:
            if money >= 1:
                print('Вы садитесь и пьёте кофе.')
                energy += 3
                money -= 1
                print('Деньги: ' + str(money) + '\nЭнергия: ' + str(energy))
            else:
                print('У вас недостаточно монет, попробуйте найти работу у мудрого бармена.')
        elif x == 3:
            while True:
                chance = 100
                print('\nТы заходишь в игральную комнату, в левом углу сидит Шуллер Джо, в центре - большой стол у которого '
                      'столпились игроки, они по очереди бросают кости. Отовсюду слышится смех и вздохи разочарования. '
                      'Справа ты замечаешь занавеску. Интересно, что она прикрывает?')
                print('\n-Подойти к шуллеру Джо (-1 Монета / +100% Шанс выиграть)\n-Сыграть в кости (-2 Энергии / + '
                      'Выигрыш)\n-Проверить что за шторой(-1 Энергии)\n-Выход')
                print('Введи номер варианта, чтобы его выбрать:')
                while True:
                    try:
                        x = int(input())
                        break
                    except:
                        print('Попробуй ещё раз!')
                if x == 1:
                    if money >= 1:
                        print('Привет, я помогу тебе и заменю здешние кости на мои собственные, но толко на один бросок. За это я попрошу всего одну монету.')
                        chance += 100
                        money -= 1
                        print('Деньги: ' + str(money) + '\nЭнергия: ' + str(energy))
                    else:
                        print('У вас недостаточно монет, попробуйте найти работу у мудрого бармена.')
                elif x == 2:
                    if energy >= 2:
                        result = 0
                        energy -= 2
                        bet = int(input('Введите вашу ставку: '))
                        if money >= bet:
                            if energy >= 2:
                                if chance == 100:
                                    result = random.randint(1,4)
                                elif chance > 100:
                                    result = random.randint(1,1)
                                else:
                                    result = 1
                            if result == 1:
                                print('Вы выиграли! +' + str(bet*3) + ' монет')
                                money += (bet*3)
                                chance = 100
                            else:
                                print('К сожалению, Вы проиграли!')
                                money -= bet
                                chance = 100
                        else:
                            print('У вас недостаточно монет, попробуйте найти работу у мудрого бармена.')
                    else:
                        print('Выпей кофе, чтобы регенерировать энергию!')
                elif x == 3:
                    if reputation >= 2:
                        if energy >= 1:
                            energy -= 1
                            if 3 <= timen < 5:
                                print('Вы видите старое зеркало. Однако в нём ничего не видно. Вас это настораживает!')
                            elif 5 <= timen < 8:
                                print('Вы видите огромный сундук, странно, что он поместился за этой шторой.')
                            else:
                                print('За шторой ничего нет. Но вдруг, свет резко выключается. А из щелей в полу поднимается зелёный дым. Вы выбегаете из таверны.')
                                reputation -= 2
                                file = io.open('text', 'w')
                                file.write(str(energy) + ' ' + str(money) + ' ' + str(reputation) + ' ' + str(ishome) + ' ' + str(products) + ' ' + str(gostinn))
                                file.close()
                                sys.exit()
                        else:
                            print('Выпей кофе, чтобы регенерировать энергию!')
                    else:
                        print('Тебя останавливает высокий мужчина, послушай сплетни в гостиной, чтобы поднять свою репутацию.')
                elif x == 4:
                    break
        elif x == 4:
            if energy >= 1:
                print('Ты присаживаешься за стол к постоянным посетителям бара. Вы по очереди рассказываете друг другу анекдоты и истории. Твоя репутация повышена.')
                reputation += 2
                energy -=1
            else:
                print('Выпей кофе, чтобы регенерировать энергию!')
        elif x == 5:
            while True:
                print('\nНу, здравствуй, какую работу ты хочешь получить?')
                print('-Протереть стаканы (-2 Энергии / +1 Монета / -1 Репутации)\n-Подмести пол (-4 Энергии / +2 Монеты)\n-Поиграть в сломанный автомат (20% шанс выиграть 1 Монету)\n-Выход')
                print('Введи номер варианта, чтобы его выбрать:')
                while True:
                    try:
                        x = int(input())
                        break
                    except:
                        print('Попробуй ещё раз!')
                if x == 1:
                    if energy >= 2:
                        if reputation >= 1:
                            reputation -= 1
                            energy -= 2
                            print('Стаканы чисты! Бармен доволен твоей работой и награждает тебя 1 Монетой.')
                            money += 1
                        else:
                            print('Послушай сплетни в гостиной, чтобы поднять свою репутацию.')
                    else:
                        print('Выпей кофе, чтобы регенерировать энергию!')
                elif x == 2:
                    if energy >= 4:
                        energy -= 4
                        money += 2
                        print('Пол чист! Бармен доволен твоей работой и награждает тебя 2 Монетами.')
                    else:
                        print('Выпей кофе, чтобы регенерировать энергию!')
                elif x == 3:
                    print('Опять от работы отлыниваешь?')
                    print('Автомат крутиться...')
                    for i in range(random.randint(3, 7)):
                        result = str(random.randint(1, 3))+str(random.randint(1, 3))+str(random.randint(1, 3))
                        print(result)
                    if result[0] == result[1] == result[2]:
                        print('\nВы выиграли!')
                        money += 1
                        print('Деньги: ' + str(money) + '\nЭнергия: ' + str(energy))

                    else:
                        print('\nБез потерь сложно что-либо заработать...')
                elif x == 4:
                    break

        elif x == 6:
            print('Деньги: ' + str(money) + '\nЭнергия: ' + str(energy))
        elif x == 7:
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

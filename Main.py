import time
print('-----------------------')
print('Добро пожаловать нищета')
print('-----------------------')

que = ['А, И, О, Х, М \n что идет дальше?', '8,478,624/5,698 - 140,679/ 99', 'Вотчиноу бар доу ___ \n что идет дальше?']
fo_que = [['Щ, а, ь','И, я', 'О, Р, П', 'ЩЩЩЩЩЩЩ'], [69, 66, 666, 67], ['Бар кекеги','Даун нененги','Танегоу итс э мани','сiкс сeveн']]
ri_ans = ['2','4', '2']
money = 0
moneysum = 100
b = len(que)

for i in range(b):
    print(que[i])

    for j in range(4):
        print(f'{j + 1}. {fo_que[i][j]}')

    answer = input('Ваш ответ? \n')

    if answer == ri_ans[i]:
        moneysum += 100
        print('ЭТО правильный ответ')
        money += moneysum
        print(f'Ваш баланс {money}')
    else:
        print('ВЫ ПРОИГРАЛИ')
        print(f'у вас на балансе {money}')
        print(f'Правильный ответ был {ri_ans[i]}')
        break

    time.sleep(2)
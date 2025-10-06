from random import randint as random

count = {'Выйграшей': 0, 'Проигрышей': 0, 'Всего сыгранно': 0}
RSP = ['камень', 'ножницы', 'бумага']
RSP_LOGIC = {'камень': 'ножницы', 'ножницы': 'бумага', 'бумага': 'камень'}


def inf_input(text, answers, type_ans):
    answer_input = None
    while True:
        answer_input = type_ans(input(text + '\n\n>> '))
        if answer_input not in answers:
            print('Ответ не совпадает с возможными')
        else:
            break
    return answer_input


while True:
    answer = int(input('Что вы хотите сделать?\n 1 - Сыграть КНБ\n 2 - Узнать статистику\n 3 - Выйти из программы\n\n>> '))
    print()
    if answer == 1:
        want_play = True
        while want_play:
            count['Всего сыгранно'] += 1
            chose_player = inf_input('Что вы хотите выбрать? (камень, ножницы, бумага)', RSP, str)
            chose_computer = RSP[random(0, 2)]
            if chose_computer == chose_player:
                print('Ничья.')
            else:
                result = RSP_LOGIC[chose_player] == chose_computer
                count['Выйграшей' if result else 'Проигрышей'] += 1
                print('Поздравляю, вы - выиграли!' if result else 'Печально. Вы - проиграли...')
            want_play = inf_input('Вы хотите ещё сыграть?\n 1 - ДА\n 2 - НЕТ', [1, 2], int) == 1
            print()
    elif answer == 2:
        print('Ваша статистика: ')
        for name, val in count.items():
            print(f'\t{name} - {val}')
        print()
    elif answer == 3:
        break

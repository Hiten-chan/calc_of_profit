import re
import sys


def dec_word(s):
    if s in range(5, 21) or s % 100 in range(5, 21):
        return 'лет'
    elif s > 20:
        s %= 10
    return {
        0: 'лет',
        1: 'год',
        2: 'года',
        3: 'года',
        4: 'года',
        5: 'лет',
        6: 'лет',
        7: 'лет',
        8: 'лет',
        9: 'лет',
    }[s]


def check(s):  # checking the value (is it number?)
    pattern = r'^[+]?\d+[,.]?\d*?$|^\d*[,.]?\d+?$|^exit$'
    return re.match(pattern, s)


def test_input(value, m):  # final checking
    if type(value) == str:
        value = value.replace(',', '.')
        if not check(value):
            print('Значение должно быть числом > 0')
            return test_input(input(m), m)
        else:
            if value == 'exit':
                c = input('Вы уверены, что хотите выйти? (y/n):')
                if c == 'y':
                    print('\nGoodbye!')
                    sys.exit(0)
                else:
                    return test_input(input(m), m)

        value = float(value)

    if m == 'Введите кратность увеличения суммы вклада:' and value < 1:
        print('Значение должно быть числом > 1')
        return test_input(input(m), m)

    if value <= 0:
        print('Значение должно быть числом > 0')
        return test_input(input(m), m)

    if value % 1 == 0:
        return int(value)
    else:
        return float(value)


# Welcome
print('\nWelcome! Это программа для расчета времени увеличения'
      '\nсуммы первоначального вклада согласно заданной кратности\n'
      '\nДля расчета требуется последовательно ввести следующие параметры:'
      '\n1. Сумму вклада в рублях'
      '\n2. Годовую процентную ставку по вкладу в %'
      '\n3. Кратность увеличения суммы вклада\n'
      '\nДля выхода из программы введите exit\n')

amount = test_input(input('Введите сумму вклада в рублях:'), 'Введите сумму вклада в рублях:')
percent = test_input(input('Введите процентную ставку в %:'), 'Введите процентную ставку в %:') / 100
mult = test_input(input('Введите кратность увеличения суммы вклада:'), 'Введите кратность увеличения суммы вклада:')
re_amount = amount
result = 0

# Сalculation
while re_amount < amount * mult:
    re_amount += round(re_amount * percent, 2)
    result += 1

# Show result
print('\nСумма первоначального вклада увеличится в {0} раз(a) '
      'через {1} {2} и будет равна {3} руб.'.format(mult, result, dec_word(result), round(re_amount, 2)))

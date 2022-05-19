def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


def test():
    try:
        my_int = int(input('Введите целое число: '))
        print('Вы ввели 0') if my_int == 0 else negative() if my_int < 0 else positive()
    except ValueError:
        print('Вы ввели не целое число.')


test()

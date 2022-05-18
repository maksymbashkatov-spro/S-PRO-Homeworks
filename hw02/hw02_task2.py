def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


def test():
    my_int = int(input('Введите целое число: '))
    negative() if my_int < 0 else positive()


test()

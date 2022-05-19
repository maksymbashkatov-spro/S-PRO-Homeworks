def str_conc():
    return input('Введите первую строку: ') + input('Введите вторую строку: ')


print(str_conc())


def inf_multi():
    multi = 1
    num = int(input('Введите число: '))
    while num != 0:
        multi *= num
        num = int(input('Введите число: '))
    return multi if num != 0 else 0


print(inf_multi())

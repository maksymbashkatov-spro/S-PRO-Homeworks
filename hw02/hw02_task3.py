def str_conc():
    return input('Введите первую строку: ') + input('Введите вторую строку: ')


print(str_conc())


def inf_multi():
    multi = 1
    num = int(input('Введите число: '))
    count = 0
    while num != 0:
        count += 1
        multi *= num
        num = int(input('Введите число: '))
    return multi if num else (multi if count else 0)


print(inf_multi())

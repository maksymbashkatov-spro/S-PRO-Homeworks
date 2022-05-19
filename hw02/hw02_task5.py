# 5.1
def print_symbol():
    unicode_code = int(input('Введите unicode из range(0, 1114112): '))
    while unicode_code != 0:
        try:
            print(chr(unicode_code))
            unicode_code = int(input('Введите unicode из range(0, 1114112): '))
        except ValueError:
            print('Вы ввели unicode не из range(0, 1114112)')
            unicode_code = int(input('Введите unicode из range(0, 1114112): '))


print_symbol()


# 5.2
def str_size():
    my_str = input('Введите строку: ')
    print(f'{my_str} > 10 символов!' if len(my_str) > 10 else my_str + (10 - len(my_str)) * '*')


str_size()


# 5.3
def my_min_max(floats: list):
    for i in range(len(floats) - 1):
        min_float = floats[i] if floats[i] < floats[i + 1] else floats[i + 1]
        max_float = floats[i] if floats[i] > floats[i + 1] else floats[i + 1]
    return round(min_float, 2), round(max_float, 2)


min_max_floats = my_min_max([float(input('Введите вещественное число: ')) for i in range(6)])
print(f'min = {min_max_floats[0]}; max = {min_max_floats[1]}.')

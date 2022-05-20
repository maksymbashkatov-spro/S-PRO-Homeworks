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
    min_float = floats[0]
    max_float = floats[0]
    for i in range(1, len(floats)):
        min_float = min_float if min_float < floats[i] else floats[i]
        max_float = max_float if max_float > floats[i] else floats[i]
    return round(min_float, 2), round(max_float, 2)


min_max_floats = my_min_max([float(input('Введите вещественное число: ')) for i in range(6)])
print(f'min = {min_max_floats[0]}; max = {min_max_floats[1]}.')

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


def str_size():
    my_str = input('Введите строку: ')
    print(f'{my_str} > 10 символов!' if len(my_str) > 10 else my_str + (10 - len(my_str)) * '*')


str_size()

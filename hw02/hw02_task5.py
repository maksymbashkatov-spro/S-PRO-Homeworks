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

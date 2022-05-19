def get_input():
    return input('Введите значение: ')


def test_input(may_int):
    try:
        int(may_int)
        return True
    except ValueError:
        return False


def str_to_int(may_int):
    return int(may_int)


def print_int(num):
    print(num)


may_int = get_input()
if test_input(may_int):
    print_int(str_to_int(may_int))

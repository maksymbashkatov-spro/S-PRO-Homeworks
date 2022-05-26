def fib_generator(n):
    num1, num2 = 0, 1
    for i in range(n):
        yield num1
        num1, num2 = num2, num1 + num2


def fib_list(n):
    f_lst = []
    f_gen = fib_generator(n)
    for i in range(n):
        f_lst.append(next(f_gen))
    return f_lst


# Тесты.
print('Первые 3 числа Фибоначчи.')
print(fib_list(3))

print('\n', 'Первые 15 чисел Фибоначчи.', sep='')
print(fib_list(15))

my_str = input('Введите строку: ')
upper_count = 0
lower_count = 0

for i in my_str:
    if i.isupper():
        upper_count += 1
    else:
        lower_count += 1

print(my_str.lower() if lower_count >= upper_count else my_str.upper())

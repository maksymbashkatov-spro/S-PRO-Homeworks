school = {'1а': 20, '1б': 25, '2б': 22, '6а': 18, '7в': 16}

school['1а'] += 1
school['3a'] = 24
del school['7в']
print('Общее количество учащихся в школе:', sum(school.values()))


def val_keys_swap(my_dict):
    return {v: k for k, v in my_dict.items()}


print('Исходный словарь', school)
print('Перевернутый словарь', val_keys_swap(school))

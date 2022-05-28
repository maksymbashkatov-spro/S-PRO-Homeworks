def str_without_punctuation(user_str):
    return ''.join(i for i in user_str if i.isalpha() or i == ' ')


print('Очистить предложение от знаков препинания.')
print(str_without_punctuation('Hello friend, how much does it cost?'))


def get_list_of_words(user_str):
    return str_without_punctuation(user_str).split()


print('\n', 'Получить список слов из предложения.', sep='')
print(get_list_of_words('Hello friend, how much does it cost?'))


def get_more_long_word(user_str):
    t_l1 = get_list_of_words(user_str)
    return max([i.lower() for i in t_l1], key=len)


print('\n', 'Получить самое длинное слово в предложении.', sep='')
print(get_more_long_word('Hello friend, how much does it cost.'))

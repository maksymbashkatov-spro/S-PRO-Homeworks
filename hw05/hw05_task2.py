from word_utils import str_without_punctuation, get_list_of_words, get_more_long_word

print('Очистить предложение от знаков препинания.')
print(str_without_punctuation('Hello friend 123, how much does it cost?'))

print('\n', 'Получить список слов из предложения.', sep='')
print(get_list_of_words('Hello friend, how much does it cost?'))

print('\n', 'Получить самое длинное слово в предложении.', sep='')
print(get_more_long_word('Hello friend, how much does it cost.'))

def str_without_punctuation(user_str):
    return ''.join(i for i in user_str if i.isalpha() or i.isnumeric() or i == ' ')


def get_list_of_words(user_str):
    return str_without_punctuation(user_str).split()


def get_more_long_word(user_str):
    t_l1 = get_list_of_words(user_str)
    return max([i.lower() for i in t_l1], key=len)

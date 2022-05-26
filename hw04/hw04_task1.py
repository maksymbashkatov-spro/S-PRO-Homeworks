import operator


def calc_from_str():
    """
    m_e_lst: math expression list, список с элементами математического выражения.
    """
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv}
    m_e_lst = input('Введите математическое выражение: ').split()

    if len(m_e_lst) != 3 or m_e_lst[1] not in ('+', '-', '*', '/'):
        raise FormulaError(m_e_lst)

    try:
        float(m_e_lst[0])
        float(m_e_lst[2])
    except ValueError:
        raise FormulaError(m_e_lst)

    return operators[m_e_lst[1]](int(m_e_lst[0]), int(m_e_lst[2]))


class FormulaError(Exception):
    def __init__(self, m_e_lst, message='моё исключение FormulaError'):
        self.m_e_lst = m_e_lst
        super().__init__(message)

    def __str__(self):
        return f'Данные {" ".join(self.m_e_lst)} являются невалидными.'


print(calc_from_str())

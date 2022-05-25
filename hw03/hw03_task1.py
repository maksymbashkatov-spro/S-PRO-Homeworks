from math import lcm
import operator


class Fraction:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den):
        self.__den = den

    def __add_sub_pattern(self, f2, sign):
        """
        Метод-шаблон для необходимых математических действий с объектами класса дробь.
        Сложение и вычитание дробей выполняется по математическим правилам,
        с нахождением НОК, если знаменатель у дробей разный.
        :param f2: объект класса Fraction
        :param sign: арифметический знак (+ или -)
        :return: кортеж (числитель, знаменатель)
        """
        operators = {'+': operator.add,
                     '-': operator.sub}
        if self.den == f2.den:
            num = operators[sign](self.num, f2.num)
            den = self.den
        else:
            LCM = lcm(self.den, f2.den)
            num = operators[sign](self.num * (LCM // self.den), f2.num * (LCM // f2.den))
            den = LCM
        return num, den

    def __sub__(self, f2):
        return self.__class__(*self.__add_sub_pattern(f2, '-'))

    def __add__(self, f2):
        return self.__class__(*self.__add_sub_pattern(f2, '+'))

    def __mul__(self, f2):
        """
        :return: новый объект Fraction являющийся результатом произведения дробей
        (2х других объектов Fraction) по математическим правилам
        """
        return self.__class__(self.num * f2.num, self.den * f2.den)

    def __truediv__(self, f2):
        """
        :return: новый объект Fraction являющийся результатом деления дробей
        (2х других объектов Fraction) по математическим правилам
        """
        return self.__class__(self.num * f2.den, self.den * f2.num)

    def __str__(self):
        return f'{self.num}/{self.den}'


# ---
f1 = Fraction(3, 7)
f2 = Fraction(4, 5)
print(f'f1 = {f1}')
print(f'f2 = {f2}')

f4 = f1 + f2
print(f'{f1} + {f2} = {f4}')

f3 = f1 - f2
print(f'{f1} - {f2} = {f3}')

f5 = f1 * f2
print(f'{f1} * {f2} = {f5}')

f6 = f1 / f2
print(f'{f1} / {f2} = {f6}')

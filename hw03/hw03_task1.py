from math import lcm
import operator


class FractionMixin:
    @staticmethod
    def __add_sub_pattern(f1, f2, sign):
        operators = {'+': operator.add,
                     '-': operator.sub}
        if f1.den == f2.den:
            num = operators[sign](f1.num, f2.num)
            den = f1.den
        else:
            LCM = lcm(f1.den, f2.den)
            num = operators[sign](f1.num * (LCM // f1.den), f2.num * (LCM // f2.den))
            den = LCM
        return num, den

    @staticmethod
    def add(f1, f2):
        return Fraction(*FractionMixin.__add_sub_pattern(f1, f2, '+'))

    @staticmethod
    def sub(f1, f2):
        return Fraction(*FractionMixin.__add_sub_pattern(f1, f2, '-'))

    @staticmethod
    def mul(f1, f2):
        return Fraction(f1.num * f2.num, f1.den * f2.den)

    @staticmethod
    def truediv(f1, f2):
        return Fraction(f1.num * f2.den, f1.den * f2.num)


class Fraction(FractionMixin):
    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        try:
            self.__num = int(f'{num}')
        except ValueError:
            print(f'{num} не является целым числом.')

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den):
        try:
            self.__den = int(f'{den}')
        except ValueError:
            print(f'{den} не является целым числом.')

    def __init__(self, num, den):
        self.num = num
        self.den = den

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

    def __add__(self, f2):
        return self.__class__(*self.__add_sub_pattern(f2, '+'))

    def __sub__(self, f2):
        return self.__class__(*self.__add_sub_pattern(f2, '-'))

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

    @classmethod
    def create_fraction_from_str(cls, f_str):
        return cls(*f_str.split('/'))

    def __str__(self):
        return f'{self.num}/{self.den}'


# Тесты.
f1 = Fraction(3, 7)
f2 = Fraction(4, 5)
print(f'f1 = {f1}')
print(f'f2 = {f2}')

print('\n', 'Тесты переопределённых методов.', sep='')
f4 = f1 + f2
print(f'{f1} + {f2} = {f4}')

f3 = f1 - f2
print(f'{f1} - {f2} = {f3}')

f5 = f1 * f2
print(f'{f1} * {f2} = {f5}')

f6 = f1 / f2
print(f'{f1} / {f2} = {f6}')

print('\n', 'Тест метода класса.', sep='')
f7 = Fraction.create_fraction_from_str('3/5')
print(f'{f7}\nчислитель - {f7.num}\nзнаменатель - {f7.den}')

print('\n', 'Тесты статических методов миксина.', sep='')
f8 = Fraction.add(f1, f2)
print(f'{f1} + {f2} = {f8}')

f9 = Fraction.sub(f1, f2)
print(f'{f1} - {f2} = {f9}')

f10 = Fraction.mul(f1, f2)
print(f'{f1} / {f2} = {f10}')

f11 = Fraction.truediv(f1, f2)
print(f'{f1} / {f2} = {f11}')

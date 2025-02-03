
# Task 3

# Fraction

# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) 
# з належною перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

from math import gcd
 

class Fraction:

    def __init__(self, numerator, denominator):

        # Перевіряєм знаменник на 0
        if denominator == 0:
            raise ValueError("Знаменник не може бути нулем.")
        
        # Спростимо дроби:
        divide = gcd(numerator, denominator)
        self.numerator = int(numerator/divide)
        self.denominator = int(denominator/divide)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    
    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def _sub__(self, other):
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Не можна ділити на нуль.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)
    
    def __eq__(self, other):
        return (self.numerator == other.numerator and other.denominator == self.denominator)

if __name__ == "__main__":
    x = Fraction(1, 2)
    print(x)
    y = Fraction(2, 8)
    print(y)
    result = x + y
    print(result)
    assert x + y == Fraction(3, 4); 'Щось не так'
    



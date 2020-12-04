from lec_2020.lec_13.fib import *


def main():
    n = int(input('Введите номер числа Фибоначчи: '))
    f = fib(n)
    print('Ваше число Фибоначчи:', f)


if __name__ == '__main__':
    main()

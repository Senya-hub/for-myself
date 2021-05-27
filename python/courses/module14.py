import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)


print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))


x_diff = x1 - x2
if x_diff == 0:
    x_diff = 1
y_diff = y1 - y2
k = y_diff / x_diff
b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)


def sum_numeral(num):
    summNumeral = 0

    for i in num:
        summNumeral += int(i)
    print('\nСумма цифр: ', summNumeral)
    return summNumeral

def number_of_digits(number):
    counter = 0
    number = int(number)

    while number != 0:
        counter += 1
        number //= 10
    print('Кол-во цифр в числе: ', counter)
    return counter

n = input('Введите число: ')

summa = sum_numeral(n)
counter = number_of_digits(n)
print('Разность суммы и кол-ва цифр: ', summa - counter)


def coup_first(num):
    part = ''
    partNum = ' '
    for i in num:
         if i == '.':
            partNum += part
            partNum += i
            part = ''
         else:
            part = i + part
    partNum += part
    return partNum

firstNumber = input('Введите первое число: ')
secondNumber = input('Введите второе число: ')

firstNum = coup_first(firstNumber)
print('\nПервое число наоборот: ', firstNum)
secondNum = coup_first(secondNumber)
print('Второе число наоборот: ', secondNum)
firstNum = float(firstNum)
secondNum = float(secondNum)
print('Сумма: ', firstNum + secondNum)


def min_divider(num):
    for i in range(2, num + 1):
        round = num % i
        if round == 0:
            print('Наименьший делитель, отличный от единицы: ', i)
            break

number = int(input('Введите число: '))

min_divider(number)



import math

def look_for_coin(x, y, r):
    newDistance = math.sqrt(x ** 2 + y ** 2)
    if newDistance > r:
        print('Монетки в области нет')
    else:
        print('Монетка где-то рядом')

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))

look_for_coin(x, y, r)


def count(f, s):
    u = []
    for n in range(f, s):
      n = str(n)
      for i in n:
        u.append(i)
      a = u[0]
      b = u[1]
      c = u[2]
      d = u[3]
      if a == c and a == d:
        print(n)
      elif b == c and b == d:
        print(n)
      elif a == b and a == c:
        print(n)


      u = []

f = int(input('Введите первый год: '))
s = int(input('Введите второй год: '))

count(f, s)
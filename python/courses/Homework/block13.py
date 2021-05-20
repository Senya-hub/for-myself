
# вычисление налога.-----------------------------------
def calculate_tax(price, tax):
  tax += 10
  print('После увеличения налога', tax)
  total = price + (price * tax / 100)
  print('В самой функции: ', total)
  return total

myPrice = float(input('Введите цену: '))
myTax = int(input('Введите налог (в %): '))

totalPrice = calculate_tax(myPrice, myTax)
print('Сумма после первого вызова функции: ', totalPrice)

new = int(input('Введите новый налог (в %): '))

totalPrice = calculate_tax(totalPrice, new)

print('Итоговая сумма: ', totalPrice)

# Определение большего числа.--------------------------
def numeral_count(number):
  if number < 0:
    print('Число отрицательное. Обнуляю.')
    return 0
  count = 0
  while number > 0:
    count += 1
    number //= 10

  return count

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))

backA = numeral_count(a)
backB = numeral_count(b)

if backA > backB:
  print('Первое число больше второго.')
elif backA < backB:
  print('Второе число больше первого.')
else:
  print('Равное кол-во цифр.')


print('Задача 1. Сумма чисел 2\n')

def summNumeral(nam):
  count = 0
  for i in range(1, nam + 1):
    count += i

  return count

namber = int(input('Введите число: '))
firstNumeral = summNumeral(namber)
secondNumeral = summNumeral(firstNumeral)

print('Сумма от 1 до ', namber, ' = ', firstNumeral)

print('Сумма от ', namber, ' до ', firstNumeral, ' = ', secondNumeral)


print('Задача 2. «Назад в будущее»\n')
import math

def gcd(first, second):
  number = math.gcd(first, second)

  return number

firstNumber = int(input('Введите первое число: '))
secondNumber = int(input('Введите второе число: '))
nod = gcd(firstNumber, secondNumber)

print('НОД = ', nod)


print('Задача 3. Приоритет задач\n')

def numeral_count(variable):
  if variable < 0:
    print('Функция обнуляется.')
    
    return 0
  
  i = 0
  while variable != 0:
    i += 1
    print(i)
    variable //= 10

  return i

quantity = int(input('Введите кол-во задач: '))
firstNumber = int(input('Введите число: '))
secondNumber = int(input('Введите число: '))
thirdNumber = int(input('Введите число: '))
fourthNumber = int(input('Введите число: '))

a = numeral_count(firstNumber)
b = numeral_count(secondNumber)
c = numeral_count(thirdNumber)
d = numeral_count(fourthNumber)

if (a > b) and (a > c) and (a > d):
  print('\nПервая задача на обработку: ', firstNumber)
elif (b > c) and (b > d) and (b > a):
  print('\nПервая задача на обработку: ', secondNumber)
elif (c > d):
  print('\nПервая задача на обработку: ', thirdNumber)
else:
  print('\nПервая задача на обработку: ', fourthNumber)


# Деление 1 на 2---------------------------------------
x = 1
count = 0
while x != 0:
  count += 1
  x /= 2
  print(x)
print('Итераций: ', count)

# Плотность планет.-------------------------------------
vFristPlanet = 1.43128e15  #км^3
vSecondPlanet = 6.254e13   #км^3
pEarth = 5.5153e12         #кг/км^3

mFristPlanet = float(input('Масса первой планеты: '))
mSecondPlanet = float(input('Масса второй планеты: '))

pFirstPlanet = mFristPlanet / vFristPlanet 
pSecondPlanet = mSecondPlanet / vSecondPlanet 

print('Плотность первой планеты: ', pFirstPlanet)
print('Плотность первой планеты: ', pSecondPlanet)

if abs(pEarth - pFirstPlanet) < abs(pEarth - pSecondPlanet):
  print('Плотность первой планеты ближе к плотности Земли')
else:
  print('Плотность второй планеты ближе к плотности Земли')

print('Задача 1. Возможности компьютера')
def count(num):
  i = 0
  while num != 0:
    num /= 2
    i += 1
    print(num)
  print('Количество делений = ', i)

number = int(input('Введите число: '))
count(number)


print('Задача 2. Тестирование\n')

def summ(num):
  x = 1
  i = 0
  while x < 2:
    x += num
    i += 1
  print('Кол-во прибавлений: ', i)

number = float(input('Введите число в эксп. форме: '))
summ(number)


print('Задача 3. Урок информатики\n')

def count(num):
  i = 0
  while num != 0:
    i += 1
    num //= 10

  return i

number = float(input('Введите число: '))
iteration = count(number)

print('Формат плавающей точки: x = ', number / 10 ** (iteration - 1), '* 10 **', (iteration - 1))


# Не брать сравнения с плавающей точкой------------------
if (1.1 + 2.2) == 3.3:
  print('Равна')
else:
  print('Не равна')
  print(1.1 + 2.2)

# ----------------------------------------------------
a = 1.0

while True:
  a += 1e-15
  print(a)

# Разность жутко мала
a = 1.1
b = 2.2
c = a + b
d = 3.3

if abs(c - d) < 1e-15:
  print('Равна')
else:
  print('Не равна')
  print(1.1 + 2.2)


print('Задача 1. Опять налоги\n')
import math

def budget(a, b):
  c = a + b
  d = (c - a)
 
  if math.floor(d) > 0:
    print('\nРезультат: Бюджет увеличится')
  else:
    print('\nРезультат: Бюджет не изменится')

tax = float(input('Введите бюджет страны: '))
new_tax = float(input('Новые поступления (налог): '))
budget(tax, new_tax)

print('Задача 2. Сравнение\n')

def egv(a, b, c):
  a = a + b
  if abs(a - c) < 1e-15:
    return True
  else:
    return False

firstNumber = float(input('Введите первое число: '))
secondNumber = float(input('Введите второе число: '))
thirdNumber = float(input('Введите третье число: '))
count = egv(firstNumber, secondNumber, thirdNumber)

print(count)
print('Задача 1. Робот')
def greeting():
 print('Привет!')
 print('Добро пожаловать!')

while True:
  a = input('Зайдёте? Да/Нет: ')
  if a == 'Да':
   greeting()
  print('Следующий.\n')

print('Задача 2. Провизия')
def food():
  a = int(input())
  b = int(input())
  print("Всего", a+b, "шт.")

print("Сколько мешков рыбы и мяса?")
food()
print("Сколько буханок белого и чёрного хлеба?")
food()
print("Сколько вёдер воды и молока?")
food()

print('Задача 3. Почта')
surname = 'Иванов'
name = 'Василий'
street = 'Пушкина'
hom = '32'
def mail(): 
  print('Фамилия: Иванов')
  print('Имя: Василий')
  print('Улица: Пушкина')
  print('Дом: 32\n')
  
mail()
mail()
mail()


print('Задача 1. Вода')

def water(price):
  print('\nНазвание: КлирВотер')
  print('Производитель: ВодЗавод')
  print('Цена: ', price)

water(25)
water(30)
water(40)


import math
print('Задача 2. Вот это объёмы 2')

def sphereArea():
  s = 4 * math.pi * radius ** 2
  print('Площадь сферы =', round(s, 4))
def sphereVolume():
  v = 4 / 3 * math.pi * radius ** 3
  print('Объём шара =', round(v, 4))

radius = float(input('\nВведите радиус планеты: '))
sphereArea()
sphereVolume()


print('Задача 3. Простые числа')
n = int(input('Введите кол-во чисел последовательности: '))
def isPrime():
  if number > 0:
    if number % 2 == 0 or number % 5 == 0:
      print('Число простое: ', number)
  else:
    print('Число составное: ', number)

for num in range(1, n + 1):
  print('Введите', num, 'число:', end = ' ')
  number = float(input())
  isPrime()


  Задача 1. Среднее арифметическое
# цикл
a = int(input('Введите левую границу: '))
b = int(input('Введите правую границу: '))
count = 0
col = 0

for num in range(a, b + 1):
  col = col + num 
  count += 1
summ = col / count
print(summ)

# функция
a = int(input('Введите левую границу: '))
b = int(input('Введите правую границу: '))
n = 0

def summ():
  n = (a + b) / 2
  print('Среднее:', n)
summ()

print('Задача 2. Почта 2')
def mail(surname, name, street, hom): 
  print('Фамилия:', surname)
  print('Имя:', name)
  print('Улица:', street)
  print('Дом:', hom)
  
mail('Иванов', 'Василий', 'Пушкина', 32)
print()
mail('Иванов', 'Петр', 'Пушкина', 38)
print()
mail('Иванова', 'Лена', 'Пушкина', 2)

print('Задача 3. GPS-навигатор 2.0')
import math

def myDistance(x, y):
  distance = math.sqrt(x ** 2 + y ** 2)
  print(distance)

def betweenDistance(x_1, y_1, x_2, y_2):
  distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 + y_1) ** 2) 
  print(distance)

choice = int(input('1 - расстояние до точки; 2 - расстояние между двуья точками.'))

if choice == 1:
  x = float(input('Введите координату икс: '))
  y = float(input('Введите координату игрек: '))
  myDistance(x, y)
elif choice == 2:
  x_1 = float(input('Введите координату икс первой точки: '))
  y_1 = float(input('Введите координату игрек первой точки: '))
  x_2 = float(input('Введите координату икс второй точки: '))
  y_2 = float(input('Введите координату игрек второй точки: '))
  betweenDistance(x_1, y_1, x_2, y_2)
else:
  print('Ошибка ввода!')
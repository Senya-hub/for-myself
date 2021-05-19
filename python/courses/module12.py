print('Задача 1. Сумма чисел')
n = int(input('Введите число: '))

def summNamber():
  summ = 0
  for num in range(1, n + 1):
    summ += num
  print('Я знаю, что сумма чисел от 1 до', n, 'равна', summ)

summNamber()


print('Задача 2. Функция в функции')
def test():
  print('Введите целое число:', end = ' ')
def positive():
  print('Положительное.')
def negative():
  print('Отрицательное.')

test()
num = int(input(''))
print()
if num > 0:
  positive()
else:
  negative()


print('Задача 3. Апгрейд калькулятора')


def meinMenu():
  print('\n1. Вывести сумму цифр.')
  print('2. Вывести минимальную цифру.')
  print('3. Вывести максимальную цифру.')
  choice = int(input('Введите пункт меню: '))
  if choice == 1:
    summ()
  elif choice == 2:
    minNumeral()
  elif choice == 3:
    maxNumeral()
  else:
    print('\nОшибка! Введите цифру от 1 до 4.')
    meinMenu()

def summ():
  summ_num = 0
  summ_cycle = number
  while summ_cycle != 0:
    a = summ_cycle % 10
    summ_num += a
    summ_cycle //= 10
  print('\nСумма цифр = ', summ_num)
  meinMenu()

def minNumeral():
  min_num = 10
  min_cycle = number
  while min_cycle != 0:
    a = min_cycle % 10
    if a < min_num:
      min_num = a
    min_cycle //= 10
  print('\nMинимальное число - ', min_num)
  meinMenu()

def maxNumeral():
  max_num = 0
  max_cycle = number
  while max_cycle != 0:
    a = max_cycle % 10
    if a > max_num:
      max_num = a
    max_cycle //= 10
  print('\nMинимальное число - ', max_num)
  meinMenu()


number = int(input('Введите число: '))
meinMenu()



print('Задача 4. Число наоборот\n')

def contra(number):
  contra = ''
  for sym in number:
    contra = sym + contra
  if int(contra) == 0:
    print('Программа завершена!')
  else: 
    print('Число наоборот: ', int(contra), '\n') 

number = input('Введите число: ')
contra(number)


print('Задача 5. Текстовый редактор\n')

def count_letters(text):
  n = 0
  k = 0
  print('Какую цифру ищем? ', end = '')
  numeral = input()
  print('Какую букву ищем? ', end = '')
  letter = input()
  for symbol in text:
    if symbol == numeral:
      k += 1
    if symbol == letter:
      n += 1
  print('\nКоличество цифр', numeral, ':', k)
  print('Количество букв', letter, ':', n)
    
text = input('Введите текст: ')
count_letters(text)


print('Задача 6. Монетка\n')
def coin(x, y):
  if (abs(x) <= 1) and (abs(y) <= 1):
    print('\nМонетка где-то рядом')
  else:
    print('\nМонетки в области нет')

x = float(input('Введите координату икс: '))
y = float(input('Введите координату игрек: '))
coin(x, y)


print('Задача 7. Опять?\n')

def minNum(a, b):
  min_namber = (a + b - abs(a - b)) / 2
  print('\nМинимальное число = ', int(min_namber))

a = int(input('Ввведите первое число: '))
b = int(input('Введите второе число: '))
minNum(a, b)


print('Задача 8. НОД\n')

def gcf(firstNum, secondNum):
  count = True
  while count:
    if firstNum == secondNum:
      print('\nНаибольший общий делитель = ', firstNum)
      count = False
    elif firstNum > secondNum:
      firstNum -= secondNum 
    elif firstNum < secondNum:
      secondNum -= firstNum
    else: 
      print('Ошибка! Что - то пошло, не так.')
      count = False

firstNum = int(input('Введите первое число: '))
secondNum = int(input('Введите второе число: '))
gcf(firstNum, secondNum)


print('Задача 9. Недоделка\n')

def rock_paper_scissors():
  print('Игра - "камень, ножницы, бумага"\n')
  word = input('Введите загаданное слово: ')
  if word == 'камень':
    print('Ничья. Давай еще раз.')
    rock_paper_scissors()
  elif word == 'ножницы':
    print('Ты проиграл. Камень бьёт ножницы.')
  elif word == 'бумага':
    print('Ты выиграл! Бумага кроет камень.')
  else:
    print('Ошибка ввода! Введи слово - камень или ножницы или бумага.')
    rock_paper_scissors()

def guess_the_number():
    print('Игра - "Угадай число"')
    while True:
      print('Введите число от 1 до 10: ', end = '')
      number = int(input()) 
      if number == 7:
        print('Молодец. Ты победил!')
        break
      else:
        print('\nНе верно! Попробуй еще раз.')

def mainMenu():
  print('Выбери игру: ')
  print('1. Камень, ножницы, бумага.')
  print('2. Угадай число.')
  numeral = int(input())
  if numeral == 1:
    rock_paper_scissors()
  elif numeral == 2:
    guess_the_number()
  else:
    print('\nОшибка ввода. Введите 1 или 2.')
    mainMenu()

mainMenu()


print('Задача 10\n')

def bedroom():
  print('\nВы в спальне. Куда идём?')
  print('1 - в коридор')
  print('2 - в ванну')
  numeral = int(input())
  if numeral == 1:
    corridor()
  elif numeral == 2:
    bathroom()
  else:
    print('Ошибка! Введите 1 или 2.')
    bedroom()
 
def corridor():
  print('\nВы в коридоре. Куда идем?')
  print('1 - в спальню')
  print('2 - в ванну')
  print('3 - на кухню')
  print('4 - в дверь')
  numeral = int(input())
  if numeral == 1:
    bedroom()
  elif numeral == 2:
    bathroom()
  elif numeral == 3:
    kitchen()
  elif numeral == 4:
    print('Поздравляю! Вы победили.')
  else:
    print('Ошибка! Введите цифру от1 до 4.')
    corridor()

def bathroom():
  print('\nВы в ванне. Куда идём?')
  print('1 - в коридор')
  print('2 - в спальню')
  numeral = int(input())
  if numeral == 1:
    corridor()
  elif numeral == 2:
    bedroom()
  else:
    print('Ошибка! Введите 1 или 2.')
    bathroom()

def kitchen():
  print('\nВы на кухне. Куда идём?')
  print('1 - в коридор')
  print('2 - в открытое окно')
  numeral = int(input())
  if numeral == 1:
    corridor()
  elif numeral == 2:
    print('Вы разбились! Вы проиграли.')
  else:
    print('Ошибка! Введите 1 или 2.')
    kitchen()

bedroom()
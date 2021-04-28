rain = int(input('На улице идёт дождь? '))
if rain == 1:
  print('Пошел дождь. Возмите зонтик!')
else:
  print('Дождя нет =)')

  rus_language = int(input('Введите кол-во баллов по русскому языку: '))
mach = int(input('Введите кол-во баллов по математике: '))
informatics = int(input('Введите кол-во баллов по информатике: '))
summ = rus_language + mach + informatics
if summ >= 270:
  print('Поздравляю, ты поступил на бюджет!')
else:
  print('К сожалению, ты не прошел на бюджет.') 

  date = int(input('Введите какое сегодя число: '))
balance = date/2 
if balance%1 == 0:
  print('Сегодня используем зубную нить!')
else:
  print('Сегодня число не четное.')

  chair1 = int(input('Введите стоимость 1-го стула: '))
chair2 = int(input('Введите стоимость 2-го стула: '))
chair3 = int(input('Введите стоимость 3-го стула: '))
sum = chair1 + chair3 + chair2 
if sum > 10000:
  sum = sum * 10 / 100
  print('Сумма со скидкой составит: ', sum)
else:
  print('Итого: ', sum)

  number = int(input('Введите число: ')) 
if number < 0:
  number = number * -1
  print('Ответ: ', number)
else:
  print('Ответ: ', number)

 guy = int(input('Кубик Кости: ')) 
owner = int(input('Кубик владельца: '))
if guy >= owner:
  debt = guy - owner
  print('Сумма: ', debt)
  print('Костя платит')
else:
  sum = guy + owner
  print('Сумма: ', sum)
  print('Владелец платит')
print('Игра окончена')

many = int(input('Введите сумму: ')) 
res = many % 100
if res > 0:
  print('Такую сумму снять невозможно. Обратитесь в другой банкомат.')

  hours = int(input('Введите количество отработанных часов: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите количество денег на еду: '))

sum = hours + credit + food
salary = (200*hours) / 2**3 + hours

if salary >= sum:
  print('Часов хватает. Можно отдохнуть.')
else:
  print('Часов не хватает. Придётся работать!')

  run = int(input('Введите пробег: '))
if run < 100:
  print('Введите 3х значное значение')
number = int(input('Введите номер дня: '))
a = run//100
b = run//10%10
c = run%10
sum = a + b + c
if sum > number:
  print('Сброс')
  run = 0
else:
  print('Сегодня не сломался')
print('Пробег: ', run)

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first > second:
  if first > third:
    print('Первое число больше всех', first)
  else:
    print('Третье число больше всех', third)
if second > first:
  if second > third:
    print('Второе самое большое число:', second)
  else:
    print('Третье число больше всех', third)
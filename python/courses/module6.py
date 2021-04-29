power = int(input("Введите кол-во раз: "))
count = 1
while count <= power:
  result = count ** 3
  print(result)
  count += 1
print("Программа закончена!")

name = input("Введите имя должника: ")
summ = int(input('Введите сумму долга: '))
debet = 0
returns = True
while returns:
   debt = int(input('Сколько рублей вы внесете прямо сейчас, чтобы её погасить? '))
   debet += debt
   print(debet)
   if debet >= summ:
     print('Отлично, Василий! Вы погасили долг. Спасибо!')
     balance = debet - summ
     returns = False
   else:
     print('Маловото, ', name, '. Давайте еще раз.')
print('Программа закончена! Остаток на счете: ', balance)

number = int(input('Введите число: '))
rotate = True
n = 0
while rotate:
  number = number // 10
  n += 1
  if number == 0:
    rotate = False
print('Кол-во десятичных знаков = ', n)

rotate = True
even = 0
not_even = 0
while rotate:
  number = int(input('Введите число: '))
  if number == 0:
    rotate = False
  elif number / 2 % 1 == 0:
    even += 1
    print('Число четное')
  else:
    print('Число не четное')
    not_even += 1
print('Кол-во четных чисел = ', even)
print('Кол-во не четных чисел = ', not_even)

rotate = True
n = 0
m = 0
while rotate:
  number = int(input('Введите номер билета или 0 для выхода: '))
  n = number // 1000
  m = number % 1000
  first = n%10 + (n//10%10) + (n//100)
  second = m%10 + (m//10%10) + (m//100)
  if number == 0:
    rotate = False
  elif first == second:
    print('Этот билет счастливый - ', first, ' = ', second)
  else:
    print('Билет не счастливый')
    print('Циклы для этой задачи не нужны и решение займет 6 строчек.')

rotate = True 
positive_number = 0
negative_number = 0
while rotate:
  number = int(input('Введите число: '))
  if number > 0:
    positive_number +=1
  elif number < 0:
    negative_number +=1 
  elif number == 0:
    rotate = False
print('Кол-во положительных чисел: ', positive_number)
print('Кол-во отрицательных чисел: ', negative_number)

print('Начался 8-часовой рабочий день')
rotate = 0
summ_task = 0
while rotate != 8:
  rotate += 1
  print(rotate, ' час')
  task = int(input('Сколько задач решит Максим? '))
  summ_task += task
  phone = int(input('Звонит жена. Взять трубку?'))
print('Рабочий день закончился. Всего выполнено задач: ', summ_task) 
if phone > 0:
  print('Нужно зайти в магазин')
else:
  print('Не надо заходить в магазин')

x = int(input('Введите сумму вклада: '))
p = int(input('Введите ежегодный процент: '))
y = int(input('Введите итоговую желаемую сумму: '))
profit = 0
term = 0
while profit < y:
  term += 1
  year = (x*p//100) 
  profit += year
  print(profit)
print('Сумма достигнет ', y, ' рублей через ', term, ' лет')

riddle = int(input('Загадайте число: '))
rotate = True
n = 0
while rotate:
  number = int(input('Введите число: '))
  n += 1
  if number == riddle:
    print('Вы угадали! Число попыток: ', n)
    rotate = False
  elif number > riddle:
    print('Число больше, чем нужно. Попробуйте ещё раз!')
  elif number < riddle:
    print('Число меньше, чем нужно. Попробуйте ещё раз!')

print('Загадай число от 0 до 100')
n = 100
m = 1
i = 0
while True:
  variable = (n + m) // 2
  i += 1
  print('Твое чило- ', variable)
  number = int(input('Число больше-2, меньше-3 или равно-1: '))
  if number == 1:
     print('Твое число - ', variable)
     break
  elif number == 2:
    m = variable + 1
  else:
     n = variable - 1
print('Число попыток: ', i)
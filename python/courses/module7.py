for number in 114, 12, 14, 10605, 4907, 450, 20:
  if number % 2 == 0:
    if number % 3 != 0:
      print('Число подходит.', number)
    else:
      print('Число не подходит. ', number)
  else: 
    print('Число не соответствует. ', number)

    i = 0
for amout in range(10):
   number = int(input('Введите число: '))
   if number % 2 == 0:
    number > 0
    print('Четное и положительное число: ', number)
    i += 1
   else:
    print('Число не подходит.')  
print('Всего четных и положительных чисел: ', i)

summ = 0
for m in range(12):
   salary = int(input('Введите за месяц зарплату: '))
   summ += salary
   print(summ)
medium = summ // 12
print('Средняя зарплата за год: ', medium)

i = 0
for sector in range(30, 35+1):
    number = str(sector)
    people = int(input('Людей в ' + number + ' секторе: '))
    if people < 10:
      print('Все спокойно.')
    else:
      print('Нарушение! Слишком много людей в секторе.')
      i += 1  
print('Количество нарушений: ', i)

factorial = 1
n = int(input('Введите число: '))
for number in range (1, n+1):
  factorial *= number
print('Факториал числа ', n, ' равен ', factorial)

rating3 = 0
rating4 = 0
rating5 = 0
child = int(input('Сколько человек в классе: '))
for number in range (1, child + 1):
  num = str(number)
  rating = int(input('Введите оценку ' + num + ' ученику - '))
  if rating == 3:
    print('удовлетворительно')
    rating3 += 1
  elif rating == 4:
    print('хорошо')
    rating4 += 1
  elif rating == 5:
    print('отлично')
    rating5 += 1
  else: 
    print('Такую оценку ставить нельзя.')
if (rating3 > rating4) and (rating3 > rating5):
  print('Троечников больше всех: ', rating3)
elif (rating4 > rating5) and (rating4 > rating3):
  print('Хорошистов больше всех: ', rating4)
else:
  print('Отличников больше всех: ', rating5)

  a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
i = 0
total = 0
for number in range(a, b):
  if number % 3 == 0:
    total += number
    print('Накопительное кратное три - ', total)
    i += 1
amount = total // i
print('Среднее арифметическое чисел кратное трем: ', amount)

for number in range(10, 99):
  if number % 3 == 0:
    print('Двухзначные числа равные утроеному произведению: ', number)

fun = 0
i = 0
for compare in range(1, 11):
  number = int(input('Введите число: '))
  if fun < number:
    print('число упорядочено по возрастаию ', number)
    fun = number
    i += 1
  else:
    print('Число не упорядочено ', number)
print()
print('Упорядоченных месяцев: ', i) 

card = int(input('Введите кол-во карточек: '))
total_card = 0
total_summ = 0
for number in range(1, card + 1):
  total_card += number
print('Итоговая сумма: ', total_card)
for summ_namber in range(1, card):
  namber_card = int(input('Введите номера карточек: '))
  total_summ += namber_card
print('Сумма номеров карточек: ', total_summ)
total_ask = total_card - total_summ
print()
print('Номер отсутсвующей карточки - ', total_ask)
trial = int(input('Введите количество опыта: '))
if (trial > 0) and (trial <= 1000):
  print('Ваш уровень: 1')
elif (trial > 1000) and (trial <= 2500):
  print('Ваш уроветь: 2')
elif (trial > 2500) and (trial <= 5000):
  print('Ваш уроветь: 3')
else:
  print('Ваш уроветь: 4')

  a = int(input('Введите первую переменную: '))
b = int(input('Введите вторую переменную: '))
c = int(input('Введите третью переменную: '))
if (a>b) and (a>c):
  print('Максимум переменная a')
elif (b>c) and (b>a):
  print('Максимум переменная b')
else:
   print('Максимум переменная c')

x = int(input('Введите икс: '))
if x > 0:
  y = x - 12
  print('Игрек равен ', y)
elif x == 0:
  y = 5
  print('Игрек равен ', y)
elif x < 0:
  y = x**2
  print('Игрек равен ', y)

  list = int(input('Введите место в списке поступающих: '))
score = int(input('Введите количество баллов за экзамены: '))
if score >= 290:
  print('Поздравляем, Вы поступили!')
  if (list < 10) and (list > 0):
    print('Бонусом Вам будет начисляться стипендия')
  else:
    print('Но Вам не хватило баллов для стипендии')
else:
  print('Вы не поступили.')

 rating = int(input('Что получил по математике? '))
if rating == 2:
    print('Плохо. Марш учиться!')
if rating == 3:
    print('Плохо. Марш учиться!')
if rating == 4:
    print('Молодец! Можешь отдохнуть.')
if rating == 5:
    print('Молодец! Можешь отдохнуть.')

 umber = int(input('Введите двухзначное число: '))
if (number > 10) and (number < 100) or (number < -10) and (number > -100):
  print('Двухзначное число.')
else:
  print('Введите корректное число.')

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
if (number1 == number2) and (number1 == number3):
  print('3')
elif (number1 == number2) or (number1 == number3) or (number2 == number3):
  print('2')
else:
  print('0')

area = int(input('Введите площадь квартиры: '))
price = int(input('Введите стоимость квартиры: '))
if (area > 100) and (price < 10):
  print('Данный вариант подходит')
elif (area > 80) and (price < 7):
  print('Данный вариант подходит')
else:
  print('Данный вариант не подходит')

price = int(input('Введите сумму дохода: '))
if price > 50000:
  tax = (30*(price-50000) / 100) + (20*40000/100) + (13*10000/100)
  print('Cумма налога составляет: ', tax)
elif price > 10000:
  tax = (20*(price-10000) / 100) + (13*10000/100)
  print('Размер налога составляет: ', tax)
elif price > 0:
  tax = price*13/100
  print('Размер налога: ', tax)
else:
  print('Размер налога: 0')

time_work = int(input('Введите время в часах: '))
if (time_work > 8) and (time_work < 10) or (time_work > 12) and (time_work < 14) or (time_work > 15) and (time_work < 18) or (time_work > 20) and (time_work < 22):
  print('Можно получить посылку')
else:
  print('Посылку не получить. Попробуйте другое время.')

# Второй вариант решения
time_work = int(input('Введите время в часах: '))
if (time_work != 9) and (time_work != 13) and (time_work != 16) and (time_work != 17) and (time_work != 21):
  print('Посылку получить нельзя.')
else:
  print('Посылку можно получить.')
bank = int(input('Сколько денег на счету? '))
if bank > 75000:
  bank -= 75000
  print('Курс успешно приобретен')
  if bank < 5000:
    bank += 1000
    print('Вам начилена скидка 1000руб.')
else:
  print('Не хватает денег на счету')
print('Хорошего дня!')
print('Остаток на счете: ', bank)
#----------------------------------
x = int(input('Введите икс: '))
y = int(input('Введите игрек: '))
if x >= y:
  if x > y:
    print('X больше Y')
  else:
    print('X равно Y')
else:
  print('X меньше Y')
  #--------------------------------
many = int(input('Кол-во денег? '))
cheese = 60
ice = 20
if many >= cheese:
  print('На сыр денег хватило')
  many -= 60
  if many >= 20:
    print('И на мороженое тоже')
    many -= 20
  else:
    print('На мороженое не хватает')
else:
    print('Денег маловато')
#-------------------------------------
x = int(input('Введите икс: '))
y = int(input('Введите игрек: '))
if x > y:
  print('X больше Y')
elif x < y:
  print('X меньше Y')
else:
  print('X равно Y')
#-------------------------------------
income = int(input('Введите сумму прибыли: '))
if income >= 0:
  if income < 10000:
    tax = income * 13 / 100
    print('Сумма налога 13% равна: ', tax)
  elif income < 50000:
    tax = income * 20 / 100
    print('Сумма налога 20% равна: ', tax)
  else:
    tax = income * 30 / 100
    print('Сумма налога 30% равна: ', tax)
else:
  print('Ошибка: доход не может быть отрицательным')
#-----------------------------------------
coin1 = int(input('Введите вес первой мотеты: '))
coin2 = int(input('Введите вес второй мотеты: '))
coin3 = int(input('Введите вес третьей мотеты: '))
if coin1 == coin2:
    print('Фальшивая третья мотета')
elif coin1 < coin2:
    print('Фальшивая первая мотета')
else:
  print('Фальшивая вторая монета')
#-----------------------------------------
bicycle = int(input('Введите год выпуска велосипеда: '))
speeds = int(input('Введите кол-во скоростей: '))
if bicycle >= 2018 and speeds >= 24:
    print('Отлично. Покупаем этот велосипед.')
else:
  print('Рухлять не рассматривать вообще.')
if bicycle < 2018:
      print('Не покупаем, старый велосипед!')
elif speeds < 24:
      print('Не покупаем, мало скоростей.')
#-------------------------------------------
score = int(input('Сколько баллов набрал? '))
medal = int(input('Есть медаль? '))
if score >= 280 and medal == 1:
    print('Поздравляем! Ты поступил!')
else:
  print('К сожалению, ты не прошел в наш университет.')
#--------------------------------------------
t = int(input('Введите температуру: '))
if t >= 0 and t <= 100:
    print('Среда в допустимых рамках.')
else:
  print('Опасность. Температура вышла за допустимые рамки.')
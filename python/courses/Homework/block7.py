for meters in 100, 90, 95, 87, 102:
 if meters % 3 == 0:
   print(meters, 'Подходит')
 else:
   print(meters, 'Не подходит')
#--------------------------------------
for number in 3, 7, 5, 6, 4:
  two = number ** 2
  three = number ** 3
  four = number ** 4
  print(two, three, four) 
  #-------------------------------------
  i = 0
for number in 345, 19, 87, 1020, 421, 555, 55:
  if number // 100 != 0:
    if number % 5 == 0:
      i += 1
      print('Номер выигрышный! ', number)
print('Кол-во победителей: ', i) 

for number in range(11):
  scuare = number ** 2
  print(scuare)   
#------------------------------------
hour = int(input('Который час? '))
for number in range(hour):
  print('Ку-ку')
#-------------------------------------
for number in range(21):
  summ = 2 ** number
  print(summ)

  for number in range(1, 11):
  summ = number ** 3
  print(summ)
#-----------------------------
start_number = int(input('Введите первое число: '))
end_number = int(input('Введите последнее число: '))
number = 0
summ = 0
for number in range(start_number, end_number+1):
   summ += number
   print(number)
print('Сумма чисел от ', start_number, ' до ', end_number, ' равна ', summ)
#-----------------------------
wake_up = int(input('Во сколько проснулся: '))
awake_hours = 0
calories_sum = 0
for hours in range(wake_up, 23):
  print('Ceйчас ', hours, ' часов')
  colorias = int(input('Cколько съел за час: '))
  calories_sum += colorias
  if calories_sum > 2000:
    print('Хорошо поел, хорошо поспал!') 
    break
  awake_hours += 1
print('Съедено калорий за день ', calories_sum) 
print('Часов не спал: ', awake_hours)
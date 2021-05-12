print('Задача 1. Календарь')
day = input('Введите день недели: ')
week = 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'
namberDay = 0

for d in week:
  namberDay += 1
  if d == day:
    print('Номер дня недели: ', namberDay)



print('Задача 2. Я стал новым пиратом!')
wordKey = 'Карамба'
i = 0

for number in range(10):
  word = input('Введите слово: ')
  if word == wordKey:
    i += 1
print('Попадут на борт ', i, ' человека')


print('Задача 3. Кривой мессенджер')
text = input('Введите текст: ')
i = 0

for symbol in text:
  i += 1
  if symbol == '*':
    print('Символ * стоит на позции ', i)


print('Задача 4. Театр')
rows = int(input('Введите кол-во рядов: '))
seats = int(input('Введите кол-во сидений в ряде: '))
distance = int(input('Введите кол-во метров между рядами: '))
print('\nСцена\n')

for number in range(rows):
  print('=' * seats, end = ' ')
  print('!' * distance, end = ' ')
  print('=' * seats)




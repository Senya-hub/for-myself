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


print('Задача 5. Марсоход 2')
print('В какую сторону направить робота - W(север), S(юг), A(запад), D(восток)')
print('Выход из игры, любая другая клавиша!\n')
x = 8
y = 10
get = True

while get:
  print('Марсоход находится на позции ', x, y, end = ' ')
  traffic = input('введите команду:\n')
  if traffic == 'w':
    x += 1
    if x >= 15:
      x = 15
  elif traffic == 's':
    x -= 1
    if x <= 0:
      x = 0
  elif traffic == 'd':
    y += 1
    if y >= 20:
      y = 20
  elif traffic == 'a':
    y -= 1
    if y <= 0:
      y = 0
  else:
    print('Выход из игры!')
    get = False


print('Задача 6. Спецшифр')
string = input('Введите строку: ')
prevSyn = ''
i = 1
n = 1

for letter in string:
  if letter == prevSyn:
    i += 1
  elif letter != prevSyn:
    prevSyn = letter
    i = n
  if i > n:
    c = i
print('Самая длинная последовательность: ', c)


print('Задача 7. Великий и могучий')
text = input('Введите текст: ')
i = 1
c = 0

for letter in text:
  if letter != ' ':
    i += 1
  elif letter == ' ':
    i = 0
  if i > c:
    c = i
 
print('Длина самого длинного слова: ', c)


print('Задача 8. Колонтитул')
footer = int(input('Введите общую длину колонтитула в символах: '))
point = int(input('Введите кол-во восклицательных знаков: '))
print('\n')

for letter in range(footer):
  if letter < (footer - point) // 2:
    print('~', end = '')
  elif letter < (footer + point) // 2:
    print('!', end = '')
  else:
    print('~', end = '')
print('\n')


print('Задача 9. Коровы')
string = input('Введите строку с привязкой коров к стоилу: ')
i = 0
m = 0

for letter in string:
  i += 2
  if letter == 'b':
    m += i
print('Произведено молока за день: ', m)

print('Задача 10. Метод бутерброда')
letter = input('Введите зашифрованное сообщение: ')
i = 0
symbols = ''
symbolw = ''

for symbol in letter:
  i += 1
  if i % 2 != 0:
    symbols += symbol
  else:
    symbolw = symbol + symbolw 

print(symbols + symbolw) 

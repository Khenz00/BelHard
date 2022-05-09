def calc(number_1,number_2,operation):
    if operation == '+':
      print(number_1+number_2)
    elif operation == '-':
      print(number_1-number_2)
    elif operation == '*':
      print(number_1*number_2)
    elif operation == '/':
      print(number_1/number_2)
    try:
      print(number_1/number_2)
    except ZeroDivisionError:
      print('Деление на ноль!')
    else:
     print(number_1/number_2)
number_1 = int(input('Введите первое число: '))
operation = input('Введите операцию')
number_2 = int(input('Введите второе число: '))
count = 1
while operation!='stop':
       calc(number_1,number_2,operation)
       if operation!= 'stop':
           number_1 = int(input('Введите первое число: '))
           number_2 = int(input('Введите второе число: '))
       count+=1
       print(f'было выполнено {count}')
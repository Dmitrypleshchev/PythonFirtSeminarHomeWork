# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

print('Введите шестизначное число:')
number = input()
if len(number) != 6:
  print('Введенное Вами число не шестизначное')
else:
  sum1 = 0
  sum2 = 0
  for elements in range (len(number)//2):
    sum1 += int(number[elements])
    sum2 += int(number[len(number)//2 + elements])
  if sum1 == sum2:
    print(f'{number}', '- yes')
  else:
    print(f'{number}', '- no')


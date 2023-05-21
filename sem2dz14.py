#  Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input('vvedite chislo '))
num = 0
while  2**num <= n:
  print(2**num)
  num+=1
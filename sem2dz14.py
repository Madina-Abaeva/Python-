#  Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input('vvedite chislo '))
num = 0
i=0
for i in range(n):
    num= 2**i
    if num <= n :
        print(f'chislo {num}')
else :
  quit()

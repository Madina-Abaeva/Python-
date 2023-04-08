# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
print('Vvedite chislo')
n = int (input())
summa = 0 
if n < 1000 and n > 99 :
  while n > 0 :
    summa = summa + n % 10
    n =float(n) / 10
  print(int(summa))
else:
  print(" ne yavlyaetsya trexznachnim chislom")
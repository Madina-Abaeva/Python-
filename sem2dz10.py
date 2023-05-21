# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
# число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
n = input('vvedite znachenie vsex monetok ')
orel=0
rech =0
for i in  range(len(n)): 
  if int(n[i])==1:
   orel+=1
  elif int(n[i])==0:
    rech+=1
if orel < rech :
    print(f'perevernut {orel} orlov')
else:
    print(f'perevernut {rech} rechek')
      
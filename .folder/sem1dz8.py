# Задача 8: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*3 2 4 -> yes
# 3 2 1 -> no
width=int(input("vvedite shirinu shokoladki "))
length=int(input("vvedite dlinu shokoladki "))
n=int(input("vvedite kolichestvo dolek "))
if n<=width*length :
 if(n%width or n%length):
  print("da")
 else:
  print("net")
else:
    print(("vvedennoe chislo nekorrektno "))

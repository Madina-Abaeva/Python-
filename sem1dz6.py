# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и 
#получали билет с номером. Счастливым билетом называют такой билет
#с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
#программу, которая проверяет счастливость билета.
#*Пример:*385916 -> yes   123456 -> no
N= int(input("Vvedite shestiznachniy nomer "))

if len(str(N))==6:

 firsthalf=N//1000
 onenum=firsthalf//100
 twonum=firsthalf//10%10
 threenum=firsthalf%10

 secondhalf=N%1000
 onenum2=secondhalf//100
 twonum2=secondhalf//10%10
 threenum2=secondhalf%10

 if (onenum+twonum+threenum)==(onenum2+twonum2+threenum2):
  print("счастливый")
 else:
  print("net")
else:
 print("ne shestiznachniy nomer")

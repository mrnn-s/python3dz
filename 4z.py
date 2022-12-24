#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Num= 45
drob = []
while True:
    drob.append(Num%2)
    Num = Num//2
    if Num//2 == 0 and Num != 1:
        break
print(drob,end=" ",sep=", ")
#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fibonachi(Num):
    if Num == 1 or Num == -1:
        return 1
    elif Num == 0:
        return 0
    else:
        if Num > 0:
            return Fibonachi(Num-1) + Fibonachi(Num-2)
        elif Num < 0:
            return Fibonachi(Num+2) - Fibonachi(Num+1)

k = int(input('enter k for fibonachi'))
fib_numb = []
for i in range(-k,k+1):
    fib_numb.append(Fibonachi(i))
print(fib_numb)
#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

my_list= [2, 3, 4, 5, 6]
para=[]
print (f'length list {len(my_list)}')
if len(my_list)%2 !=0:
    for i in range(len(my_list)//2+1):
        para.append(my_list[i]*my_list[len(my_list)-i-1])
else:
    for i in range(0, len(my_list)//2):
      para.append(my_list[i]*my_list[len(my_list)-i-1])
print(para)
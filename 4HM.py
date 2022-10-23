#4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.

from random import randint
a = [ ]     
n = int(input("Введите число: "))  
for i in range (n):  
    number = randint(-n, n)   
    a.append (number)    
print (a)

def move_array(arr: a, n: int):
    output = list()
    for i in range(n):
        output.append(arr[(i - 2) % len(arr)])
    return output

new_arr = move_array(a, len(a))
print (new_arr)
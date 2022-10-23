# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.

number = int(input("Введите число: "))
nums=[]
value=1
for i in range(1, number+1):
    nums.append(value)
    value*=i+1
    print(i)
    print(nums)

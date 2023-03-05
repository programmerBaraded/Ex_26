# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def stepen (nam_a, nam_b):
    if nam_b == 1:
        return nam_a
    else:
        return (nam_a * stepen (nam_a, nam_b - 1))
nam_a = int(input("Введите число: "))
nam_b = int(input("Введите степень: "))
print (stepen(nam_a, nam_b))
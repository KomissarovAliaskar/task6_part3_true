mas = []
number = int(input())
for i in range(number):
    n = int(input())
    mas.append(n)
x = int(input())
str = mas[0:x]
del mas[0:x]
mas = mas + str
print(mas)

mas = []
number = int(input())
for x in range(number):
    str = int(input())
    mas.append(str)
mas.sort()
mas.append(mas[len(mas) - 1])
mx = 1
for i in range(len(mas)):
    if mas[i] > 0:
        if mas[i] + 1 != mas[i+1]:

            mx = mas[i] + 1
            break
if mx == 1:
    print(mx)
else:
    print(mx)

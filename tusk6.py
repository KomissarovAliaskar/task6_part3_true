number = int(input())
for c in range(number):
    str = input()
    mas = []
    mas2 = []
    for i in range(len(str)):
        if str[i] == '(' or str[i] == '[' or str[i] == '{':
            mas.append(str[i])
        if str[i] == ')':
            if mas[len(mas) - 1] == '(':
                mas.pop()
            else:
                mas2.append(str[i])
        if str[i] == ']':
            if mas[len(mas) - 1] == '[':
                mas.pop()
            else:
                mas2.append(str[i])
        if str[i] == '}':
            if mas[len(mas) - 1] == '{':
                mas.pop()
            else:
                mas2.append(str[i])
    if mas == [] and mas2 == []:
        print("YES")
    else:
        print("NO")

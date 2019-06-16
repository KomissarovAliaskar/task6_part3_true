number = int(input())
for c in range(number):
    str = input()
    mas = []
    for i in range(len(str)):
        if str[i] == '(' or str[i] == '[' or str[i] == '{':
            mas.append(str[i])
        if str[i] == ')' and mas[len(mas) - 1] == '(':
            mas.pop()
        if str[i] == ']' and mas[len(mas) - 1] == '[':
            mas.pop()
        if str[i] == '}' and mas[len(mas) - 1] == '{':
            mas.pop()
    if mas == []:
        print("YES")
    else:
        print("NO")

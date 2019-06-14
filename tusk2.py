
def sort_by_length(str):
    return len(str)
mas = []
number = int(input())
for i in range(0,number):
    str = input()
    mas.append(str)
mas.sort(key = sort_by_length)
print(mas)

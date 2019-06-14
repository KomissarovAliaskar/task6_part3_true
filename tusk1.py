str = input()
verh = 0
niz = 0
for i in range(0, len(str)):
    if str[i].isupper():
        verh = verh + 1
    elif str[i].islower():
        niz = niz + 1
print("Заглавных букв: ", verh * 100 / len(str) , '%')
print("Прописных букв", niz * 100 / len(str),'%')

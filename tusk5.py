
def oksh(str1,str2):
    for i in str1:
        for x in str2:
            if i == x:
                return True
    return False

number = int(input())
for i in range(number):
    s1 = input()
    s2 = input()
    s1 = set(s1)
    s2 = set(s2)
    if oksh(s1,s2) is True:
        print('YES')
    else:
        print('NO')

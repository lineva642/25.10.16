n = int(input())
f = open('input.txt')
l = f.read().split('\n')
A = []
a = {}
for i in range(n):
    A.append(input())
for i in A:
    for j in l:
        if i in j.split(':')[1].split():
            a[j] = i
B = []
for i in a:
    B.append(i.split(' : '))
for i in B:
    print(i[0], ':', i[1])

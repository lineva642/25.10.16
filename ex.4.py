import string
A=[]
with open('slovar','r') as dict:
    for i in dict:
        A.append(i.rstrip())
B=[]
with open('input.txt','r') as f:
    for i in f:
        B.append(i)

english=[]
russian=[]
for i in range(len(A)):
    A[i]=A[i].split('\t-\t')
    english.append(A[i][0])
    russian.append(A[i][1])
ru_en={english: russian for russian,english in zip(russian,english)}

def trans(A):
    p=set(string.punctuation)
    sp=''.join(x for x in A if x not in p)
    s=sp.lower().split(' ')
    for i in range(len(s)):
        if s[i] in ru_en:
            s[i]=ru_en[s[i]]
    return ' '.join(s)
for i in range(len(B)):
    print(B[i])
    print(trans(B[i]))







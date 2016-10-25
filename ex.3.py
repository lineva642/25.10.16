import string

def key_max_val(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

f = open('/usr/share/licenses/python/LICENSE','r')
f = f.read()
p = set(string.punctuation)
sp = ''.join(x for x in f if x not in p)
s = sp.lower()

d = {}
for i in s.split():
    if i in d:
        d[i] += 1
    else:
        d[i] = 1


for i in range(10):
    a = key_max_val(d)
    print(a, d[a])
    del d[a]

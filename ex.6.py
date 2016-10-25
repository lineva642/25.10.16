dic = dict()
sl = open('input_1.txt')
slt = open('ru-en.txt', 'w')
a = sl.readline().rstrip()
while len(a) > 0:
    en_trans, ru_trans = list(a.split('\t-\t'))
    if ',' in ru_trans:
        for i in ru_trans.split(','):
            i = i.lstrip()
            if i in dict:
                dic[i] = dic[i]+', '+en_trans
            else:
                dic[i] = en_trans
    else:
        if ru_trans in dict:
            dic[ru_trans] = dic[ru_trans]+', '+en_trans
        else:
            dic[ru_trans] = en_trans

    a = sl.readline().rstrip()

key_sort = sorted(dic.keys())
for i in key_sort:
    print('\t-\t'.join((i, dic[i])), file=slt)

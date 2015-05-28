1. slovar = {"a":1,"b":2,"c":3,"d":4}
res = dict((k, v**v if v % 2 != 0 else v) for k, v in slovar.items())
print(res)


2. alist=[2,4,4,5,1,6,1,7,89,3,2,1]
res = dict((i, alist.count(i)) for i in alist)
print(res)

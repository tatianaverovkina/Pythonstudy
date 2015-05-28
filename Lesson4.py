'''def listsum(a,n):
    res = sum([ x for x in a if x % n == 0])
    return res


assert(listsum([5,8,15,30,47],10)) == 30
assert(listsum([5,8,15,34,47],2)) == 42
assert(listsum([1,6,12,30,47],6)) == 48'''


# Функция что делает лист умноженный сам на себя в степени
def funct(a):
    res = ([x ** x for x in a])
    return res

a = [1,2,3,4]
print(funct(a))


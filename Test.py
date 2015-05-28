def listsum(numlist,n):
    result = 0
    for i in numlist:
        if i % n == 0:
            result+= i
    return result
    


assert(listsum([5,8,15,30,47],10)) == 30
assert(listsum([5,8,15,34,47],2)) == 42
assert(listsum([1,6,12,30,47],6)) == 48

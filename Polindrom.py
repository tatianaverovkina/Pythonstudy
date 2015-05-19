''' получить сумму четных элеменотов в массиве и multiply result to last element'''

'''
def sumeven(name):
    amount = 0
    for i in name[::2]:
        print(i)
        amount += i
    print(amount)
    print(amount * name[-1])


sumeven([1,2,3,4,5,6,7,8,9])'''

def ispalindrome(word):
    word = word.replce(" ","")
    draw = word[::-1]
    if draw == word:
       return True, print('This is a palindrom')
    else:
        print('This is not a palindrom')


ispalindrome('mama eats breakfast')

    




    
            
    



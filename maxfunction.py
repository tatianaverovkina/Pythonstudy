# max function with teo argument
def max(a,b):
    if a >= b:
        return a
    else:
        return b
    
# max function with three arguments

def max(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

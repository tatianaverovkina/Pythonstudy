Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

def frame(lst):
    maxlen = 0
    for i in lst:
        x = len(i)
        if x > maxlen:
            maxlen = x
    print ('*'*(maxlen+2))
    for word in lst:
        print('*'+word + ((maxlen - len(word))* " ") + '*')
    print ('*'*(maxlen+2))

frame(["Hello", "World", "in", "a", "frame"])'''

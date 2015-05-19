Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
list1 = [1,2,3]
list2 = ['a','b','c']
'''new_list = []
# 1st solution
for i in range(len(list1)):
     new_list = str(list1[i]) + list2[i]'''
# 2nd solution
print(''.join(str(i)+j for i,j in zip(list1,list2)))

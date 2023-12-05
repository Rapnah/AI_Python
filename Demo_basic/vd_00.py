#bai tap 1
#print("Hello The!")

#bai tap 2
"""
if 6 <  1:
    print("6 nho hon 1 la sai")
else:
    print("6 lon hon 1")
"""

#bai tap 3.1
"""
a="1"
b="the"
print(a,b)
"""
#bai tap 3.2
"""
a=str(1)	#ki tu
b=int(2)	#so
c=float(3)	#so thap phan
print(a, b, c)
"""
#bai tap 3.3
"""
d=3
b="the"
a=3.0
print(type(d))
print(type(b))
print(type(a))
"""
#bai tap 3.4
"""
a="the"
b='the'
print(a,b)
"""
#bai tap 3.5
"""
a='the'
A=1
print(a, A)		#A se khong ghi de len a
"""
#Bai tap 3.6
"""
myvar = 'the'
my_var='the'
MYVAR=1
_my_var=3
myVar='huynh'
myvar2=0.2
print(myvar, myVar, MYVAR, myvar2, _my_var, my_var)
"""
#bai tap 3.7
"""
aiBiCi="The"	#camel case: tru chu dau, tat ca chu con lai bat dau bang chu in hoa
AiBiCi='the'	#pascal case: tat ca cac chu bat dau bang chu in hoa
ai_bi_ci=1		#snake case: cac chu duoc cach voi nhau bang dau gach duoi
print(aiBiCi,AiBiCi,ai_bi_ci)
"""
#bai tap 3.8
"""
a,b,c = "orange", 'watermelon', 'dragonfruit'
d=e=f=1
print(a)
print(b)
print(c)
print(d,e,f)
"""
#bai tap 3.9
'''
traicay='cam','dua hau','xoai'
a,b,c=traicay
print(a,b,c)
'''
#bai tap 3.10
'''
x='Huynh Thanh The'
print(x)
'''
#bai tap 3.11
'''
x='huynh'
y='thanh'
z='the'
print(x,y,z)
'''
#bai tap 3.12
'''
x='huynh'
y='thanh'
z='the'
j=2
print(x+y+z,j)
'''
#bai tap 3.13
'''
x='the'
def myfunc():
    print('huynh thanh' + x)
myfunc()
'''
#bai tap 3.14
'''
x=1
def myfunc():
    x=2
    print("1 + 1 =", x)
myfunc()
print("2 - 1 = ",x)
'''
#3.15
'''
def myfunc():
    global x
    x='the'
myfunc()
print('huynh thanh', x)
'''
#3.16
'''
x='the'
def myfunc():
    global x
    x=1
myfunc()
print(x)
'''
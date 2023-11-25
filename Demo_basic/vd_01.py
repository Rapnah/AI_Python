#BT 1
'''
x=1
print(type(x))
'''
#BT 2
'''
a = "the"							#string
b=2									#int
c=2.0								#float
d=1j								#complex
e=['tao', 'cam', 'nho']				#list
f=('tao','cam','nho')				#tuple
g=range(9)							#range
h={'ten' : 'the', 'tuoi': 23}		#dict
i={'cam', 'tao', 'nho'}				#set
j=frozenset({'tao','cam','nho'})	#frozenset
k= True								#bool
l=b'huynh'							#bytes
m=bytearray(4)						#bytearray
n=memoryview(bytes(5))				#memoryview
o= None								#nonetype
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
print(type(o))
'''
#BT 3
'''
x = int(2)
print(x, type(x))
'''
#BT4
'''
a=1
b=1000000
c= -1000000
print(type(a), type(b), type(c))
'''
#BT 5
'''
x=1.1
y=1.00
z=-10.2
print(type(x), type(y), type(z))
'''
#BT 6
'''
a=10e2
b=8e4
c=-6e1
print(a, b, c)
print(type(a), type(b), type(c))
'''
#BT7
'''
a=1+2j
b=2j
c=-6j
print(type(a), type(b), type(c))
'''
#BT 8
'''
a=1				#int
b=2.5			#float
c=2j			#complex

#convert int to float:
x=float(a)
#convert float to int:
y=int(b)
#convert int to complex:
z=complex(a)

print(a, b, c)
print(x, y, z)
print(type(a))
print(type(b))
print(type(c))
'''
#BT 9
'''
import random 						#truy xuat module random
print (random.randrange(1,10))		#lay du lieu ngau nhien (lay 1 so trong bo du lieu int tu 1 den 20)
'''

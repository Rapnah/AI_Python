#BT 1

#a='''huynh thanh the,
#bo mon: He thong thong minh nhan tao
#GVHD: Ts. Vu Duc Huy'''

#print(a)


#BT 2
'''
a = 'huynh thanh the'
print(a[1])

'''

#BT 3
'''
for x in 'huynh thanh the':
    print (x)
'''

#BT 4
'''
a = 'huynh thanh the'
print(len(a))
'''

#BT 5
'''
a = 'huynh thanh the'
if 'huynh' in a:
    print("'co', 'huynh' trong cau")
if 'cam' in a:
    print("'co, 'cam' co trong cau")
else:
    print("'khong', 'cam' trong cau")
'''
#BT 6
'''
a = 'huynh thanh the'
if 'huynh' not in a:
    print("khong co 'huynh' trong cau")
else:
    print("co 'huynh' trong cau")
'''
#BT 7
'''
a = 'huynh thanh the'
print(a[1:7])
'''
#BT 8
'''
a = 'huynh thanh the'
print(a[:7])
'''
#BT 9
'''
a = 'huynh thanh the'
print(a[1:])
'''
#BT 10
'''
a = 'huynh thanh the'
print(a[-4:-1])
'''
#BT 11
'''
a = 'the'
print(a.upper())
'''
#BT 12
'''
a = 'Huynh Thanh The'
print(a.lower())
'''
#BT 13
'''
a = ' huynh thanh the'
print(a.strip())
'''
#BT 14
'''
a = 'huynh thanh the'
print(a.replace('h','e'))
'''
#BT 15
'''
a = 'huynh thanh - the'
b = 'huynh thanh, the'
print(a.split('-'), b.split(','))
'''
#BT 16
'''
a = 'huynh thanh'
b = 'the'
c = a+b
print(c)
'''
#BT 17
'''
a = 'huynh thanh'
b = 'the'
c = a + " " + b
print(c)
'''
#BT 18
'''
age = 23
txt = 'Toi ten la The, nam nay toi {}  tuoi'
print(txt.format(age))
'''
#BT 19
'''
quantity = 4
itemno = 100
price = 20.45
order = 'Toi muon {} mon hang so {} voi gia la {}'
print(order.format(quantity, itemno, price))
'''
#BT 20
'''
quantity = 4
itemno = 100
price = 20.45
order = 'Toi muon tra {2} dollar cho {0} mon hang so {1}'
print(order.format(quantity, itemno, price))
'''
#BT 21
'''
a = 'Chung toi la nhung \'sinh vien\' dai hoc'
print(a)
'''

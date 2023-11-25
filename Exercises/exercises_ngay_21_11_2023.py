#Exercise 1: Calculate the multiplication and sum of 2 numbers:

#Given 1:
'''
number1 = 20
number2 = 30
x = number1*number2
print(x)
'''

#Given 2:
'''
number1 = 40
number2 = 30
y = number1 + number2
print(y)
'''

#Exercise 2: Print the sum of current number and the previous number
y=0
txt = "So hien tai {}, So truoc do {}, Tong hai so {}"
for x in range(10):
    y = x + 1
    z = x + y
print(txt.format(len(x), len(y), z))
 
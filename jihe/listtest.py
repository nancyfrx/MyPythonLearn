list = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(list.count('apple'))
print(list.index('banana'))
list.remove('orange')
print(list)
list.append('hahaha')
print(list)
list.copy()
print("copy" , list)
print(sorted(list))


#列表循环
square = []
for n in range(6):
    square.append(n**2)

print(square)

#列表推导式
square2=[x**2  for x in range(7)]
print(square2)


#square3=list(map(lambda x: x**3, range(5)))
#print(square3)


#del 语句
a = [-1, 1, 66.25, 333, 444, 1234.5]
del a[0]
print(a)
del a[2:3]
print(a)
del a[:]
print(a)

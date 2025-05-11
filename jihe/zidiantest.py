# 输出
tel = {"a":1,"b":2,"c":3}
print(tel['a'])
print(tel)


#删除字典值
del tel['b']
print(tel)

# 定义字典值,不会删掉之前的
tel['d'] = 4
print(tel)

print(list(tel))

#判断值
print('a' in tel)


# 使用dict 创建字典 , 中间使用逗号分隔
print(dict([('e',1),('f',4)]))
print(dict(a=66,b=7,c=0))

#字典推导式
a ={x: x**2 for x in range(4)}
print(a)

#打印字典

tel4 = {"a":1,"b":2,"c":3}

for i,v in tel4.items():
    print(i,v)

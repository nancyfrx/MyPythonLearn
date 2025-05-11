#引号的用法
print(" hello python")
print('''
Hello
ruxue 
''')
x=112
print(f"ruxue {x}")
#字符串链接
var = "ab" + "bc"
print(var)
print("xy" in "12415xy57")

#切片
s="abcdef"
print(s[1])
print(s[1:6:5])
print(s[1:3])
print(s[-1])

#字符串函数
print (",".join("abacd"))
print("aaaa".count("a"))
print("a,b,c,d".split(','))
print("xysze".isalnum())



#单引号，双引号，三引号
a='"hello ruuxe"'
print(a)

b=" hello 'ruxue'"

print(b)

c="""hello 'ruxue'
test
"""
print(c)


# str 常用的一些方法：
print("This is {0}.".format(3))
print('python'.find('py'))
print('12f1251'.isdigit())
print('dFasgah'.islower())
print('dFasgah'.isupper())
print('dFasgah'.join('d'))
print('dFasgah'.replace('d','f'))
print('1,3,3'.split(','))
print('  dd   '.strip())
print('teste'.upper())

a = 'test'
print(f'{a} is right')

#join 的用法
parts = ["user","fengruxu","test"]
print("/".join(parts))


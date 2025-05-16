class Father:
    def __init__(self,name):
        self.name =name

    def eat(self):
        print(f"{self.name} 正在吃饭")

    def walk(self):
        print(f"{self.name} 正在走路")



# 继承的写法
class Son(Father):
    def __init__(self, name,age):
        super().__init__(name)
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} 用滑板走路！")  # 改进了走路方式

    def sing(self):
        print(f"{self.name} 唱歌！")  # 改进了走路方式


f =Father("父亲")
f.walk()
f.eat()


s =Son("儿子","1")
s.sing()


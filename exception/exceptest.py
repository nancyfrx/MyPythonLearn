import sys
# while True:
#     try:
#         x = int(input("please   "))
#         break
#     except ValueError:
#         print("类型错了，要输入整形")



# 一般用法
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


# 链式异常 raise ..from

# try:
#     open("aaa")
# except FileNotFoundError as exc:
#     raise RuntimeError("文件系统找不到") from exc



# finally 语句，最后都会执行的语句


# try:
#     raise  KeyboardInterrupt
# finally:
#     print("最后会执行")
#


# add_note(note)  方法可以细化异常
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information') # 这个是python13 的版本才有的方法
    raise
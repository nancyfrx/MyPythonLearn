def fib(n):    # 打印小于 n 的斐波那契数列
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# 现在调用我们刚定义的函数：
fib(2000)

#没有return 的函数其实有返回值，默认是none
print(fib(0))


def ask(prompt,retry=4,reminder="try again"):
    while True:
        reply=input(prompt)
        if reply in {'yes','y'}:
            return True
        if retry in {'no','n'}:
            return  False
        retry =retry - 1
        if retry < 0:
            raise  ValueError("END")
        print(reminder)


# prompt 为必选入参
ask('提示传参')
ask('OK to overwrite the file?', 2, 'Come on, only yes or no!')
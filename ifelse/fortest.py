x = ["11","222","666"]
for a in x:
    print(a)

# range 的用法
for b in range(10):
    print(b)
    print(list(range(3)))

print(sum(range(10)))

#break 和continue 的用法
for n in range(0,4):
    for b in range(2,n):
        if n == 1:
            continue
        print(f"{n} ----{b}")
    else:
        print("111111111111")


#pass 的用法
#while True:
 #   pass


#mathch 语句，类似Switch

def http_error(status):
    match status:
        case 400:
           print("4000000000")
           return "400"
        case 300:
           return "300"


http_error(400)




def outer():
    x = 10
    def midder():
        x = 20
        def inner():
            #nonlocal  x
            x =30
            print("inner x---", x)
        inner()
        print("midder x---",x)
    midder()
    print("outer ",x)

outer()




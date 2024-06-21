def outer_fun():
    var1 = 30

    def inner_fun():
        print(var1)

    inner_fun()


outer_fun()

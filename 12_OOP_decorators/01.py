def uppercase_decorator(func):
    def nested():
        # txt = func()
        # txt = txt.upper()
        # return txt
        return func().upper()
    return nested


@uppercase_decorator
def lorem_generator():
    return "bla bla bla"

@uppercase_decorator
def slogan1():
    return "promocja"

print(slogan1())
print(lorem_generator())


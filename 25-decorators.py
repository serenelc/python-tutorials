def cough_dec(func):
    def func_wrapper():
        print("*Cough cough*")
        func()
        print("*laughs*")

    return func_wrapper()


@cough_dec
def question():
    print("Can you give me a discount on that?")


@cough_dec
def answer():
    print("as if")

def before_after(func):
    def wrapper():
        print("function is starting")
        func()
        print("function is finished")
    return wrapper

@before_after
def calculate():
    print("calculating...")
calculate()




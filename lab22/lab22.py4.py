def check_positive(func):
    def wrapper(num):
        if num > 0:
            return func(num)
        else:
            print("Number must be positive")
    return wrapper

@check_positive
def display_number(num):
    print("Number is:", num, "and it is positive")

display_number(5)   # Number is: 5
display_number(-3)  # Number must be positive
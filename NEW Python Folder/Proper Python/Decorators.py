def add_sprinkles(func):
    def wrapper(*args, *kwargs):
        print("you added sprinkles")
        func(*args,*kwargs)
    return wrapper()

def add_fudge(func):
    def wrapper(*args,*kwargs):
        print("you added fudge")
        func(*args, *kwargs)
    return wrapper()

@add_sprinkles
@add_fudge
def get_iceCream(flavour):
    print(f"Here is your {flavour} ice cream")

get_iceCream("Blueberry")

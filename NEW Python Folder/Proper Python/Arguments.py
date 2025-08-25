def add(*args):
    total = 0
    for index in args:
        total += index
    return total

print(add(1,3,6,7))

def adress (**kwargs):
    for index in kwargs.values():
        print(index)

adress(street="232",
       city= "Chicago",
       state = "colorado",
       zip = "1234"
       )

def shipping_label(*args, **kwargs):
    for customer in args:
        print(customer,end=" ")
    print()
    for adress in kwargs:
        print(adress,end=" ")

shipping_label(Sarmad,Ansari,III,
               house ="233", city= "York", country= "Uk"  )
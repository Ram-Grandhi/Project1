def make_counter():
    i = 0
    def counter(): # counter() is a closure
        nonlocal i
        i += 1
        return i
    return counter

c1 = make_counter()
c2 = make_counter()

print (c1(), c1(), c2(), c2())

# https://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
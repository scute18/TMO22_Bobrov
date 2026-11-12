g = (x + 2 for x in [1, 2, 3])
print(list(g))

def announce(func):
    def wrapper():
        result = func()
        print("Внимание")
        return result
    return wrapper

@announce
def hello():
    print("Привет!")

hello()

outer = "Hello World"

def example_function(param):
    inner = "Hello function:  {}".format(param)
    print(inner, outer)


example_function("first")
example_function("second")

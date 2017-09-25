import math


def example_funtion(name: str, radius: float) -> str:
    area = math.pi * radius ** 2
    return "The area of {} is {}".format(name, area)


print(example_funtion('Bob', 5))

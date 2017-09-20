def sum_multiples(num, limit):
    """ Calculates the sum of multiples of a given number.
    Args:
        num: The multiple.
        limit: The upp;l;ler limit.
    Returns:
        The sum of the terms of a given multiple.
    """
    sum = 0
    for i in range(num, limit, num):
        sum += i
    return sum

def sum(limit):
    return (sum_multiples(3, limit) +
            sum_multiples(5, limit) -
            sum_multiples(15, limit))

print (sum(1000))
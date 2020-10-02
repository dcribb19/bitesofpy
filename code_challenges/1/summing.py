def sum_numbers(numbers=None):
    sum = 0
    if numbers == None:
        for x in range(1, 101):
            sum += x
    else:
        for number in numbers:
            sum += number
    return sum
def find_number_pairs(numbers: list, N=10):
    number_pairs = []
    for x in numbers:
        numbers.remove(x)
        for y in numbers:
            if x + y == N:
                if (x, y) not in number_pairs:
                    number_pairs.append((x, y))
    return number_pairs

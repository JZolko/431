
num_tests = int(input())


for test_idx in range(num_tests):
    line = input().split()
    min_value = int(line[0]) # Gallons of fuel
    max_value = int(line[1]) # Gallons required to reach a full charge

    d = 0
    s = 0
    b = 0

    for i in range(min_value, max_value + 1):
        if not i**(1/2) % 1 and not i % 12:
            b += 1
        if not i**(1/2) % 1:
            s += 1
        if not i % 12:
            d += 1

    print(d, s, b)

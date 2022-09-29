from math import sqrt, ceil, floor

global d, s, b
d = 0
s = 0
b = 0

def perfectSquares(min_val, max_val):
    global s
    s = floor(sqrt(max_val)) - ceil(sqrt(min_val)) + 1


def divisibleBy12(min_val, max_val):
    global d
    d = max_val // 12 - min_val // 12 + 1 if min_val % 12 == 0 else max_val // 12 - min_val // 12



def perfectSquareAndDivisibleBy12(min_val, max_val):
    global b

    lower = min_val if min_val % 12 == 0 else min_val + (12 - min_val % 12)
    upper = max_val if max_val % 12 == 0 else max_val - max_val % 12

    lower_range = int(sqrt(lower))
    upper_range = int(sqrt(upper))

    local_out = 0
    for i in range(lower_range, upper_range + 1):
        if lower <= i * i <= upper and i**2 % 12 == 0:
            local_out += 1
    b = local_out

num_tests = int(input())
for test_idx in range(num_tests):
    line = input().split()
    min_value = int(line[0]) # Gallons of fuel
    max_value = int(line[1]) # Gallons required to reach a full charge

    perfectSquares(min_value, max_value)
    divisibleBy12(min_value, max_value)
    perfectSquareAndDivisibleBy12(min_value, max_value)

    print(d, s, b)

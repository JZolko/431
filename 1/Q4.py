from itertools import combinations_with_replacement
num_tests = int(input())


for test_idx in range(num_tests):
    line = input().split()
    x = int(line[0]) # Distance forward
    y = int(line[1]) # Distance forward
    n = int(line[2]) # Number of times the button must be pressed

    combos = list(combinations_with_replacement([x, y], n))

    for combo in combos:
        print(sum(combo), end=" ")
    print()
from itertools import combinations_with_replacement
num_tests = int(input())

for test_idx in range(num_tests):
    line = input().split()
    x = int(line[0]) # Distance forward
    y = int(line[1]) # Distance forward
    n = int(line[2]) # Number of times the button must be pressed

    unique = {}

    if x == y:
        print(x * n)
    else:
        combos = list(combinations_with_replacement([x, y], n))

        out = []
        for combo in combos:
            added = sum(combo)
            if unique.get(added) is None:
                out.append(added)
                unique[added] = 1

        out.sort()
        print(' '.join(map(str, out)))

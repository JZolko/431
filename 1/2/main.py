num_tests = int(input())

milli = 1000000
for test_idx in range(num_tests):
    line = input().split()
    S = int(line[0]) # Starting bet
    k = int(line[1]) # Number of rounds

    for rounds in range(k):
        if S % 2:
            S = (S - 15) % milli
            S = (S * 2) % milli
        else:
            S = (S - 99) % milli
            S = (S * 3) % milli
    print(S)

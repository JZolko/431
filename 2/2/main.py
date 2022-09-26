from collections import Counter


def main():

    N = int(input())

    sats = []
    for test_idx in range(N):
        sats.append(int(input()))

    most_common = Counter(sats).most_common(1)[0][0]

    print(most_common)




if __name__ == "__main__":
    main()

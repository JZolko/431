

def main():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        B = list(map(int, input().split()))

        table = [0 for _ in range(K + 1)]

        table[0] = 1

        for i in range(0, N):
            for j in range(B[i], K + 1):
                table[j] += table[j - B[i]]

        if table[-1]:
            print(K)
        else:
            for i in range(K, -1, -1):
                if table[i]:
                    print(i)
                    break


if __name__ == '__main__':
    main()

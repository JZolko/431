
def main():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        B = list(map(int, input().split()))

        W = K
        arr = B
        n = len(B)
        d = [[0 for i in range(W + 1)] for j in range(n + 1)]
        
        for i in range(n + 1):
            d[i][0] = 1
        for x in range(1, W + 1):
            d[0][x] = 0

        for i in range(1, n + 1):
            for x in range(1, W + 1):
                d[i][x] = d[i - 1][x]
                if x >= arr[i - 1]:
                    d[i][x] = d[i][x] or d[i - 1][x - arr[i - 1]]
        print(d)
        print(d[n][W])



if __name__ == '__main__':
    main()

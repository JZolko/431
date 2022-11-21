

def main():

    N = int(input())
    dlist = [0] * N
    arr = list(map(int, input().split()))

    if N == 1:
        print(arr[0])
        return

    dlist[0] = arr[0]
    dlist[1] = max(arr[0], arr[1])

    for i in range(2, N):
        dlist[i] = max(dlist[i - 1], dlist[i - 2] + arr[i])

    print(dlist[N - 1])


if __name__ == "__main__":
    main()

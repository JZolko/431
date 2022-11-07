import sys

sys.setrecursionlimit(100_000)


def NoAdjacentSum(arr, i, n):
    if i >= n:
        return 0
    if solved[i]:
        return dlist[i]
    dlist[i] = max(arr[i] + NoAdjacentSum(arr, i + 2, n), NoAdjacentSum(arr, i + 1, n))
    solved[i] = 1
    return dlist[i]

dlist = list()
solved = list()

N = int(input())
dlist = [0] * N
solved = [0] * N
arr = list(map(int, input().split()))
print(NoAdjacentSum(arr, 0, N))

   



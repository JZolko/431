
def isSorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


def canSwap(arr):
    sorted_list = sorted(arr)

    ooo = 0
    swapidx = []

    for i in range(len(arr)):
        if arr[i] != sorted_list[i]:
            ooo += 1
            swapidx.append(i)

    if ooo > 2:
        return -1, -1
    elif ooo:
        return swapidx[0] + 1, swapidx[-1] + 1
    else:
        return -1, -1


def canReverse(arr):
    sorted_list = sorted(arr)
    i = 0
    j = 0
    for i in range(len(arr)):
        if arr[i] != sorted_list[i]:
            break
    for j in range(len(arr)-1, -1, -1):
        if arr[j] != sorted_list[j]:
            break
    while i != j:
        i += 1
        if arr[i - 1] < arr[i]:
            return -1, -1
    for i in range(len(arr)):
        if arr[i] != sorted_list[i]:
            break
    return i + 1, j + 1


def main():

    N = int(input())
    arr = list(map(int, input().split()))


    sorted = isSorted(arr)
    if sorted:
        print("yes")
        return
    first, last = canSwap(arr)
    if first != -1 and last != -1:
        print("yes")
        print("swap", first, last)
        return
    i, j = canReverse(arr)
    if i != -1 and j != -1:
        print("yes")
        print("reverse", i, j)
        return
    print("no")

if __name__ == '__main__':
    main()

from heapq import heappush, heappop, heapify
def main():

    minHeap = []
    maxHeap = []
    curr_median = 0
    minValues = {}
    maxValues = {}

    N = int(input())

    for operations in range(N):
        line = input().split()
        operation = line[0]
        value = int(line[1])

        if operation == "a":
            if value > curr_median:
                heappush(maxHeap, -value)
                maxValues[value] = 1 if maxValues.get(value) is None else maxValues[value] + 1
            else:
                heappush(minHeap, value)
                minValues[value] = 1 if minValues.get(value) is None else minValues[value] + 1
        elif operation == "r":
            if minValues.get(value) is not None and minValues[value] > 0:
                minValues[value] -= 1
                heappop(minHeap, value)
            elif maxValues.get(value) is not None and maxValues[value] > 0:
                maxValues[value] -= 1
                heappop(maxHeap, -value)
            else:
                print("Wrong!")
                continue

        if len(minHeap) == len(maxHeap):
            curr_median = (minHeap[0] + -maxHeap[0]) / 2
        else:
            -maxHeap[0]

        print(curr_median)

if __name__ == "__main__":
    main()














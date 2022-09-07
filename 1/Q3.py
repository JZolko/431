from heapq import heapify, heappush, heappop
qty = int(input())
parts = list(map(int, input().split()))

remain = len(parts)
print(remain)

intervals = []
heapify(intervals)
times = {}

for person in parts:
    if times.get(person) is None:
        times[person] = 1
        heappush(intervals, person)
    else:
        times[person] += 1


while intervals:
    remain -= times.get(heappop(intervals))
    if remain <= 0: break
    print(remain)

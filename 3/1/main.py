from heapq import heappush, heappop


def main():
    
    heap = []
    N, k = map(int, input().split())

    for i in range(N):
        heappush(heap, -int(input()))

    for i in range(k):
        print(-heappop(heap))

if __name__ == '__main__':
    main()

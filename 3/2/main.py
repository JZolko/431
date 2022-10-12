from heapq import heapify, heappop, heappush


def main():
    num_tasks, num_workers = map(int, input().split())
    jobs = list(map(int, input().split()))
    jobs = [-job for job in jobs]
    heapify(jobs)

    total_cost = 0
    curr_worker = 1
    curr_level = 1
    while jobs:
        total_cost += -heappop(jobs) * curr_level
        if curr_worker == num_workers:
            curr_worker = 0
            curr_level += 1
        curr_worker += 1
    print(total_cost)


if __name__ == "__main__":
    main()

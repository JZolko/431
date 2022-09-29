

def scheduler(tasks):

    arrival = 0
    duration = 1
    finish = 2
    tasks.sort(key=lambda x: x[0])

    for i in range(1, len(tasks)):

        prev_end = tasks[i - 1][2]
        waiting = []
        for j in range(i, len(tasks)):
            if tasks[j][0] <= prev_end:
                waiting.append(tasks[j])

        tasks[i:i+len(waiting)] = sorted(waiting, key=lambda x: x[1])

        prev_task = tasks[i - 1]
        curr_task = tasks[i]

        if prev_task[finish] >= curr_task[arrival]:
            curr_task[finish] = prev_task[finish] + curr_task[duration]
        else:
            curr_task[finish] = prev_task[finish] + curr_task[duration] + curr_task[arrival] - prev_task[finish]

    total_time = 0
    for task in tasks:
        total_time += task[finish] - task[arrival]

    print(int(total_time / len(tasks)))


def main():
    N = int(input())

    tasks = []

    for text_idx in range(N):
        line = input().split()
        Ti = int(line[0])
        Li = int(line[1])

        tasks.append([Ti, Li, Ti + Li])

    scheduler(tasks)



if __name__ == "__main__":
    main()

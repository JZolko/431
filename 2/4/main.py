from bisect import bisect, insort


def main():

    values = []
    dic = {}
    curr_median = 0

    N = int(input())

    for operations in range(N):
        line = input().split()
        operation = line[0]
        value = int(line[1])

        if operation == "a":
            if dic.get(value) is not None:
                dic[value] += 1
            else:
                dic[value] = 1

            insort(values, value)
            if len(values) % 2:
                curr_median = values[len(values) // 2]
            else:
                out = (values[len(values) // 2] + values[len(values) // 2 - 1]) / 2.0
                if -0.5 < out - int(out) < 0.5:
                    curr_median = int(out)
                else:
                    curr_median = out

        elif operation == "r":
            if dic.get(value) is not None and dic[value] > 0:
                values.remove(value)
                dic[value] -= 1
                if len(values) % 2 and values:
                    out = values[len(values) // 2]
                    if -0.5 < out - int(out) < 0.5:
                        curr_median = int(out)
                    else:
                        curr_median = out

                elif not len(values) % 2 and values:
                    out = (values[len(values) // 2] + values[len(values) // 2 - 1]) / 2.0
                    if -0.5 < out - int(out) < 0.5:
                        curr_median = int(out)
                    else:
                        curr_median = out
                else:
                    print("Wrong!")
                    continue

            else:
                print("Wrong!")
                continue

        print(curr_median)

if __name__ == "__main__":
    main()














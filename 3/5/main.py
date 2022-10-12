




def main():
    num_tubes, num_expolode = map(int, input().split())
    exploding_tubes = list(map(int, input().split()))

    tubes = [0] * num_tubes
    for i in exploding_tubes:
        tubes[i] = 1

    max_dist = 0
    prev = None
    for i in range(num_tubes):
        if tubes[i]:
            if prev is None:
                max_dist = max(max_dist, i)
            else:
                max_dist = max(max_dist, (i - prev) // 2)
            prev = i

    print(max(max_dist, num_tubes - prev - 1))


if __name__ == "__main__":
    main()

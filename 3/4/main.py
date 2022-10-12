from random import randint

def main():
    num_darts, curr_agent = map(int, input().split())
    possible = list(map(str, input().split()))
    stuck = list(map(str, input().split()))

    possible_dict = {}
    for i in range(len(possible)):
        possible_dict[possible[i]] = i

    value = 0
    for i in range(len(stuck)):
        value += possible_dict[stuck[i]]

    print(possible[(len(possible) + curr_agent) % len(possible)])


if __name__ == "__main__":
    main()

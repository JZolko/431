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

    # sum + x % 5 = agent number
    for i in range(len(possible)):
        if (value + i) % num_darts == curr_agent:
            print(possible[i])
            return


if __name__ == "__main__":
    main()

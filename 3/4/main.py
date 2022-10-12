from random import randint

def main():
    num_darts, curr_agent = map(int, input().split())
    possible = list(map(str, input().split()))
    stuck = list(map(str, input().split()))

    print(possible[(len(possible) + curr_agent) % len(possible)])

if __name__ == "__main__":
    main()

def main():
    N, K = map(int, input().split())
    required = list(map(str, input().split()))
    agents = {}

    for i in range(N):
        number_of_skills = int(input())
        agents[i] = [number_of_skills, list(map(str, input().split()))]


if __name__ == "__main__":
    main()

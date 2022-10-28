

def main():
    N = int(input())
    for i in range(N):
        start_value, end_value = map(int, input().split())
        print(bin(start_value - end_value).count('1'))


if __name__ == "__main__":
    main()

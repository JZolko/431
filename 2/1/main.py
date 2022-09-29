def traverse(sats):
    path = []
    visited = {}
    curr_fuel = 0
    i = 0

    # DONT START AT A PREVIOUSLY VISITED SAT IF ITS IN THE DICT
    # can iterate over visited if there is a current path
    #
    # go over each sat
    while True:
        curr_sat = sats[i % len(sats)]
        #  if start is visited then skip it, do the next
        if visited.get(curr_sat[0]) is not None and not path:
            i += 1
            curr_fuel = 0
            continue
        #  add the current power
        curr_fuel += curr_sat[1]
        #  if you can't reach the next sat then its not worth starting at
        if curr_fuel < curr_sat[2]:
            #  add it to visited
            visited[curr_sat[0]] = 1
            path = []
            i += 1
            curr_fuel = 0
            continue
        #  if you can then cool, add it to the path
        path.append(curr_sat[0])
        #  go to the next sat
        i += 1
        curr_fuel -= curr_sat[2]
        if len(path) > 1 and path[0] == path[-1]:
            return path[0]




def main():
    sats = []
    N = int(input())
    for sat_num in range(N):
        line = input().split()
        curr_fuel = int(line[0])
        fuel_to_next = int(line[1])

        sats.append((sat_num, curr_fuel, fuel_to_next))

    print(traverse(sats))


if __name__ == "__main__":
    main()

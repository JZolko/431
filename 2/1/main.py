

def main():

    sats = []
    N = int(input())
    for sat in range(N):
        line = input().split()
        curr_fuel = int(line[0])
        fuel_to_next = int(line[1])

        sats.append((curr_fuel, fuel_to_next))

        # pick start
        #   for next satellite in satellites
        # current fuel = start fuel
        # fuel to next = fuel to next
        # current fuel - fuel to next
        # if current fuel < 0 then you cant make it
        # else, go to next and add add sat fuel to curr fuel
        # # at next

        for i in range(len(sats)):
            current_fuel = sats[i][0]
            fuel_to_next = sats[i][1]
            for j in range(i+1, len(sats) + i):
                current_fuel -= sats[j][1]
                if current_fuel < 0:
                    break

                current_fuel += sats[j+1][0]




if __name__ == "__main__":
    main()













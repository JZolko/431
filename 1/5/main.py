num_tests = int(input())


for test_idx in range(num_tests):
    line = input().split()
    n = int(line[0]) # Gallons of fuel
    m = int(line[1]) # Gallons required to reach a full charge
    c = int(line[2]) # Number of fuel cells that can be combined

    miles = n // m
    fuel_cells = n//m
    current_cells = 0

    while fuel_cells > 0:
        current_cells += 1
        fuel_cells -= 1
        if current_cells == c:
            fuel_cells += 1
            miles += 1
            current_cells = 0

    print(miles)

num_tests = int(input())


for test_idx in range(num_tests):
    line = input().split()
    n = int(line[0]) # Gallons of fuel
    m = int(line[1]) # Gallons required to reach a full charge
    c = int(line[2]) # Number of fuel cells that can be combined

    # get full number of cells that can be made

    # get number of cells that can be made with remainer cells

    miles = 0

    made_fuel_cells = n // m
    miles += made_fuel_cells
    
    remainder = made_fuel_cells % c if made_fuel_cells > c else 0
    
    while made_fuel_cells >= 0:
        miles += (made_fuel_cells - remainder) // c
        remainder = made_fuel_cells % c if made_fuel_cells > c else 0
        made_fuel_cells = (made_fuel_cells - remainder) // c

    print(miles)


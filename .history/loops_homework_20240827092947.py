inp_year = int(input('Enter any year: '))

leap_counter = 0
common_counter = 0
for yr in range (inp_year, 2025):
    if yr % 4 == 0:
        leap_counter+=1
    else:
        common_counter+=1

print(f"{leap_counter} leap years and {common_counter} common years from {str(inp_year)} to 2024.")

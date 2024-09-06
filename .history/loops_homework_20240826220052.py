inp_year = int(input('Enter any year: '))

year_counter = 0
leap_counter = 0
normal_counter = 0
for yr in range (inp_year, 2024):
    if yr % 4 == 0:
        leap_counter+=1
    else:
        normal_counter+=1

print(f"")

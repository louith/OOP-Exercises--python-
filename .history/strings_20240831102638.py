# str1 = "Welcome to USA! usa is awesome right?"
# subString = 'usa'
# str1_lower = str1.lower().split()
# str_count = 0
# for i in str1_lower:
#     if i == subString.lower():
#         str_count += 1

# print(str_count)

str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

# convert string to lowercase
temp_str = str1.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)

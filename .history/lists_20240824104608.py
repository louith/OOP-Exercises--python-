str_input = input('Enter a word: \n')
vowels = ('a','e', 'i', 'o', 'u')
str_lower = str_input.lower()
count = 0
for char in str_lower:
    if char in vowels:
        count+=1
print(f"There are {count} vowels in {str_input}")
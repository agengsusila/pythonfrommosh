numbers = [5,2,1,5,7,4,4,3,1,2]
# Use dictionary
numbers = list(dict.fromkeys(numbers))
print(numbers)
# Use for loop
unique = []
for number in numbers:
  if number not in unique:
    unique.append(number)
print(unique)
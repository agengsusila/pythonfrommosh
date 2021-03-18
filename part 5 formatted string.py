first = "Ageng"
last = "Susila"
# This is the different between concatination/regular string and formatted string.
# I want to make a output : "Ageng [Susila] is a python enthusiast"

# CONCATINATION/REGULAR STRING
message = first + " ["+ last +"] is a python enthusiast"

# FORMATTED STRING
# We need to prefix our strings with F and use curly braces to dynamically insert a values
# We use formatted string to easily visualize the output 
msg = f'{first} [{last}] is a python enthusiast'
print(message)
print(msg) 
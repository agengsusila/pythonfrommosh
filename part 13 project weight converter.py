# Works but cannot ignore a lower or upper case
weight = input("Weight: ")
convert_to = input("(L)bs or (K)g: ")
kilos = "k"
pounds = "l"
if convert_to.casefold==kilos.casefold:
    print(f"Your weight {float(weight)*2.205} pounds")
elif convert_to.casefold==pounds.casefold:
    print(f"Your weight {float(weight)/2.205} kilograms")
else:
    print("Can't run the program, wrong input")

# Mosh Version
weight2 = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper()=="L":
    converted = weight2*0.45
    print(f"You are {converted} kilos")
else:
    converted = weight2/0.45
    print(f"You are {converted} pounds")

# Mosh Version get edited by Gengs
weight3 = int(input("Weight: "))
unit2 = input("(L)bs or (K)g: ")
if unit2.upper()=="L":
    print(f"You are {weight3*0.45} kilos")
elif unit2.upper()=="K":
    print(f"You are {weight3/0.45} pounds")
else:
    print("Wrong input")

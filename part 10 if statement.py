# My Solution (Not wrong and works, but not eficient)
price = 1000000
good_credit = True

if good_credit:
    print("The buyer need to pay $", float(price)*0.1)
else:
    print("The buyer need to pay $", float(price)*0.1)

# Mosh Solution
if good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down Payment: ${down_payment}")

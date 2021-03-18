try:
  age = int(input("Age: "))
  income = int(input("Income: "))
  risk = income / age
  print(f"Your age {age}, your income {income}, and your risk is {risk}.")
except ZeroDivisionError:
  print("Age cannot be 0.")
except ValueError:
  print("Invalid value")
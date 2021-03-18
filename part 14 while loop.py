i = 0
"""while i <= 5:
    print("*" * i)
    i = i + 1
print("Done")
"""
while i <= 5:
    i += 1
    if i == 3:
        break
    print(i)
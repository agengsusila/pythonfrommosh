# Int to String
phone = input("Phone: ")
digit = {
  "1":"One",
  "2":"Two",
  "3":"Three",
  "4":"Four",
  "5":"Five",
  "6":"Six",
  "7":"Seven",
  "8":"Eight",
  "9":"Nine",
  "0":"Zero"
}
output = ""
for ch in phone:
  output += digit.get(ch,"!") + " "
print (output)
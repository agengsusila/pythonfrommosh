def ch_to_emoji(message):
  words = message.split(" ")
  emojis = {
      ":)":"😊",
      ":(":"🙁",
      ":*":"😘",
      ":p":"😋"
  }
  output = ' '
  for word in words:
     output += emojis.get(word,word) + " "
  return output

message = input(">")
print(ch_to_emoji(message))
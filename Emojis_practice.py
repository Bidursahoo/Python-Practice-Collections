def emoji(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😞",
        ":)'": "🥲"
    }
    output = ""
    for w in words:
        output += emojis.get(w, w) + " "
    return output


message = input("Enter a message")
print(emoji(message))
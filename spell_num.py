num = input("Enter the number to spell-out: ")
spellings = {"1": "one", "2": "two", "3": "three","4": "four","5": "five","6": "six","7": "seven","8": "eight","9": "nine"}
output = ""
for i in num:
    output += spellings.get(i) + " "
print(output)


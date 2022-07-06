w = int(input("Enter the weight: "))
v = input("(L)pounds or (K)kgs: ")
if v == "l" or v == "L":
    pounds = w*0.45
    print(f"Your weight is {pounds} kgs")
elif v == "k" or v =="K":
    kilo = w*2.2
    print(f"Your weight is {kilo} lbs")
else:
    print("Enter a valid input")
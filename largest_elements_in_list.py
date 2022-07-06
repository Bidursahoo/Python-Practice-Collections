list = ["bidur" , "bibhab" , "sahoo" , "bhubaneswar" , "newtown" , "cuttack"]
largest = len(list[0])
ind = 0
for i in range(len(list)):
    if len(list[i]) > largest:
        largest = len(list[i])
        ind = i
print(f"largest is {list[ind]} with length is {largest}")
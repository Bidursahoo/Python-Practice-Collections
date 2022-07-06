snum = 12
trials = 3
while trials>0:
    a = int(input("Guess the number: "))
    if a == snum:
        print("Yah! you got it right ......")
        break
    trials-=1
if trials == 0:
    print("ohh no! \nyou lost...")
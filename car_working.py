num = int(input("To start press 1 "))
if num == 1:
    print("start - to start the car \nstop - to stop the car \nquit - to get out of the car")
    key_inserted = True
    status = "null"
    while key_inserted:
        com = input("Enter the commmand");
        if com.lower() == "start" :
            if status.lower() == "started":
                print("already started");
            else:
                print("Car is started")
                status = "started"
        elif com.lower() == "stop":
            if status.lower() == "stopped":
                print("already stoppped");
            else:
                print("Car is stopped")
                status = "stopped"
        elif com.lower() == "quit":
            print("Thank you! for playing with us")
            key_inserted = False
        else:
            print("I don\'t get it")
    print("See you next time...")
else:
    print("Game not started")

car_started = False
while(1):
    usr_input = input("===>").upper()
    if usr_input == "HELP":
        print('''start - tostart the car
stop - to stop the car
quit -to exit''')
    elif usr_input == "START":
        if not car_started:
            print("Car started... Ready to go!")
            car_started = True
        else:
            print("Already started")
    elif usr_input == "STOP":
        if car_started:
            print("Car stopped!")
            car_started = False
        else:
            print("already stopped".title())
    elif usr_input == "QUIT":
        break
    else:
        print("I don't understand that...")
command = ""
car_running = False
while command != 'quit' :
    command= input("> ").lower()
    if command == "start" and car_running == False:
        print("car started! ready to go!")
        car_running = True
    elif command== 'start' and car_running == True:
        print("car is already running!")
    elif command== 'stop' and car_running == True:
        print('the car stops running.')
        car_running = False
    elif command== 'stop' and car_running == False:
        print("car is not running!")
    elif command != 'quit'  :
        print(" I don't understand that... ")
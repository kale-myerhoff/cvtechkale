import random
import sys
import time


print("welcome to russian roulette! :D ")
print('')
try:
    player_number = int(input("How many players? > "))
except:
    print('please use a valid number')
print('')
player = []
i = 1
while i <= player_number :
    player.append(i)
    i+=1






chamber = ["blank", "blank", "blank", "blank", "blank", "live"]
bullet_type = ""


bullet_num = len(chamber)
live_num = 1
blank_num = 5



def result():
    global bullet_type
    bullet_type = random.choice(chamber)

def reload(chamber):
    global live_num, blank_num
    print("re-loading")
    print('')
    chamber = ["blank", "blank", "blank", "blank", "blank", "live"]

    live_num = 1
    blank_num = 5

reload(chamber)


def player_turn():
    if len(player) <= 1:
        print(f"player {player[0]} wins! ")
        sys.exit()
    if len(chamber) <= 0:
        reload()

    print(f"it's player {player[0] }'s turn!")
    print(f"there are {bullet_num}/6 bullets in play, {live_num} live {blank_num} blank")


    p_opt_shoot()



    player_turn()

def p_opt_shoot():
    global  blank_num, live_num
    shoot = input("ready? y/n >")
    if str(shoot) in ["y" , "Y"]:
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(3)

        result()



        if bullet_type == "blank":
            print('*click*')
            print('')
            chamber.remove("blank")
            turn_opt()
            blank_num -= 1

        elif bullet_type == "live":
            print('*B A N G!*')
            print("you lose!")
            print('')
            player.pop(0)
            reload(chamber)
            player_turn()
            live_num -= 1

        else:
            print (bullet_type)

    elif str(shoot) in ["n" , "N"]:
        print("take your time.")
        print('')
        time.sleep(1)
        p_opt_shoot()


def turn_opt():
    global live_num

    print(f"there are {bullet_num}/6 bullets in play, {live_num} live {blank_num} blank")

    player_opt = input("""What would you like to do?
1) shoot again
2) load live round
3) Pass to next player>""")
    print('')

    if player_opt == "1":
        p_opt_shoot()
    elif player_opt == "2" and len(chamber) < 6:
        chamber.append("live")
        live_num += 1

        turn_opt()
    elif player_opt == "2" and len(chamber) >= 6:
        print("Chamber full!")
        print("")

        turn_opt()
    elif player_opt == "3":
        player.append(player[0])
        player.remove(player[0])
        print(player)
        player_turn()



player_turn()

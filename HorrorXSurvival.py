health = 100
load_game = 2
current_bullets = 2
gold = 200
has_shotgun = False
has_basement_key = False
has_invisible_coat = False
has_terrace_key = False
has_car_key = False
has_secret_room_key = False

import random


print("===========HorrorXSurvival================")
print("1 play_game")
print("2 check_stats")
print("3 game_info")
print("4 exit")


player_choice = int(input("enter player choice:"))



def play_game():
    print("welcome to HorrorXSurvival")
    load_game = int(input("press 2 to start the game:"))
    if(load_game == 2):
        print("entering")
        room1()

    else:
        print("Invalid choice")
        
    
def room1():
    print("1 check_room")
    print(" 2 go_outside")
    print("3 go_another_side")
    print("4 another_room")
    player = int(input("enter player choice:"))
    if(player == 1):
        check_room()

    elif(player == 2):
        go_outside()

    elif(player ==3):
        room3()

    elif(player ==4):
        room4()

    else:
        print("Invalid choice")

def check_room():
    print(" nothing is found in room ")

def go_outside():
    print("going outside")
    room2()

def go_another_room():
    print("entering")
    room3()

def another_room():
    print("going")
    room4()

    

def room2():
    print("1 search_surrounding")
    print("2 kitchen")
    print("3 upstair")

    player = int(input("enter choice:"))

    if(player == 1):
        search_surrounding()
    elif(player == 2):
        kitchen()
    elif(player == 3):
        upstair()
    else:
        print("Invalid choice")


def search_surrounding():
    global has_terrace_key
    print("searching surrounding")
    print("1 found_box")
    player = int(input("open box:"))
    if(player == 1):
        print("found terrace key")
        has_terrace_key = True

    else:
        print("Invalid choice")

def kitchen():
    global has_shotgun
    print(" 1 searching in kitchen")
    player = int(input("searching: "))
    if((player == 1)):
        print("found_shotgun with 1 new_bullet")
        has_shotgun = True
        monster()

    else:
        print("Invalid choice")

def shotgun():
            global current_bullets
            new_bullet = 1 
            current_bullets = current_bullets + new_bullet  
            print(current_bullets) 
            print("1 load shotgun")
            player = int(input("choose 1 to load the shotgun"))
            if(player ==1):
                print("shotgun is loaded now")
                print("1 shoot")
                player = int(input(" Tap 1 to shoot the monster"))
                if(player == 1):
                    print("SHOOT..\n Monster is down for 1.20 minutes")

            else:
                print("Invalid choice")
                    

           

def upstair():
    print("1 room_1")
    print("2 room_2")
    print("3 room_3")
    print("4 room_4")

    player = int(input("enter choice:"))
    if(player == 1):
        room_1()
    elif(player ==2):
        room_2()
    elif(player == 3):
        room_3()
    elif(player == 4):
        room_4()
    else:
        print("Invalid choice")

def room_1():
    print("This room is so dark.\nlet me turn on the lights.\nsearching.........\ni think i found something in table dror.")

    print("1 found_a_letter")
    print("read the letter")
    

    player = int(input("Tap 1 to read the letter:"))

    if(player == 1):
        found_a_letter()
def found_a_letter():
    print("Hey,if you are reading this letter it means iam dead.\n I got stuck here from last 1 year.\n I came here with my freinds but they all dissapear i think the monster kill them.\n When i tried to run he got me everytime.\n If you want to escape from here make sure to dont appear in front of him.  ")
    monster()

def room_2():
    global has_basement_key
    print("1 go_under_the_bed")
    print("2 basement_key")
    print("3 torch")
    player = int(input("enter choice:"))

    if(player == 1):
        print("you are under the bed")
    elif(player == 2):
        print("found basement key")
        has_basement_key = True
    elif(player == 3):
        print("you found a torch")
    
    else:
        print("Invalid choice")

    shotgun()


def room_3():
    print("monster_hunt")
    print("1 Run")
    print("2 get invisible")
    player = int(input("enter choice:"))
    if(player == 1):
        print("running")
    elif(player == 2):
        INcoat()
    monster()
def room_4():
    global has_invisible_coat
    print("searching......")
    print("1 found_a_invisible_coat")
    player = int(input("enter choice:"))

    if(player ==1):
        print("you got invisible coat")
        has_invisible_coat = True

    else:
        print("Invalid choice")
    monster()

def INcoat():
    print("wearing invisible coat.\n valid for 10 seconds")


def monster():
    global health
    global gold
    chance = random.choice([1,2,3,4])

    if(chance == 1):
        print("footsteps are coming")
    
    elif(chance ==2):
        print("escaping from monster")

    elif(chance ==3):
        print("monster is down by shotgun")
        gold = gold + 100
        print("gold=",gold)

    elif(chance ==4):
        if(has_invisible_coat):
            print("monster  cant see you!")

        elif(has_shotgun and current_bullets > 0):
            print("monster is down by shotgun!")
            gold += 100

        else:
            print("monster finds you")
            health -= 20
            print("health=",health)
    
    else:
        print("Invalid choice")
    

def room3():
    print("1 basement")
    print("2 terrace")

    player = int(input("enter choice:"))
    
    if(player == 1):
        basement()
    elif(player == 2):
    
      terrace()

def basement():
    global has_basement_key
    print("1 basement_key")
    player = int(input("enter choice:"))
    if(player == 1):
        print("opening basment key")
        has_basement_key = True
    
    print("1 car")
    print("2 dror")
    

    player = int(input("enter choice:"))

    if(player == 1):
        car()
    elif(player ==2):
        dror()
    else:
        print("Invalid choice")
    

def car():
    print("car is locked you need a car key")
    car_key()
    

def car_key():
    global has_car_key
    print("1 found car key")
    player = int(input("enter choice:"))
    if(player == 1):
        print("car is open now")
        has_car_key = True
        print("You need petrol to start the car")

def dror():
    global has_car_key
    global has_secret_room_key
    print("1 dror_1")
    print("2 dror_2")
    player = int(input("enter choice:"))
    if(player  ==1):
        print("searching.....")
        print("found a car key")
        has_car_key = True

    elif(player ==2):
        print("found secret room key")
        has_secret_room_key = True
        
    else:
        print("Invalid choice")



def terrace():
    global has_terrace_key
    print("1 terrace_key")
    player = int(input("Tap 1 to enter in terrace:"))
    if(player  == 1):
        print("opening terrace")

        has_terrace_key = True
        print("Found a tunnel.")
        print(" I think I can escape through this tunnel.")
        print("1 Slide through the tunnel")
        player = int(input("Tap 1 for sliding:"))
        if(player ==1):
            print("Sliding..........")
            print("=======================================")
            print("Congratulations!")
            print("You escaped from the Horror House")
            print("YOU WIN!")
            print("====================================")

def room4():
    global has_secret_room_key
    global has_shotgun
    global has_invisible_coat

    print(" 1 secret room")
    player = int(input("enter choice:"))
    if(player ==1):
        print("entering in secret room")
        has_secret_room_key = True

    print("You entered in secret room")
    print("1 found a letter ")
    player = int(input("Tap 1 to read the letter:"))
    if(player ==1):
        print("The monster was once a human.\nI created him.\nI tried to bring my dead son back to life...but the experiment failed.\nNow he cannot die by normal weapons.\nHe cannot see someone wearing the invisible coat.\nThere is only one chance.\nOne bullet.\nOne shot.\nIf you fail...you will become his next victim.                \nYou hear heavy footsteps outside the room.....")

        print("Monster is comming") 
        print("1 Fight")
        print("2 Run")
        player = int(input("What should i do...?:"))
        if(player ==1):
                print("I will fight with the monster")
                print("1 Wear invisible coat")
                print("2 Shoot monster")

                choice = int(input("Enter choice:"))

                if choice == 1:
                    if has_invisible_coat:
                        INcoat()
                        print("Go to terrace.\n Going terrace......")

                        terrace()
                    else:
                        print("You dont have invisible coat!")
                        print("Monster catches you...")
                        print("=============GAME OVER=====================")


                elif choice == 2:
                    if has_shotgun and current_bullets > 0:
                        shotgun()
                        print("Go to terrace.\n Going terrace......")
                        terrace()
                    else:
                        print("You dont have shotgun or bullets!")
                        print("Monster catches you...")
                        print("GAME OVER")
        elif(player ==2):
            print("RUN.\nRunning...\nMonster cathes you.\nYou are dead...")
            print("GAME OVER")

def game_info():
    print("===== HORROR X SURVIVAL =====\nA horror survival adventure game.\nExplore the house, collect keys and uncover secrets.\nA monster is hunting you.\nSurvive and find a way to escape.\n\n===== GOOD LUCK =====")

def check_stats():
    print("===== PLAYER STATS =====")
    print("Health:", health)
    print("Gold:", gold)
    print("Bullets:", current_bullets)
    print("Shotgun:", has_shotgun)
    print("Basement Key:", has_basement_key)
    print("Terrace Key:", has_terrace_key)
    print("Car Key:", has_car_key)
    print("Invisible Coat:", has_invisible_coat)
    print("Secret Room Key:", has_secret_room_key)
    print("========================")


if(player_choice == 1):
    play_game()

elif(player_choice ==2):
    check_stats()

elif(player_choice ==3):
    game_info()  

elif(player_choice == 4):
    print("Thanks for playing Horrorxsurvival")      
        
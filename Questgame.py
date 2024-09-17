import random
import time

# C H A N C E S
chance_a = 5
chance_b = 5
live = 3
life_jacket = 0
steps = 0


# N A M E 
while True:
    print("Sly Stoat: Oh another adventerer. Hey! What's your name?")
    name = input(" ?: ")
    if name != "":
        break
    print(" \nPlease enter a valid name")
    
# W E L C O M E
welcome = input(" \nSly Stoat: Hello" + " " + name  + ".")
play_orno = input(" \nSly Stoat: You seem lost! Do you need help? \n(Yes, press any key. Q to quit): ").upper()

print(" ")
if play_orno != "Q":
    print(name + ": " + "Yes, I need help!!")
    
elif play_orno == "Q":
    print("Sly Stoat: Oh, bye...")
    quit()
    
input()
print(" \nSly Stoat: Win my game first then I will help you. It's not going to be so easy though... \n ")

# R U L E S
print("◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤")
print(" \nThe rules: \n1. You get to pick 1 out of 2 doors. Choose carefully as it will affect your choice of games.")
print(" \n2. You have 5 chances to replay for Door A, B until you win. \n ")
print("◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤")
input()


# P I C K   D O O R
while True:
    print("Sly Stoat: Pick 1 out of these 2 doors: (Type A / B)")
    
    print(" ________ ")
    print("|        |")
    print("|        |")
    print("|        |")
    print("|        |")
    print("|      O |              D O O R  A")
    print("|        |")
    print("|        |")
    print("|        |")
    print("|________|")
    
    print(" ________ ")
    print("|        |")
    print("|        |")
    print("|        |")
    print("|        |")
    print("|      O |              D O O R  B")
    print("|        |")
    print("|        |")
    print("|        |")
    print("|________|")
    
    
    
    print(" \nSly Stoat: Pick a door!")
    user_door = input(name + ": ").upper()
    
    # D O O R  A
    if user_door == "A":
        print(" ________ ")
        print("|\       |")
        print("|   \    |")
        print("|     |  |")
        print("|     |  |            ⌜                                                       ⌝")
        print("|     |  |              D O O R  A :  R O C K , P A P E R , S C I S S O R S")             
        print("|   O |  |            ⌞                                                        ⌟")
        print("|     |  |")
        print("|     |  |")
        print("|     |__|")
        print(" \    |  ")    
        
        print(" \nSly Stoat: Win at least 2 rounds of a rock, paper, scissors game :D")
    
        choice_list = ["rock", "paper", "scissors"]
        score = 0
        while True:
            print(" ")
            print(" \n -------------------- R E S T A R T  C h a n c e s  L e f t : " + str(chance_a) + " -------------------- \n")
            print("R = Rock, P = Paper, S = Scissors")
            
            for i in range(3):
                print("✄┈┈┈┈┈┈┈┈┈┈✄┈┈┈┈┈┈┈┈┈┈✄┈┈┈┈┈┈┈┈┈┈✄┈┈┈┈┈┈┈┈┈┈")
                user = input("rock / paper / scissors : ").upper()
                choice = random.choice(choice_list)
                
                print(" \nAnastasia: " + choice)
                if user == "R":
                    if choice == "paper":
                        print(" \n------ You Lost ------")
                    elif choice == "rock":
                        print(" \n------ You Tie ------")
                    elif choice == "scissors":
                        score += 1
                        print(" \n------ You Win. Current score: " + str(score) +" ------")
                elif user == "S":
                    if choice == "paper":
                        score += 1 
                        print(" \n------ You Win. Current score: " + str(score) +" ------")
                    elif choice == "rock":
                        print(" \n------ You Lost ------")
                    elif choice == "scissors":
                        print(" \n------ You Tie ------")
                elif user == "P":
                    if choice == "paper":
                        print(" \n------ You Tie ------")
                    elif choice == "rock":
                        score += 1 
                        print(" \n------ You Win. Current score: " + str(score) +" ------")
                    elif choice == "scissors":
                        print(" \n------ You Lost ------")
                else:
                    print(" \nAnastasia: Don't forget there's only R P or S! ")
                    print(" \n------ You Lost ------")

            if score == 2 or score == 3:
                print(" ")
                print("⌜                                                        ⌝")
                print(" \n    YOU WON (Just the first game...) by " + str(score) + " " + " / 3 scores")
                print("⌞                                                        ⌟")
                break
            
            # O U T  O F C H A N C E
            if chance_a == 0:
                print("")
                print("⌜                                                       ⌝")
                print(" \n    DOOR A's result: You  l O S T  by" + " " + str(score) +  " " + "/ 3 score ")
                print("⌞                                                       ⌟")
                input()
                print("Sly Stoat: It's over. You used all the 6 chances. Goodbye!!")
                quit()
            
            # B A D S C O R E
            else:
                A_decide = input(" \nSly Stoat: Your score didn't reach 2/3. Do you want to restart the game? Press any key to restart, if not press Q: ").upper()
                if A_decide != "Q":
                    chance_a = chance_a - 1
                    print(" \n" + name + ": " + "RESTART ME PLEASE!")
                    continue
                elif A_decide == "Q":
                    print(name + ": " + "Nah, I gave up.")
                    print("Sly Stoat: Bye")
                    break
                    quit()
                            
    

# D O O R  B
    elif user_door == "B":
        print(" ________ ")
        print("|\       |")
        print("|   \    |")
        print("|     |  |")
        print("|     |  |            ⌜                                            ⌝")
        print("|     |  |              D O O R  B :  T Y P I N G   M A S T E R")             
        print("|   O |  |            ⌞                                            ⌟")
        print("|     |  |")
        print("|     |  |")
        print("|     |__|")
        print(" \    |  ")    
    
        chance_b = 5
        sentences = "I love tacos so much. That is probably the best thing here. I dont know why it is so good. I'm going to take the salsa sauce back home, if I could. The sour cream plus with salsa sauce is something else. I need tacos so so bad..." 
    
        print(" \nBlubby: Type the given sentence within 50 seconds :D \n")
        input()
        
        # C H E C K  I F  T H E Y  C A N  R E S T A R T
        while chance_b > 0:  
            print(" \n-------------------- R E S T A R T  C h a n c e s  L e f t : " + str(chance_b) + " -------------------- \n")
        
            # S T A R T  T I M E R
            print("Blubby: Press enter to start the timer")
            input()
            starting_time = time.time()
        
            print(" \n \n︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾ \n")
            print(sentences)
            print(" \n︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾")
            user_type1 = str(input(" \nType the sentence above: "))
        
            # E N D T I M E R
            end_time = time.time()
        
            # C O R R E C T
            if user_type1 == sentences and (end_time - starting_time) <= 50:
                print(" \n \n")
                print("⌜                                                  ⌝")
                print("\n     DOOR B's result: You W I N" + " : " + str(round(end_time - starting_time, 2)) + " seconds.")
                print("⌞                                                  ⌟")
                break
            
            else:
                
                # R E S T A R T ?
                print("--------------------------------------------------------------------------------------------------------------------------")
                print(" \nSly Stoat: You failed.")
                chance_b = chance_b - 1
                B_decide = input(" \nSly Stoat: Do you want to restart the game? You will have " + str(chance_b) + " restart chances left. Press any key to restart, Q to quit: ").upper()
                if B_decide != "Q":
                    print(" \n" + name + ": " + "RESTART ME PLEASE!")
                    
        
                    # C H E C K  C H A N C E
                    if chance_b == 0:
                        print(" \nSly Stoat: AHA. No, sorry. It's over. You used all the chances. Goodbye!! \n")
                        print("⌜                                       ⌝")
                        print(" \n   DOOR B's result: You  l O S T ")
                        print("⌞                                       ⌟")
                        input()
                        quit() 
        
                # N O  R E S T A R T
                else:
                    print(" \n" + name + ": " + "Nah, I gave up.")
                    print(" \nSly Stoat: Goodbye!")
                    break
        break
    
     # N E I T H E R A/B
    else:
        print("Sly Stoat: Please choose one of the option!!")
    
    break 
# L A S T. G A M E
L = " <<< ╸╸╸╸╸╸ "
R = " ╸╸╸╸╸╸ >>>"
findl = ["﹏ ﹏ ﹏ River", " 🕷 🕸 Poisonous spider", " ʕ·ᴥ·ʔ Kodiak bear"]
findr = [" ⾕ House", " 🧊 Ice cube", " 𓉞 ??? Weird door"]
step = [1, 2, 3]

def lose(live):
    live = live - 1
    print(" \n----------------------------------- L I V E (S) R E M A I N E D : " + str(live) + " -----------------------------------")
    return live

def left(findl_, live, life_jacket):
    if findl_ == "﹏ ﹏ ﹏ River":
        print(" \nAncient Algae: Do you want to cross the river? If yes, press any key. No, press Q: ")
        cross = input(name + ": ").upper()
        if cross == "Q":
            print(" \nAncient Algae: Congrats!!! you survived from drowning.")
        elif cross != "Q":
            print(" \nAncient Algae: NO! YOU ARE DROWNING")
            if life_jacket > 0:
                print(" \nAncient Algae: But you have a life jacket. You survived.")
            elif life_jacket == 0:
                print(" \nAncient Algae: You lost 1 life because you don't have the life jacket.")
                live = lose(live)
    elif findl_ == " 🕷 🕸 Poisonous spider":
        print(" \nAncient Algae: You got bitten by a poisonous spider.")
        live = lose(live)
    elif findl_ == " ʕ·ᴥ·ʔ Kodiak bear":
        print(" \nAncient Algae: You encounter a Kodiak bear. You can just hide or fight. Press any key to fight. Press Q to hide. ")
        bear = input(name + ": ").upper()
        if bear == "Q":
            print("The bear found you!!!!")
            live = lose(live)
        elif bear != "Q":
            while True:
                print(" \nAncient Algae: Pick your item to fight. Bare hands = A. Tacos = B. A gun = C")
                pick_item = input(name + ": ").upper()
                if pick_item == "A":
                    print(" \nAncient Algae: Bare hands??? Really.")
                    live = lose(live)
                    break
                elif pick_item == "B":
                    print(" \nYou throw some tacos to the opposite direction. Now the bear is chasing tacos instead. You survived.")
                    break
                elif pick_item == "C":
                    print(" \nAncient Algae: It was a water gun. The bear got wet and you lost 1 life...")
                    live = lose(live)
                    break
                else:
                    print("Enter a valid choice.")
    return live

def right(findr_):
    global live
    if findr_ == " ⾕ House":
        print(" \nAncient Algae: You found a house. Would you like to go in? Press any key to go in. Press Q to stay outside.")
        house = input(name + ": ").upper()
        if house == "Q":
            print(" \nAncient Algae: The weather got so cold. You froze to death.")
            live = lose(live)
        if house != "Q":
            print(" \nAncient Algae: You found a family. They served you a cup of hot tea.")
    elif findr_ == " 🧊 Ice cube":
        print(" \nAncient Algae: It's just an ice cube. Nothing happened.")
    elif findr_ == " 𓉞 ??? Weird door":
        print(" \nAncient Algae: You found a door. Would you go in...? It looks scary. Press any key to go in. Press Q to stay outside.")
        door = input(name + ": ").upper()
        if door == "Q":
            print(" \nAncient Algae: I bet you missed something, but nothing happened to you still.")
        elif door != "Q":
            print(" \nAncient Algae: You TOOK THE RISK AND IT WAS AMAZING. You found a portal back to your world!!!")
            print("")
            print("｡･:*:･ﾟ★,｡･:*:･ﾟ☆ ｡･:*:･ﾟ★,｡･:*:･ﾟ☆ ｡･. ⋆*:.｡. .｡.:*⊶⊹⊷*:.｡. .｡.:*⋆. ⋆*:.｡. .｡.:*⊶⊹⊷*:.｡. .｡.:*⋆:*:")
            print("                                 E A S Y  E N D I N G")
            print("═══════════════════════════════════════════⊹⊱≼≽⊰⊹═══════════════════════════════════════════════════")
            quit()
            
# C H E C K   L I V E S
def check_lives():
    if live <= 0:
        print(" \nAncient Algae: You have used all of your lives. Time to go!")
        print(" ")
        print("⌜                                         ⌝")
        print(" \n G A M E  R E S U L T : Y O U  L O S T ")
        print("⌞                                         ⌟")
        quit()
       
        
        
# S T A R T  P O I N T
print("\nSly Stoat: Wow! You made it to the last game, " + name + ".")
input()

# C A L L  C H E C K
while live > 0:
    check_lives()
    print(" ________ ")
    print("|\       |")
    print("|   \    |")
    print("|     |  |               ╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧")
    print("|     |  |")
    print("|     |  |                    L E F T   O R  R I G H T ") 
    print("|   O |  |")
    print("|     |  |               ╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧")
    print("|     |  |")
    print("|     |__|")
    print(" \    |  ")    
    
    input()
    print("Ancient Algae: The rule is simple.")
    input()
    print("Ancient Algae: You need to choose a direction each time. Make a good decision you don't know what's waiting for you.")
    input()
    print("Ancient Algae: You will come across the monsters or wild animals if you are so unlucky... They will take your lives one by one. You have a total of 3.")
    input()
    print("━━━━━━━ ⟡ ━━━━━━━━━━━━━━ ⟡ ━━━━━━━━━━━━━━ ⟡ ━━━━━━━━━━━━━━ ⟡ ━━━━━━━━━━━━━━ ")
    print("Ancient Algae: First, get your items. Let's see how lucky you are. \n")
    print("    𓃹.   𓃴    𓅷")
    print("")
    print("     A    B     C")
    while True:
        inv = input(" \nSelect your item: ").upper()
        if inv == "A":
            print(" \nAncient Algae: Nothing special for you. But you get to explore a forest in the end.")
            break
        elif inv == "B":
            print(" \nAncient Algae: You get 1 free life. \n")
            live += 1
            print(" \n------------------------ L I V E (S) R E M A I N E D : " + str(live) + " ------------------------")
            break
        elif inv == "C":
            print("Ancient Algae: You get a life jacket...?")
            life_jacket = life_jacket + 1
            break
        else:
            print(" \nEnter a valid choice.")

    for i in range(6):
        while True:
            move = input("\nAncient Algae: Where do you want to go? Left = L, Right = R: ").upper()
            if move != "L" and move != "R":
                print("Enter a valid direction")
                continue
            print(" \nAncient Algae: And how many steps? Enter a number from 1-3: ")
            steps = int(input(name + ": "))
            if steps not in step:
                print("Only enter a number between 1-3")
                continue
            if steps == 24:
                print(" \n------------------ 24th  S T E P  A C H I E V E M E N T  U N L O C K E D ------------------")
            else:
                break
            
        # R A N D O M  choices 
        findl_ = random.choice(findl)
        findr_ = random.choice(findr)
        
        check_lives()
        if move == "L":
            print("\n" + " " * 20 + " You found: " + findl_ + (L * steps))
            live = left(findl_, live, life_jacket)

        if move == "R":
            print("\n" + " " * 40 + (R * steps) + " You found: " + findr_ )
            right(findr_)


    break

# E N D W I N
print(" \nSly Stoat: Wow! You completed all the quests, and survived. Follow me to the exit portal ... ")  

print("═══════════════════⊹⊱≼≽⊰⊹═══════════════ ")
print(" \n G A M E  R E S U L T : Y O U  W I N  \n")
print("═══════════════════⊹⊱≼≽⊰⊹═══════════════")

input()
print("●•.✦.✧.✦.✧.•☾•.✦.✧.✦.✧.••.✦.✧.✦.✧.•☾•.✦.✧.✦.✧.•      _________")
print("                                                     |        | \ ")
print("                                                     |        |  \ ")
print("╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲ > > > > > > >       |        |  |")
print("                                                     |        | O|")
print("⋆*:.｡. .｡.:*⊶⊹⊷*:.｡. .｡.:*⋆.｡.:*⋆.｡.:*⋆              |________|  | ")
print("                                                               \ ")


# I N V = A
if inv == "A":
    print(" \n \n \n")
    print("As you wish. \n")
    print(". 𓍊𓋼𓆏𓋼𓍊   𖤓𖡼𖤣𖥧𖡼𓋼𖤣𖥧𓋼𓍊༉‧₊˚       ✩*⋆ ⍋*☪⋆⍋⋆*✩ ")
quit()
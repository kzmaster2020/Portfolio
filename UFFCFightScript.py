# First and foremost thank you very much for taking the time to review the code below. I truly appreciate it. This is my first game project and, to be honest, I may be in over my head. There's a lot I'm uncertain on how to do, so if you can take a look and tell me what's working and not, that'd be helpful. 

# The UFFC works in 3 seperate parts. 
# 1) Players download the game via Ren.py and can create an account. 
# 2) The account will be part of the accounts on the website I'll make under Furhost. All data submitted by the player from Ren.py, will connect to the submission forms on the site and go to the server. 
# 3) The data is stored on the server, and pulled to use for the fighting aspect of the game. Long story short, user submit numbers, those numbers are used for the AI gameplay.
 



from random import randint 
from StrikeMoveList import *
from SubmissionVariables import *
from GroundStrikeVariables import *
from TakedownClass import *
from GroundClass import *
from ClinchClasses import *
from PlayerClass import *
import math
import sys

x = 1500
sys.setrecursionlimit(x)









    

#_______________________________________Ground Positions__________________________________


stack_guard_Offense = GroundBehavior("Stack Guard Offense", 1, [gpunch], "Full Guard Offense", "Escape", "Escape", "Escape", "Full Guard Defense", "Stack Guard Defense", [armbar] )
stack_guard_Defense = GroundBehavior("Stack Guard Defense", -5, [gpunch], "Escape", "Escape", "Full Guard Offense", "Full Guard Defense", "Escape", "Stack Guard Offense", [armbar] )
full_Guard_Offense = GroundBehavior("Full Guard Offense", 2, [gpunch], "Half Guard Offense", "Stack Guard Offense", "Full Guard Offense", "Full Guard Defense", "Half Guard Defense", "Full Guard Defense", [armbar])
full_Guard_Defense = GroundBehavior("Full Guard Defense", -1, [gpunch], "Escape", "Escape", "Full Guard Offense", "Full Guard Defense", "Escape", "Full Guard Offense", [armbar])
half_Guard_Offense = GroundBehavior("Half Guard Offense", 3, [gpunch], "Side Control Offense", "Full Guard Offense", "Half Guard Offense", "Half Guard Defense", "Side Control Defense", "Half Guard Defense", [armbar])
half_Guard_Defense = GroundBehavior("Half Guard Defense", -2, [gpunch], "Full Guard Defense", "Escape", "Half Guard Offense", "Half Guard Defense", "Full Guard Offense", "Half Guard Offense", [])
side_Control_Offense = GroundBehavior("Side Control Offense", 4, [gpunch], "Full Mount Offense", "Escape", "Side Control Offense", "Side Control Defense", "Full Mount Defense", "Side Control Defense", [armbar])
side_Control_Defense = GroundBehavior("Side Control Defense", -3, [gpunch], "Half Guard Defense", "Half Guard Defense", "Side Control Offense", "Side Control Defense", "Half Guard Offense", "Side Control Offense", [armbar])
full_Mount_Offense = GroundBehavior("Full Mount Offense", 5, [gpunch], "Back Mount Offense", "Side Control Offense", "Full Guard Offense", "Full Guard Defense", "Back Mount Defense", "Full Mount Defense", [armbar])
full_Mount_Defense = GroundBehavior("Full Mount Defense", -4, [gpunch], "Side Control Defense", "Back Mount Defense", "Full Guard Offense", "Full Guard Defense", "Side Control Offense", "Full Mount Offense", [])
north_South_Offense = GroundBehavior("North South Offense", 6, [gpunch], "Side Control Offense", "Side Control Offense", "North South Offense", "North South Defense", "Side Control Defense", "North South Defense", [armbar])
north_South_Defense = GroundBehavior("North South Defense", -5, [gpunch], "Side Control Defense", "Back Mount Defense", "North South Offense", "North South Defense", "Side Control Offense", "North South Offense", [])
back_Mount_Offense = GroundBehavior("Back Mount Offense", 7, [gpunch], "Full Mount Offense", "Escape", "Full Guard Defense", "North South Defense", "Full Mount Defense", "Back Mount Defense", [armbar])
back_Mount_Defense = GroundBehavior("Back Mount Defense", -6, [gpunch], "Full Mount Defense", "Escape", "Full Guard Offense", "Full Guard Defense", "Full Mount Offense", "Back Mount Offense", [])



# stack_guard_Offense = GroundBehavior("Stack Guard Offense", 1, [gpunch], full_Guard_Offense, gEscape, gEscape, gEscape, full_Guard_Defense, stack_guard_Defense, [armbar] )
# stack_guard_Defense = GroundBehavior("Stack Guard Defense", -5, [gpunch], gEscape, gEscape, full_Guard_Offense, full_Guard_Defense, gEscape, stack_guard_Offense, [armbar] )
# full_Guard_Offense = GroundBehavior("Full Guard Offense", 2, [gpunch], half_Guard_Offense, stack_guard_Offense, full_Guard_Offense, full_Guard_Defense, half_Guard_Defense, full_Guard_Defense, [armbar])
# full_Guard_Defense = GroundBehavior("Full Guard Defense", -1, [gpunch], gEscape, gEscape, full_Guard_Offense, full_Guard_Defense, gEscape, full_Guard_Offense, [armbar])
# half_Guard_Offense = GroundBehavior("Half Guard Offense", 3, [gpunch], side_Control_Offense, full_Guard_Offense, half_Guard_Offense, half_Guard_Defense, side_Control_Defense, half_Guard_Defense, [armbar])
# half_Guard_Defense = GroundBehavior("Half Guard Defense", -2, [gpunch], full_Guard_Defense, gEscape, half_Guard_Offense, half_Guard_Defense, full_Guard_Offense, half_Guard_Offense, [])
# side_Control_Offense = GroundBehavior("Side Control Offense", 4, [gpunch], full_Mount_Offense, gEscape, side_Control_Offense, side_Control_Defense, full_Mount_Defense, side_Control_Defense, [armbar])
# side_Control_Defense = GroundBehavior("Side Control Defense", -3, [gpunch], half_Guard_Defense, half_Guard_Defense, side_Control_Offense, side_Control_Defense, half_Guard_Offense, side_Control_Offense, [armbar])
# full_Mount_Offense = GroundBehavior("Full Mount Offense", 5, [gpunch], back_Mount_Offense, side_Control_Offense, full_Guard_Offense, full_Guard_Defense, back_Mount_Defense, full_Mount_Defense, [armbar])
# full_Mount_Defense = GroundBehavior("Full Mount Defense", -4, [gpunch], side_Control_Defense, back_Mount_Defense, full_Guard_Offense, full_Guard_Defense, side_Control_Offense, full_Mount_Offense, [])
# north_South_Offense = GroundBehavior("North South Offense", 6, [gpunch], side_Control_Offense, side_Control_Offense, north_South_Offense, north_South_Defense, side_Control_Defense, north_South_Defense, [armbar])
# north_South_Defense = GroundBehavior("North South Defense", -5, [gpunch], side_Control_Defense, back_Mount_Defense, north_South_Offense, north_South_Defense, side_Control_Offense, north_South_Offense, [])
# back_Mount_Offense = GroundBehavior("Back Mount Offense", 7, [gpunch], full_Mount_Offense, gEscape, full_Guard_Defense, north_South_Defense, full_Mount_Defense, back_Mount_Defense, [armbar])
# back_Mount_Defense = GroundBehavior("Back Mount Defense", -6, [gpunch], full_Mount_Defense, gEscape, full_Guard_Offense, full_Guard_Defense, full_Mount_Offense, back_Mount_Offense, [])


#_______________________________________Takedowns________________________________________
singleLegTakedown = takedownBehavior("Single Leg Takedown", 70, 4, 4, 4, 4, "Half Guard Offense", "Half Guard Defense")
doubleLegTakedown = takedownBehavior("Double Leg Takedown", 70, 4, 4, 4, 4, "Full Guard Offense", "Full Guard Defense")





#_______________________________________Clinch Positions__________________________________

againstCageOffense = clinchBehaviour("Against Cage Offense", "Cage Knee", 20, 3, 5, "Thai Clinch Offense", "Double Under Offense", "Against Cage Defense", [armbar], [singleLegTakedown])
againstCageDefense = clinchBehaviour("Against Cage Defense", "Defensive Cage Knee", 20, 2, -1, "Over Under", "Escape", "Against Cage Offense", [armbar], [singleLegTakedown])
overUnder = clinchBehaviour("Over Under", "Punch", 20, 2, 1, "Double Under Offense", "Escape", "Over Under", [armbar, kneebar], [singleLegTakedown])
singleCollar = clinchBehaviour("Single Collar", "Uppercut", 20, 2, 4, "Double Under Offense", "Over Under", "Double Under Defense", [armbar], [singleLegTakedown])
doubleUnderOffense = clinchBehaviour("Double Under Offense", "Shoulder Chuck", 20, 2, 3, "Thai Clinch Offense", "Over Under", "Double Under Defense", [armbar], [singleLegTakedown])
doubleUnderDefense = clinchBehaviour("Double Under Defense", "Punch", 20, 2, -1, "Over Under", "Escape", "Double Under Offense", [armbar, kneebar], [singleLegTakedown])
thaiClinchOffense = clinchBehaviour("Thai Clinch Offense", "Knee", 20, 3, 4, "Back Offense", "Double Under Offense", "Thai Clinch Defense", [armbar], [singleLegTakedown])	
thaiClinchDefense = clinchBehaviour("Thai Clinch Defense", "Punch", 20, 2, -1, "Over Under", "Escape", "Thai Clinch Offense", [armbar], [singleLegTakedown])
backOffense = clinchBehaviour("Back Offense", "Punch", 20, 2, 6, "Back Offense", "Double Under Offense", "Back Defense", [armbar, rnc], [singleLegTakedown])
backDefense = clinchBehaviour("Back Defense", "Elbow", 20, 2, -1, "Over Under", "Escape", "Back Offense", [armbar], [singleLegTakedown])


# againstCageOffense = clinchBehaviour("Against Cage Offense", "Cage Knee", 5, 3, 5, thaiClinchOffense, doubleUnderOffense, againstCageDefense, [armbar], [singleLegTakedown])
# againstCageDefense = clinchBehaviour("Against Cage Defense", "Defensive Cage Knee", 1, 2, -1, overUnder, cEscape, againstCageOffense, [armbar], [singleLegTakedown])
# overUnder = clinchBehaviour("Over Under", "Punch", 3, 2, 1, doubleUnderOffense, cEscape, overUnder, [armbar, kneebar], [singleLegTakedown])
# singleCollar = clinchBehaviour("Single Collar", "Uppercut", 4, 2, 4, doubleUnderOffense, overUnder, doubleUnderDefense, [armbar], [singleLegTakedown])
# doubleUnderOffense = clinchBehaviour("Double Under Offense", "Shoulder Chuck", 2, 2, 3, thaiClinchOffense, overUnder, doubleUnderDefense, [armbar], [singleLegTakedown])
# doubleUnderDefense = clinchBehaviour("Double Under Defense", "Punch", 1, 2, -1, overUnder, cEscape, doubleUnderOffense, [armbar, kneebar], [singleLegTakedown])
# thaiClinchOffense = clinchBehaviour("Thai Clinch Offense", "Knee", 10, 3, 4, backOffense, doubleUnderOffense, thaiClinchDefense, [armbar], [singleLegTakedown])	
# thaiClinchDefense = clinchBehaviour("Thai Clinch Defense", "Punch", 1, 2, -1, overUnder, cEscape, thaiClinchOffense, [armbar], [singleLegTakedown])
# backOffense = clinchBehaviour("Back Offense", "Punch", 3, 2, 6, backOffense, doubleUnderOffense, backDefense, [armbar, rnc], [singleLegTakedown])
# backDefense = clinchBehaviour("Back Defense", "Elbow", 1, 2, -1, overUnder, cEscape, backOffense, [armbar], [singleLegTakedown])
# escape = clinchBehaviour("Escape", "Escape", 0, 0, -5 , cEscape, cEscape, cEscape, [], [])

#________________________________________Players__________________________________________

p1 = PlayerName("Chad", "Gable", "Male", "Tiger", 130, 130, 100, 100, 70, 70, 7, 6, 9, 3,80, 80,  90, 90, 100,90,90, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 4, 5, 'Stand up', [Punch, Kick], [doubleLegTakedown], [armbar, rnc],[singleLegTakedown], [gpunch], [armbar], doubleUnderOffense, "Clinch Strike", full_Mount_Offense, gpunch,  50, 50, 50, 50 )
p2 = OtherPlayerName("Seth", "Rollins", "Male", "Weasel", 110, 110, 90, 90, 70, 70, 5, 2, 3, 90, 9, 80, 90, 80, 90,90,90, 85, 95, 95, 95, 85, 80, 85, 85, 85, 85, 85, 85, 5, 5, 'Stand up', [Kick, Punch], [doubleLegTakedown], [kneebar, armbar],[singleLegTakedown], [gpunch], [armbar], backOffense, "Clinch Takedown", back_Mount_Offense, armbar, 50, 50, 50, 50)

#________________________________________Game__________________________________________


Range = False  #Initiating the starting positions of the fighters. 
current_Player_Count = 0 # Setting the current turn count
Position = 'Stand up'  # Position keeps track of where the fight is. Functions depends on it. 
counter_Turn = 0 # Initializes the integer that determines how many counter attacks have been thrown. Helps me limit the counter function so opponents aren't just constantly countering each other. 
current_Turn = p1
second_Move = p2
counter_Attack = False
winner = "No one"
win_by = None




def go_First():  
    global current_Turn
    global second_Move
                    # This is a function that will run to see what player goes first
    p1A = p1.aggression/10       # Function takes in the user's set aggression level 
    p1Agg = p1A * (p1.stamina/10)  #Player's stamina plays a factor in the final score.
    p1A2 = (p1Agg * p1.footwork)/100    #Player's footwork is factored into the final score of aggression. 
    print(p1.first_Name + "score was " + str(p1A2))

    p2A = p2.aggression/10      #Player 2 is then calculated.
    p2Agg = p2A * (p2.stamina/10)
    p2A2 = (p2Agg * p2.footwork)/100
    print(p2.first_Name + "score was " + str(p2A2))

    if (p1A2 >= p2A2):    #whoever has the highest score will go first. 
        current_Turn = p1
        second_Move = p2
    else: 
        current_Turn = p2
        second_Move = p1
  
    
def in_Range(x, y, a, b):
    global current_Turn
    global second_Move
    global Range
    E = current_Turn.max_Stamina * (current_Turn.stamina_Aggression/100)  
    H = current_Turn.max_Health * (current_Turn.health_Aggression/100)
    print(str(E) + " Energy Aggression rating " + str(H) + " Health Aggression rating.")
    print(str(Range) + " TESTING THE RANGE")
    if( abs(x - a) <= 1 and abs(y - b) <= 1 ):
     #It goes: If Player One position X +1 is equal to Player Two position X and Player position Y +1 is equal to Player Two position y
     # Each or is supposed to be a different check. 
        Range = True
        print(str(Range))
        print("Position X = " + str(x) + " Position Y = " + str(y) + " is where " + current_Turn.first_Name + " is")
        print("Position X = " + str(a) + " Position Y = " + str(b) + " is where " + second_Move.first_Name + " is")

    elif ( ((y == 7 and b == 0) or (y == 0 and b == 7)) and (abs (x - a) <= 1) ):
        #This monstrosity of an if statement is so to make up for the lack of pathfinding in the game. SEE CHART. This makes it so the 0 and the 7 zones recognize when the players are next to each other. 
        Range = True
        print(str(Range))
        print("Position X = " + str(x) + " Position Y = " + str(y) + " is where " + current_Turn.first_Name + " is")
        print("Position X = " + str(a) + " Position Y = " + str(b) + " is where " + second_Move.first_Name + " is")       
    else:
        Range = False
        print(str(Range))
        print("Position X = " + str(x) + " Position Y = " + str(y) + " is where " + current_Turn.first_Name + " is")
        print("Position X = " + str(a) + " Position Y = " + str(b) + " is where " + second_Move.first_Name + " is")
	
    if(Range == True and current_Turn.stamina >= E and current_Turn.health >= H):
        S = current_Turn.strike_Tendency + current_Turn.clinch_Tendency + current_Turn.takedown_Tendency
        P_strike = (current_Turn.strike_Tendency / S) * 100
        print(str(P_strike) + " Is the P_Strike")
        P_clinch = (current_Turn.clinch_Tendency / S) * 100
        print(str(P_clinch) + " Is the P_clinch")
        roll = randint(0, 101)
        print(str(roll) + " Is the roll")
        if(roll < P_strike):
            initiate_Strike(current_Turn.stand_Attacks[randint(0,len(current_Turn.stand_Attacks) - 1)])
        elif(roll <= P_clinch + P_strike):
            initiate_Clinch()
        else:
            initiate_Takedown(current_Turn, second_Move)
        
    elif(Range == True and current_Turn.stamina <= E and current_Turn.health >= H): #If player is in range and their stamina is below the threshold they set but their health is not.
        stand_Still()
        
    elif(Range == True and current_Turn.stamina >= E and current_Turn.health <= H): #If players in range and the stamina is more than their set threshold but their health is lower.
        move_Defensively()     #IMPORTANT: We'll focus on AI movment in this game during the next part, for now, I just want to make sure the striking is correct.
       
    
    elif(Range == False and  current_Turn.stamina >= E and current_Turn.health >= H):
        print("Player is not in range and passed the checks-")    
        move_Offensively()
        
    elif(Range == False and current_Turn.stamina <= E and current_Turn.health <= H or current_Turn.health <= H):
        move_Defensively()
        
    else:
        stand_Still()
    
    
    
def initiate_Strike(Attack):
    global current_Turn
    global second_Move
    print(str(Attack.name))        
    P = Attack.base_Accuracy * (current_Turn.footwork * current_Turn.stamina) / (second_Move.footwork * second_Move.stamina) #The 50 is a placeholder right now. There's a process to determine what attack the computer will do, but I'm not sure how to do that yet and will come back to this. 
    print("The result of the Strike formula is this number: " + str(P))
    roll = randint(1,101)
    print(str(roll)) #The formula here determines if the attack reached the opponent, opponent will get the chance to defend themselves. 
    if(roll <= P):
        print("Will strike and opponent has a chance to dodge or block.")
        blockOrDodge(second_Move, current_Turn, Attack) #This function will take in the args of the defender and the attacker. 
    else:
        print("Player missed")
        current_Turn.stamina -= Attack.stamina_Cost
        current_Turn.max_Stamina -= Attack.stamina_Cost/2

        
 
def blockOrDodge(defender,attacker, Attack):
    #This will determine if the opponent blocks or dodges based on their stats. Dodge based characters are more likely to dodge, block based character will more likely block. 
    S = defender.dodge + defender.block
    P = (defender.dodge/S) * 100
    roll = randint(1, 101)
    print(str(roll) + " is the roll")
    print(str(P))
    if(roll <= P):
        print("Opponent will attempt to dodge") 
        dodge(defender, attacker, Attack) #PRIORITY: Can functions, inside a function, take the args of the original function?
    else:
        print("Opponent will attempt to block")  
        block(defender, attacker, Attack) #Player will attempt to block the attack


    # Dodge function
def dodge(defender, attacker, Attack): #Takes in two args. I set this up because they switch roles depending on success and failure. 
    global counter_Attack
    global counter_Turn
    global win_by
    print("Attempting to Dodge.")
    P = (defender.dodge * defender.stamina) / (attacker.footwork) #Formula to calculate Dodge score
    print("Calculated Dodge score: " + str(P))
    roll = randint(1, 101)
    print(str(roll) + " is the roll")
    if(roll < P):
        defender.stamina -= 1  
        counter_Attack = False
        counter_Turn = 0 #this is used in the counter strike function to determine if the attack thrown was a counter strike or not.
        c_attempt = defender.counter_Aggression * 7 #formula to determine if the player will attempt a counter strike or not. Counter strikes are high risk/high reward. If you land, it's big damage. If you miss, the opponent can get the chance to do the same for big damage. 
        roll = randint(1, 101)
        print("Counter Attempt score is : " + str(c_attempt))
        print("Roll score is: " + str(roll))

        if(roll <= c_attempt):
            print("Defender will initiate a counter strike.")
            counter_Strike(defender, attacker, Attack)
    else:
        print("Did not dodge in time. Full damage")
        if(counter_Attack == True): #Counter Strikes do double damage to the opponent. 
            print(str(defender.health) + " is defender's health")
            print(str(defender.max_Health) + " is defender's max health")

            defender.health -= Attack.damage * 2 #10 is a placeholder. Need to figure out how to pull a number from a attack list specific to the player.
            defender.max_Health -= ((Attack.damage * 2)/2)
            defender.stamina -= Attack.stamina_Drain * 2
            defender.max_Stamina -= (Attack.stamina_Drain * 2)/2
            print(str(defender.health) + " is defender's health")
            print(str(defender.max_Health) + " is defender's max health")
            win_by = Attack.name
            health_Check(win_by)
            counter_Attack = False
            counter_Turn = 0
        else:  #If defender fails to dodge, they take full damage of the attack.
            print(str(defender.health) + " is defender's health")
            print(str(defender.max_Health) + " is defender's max health") 
            defender.health -= Attack.damage
            defender.max_Health -= (Attack.damage/2)
            defender.stamina -= Attack.stamina_Drain 
            defender.max_Stamina -= Attack.stamina_Drain/2
            print(str(defender.health) + " is defender's health")
            print(str(defender.max_Health) + " is defender's max health")
            win_by = Attack.name
            health_Check(win_by)
            counter_Attack = False
            counter_Turn = 0

def block(defender, attacker, Attack):
    global counter_Turn
    global counter_Attack
    global win_by
    P = (defender.block * defender.stamina) / (attacker.footwork)
    print(str(P) + " is the block formula") #formula to calculate block score
    roll = randint(1, 101)
    print("Roll score is: " + str(roll))
    if(roll < P): #If they successfully passed the block check. 
        Mod = (Attack.damage * defender.block)/1000 #Damage of the attack will be mitigated. 
        print(str(defender.health) + " Is the Defender health")
        defender.stamina -= 1 
        defender.health -= round(Mod)
        print(str(defender.health) + " Is the Defender health")
        win_by = Attack.name
        health_Check(win_by)
        counter_Attack = False
        counter_Turn = 0
        c_attempt = defender.counter_Aggression * 10
        print(str(c_attempt) + " is the counter aggression score.") #formula to determine if the player will attempt a counter strike or not. Counter strikes are high risk/high reward. If you land, it's big damage. If you miss, the opponent can get the chance to do the same for big damage. 
        roll = randint(1, 101)
        print(str(roll) + " is the roll.")

        if(roll <= c_attempt):
            counter_Strike(defender, attacker, Attack) 
    else:  
        if(counter_Attack == True):
            print(str(defender.health) + " Is the Defender health")
            print(str(defender.max_Health) + " Is the Defender max health.")
            defender.health -= Attack.damage * 2
            defender.max_Health -= ((Attack.damage * 2)/2)
            defender.stamina -= Attack.stamina_Drain * 2
            defender.max_Stamina -= (Attack.stamina_Drain * 2)/2
            print(str(defender.health) + " Is the Defender health")
            print(str(defender.max_Health) + " Is the Defender max health.")
            win_by = Attack.name
            health_Check(win_by)
            counter_Attack = False
            counter_Turn = 0
        else:
            print(str(defender.health) + " Is the Defender health")
            print(str(defender.max_Health) + " Is the Defender max health.") 
            defender.health -= Attack.damage
            defender.max_Health -= (Attack.damage/2)
            defender.stamina -= Attack.stamina_Drain
            defender.max_Stamina -= Attack.stamina_Drain/2
            print(str(defender.health) + " Is the Defender health")
            print(str(defender.max_Health) + " Is the Defender max health.")
            win_by = Attack.name
            health_Check(win_by)
            counter_Attack = False
            counter_Turn = 0            
#
#    # Counter Strike occurs if attack is successfully blocked/dodged) 
def counter_Strike(defender,attacker, Attack):
    global counter_Attack 
    global counter_Turn
    P = Attack.base_Accuracy * (defender.footwork * defender.stamina) / (attacker.footwork * attacker.stamina)
    print(str(P) + " is the counter strike formula.") 
    roll = randint(1,101)
    print("Roll score is: " + str(roll))
    if(roll < P): 
        counter_Attack = True
        counter_Turn += 1
        if(counter_Turn == 3):
            counter_Turn = 0
            counter_Attack = False
            return
        else:
            print("Attacker is now Defender, Counter Strike Initiated")
            blockOrDodge(attacker, defender, Attack)  
    else:
        return
    
def new_Turn():
    global current_Turn
    global second_Move
    global Position
    print("New Turn has been started.")
    current_Turn.stamina += 8
    second_Move.stamina += 8
    if(Position == 'Stand up'): #Checks to see what position the players are in to determine the function that'll be run
        go_First()
        in_Range(current_Turn.posX, current_Turn.posY, second_Move.posX, second_Move.posY)
    elif(Position == 'Clinch'):
        clinch_Go_First()
        clinchTurn()
    else:
        ground_Go_First()
        ground_Turn()
    end_Turn()

def end_Turn():
    global current_Player_Count
    global current_Turn
    global second_Move
    print(str(current_Turn.first_Name) + " was the current player turn. " + str(second_Move.first_Name) + " is next.")
    current_Player_Count += 1 #Keeps track of the turns, after 2 turns, the function will run to determine who goes first again. 
    if(current_Player_Count >= 3):
        
        print("successful cycle")
        current_Player_Count = 0        
        new_Turn()
        

    if(current_Turn == p1): #If the current turn was player 1, switch the roles.
        current_Turn = p2
        second_Move = p1
        print(str(current_Player_Count))
        print(str(current_Turn.first_Name) + " is now the current turn")
        nextTurn()
                
    elif(current_Turn == p2): #If the current turn was player 2, switch the roles.
        current_Turn = p1
        second_Move = p2
        print(str(current_Player_Count))
        print(str(current_Turn.first_Name) + " is now the current turn")
        nextTurn()
    
        
#
def nextTurn(): #This is the same as new Turn but it doesn't run the function to see who goes first. 
    global current_Turn
    global second_Move
    global Position
    if(Position == "Stand up"):
        in_Range(current_Turn.posX, current_Turn.posY, second_Move.posX, second_Move.posY)
        
        
    elif(Position == "Clinch"):
        clinchTurn()
        
    else:
        print("Ground")
        ground_Turn()
    end_Turn()

# ____________________________________MOVEMENT____________________________________________________________#
# This next section deals with the movement of the game. Since there's no pathfinder, I had to jury-rig my own sort of finder. 

def move_Offensively():
    global current_Turn
    global second_Move    
    print(str(current_Turn.posY) + " Is the current player's position and  " + str(second_Move.posY) + "Is the second player's position")  
    move_To()
    current_Turn.stamina -= 1
#
#
#
def move_To():
    global current_Turn
    global second_Move    
    theta = (math.pi/4) * (second_Move.posY - current_Turn.posY)
    theta = (theta + math.pi) % math.tau - math.pi
    theta /= (math.pi/4)
    if theta == 0:
        print("Player is in Y range")

    elif theta < 0:
        current_Turn.posY -= 1
        if (current_Turn.posY == -1):
            current_Turn.posY = 7
    
    else:
        current_Turn.posY += 1
        if (current_Turn.posY == 8):
            current_Turn.posY = 0   
    print(str(current_Turn.posY) + " Is the current player's position and  " + str(second_Move.posY) + "Is the second player's position")
    move_OffensiveX()

def move_OffensiveX():
    global current_Turn
    global second_Move 
    print(str(current_Turn.posX) + "Is the current player's X position" + str(second_Move.posX) + " Is the second player's X position.")   
    Res =  second_Move.posX  - current_Turn.posX
    print(str(Res))  #Searches for the Opponent's X number and substracts it fro the player's
    if(Res >= 0 and current_Turn.posY == second_Move.posY): #If the result is 0 or greater and both players are in the same section, the player will move directly forward. 
	    current_Turn.posX += 1
    else:
	    current_Turn.posX -= 1 #Otherwise this means the player is in another section or behind them, so they'll move back towards the center of the ring. 
	    if(current_Turn.posX == 0): #Whoever is in the middle will have their Y position match their opponent's 
	        current_Turn.posY = second_Move.posY 
    print(str(current_Turn.posX) + "Is the current player's X position" + str(second_Move.posX) + "Is the second player's X position")
    print(str(current_Turn.posY) + " " + str(current_Turn.posX) + " Is the current player's position and  " + str(second_Move.posY) + " " + str(second_Move.posX) + " Is the second player's position")


def move_Defensively():
    global current_Turn
    global second_Move
    print(str(current_Turn.posY) + " " + str(current_Turn.posX) + " Is the current player's position and  " + str(second_Move.posY) + " " + str(second_Move.posX) + " Is the second player's position")    
    Res = second_Move.posY - current_Turn.posY 
    if (Res == second_Move.posY + 3 or Res == second_Move.posY - 3): 
        print("Player will stand still")
        stand_Still()
    else: #will run the move_Away function. Takes the Res variable as its argument - I can do that right?
        print("We're moving Defensively")
        move_Away(Res)
        current_Turn.stamina -= 1
#
#
def move_Away(Result): 
    global current_Turn
    global second_Move    
    if (Result > 0 and Result < 5 or Result <= -5): 
        current_Turn.posY -= 1 
        if(current_Turn.posY == -1): 
            current_Turn.posY = 7
               #Then will move their X position away from opponent. 
    elif(Result >= 5 or Result < 0): #If the result is greater than 5 or less than 0
        current_Turn.posY += 1 #Player will move counter clockwise from opponent
        if(current_Turn.posY == 8):
            current_Turn.posY = 0
            
    
    else: #This was for a specific condition, but I can't remember. I have it just in case none of the conditions are True
        ResB = randint(0,1) #Variable will randomly choose between 0 and 1. Based on that, opponent will move clockwise or counter-clockwise.
        if(ResB == 0):
            current_Turn.posY += 1
            if(current_Turn.posY == 8):
                current_Turn.posY = 0
                

        else:
            current_Turn.posY -= 1
            if(current_Turn.posY == -1):
                current_Turn.posY = 7
    move_DefensiveX()            
    print(str(current_Turn.posY) + " " + str(current_Turn.posX) + " Is the current player's position and  " + str(second_Move.posY) + " " + str(second_Move.posX) + " Is the second player's position")

def move_DefensiveX(): #This should move the player's X position away from the opponents
    global current_Turn
    global second_Move
    Res = second_Move.posX - current_Turn.posX  
    if(Res > 0 and current_Turn.posY == second_Move.posY): #If the result is a positive and they have the same Y number
        current_Turn.posX -= 1 #They'll move back, away from the opponent
        if(current_Turn.posX == 0 ): #If they back into the 0, they'll immediately choose to move the exact opposite section of the opponent. 
            current_Turn.posY = second_Move.posY + 3
    else: #This would mean the opponent is in front of them, and they want to move towards the cage to get away.
        current_Turn.posX += 1 
        if(current_Turn.posX == 6):
            current_Turn.posX = 5





def stand_Still(): #this is just another way of saying end turn. There will be some formula for stamina and health regen here, but I haven't created it yet. 
    global current_Turn
    global second_Move
    current_Turn.stamina += 3
    current_Turn.health += 3
    if current_Turn.stamina > current_Turn.max_Stamina:
        current_Turn.stamina = int(current_Turn.max_Stamina)
    elif current_Turn.health > current_Turn.max_Health:
        current_Turn.health = int(current_Turn.max_Health)
    return
#
#
## Hopefully this all checks out. There's some very unorthodoxed code but it's the best I can do considering complex algorithims and pathfinders are out of the scope of my programming skills. 
#
##________________________________CLINCHING__________________________________________
#
##This next portion is going to piss you off cause I'm pretty sure I'm breaking all kinds of common practices here. This next portion of the game deals with the Clinch. In real MMA, there's a system, a fighter can't just magically poof behind another fighter, there's got to be a process of movement. 
#I wasn't sure how else to define each position without utilizing classes, so I created an entire list of positions in the ClinchClasses.py Every number and position there is used in different functions specified below. 
#
def initiate_Clinch():
    global current_Turn
    global second_Move      
    global Position
    P = ((current_Turn.clinch_Grapple * current_Turn.stamina) / ((second_Move.clinch_Defense * second_Move.stamina) * 2) *100) #Formula to determine successful clinch attempt.
    roll = randint(0, 101)
    print(str(P) + " is the Clinch Score and " + str(roll) + " is the roll.")
    if roll < P and current_Turn.posX < second_Move.posX:
        Position = 'Clinch'  
        current_Turn.posX += 1
        second_Move.posX += 1
        if(second_Move.posX or current_Turn.posX >= 5):  
            current_Turn.posX = 5
            second_Move.posX = 5
            current_Turn.position = againstCageOffense
            second_Move.position = againstCageDefense
            current_Turn.stamina -= 3
            current_Turn.max_Stamina -= 1
            print(str(current_Turn.position.position_Name) + " is the current position along with the opponent's : " + str(second_Move.position.position_Name))	
            in_Clinch()    
        else: 
            current_Turn.posX -= 1
            second_Move.posX -= 1
            current_Turn.position = overUnder
            second_Move.position = overUnder
            current_Turn.stamina -= 3
            current_Turn.max_Stamina -= 1
            print(str(current_Turn.position.position_Name) + " is the current position along with the opponent's : " + str(second_Move.position.position_Name))	
            
            in_Clinch()
#
    else: #If the clinch attempt failed, the opponent will have the chance to counter. 
        c_attempt = second_Move.clinch_Counter_Aggression * 5
        roll = randint(0,101)
        if(roll < c_attempt):
            initiate_Counter_Clinch()
        else:
            print("Not in Clinch")

def initiate_Counter_Clinch():
    global current_Turn
    global second_Move  
    global Position    
    print("Initiating Counter Clinch")
    P = ((second_Move.clinch_Defense * second_Move.stamina)/ ((current_Turn.clinch_Defense/current_Turn.stamina) * 2) /100)
    roll = randint(0,101)
    print(str(P) + " is the Clinch Score and " + str(roll) + " is the roll.")

    if(roll < P): #If counter is successful.
        Position = 'Clinch'
        current_Turn.position = doubleUnderDefense
        second_Move.position = doubleUnderOffense 
        current_Turn.stamina -= 3
        current_Turn.max_Stamina -= 1
        second_Move.stamina -= 1
        second_Move.max_Stamina -= 1 #This is a very good position to be in.
        print(str(current_Turn.position.position_Name) + " is the current position along with the opponent's : " + str(second_Move.position.position_Name))	

        in_Clinch() 
    else:
        second_Move.stamina -= 3
        second_Move.max_Stamina -= 1
        return
#
def in_Clinch():  #This function will run to see who goes first in the clinch and then runs the turn. 
    clinch_Go_First()
    clinchTurn()
#
#
def clinch_Go_First():
    global current_Turn
    global second_Move  

    p1A = p1.clinch_Aggression 
    p1Agg = p1A * (p1.stamina/10)
    p1A2 = p1Agg * (p1.clinch_Grapple/100)
    print(p1.first_Name + " score was " + str(p1A2))

    p2A = p2.clinch_Aggression 
    p2Agg = p2A * (p2.stamina/10)
    p2A2 = p2Agg * (p2.clinch_Grapple/100)
    print(p2.first_Name + " score was " + str(p2A2))
    if(p1A2 > p2A2):
        current_Turn = p1
        second_Move = p2
    else:
        current_Turn = p2
        second_Move = p1
    print(str(current_Turn.first_Name) + " goes First")
    print(str(second_Move.first_Name) + " goes Second")    


def clinchTurn():
    global current_Turn
    global second_Move        
    Goal = current_Turn.clinch_Desired_Position #Checks where the player wants to be
    dAttack = current_Turn.clinch_Desired_Attack #Checks what they want to do when they're in their desired position
    E = current_Turn.max_Stamina * (current_Turn.health_Aggression/100) #Checks their aggression levels to determine offensive/defensive behavior.
    H = current_Turn.max_Health * (current_Turn.stamina_Aggression/100)
    if(Goal == "Escape" or current_Turn.health <= H ): #If their goal is to escape or not be in the clinch, or their health dips below their aggression level, they'll try to escape. 
	    cEscape() 
    elif(current_Turn.stamina <= E and current_Turn.health >= H):  
	    stand_Still()
    else:
        if(E and current_Turn.submission_Tendency > second_Move.stamina):
            print(str(current_Turn.first_Name) + " will now attempt submission.")
            initiate_Clinch_Submission(current_Turn.position)
        else:
            D = int(current_Turn.clinch_Striking) + int(current_Turn.clinch_Transition)
            P = (current_Turn.clinch_Striking/D) * 100
            roll = randint(0,101)
            if(roll <= P):
                initiate_Clinch_Strike(current_Turn.position)  #This takes their position as an argument.
                
            else:
                print(str(current_Turn.first_Name) + " will now attempt a clinch transition.")
                clinchTransition() #This takes their desired attack as an argument.            


def clinch_Block_Strike(attack_Damage, defender):
    global current_Turn
    global second_Move 
    global win_by
    print("Defender will attempt to block the strike.")   
    P = (second_Move.clinch_Defense * second_Move.stamina) / (current_Turn.clinch_Striking)
    roll = randint(0,101)
    print(str(P) + " is the score, " + str(roll) + " is the roll.")
    if(roll <= P): #If successfully blocked, the damage taken is mitigated by a lot. 
        print("Attack was successfully blocked")
        Mod = (attack_Damage * second_Move.clinch_Defense)/1000
        print(str(defender.health) + " Is the Defender health")
        print(str(defender.max_Health) + " Is the Defender max health.")        
        second_Move.health -= round(Mod)
        second_Move.max_Health -= round(Mod/2)
        second_Move.stamina -= 1
        win_by = current_Turn.position.attack_Name
        health_Check(win_by)
        current_Turn.stamina -= current_Turn.position.stamina_Cost
        current_Turn.max_Stamina -= current_Turn.position.stamina_Cost/2
        print(str(defender.health) + " Is the Defender health")
        print(str(defender.max_Health) + " Is the Defender max health.")        
    else:
        print(str(defender.health) + " Is the Defender health")
        print(str(defender.max_Health) + " Is the Defender max health.")        
        second_Move.health -= attack_Damage
        second_Move.max_Health -= (attack_Damage/2)
        second_Move.stamina -= 2
        second_Move.max_Stamina -= 1
        win_by = current_Turn.position.attack_Name
        health_Check(win_by)
        current_Turn.stamina -= current_Turn.position.stamina_Cost
        current_Turn.max_Stamina -= current_Turn.position.stamina_Cost/2
        print(str(defender.health) + " Is the Defender health")
        print(str(defender.max_Health) + " Is the Defender max health.")

def clinchTransition():

    global current_Turn
    global second_Move

    print("Player will attempt to transition in the clinch")
    P = ((current_Turn.clinch_Transition * current_Turn.stamina) / (second_Move.clinch_Defense * second_Move.stamina) * 100)
    roll = randint(0,101)
    print(str(P) + " is the score, " + str(roll) + " is the roll.")
    if(roll <= P):
        if(current_Turn.position != current_Turn.clinch_Desired_Position and current_Turn.position.rank < current_Turn.clinch_Desired_Position.rank):
            current_Turn.position = current_Turn.position.advance_Position
            checkClinchClass(current_Turn)
            second_Move.position = current_Turn.position.opp_New_Pos
            checkClinchClass(second_Move)
            current_Turn.stamina -= 3
            current_Turn.max_Stamina -= 1
            print(str(current_Turn.position.position_Name) + " is the position the player is in while their opponent is " + str(second_Move.position.position_Name))#This switches the opponents position to be opposite the player. This way no won't in Full Guard while the Opponent has their back- that'd make no sense. 
        elif(current_Turn.position.rank > current_Turn.clinch_Desired_Position.rank):
            current_Turn.position = current_Turn.position.decrease_Position
            checkClinchClass(current_Turn)
            second_Move.position = current_Turn.position.opp_New_Pos
            checkClinchClass(second_Move)
            current_Turn.stamina -= 3
            current_Turn.max_Stamina -= 1
            print(str(current_Turn.position.position_Name) + " is the position the player is in while their opponent is " + str(second_Move.position.position_Name))#This switches the opponents position to be opposite the player. This way no won't in Full Guard while the Opponent has their back- that'd make no sense. 

        else:
            print("Player is where they want to be.")
            checkClinchDesiredAttack(current_Turn) #Turns out you CAN put functions as attributes so long as you don't use the () in the attribute itself, only when its time to be called. 
    else:
         #If the player failed the transition attempt, opponent can attempt to counter. 
        c_attempt = second_Move.clinch_Counter_Aggression * 5
        roll = randint(0,101)
        if(roll < c_attempt):
            print("Transition failed, opponent will attempt reversal")
            initate_Clinch_Reversal()
            print(str(current_Turn.position) + " is the position the player is in while their opponent is " + str(second_Move.position))
        current_Turn.stamina -= 4
        current_Turn.max_Stamina -= 2
#            

def initiate_Clinch_Strike(currentPlayerPosition):
    global current_Turn
    global second_Move
    
    Damage = currentPlayerPosition.damage * (current_Turn.clinch_Striking/1000)
    AttackName = currentPlayerPosition.attack_Name
    print(str(current_Turn.first_Name) + " is attacking with " + str(AttackName)) 
    clinch_Block_Strike(Damage, second_Move)



def initate_Clinch_Reversal():
    global current_Turn
    global second_Move    
    P = ((second_Move.clinch_Transition + second_Move.clinch_Grapple) * second_Move.stamina)/ ((current_Turn.clinch_Transition + current_Turn.clinch_Defense) * current_Turn.stamina) * 4 
    roll = randint(0,101)
    if(roll < P): #If the counter is successful, opponent and player will switch positions.
        reversed_Position = second_Move.position
        second_Move.position = current_Turn.position
        current_Turn.position = reversed_Position
        second_Move.stamina -= 2
        second_Move.max_Stamina -= 1
        
    else: #If opponent failed at the counter, the consequence is the player getting another chance to strike. 
        initiate_Clinch_Strike(current_Turn.position)
        second_Move.stamina -= 3
        second_Move.max_Stamina -= 2

def initiate_Clinch_Takedown(currentPosition):
    global current_Turn
    global second_Move
    global Position
  
    print("Player will initiate clinch takedown.") 
    P = ((current_Turn.takedown * current_Turn.stamina) / ((second_Move.takedown_Defense/second_Move.stamina) * 2)/100)
    roll = randint(0,101)
    print(str(P) + " is the score, " + str(roll) + " is the roll.")
    if (roll < P):
        availableMoves = [x for x in current_Turn.clinch_Takedowns if x in currentPosition.takedowns]
        print(str(current_Turn.clinch_Takedowns))
        print(str(currentPosition.takedowns))
        print(str(availableMoves)) 
        if not availableMoves:
            print("No takedowns available.")
            D = current_Turn.clinch_Striking + current_Turn.clinch_Transition
            P = (current_Turn.clinch_Striking/D) * 100
            roll = randint(0,101)
            if(roll <= P): 
                print("Player did not have any submission moves, will attempt a strike")
                initiate_Clinch_Strike(current_Turn.position)  #This takes their position as an argument.
            
            else:
                print("Player did have any submission moves, will attempt a strike")
                clinchTransition() #This takes their desired attack as an argument.
        else:
            Position = "Ground"
            availableMoves = current_Turn.clinch_Takedowns[randint(0, len(current_Turn.clinch_Takedowns) - 1)]
            current_Turn.position = availableMoves.new_Pos
            checkGroundPosition(current_Turn)
            second_Move.position = availableMoves.opp_Pos
            checkGroundPosition(second_Move)
            print("Player sucessfully completed Takedown " + str(current_Turn.position.name) + " and their opponenet is " + str(second_Move.position.name))

    else:
        print("Player failed in their takedown attempt")
        c_attempt = second_Move.clinch_Counter_Aggression * 5
        roll = randint(0,101)
        if(roll < c_attempt):
            print("Initiating Counter Clinch")
            initiate_Counter_Clinch_Takedown(second_Move, current_Turn)         

def initiate_Clinch_Submission(currentPosition):
    global current_Turn
    global second_Move
    global winner
    global win_by   
    availableMoves = [x for x in current_Turn.clinch_Submissions if x in currentPosition.submissions] 
    print(str(current_Turn.clinch_Submissions))
    print(str(currentPosition.submissions))
    print(str(availableMoves))  
    if availableMoves:
        submission = availableMoves[randint(0, len(availableMoves) - 1)]
        print("Player will a attempt a " + str(submission.name))
        for i in range(0, submission.gates):
            P = submission.base_Attack * (current_Turn.submission_Offense * current_Turn.stamina)/(second_Move.submission_Defense * second_Move.stamina)
            roll = randint(0, 101)
            current_Turn.stamina -= 3
            current_Turn.max_Stamina -= 2
            print(str(P) + " is the score, " + str(roll) + " is the roll.")
            if roll > P:
                second_Move.position = second_Move.position.advance_Position
                checkClinchClass(second_Move)
                current_Turn.position = second_Move.position.opp_New_Pos
                checkClinchClass(current_Turn)
                print("Player failed the submission attempt. Current player is now " + str(current_Turn.position.position_Name) + " and their opponenet is " + str(second_Move.position.position_Name))
                return
        winner = current_Turn.first_Name
        win_by = str(submission.name)
        matchOver()
    else:
        
        D = current_Turn.clinch_Striking + current_Turn.clinch_Transition
        P = (current_Turn.clinch_Striking/D) * 100
        roll = randint(0,101)
        if(roll <= P): 
            print("Player did not have any submission moves, will attempt a strike")
            initiate_Clinch_Strike(current_Turn.position)  #This takes their position as an argument.
            
        else:
            print("Player did have any submission moves, will attempt a strike")
            clinchTransition() #This takes their desired attack as an argument. 
            

      

def initiate_Counter_Clinch_Takedown(defender, offense):
        global Position
        availableMoves = [x for x in defender.clinch_Takedowns if x in defender.position.takedowns] 
        if not availableMoves:
            return
        else:
            takedown = availableMoves[randint(0, len(availableMoves) - 1)]
            P = (((defender.clinch_Grapple * defender.stamina) / (offense.takedown_Defense * offense.stamina)*2)/100) #Checks if the counter will reach the opponent.
            roll = randint(1,101)
            print(str(P) + " is the score, " + str(roll) + " is the roll.")
            if (roll < P): #If they pass the check, Counter Attack becomes True. This keeps track of the counter Turns so there can be a counter attack, and the opponent can counter the counter before it's a new turn. 
                
                Position = "Ground"
                defender.position = takedown.new_Pos
                checkGroundPosition(defender)
                offense.position = takedown.opp_Pos
                checkGroundPosition(offense)
                defender.stamina -= 2
                defender.max_Stamina -= 1
                print(str(defender) + " successfully completed the counter takedown, their position is " + str(defender.position.name) + " and their opponent's is " + str(offense.position.name))    
            else:
                Position = "Clinch"
                defender.position = overUnder
                offense.position = overUnder
                defender.stamina -= 4
                defender.max_Stamina -= 2
                print(str(defender.first_Name) + " couldn't complete the counter takedown. Both positions are " + str(defender.position))


def cEscape():
    global current_Turn
    global second_Move
    global Position
    if current_Turn.position in [againstCageOffense, doubleUnderOffense, thaiClinchOffense, backOffense]:
        Position = "Stand up"
        current_Turn.position = 'Stand up'
        second_Move.position = 'Stand up'
        move_Defensively()
        
    else:
        P = (current_Turn.clinch_Defense * current_Turn.stamina) / ((second_Move.clinch_Transition * second_Move.stamina)* 2)
        roll = randint(0, 101)
        if (roll < P):
            Position = "Stand up"
            current_Turn.position = 'Stand up'
            second_Move.position = 'Stand up'
            move_Defensively()

def checkClinchClass(player):
    global againstCageOffense
    global againstCageDefense
    global overUnder
    global singleCollar
    global doubleUnderOffense
    global doubleUnderDefense
    global thaiClinchOffense
    global thaiClinchDefense
    global backOffense
    global backDefense
    global current_Turn
    global second_Move
    if player.position == "Against Cage Offense":
        player.position = againstCageOffense
    elif player.position == "Against Cage Defense":
        player.position = againstCageDefense
    elif player.position == "Over Under":
        player.position = overUnder
    elif player.position == "Single Collar":
        player.position = singleCollar
    elif player.position == "Double Under Offense":
        player.position = doubleUnderOffense
    elif player.position == "Double Under Defense":
        player.position = doubleUnderDefense
    elif player.position == "Thai Clinch Offense":
        player.position = thaiClinchOffense
    elif player.position == "Thai Clinch Defense":
        player.position = thaiClinchDefense
    elif player.position == "Back Offense":
        player.position = backOffense
    elif player.position == "Back Defense":
        player.position = backDefense
    else:
        cEscape()
    return player.position            

def checkClinchDesiredAttack(player):
    if player.clinch_Desired_Attack == "Clinch Strike":
        initiate_Clinch_Strike(player.position)
    elif player.clinch_Desired_Attack == "Clinch Takedown":
        initiate_Clinch_Takedown(player.position)
    else: 
        initiate_Clinch_Submission(player.position)

## _________________________*GROUND GAME* __________________________________________
## This next series of code focuses on the ground aspects of the game. It's similar to the clinch- system of movement. 
#
#
#
#
#
def initiate_Takedown(offense, defender):
    global current_Turn
    global second_Move
    global Position   
    P = ((offense.takedown * offense.stamina) / ((defender.takedown_Defense/defender.stamina) * 2)/100)
    roll = randint(0,101)
    print(str(P) + " is the score, " + str(roll) + " is the roll.")
    if (roll < P):
        Position = "Ground"
        availableMoves = offense.stand_Takedowns[randint(0, len(offense.stand_Takedowns) - 1)]
        offense.position = availableMoves.new_Pos
        checkGroundPosition(offense)
        defender.position = availableMoves.opp_Pos
        checkGroundPosition(defender)
        offense.stamina -= 5
        offense.max_Stamina -= 2
        print(str(offense.first_Name) + " completed their takedown, their new position is " + str(offense.position.name) + " and their opponent's is " + str(defender.position.name))
        ground_Go_First()
        ground_Turn()
    else:
        print("defender will attempt a counter takedown.")
        c_attempt = second_Move.clinch_Counter_Aggression * 5
        roll = randint(0,101)
        if(roll < c_attempt):
            initate_Counter_Takedown(defender, offense)
    


def initate_Counter_Takedown(defender, offense):
    global Position 
    P =  (((defender.takedown * defender.stamina) / (offense.takedown_Defense * offense.stamina)*2) * 15) #Checks if the counter will reach the opponent.
    roll = randint(0,101)
    print(str(P) + " is the score, " + str(roll) + " is the roll.")
    if (roll < P): #If they pass the check, Counter Attack becomes True. This keeps track of the counter Turns so there can be a counter attack, and the opponent can counter the counter before it's a new turn. 
        availableMoves = defender.stand_Takedowns[randint(0, len(defender.stand_Takedowns) - 1)]
        Position = "Ground"
        defender.position = availableMoves.new_Pos
        checkGroundPosition(defender)
        offense.position = availableMoves.opp_Pos
        checkGroundPosition(offense)
        defender.stamina -= 2
        defender.max_Stamina -= 1
        print(str(defender.first_Name) + " completed their counter takedown, their new position is " + str(defender.position.name) + " and their opponent's is " + str(offense.position.name))
         
    else:
        Position = "Clinch"
        defender.position = overUnder
        offense.position = overUnder
        defender.stamina -= 4
        defender.max_Stamina -= 2
        print(str(defender) + " couldn't complete the counter takedown. Both positions are " + str(offense.position))
        

def ground_Go_First():
    global current_Turn
    global second_Move
    p1A = p1.ground_Aggression 
    p1Agg = p1A * (p1.stamina/10)
    p1A2 = p1Agg * (p1.ground_Offense/100)
    print(p1.first_Name + "score was " + str(p1A2))

    p2A = p2.ground_Aggression 
    p2Agg = p2A * (p2.stamina/10)
    p2A2 = p2Agg * (p2.ground_Offense/100)
    print(p2.first_Name + "score was " + str(p2A2))

    if(p1A2 > p2A2):
        current_Turn = p1
        second_Move = p2
    else:
        current_Turn = p2
        second_Move = p1
    print(str(current_Turn.first_Name) + " goes First")
    print(str(second_Move.first_Name) + " goes Second")

def ground_Turn():
    global current_Turn
    global second_Move
    Goal = current_Turn.ground_Desired_Position #Checks where the player wants to be
    dAttack = current_Turn.ground_Desired_Attack #Checks what they want to do when they're in their desired position
    E = current_Turn.max_Stamina * (current_Turn.health_Aggression/100) #Checks their aggression levels to determine offensive/defensive behavior.
    H = current_Turn.max_Health * (current_Turn.stamina_Aggression/100)
    if(Goal == "Escape" or current_Turn.health <= H or current_Turn.position == "Escape" or second_Move.position == "Escape"): #If their goal is to escape or not be in the clinch, or their health dips below their aggression level, they'll try to escape. 
        gEscape() 
    elif(current_Turn.stamina <= E and current_Turn.health >= H): #If they're tired, they'll rest instead of escaping. 
	    stand_Still()
    else:
        if(E and current_Turn.submission_Tendency > second_Move.stamina): #If their stamina aggression and their tendency are higher than the opponents stamina (They see them tired)
            initiate_Submission_Attempt(current_Turn, second_Move)
        else:
            print("this is a ground turn")
            D = current_Turn.ground_Striking + current_Turn.ground_Transition
            P = (current_Turn.ground_Striking/D) * 100
            roll = randint(0,101)
            print(str(P) + " is the score, " + str(roll) + " is the roll.")
            if(roll <= P):
                print(str(current_Turn.first_Name) + " Player will attempt to strike") 
                ground_Strike()  #This takes their position as an argument.
            
            else:
                print(str(current_Turn.first_Name) + " Player will attempt to transition")
                checkGroundPosition(current_Turn)
                checkGroundPosition(second_Move) 
                ground_Transition(dAttack) #This takes their desired attack as an argument. 
    


def ground_Block_Strike(offense, defender, Damage, attackName, staminaDrain):
    global win_by
    print(str(defender.first_Name) + " will attempt to block the strike.")
    P = (defender.ground_Defense * defender.stamina)/(offense.ground_Offense)
    roll = randint(0,101)
    print(str(P) + " is the score, " + str(roll) + " is the roll.")
    print(str(defender.health) + " is defender's health")
    print(str(defender.max_Health) + " is defender's max health")
    if (roll < P):
        print("Defender successfully blocked the attack.")
        Mod = (Damage * defender.ground_Defense)/1000
         #Damage is mitigated
        defender.health - round(Mod)
        c_attempt = defender.ground_Counter_Aggression * 5
        roll = randint(0,101)
        if(roll < c_attempt):
            P = defender.submission_Tendency + defender.ground_Aggression
            S = (defender.submission_Tendency/ P)
            roll = randint(0, 101)
            if roll < S:
                print("Player will attempt counter submission.")
                initiate_Submission_Attempt(defender, offense)
            else:
                print("Opponent blocked strike and will attempt to sweep the Player over")
                initiate_Sweep(defender, offense) #Opponent will try to sweep the player.
#
    else:
        print(str(defender.health) + " is defender's health")
        print(str(defender.max_Health) + " is defender's max health")
        defender.health -= Damage  #Full Damage
        defender.max_Health -= (Damage/2) 
        defender.stamina -= staminaDrain
        defender.max_Stamina -= staminaDrain/2
        print(str(defender.health) + " is defender's health")
        print(str(defender.max_Health) + " is defender's max health")
        win_by = attackName
        health_Check(win_by)
#
def ground_Transition(desiredAttack):
    global current_Turn
    global second_Move
    P = ((current_Turn.ground_Transition * current_Turn.stamina)/(second_Move.ground_Defense * second_Move.stamina)*100)
    roll = randint(0,101)
    checkGroundPosition(current_Turn)
    checkGroundPosition(second_Move) 
    print(str(P) + " is the score, " + str(roll) + " is the roll.")
    if(roll < P):
        if(current_Turn.position != current_Turn.ground_Desired_Position and current_Turn.position.rank < current_Turn.ground_Desired_Position.rank):
            second_Move.position = current_Turn.position.opp_New_Pos
            checkGroundPosition(second_Move)
            checkGroundPosition(current_Turn)    
            current_Turn.position = current_Turn.position.advance_Position
            checkGroundPosition(current_Turn)
            current_Turn.stamina -= 3
            current_Turn.max_Stamina -= 1
#            print("Player completed transition, player is at " + str(current_Turn.position.name) + " and the opponent is at " + str(second_Move.position.name))
            if(current_Turn.position == "Escape"):
                gEscape()
        elif(current_Turn.position.rank > current_Turn.ground_Desired_Position.rank):
            current_Turn.position = current_Turn.position.decrease_Position
            checkGroundPosition(current_Turn)
            second_Move.position = current_Turn.position.opp_Dec_Pos
            checkGroundPosition(second_Move)
            current_Turn.stamina -= 3
            current_Turn.max_Stamina -= 1
            print("Player completed transition, player is at " + str(current_Turn.position.name) + " and the opponent is at " + str(second_Move.position.name))
            if(current_Turn.position == "Escape"):
                gEscape()
        else:
            if desiredAttack.attack_Type == "Strike":
                desired_Ground_Strike(desiredAttack)
            elif desiredAttack.attack_Type == "Submission": 
                desired_Submission_Attempt(desiredAttack)
    else: 
        print("Transition failed, opponent will attempt to sweep them. ")
        current_Turn.stamina -= 4
        current_Turn.max_Stamina -= 2       
        if second_Move.position in [stack_guard_Defense, full_Guard_Defense, half_Guard_Defense, side_Control_Defense, full_Mount_Defense, north_South_Defense, back_Mount_Defense]:
            print("True. Counter Attempt initiated.")
            c_attempt = second_Move.ground_Counter_Aggression * 5
            roll = randint(0,101)
            if(roll < c_attempt):
                initiate_Sweep(second_Move, current_Turn)
        else:
            print("Player not in a Sweep position.")
def initiate_Sweep(defender, offense):
    P = (((defender.ground_Transition + defender.ground_Defense) * defender.stamina)/ ((offense.ground_Transition + offense.ground_Defense) * offense.stamina) * 20)
    roll = randint(0,101)
    print(str(P) + " is the score, " + str(roll) + " is the roll.")
    if (roll < P):
        defender.position = defender.position.sweep
        checkGroundPosition(defender)
        offense.position = defender.position.reversed_Position 
        checkGroundPosition(offense)
        defender.stamina -= 2
        defender.max_Stamina -= 2
        print("Sweep attempt successful, " + str(defender.position.name) + " is the defender's position and the opponent's is " + str(offense.position.name))
    else:
        print("Sweep attempt not successful.")
        defender.stamina -= 2
        defender.max_Stamina -= 2

def desired_Ground_Strike(desiredAttack):
    global current_Turn
    global second_Move
    attack = desiredAttack  
    Damage = attack.damage * (current_Turn.ground_Striking/1000)
    attackName = attack.name
    staminaDrain = attack.stamina_Drain
    ground_Block_Strike(current_Turn, second_Move, Damage, attackName, staminaDrain) 




def ground_Strike():
    global current_Turn
    global second_Move
    availableMoves = [x for x in current_Turn.ground_Attacks if x in current_Turn.position.attacks] 
    attack = availableMoves[randint(0, len(availableMoves) -1)]  
    Damage = attack.damage * (current_Turn.ground_Striking/1000) #Damage modifier based on their attributes 
    attackName = attack.name
    staminaDrain = attack.stamina_Drain 
    current_Turn.stamina -= attack.stamina_Drain
    current_Turn.max_Stamina -= attack.stamina_Drain/2
    ground_Block_Strike(current_Turn, second_Move, Damage, attackName, staminaDrain) #Opponent has the chance to block. Takes the player, opponent, and damage as arguments. 


def initiate_Submission_Attempt(attackingPlayer, defendingPlayer):
    global winner
    global win_by
    availableMoves = [x for x in attackingPlayer.ground_Submissions if x in attackingPlayer.position.submissions] 
    if not availableMoves:
        print("No available submissions")
        ground_Strike()
    else:
        submission = availableMoves[randint(0, len(availableMoves) - 1)]
        print("Player will a attempt a " + str(submission.name))
        for i in range(0, submission.gates):
            P = submission.base_Attack * (attackingPlayer.submission_Offense * attackingPlayer.stamina)/(defendingPlayer.submission_Defense * defendingPlayer.stamina)
            roll = randint(0, 101)
            print(str(P) + " is the score, " + str(roll) + " is the roll.")
            if roll > P:
                defendingPlayer.position = defendingPlayer.position.advance_Position
                checkGroundPosition(defendingPlayer)
                attackingPlayer.position = defendingPlayer.position.opp_New_Pos
                checkGroundPosition(attackingPlayer)
                print("Player failed the submission attempt. Current player is now " + str(attackingPlayer.position.name) + " and their opponenet is " + str(defendingPlayer.position.name))
                return

    winner = attackingPlayer.first_Name
    win_by = str(submission.name)
    matchOver()

def desired_Submission_Attempt(desiredAttack):
    global winner
    global win_by
    global current_Turn
    global second_Move
    


    submission = desiredAttack
    print("Player will a attempt a " + str(submission.name))

    for i in range(0, submission.gates):
        P = submission.base_Attack * (current_Turn.submission_Offense * current_Turn.stamina)/(second_Move.submission_Defense * second_Move.stamina)
        roll = randint(0, 101)
        print(str(P) + " is the score, " + str(roll) + " is the roll.")
        if roll > P:
            second_Move.position = second_Move.position.advance_Position
            checkGroundPosition(second_Move)
            current_Turn = second_Move.position.opp_New_Pos
            checkGroundPosition(current_Turn)
            print("Player failed the submission attempt. Current player is now " + str(current_Turn.position.position_Name) + " and their opponenet is " + str(second_Move.position.position_Name))
            return

    winner = current_Turn.first_Name
    win_by = str(submission.name)
    matchOver()




def gEscape():
    global current_Turn
    global second_Move
    global Position
    if current_Turn.position in [side_Control_Offense, full_Mount_Offense, back_Mount_Offense, north_South_Offense]: #If opponent is in these dominant positions, they should be able to get right up. 
        Position = "Stand up"
        
        current_Turn.position = 'Stand up'
        second_Move.position = 'Stand up'
        move_Defensively()
        
    else:
        P = (current_Turn.ground_Defense * current_Turn.stamina) / ((second_Move.ground_Offense * second_Move.stamina)* 2)
        roll = randint(0, 101)
        if (roll < P):
            Position = "Stand up"
            current_Turn.position = 'Stand up'
            second_Move.position = 'Stand up'
            move_Defensively()
        else:
            print("Player failed to escape.")
            Position = "Ground"
            current_Turn.position = "Full Guard Defense"
            second_Move.position = "Full Guard Offense"
            checkGroundPosition(current_Turn)
            checkGroundPosition(second_Move)
    print(str(Position) + str(current_Turn.position) + str(second_Move.position))


def checkGroundPosition(player):
    global stack_guard_Offense
    global stack_guard_Defense
    global full_Guard_Offense
    global full_Guard_Defense
    global half_Guard_Offense
    global half_Guard_Defense
    global side_Control_Offense
    global side_Control_Defense
    global full_Mount_Offense
    global full_Mount_Defense
    global north_South_Offense
    global north_South_Defense
    global back_Mount_Offense
    global back_Mount_Defense
    if player.position == "Stack Guard Offense":
        player.position = stack_guard_Offense
    elif player.position == "Stack Guard Defense":
        player.position = stack_guard_Defense
    elif player.position == "Full Guard Offense":
        player.position = full_Guard_Offense
    elif player.position == "Full Guard Defense":
        player.position = full_Guard_Defense
    elif player.position == "Half Guard Offense":
        player.position = half_Guard_Offense
    elif player.position == "Half Guard Defense":
        player.position = half_Guard_Defense
    elif player.position == "Side Control Offense":
        player.position = side_Control_Offense
    elif player.position == "Side Control Defense":
        player.position = side_Control_Defense
    elif player.position == "Full Mount Offense":
        player.position = full_Mount_Offense
    elif player.position == "Full Mount Defense":
        player.position = full_Mount_Defense
    elif player.position == "North South Offense":
        player.position = north_South_Offense
    elif player.position == "North South Defense":
        player.position = north_South_Defense
    elif player.position == "Back Mount Offense":
        player.position = back_Mount_Offense
    elif player.position == "Back Mount Defense":
        player.position = back_Mount_Defense
    else:
        gEscape()
    return player.position


def matchOver():
    global winner
    global win_by    
    print("Winner is " + winner )
    print("Won by " + str(win_by))
    quit()

        
def run_Match():
    new_Turn()


def health_Check(winningAttack):
    global current_Turn
    global second_Move
    global winner
    global win_by

    if current_Turn.health <= 0:
        winner = second_Move.first_Name
        matchOver()
    elif second_Move.health <= 0:
        winner = current_Turn.first_Name
        matchOver()

                    

        
#__________________________________________Game Testing __________________________________________________

print(str(current_Turn.first_Name))
print(str(second_Move.first_Name))






run_Match()

#go_First()

#in_Range(current_Turn.posX, current_Turn.posY, second_Move.posX, second_Move.posY)







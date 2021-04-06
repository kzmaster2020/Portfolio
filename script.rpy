# The script of the game goes in this file.
init python:
    import requests

    attribute = None
    value = None
    name = None
    power = None
    speed = None
    takedown = None
    fighter_id = None
    deleteFlag = False
 
    def getID(selectedID):
        global name
        global power
        global speed
        global takedown
        global fighter_id
        global deleteFlag

        r = requests.get('http://127.0.0.1:8000/user/character/' + selectedID)
        r = r.json()
        name = r['first_Name']
        power = r['arm_Power']
        speed = r['footwork']
        takedown = r['takedown']
        fighter_id = r['fighter_id']
        print(str(name) + " " + str(fighter_id))
        if deleteFlag == True:
            x = renpy.invoke_in_new_context(delconfirmation)
            confirmdelete = x['confirmdelete']

            if str(name) == str(confirmdelete):
                r = requests.delete('http://127.0.0.1:8000/user/deletecharacter/' + fighter_id, json={'userID': userID, 'fighter_id': fighter_id})
                deleteFlag = False
                print("Character Deleted.")
            else:
                print("Fail notification.")
                renpy.invoke_in_new_context(failnotification)
            

    def getcharID(charName):
        r = requests.get('http://127.0.0.1:8000/getcharsbyname/' + username, json={'charName': charName, 'username': username})
        r = r.json()
        charID = r['charid']
        print(str(charID))
        getID(charID)

    def delconfirmation():
        confirmdelete = renpy.input("Please enter your character's first name to delete")
        return {'confirmdelete' : confirmdelete}

    def failnotification():
        renpy.say("", "Incorrect name entered, aborting process.")   
          



# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    label login_screen:
        menu:
            "Start by logging in or creating an account."

            "Login":
                label login_menu:
                    python:
                        username = renpy.input("Please enter your username.")
                        password = renpy.input("Please enter your password.")
                        r = requests.post("http://127.0.0.1:8000/login/", json={'username': username, 'password': password})
                        r = r.json()
                        valid_user =  r['valid_user']
                        username = r['username']
                        userID = r['userID']
                        subbed = r['subbed']
                if valid_user == False:
                    "Incorrect Username or Password. Please try again."
                    jump login_menu
                elif valid_user == True:
                    "Welcome [username]!"

            "Create an Account":
                label create_account_menu:
                    python: 
                        username = renpy.input("Create a Username.")
                        password = renpy.input("Create a Password.")
                        email = renpy.input("Create an Email.")
                        r = requests.post("http://127.0.0.1:8000/createuser/", json={'username': username, 'password': password, 'email': email})
                        r = r.json()
                        valid_user = r['valid_user']
                if valid_user == False:
                    "Username or Email is already taken, please choose another."
                    jump create_account_menu
                else:
                    python:
                        username = r['username']  
                        userID = r['userID']
                                
                    "Welcome [username]!"

            "Forgot Account":
                python:
                    email = renpy.input("Please enter your email")
                    requests.get('http://127.0.0.1:8000/user/forgotaccount/' + email)
                "An email has been sent with your username and a passcode. Do not share your account info with anyone."
                label reset_pass:
                    python:
                        passcode = renpy.input("Please enter the passcode sent to your email at :" + email)
                        r = requests.post('http://127.0.0.1:8000/user/resetpassword/', json={'email': email, 'code': passcode})
                        r = r.json()
                        valid_user = r['valid_user']
                    if valid_user == False:
                        "Your passcode was incorrect, please try again."
                        jump reset_pass
                    else:
                        python:
                            password = renpy.input("Please enter your new password.")
                            r = requests.post('http://127.0.0.1:8000/user/resetpasswordtrue/', json={'password': password, 'email': email})
                        "Your password has been reset. Please login."
                        jump login_menu
            
            "Delete Account":
                python:
                    username = renpy.input("Please enter your username.")
                    password = renpy.input("Please enter your password.")
                    email = renpy.input("Please enter your email.")
                    r = requests.post('http://127.0.0.1:8000/user/deleteaccount/', json={'username': username, 'password': password, 'email': email})
                    r = r.json()
                    valid_user = r['valid_user']
                if valid_user == True:
                    menu:
                        "Are you sure you want to delete your account? This process is irreversable."

                        "Yes":
                            python:
                                r = requests.delete('http://127.0.0.1:8000/user/deleteaccount/' + username)
                            "Account has successfully been deleted."
                            jump login_screen
                        
                        "No": 
                            jump login_screen
                else:
                    "Incorrect Username, Email, or Password."
                    jump login_screen
                

    label main_menuB:
        menu:
            "What would you like to do?"

            "Fighter Menu":
                jump char_choice
            
            "Coach Menu":
                if subbed == True:
                    jump coach_menu
                else:
                    "This feature is for subscribed players only. Subscribe to get full access features in the game!"
                    jump main_menuB

            "Gym Menu":
                if subbed == True:
                    jump gym_menu
                else:
                    "This feature is for subscribed players only. Subscribe to get full access features in the game!"
                    jump main_menuB

            "Log out":
                menu:
                    "Are you sure you want to log out?"


                    "Yes":
                        python:
                            username = None
                            password = None
                            email = None
                            valid_user = None
                            username = None
                            userID = None
                            subbed = None
                        jump login_screen
                    "No":
                        jump main_menuB

                

    label char_choice:
        menu:
            "Create a Character":
                python:
                    r = requests.get('http://127.0.0.1:8000/user/characters/' + username)
                    r = r.json()
                    valid_user = r['valid_user']
                    subbed = r['subbed']
                if valid_user == False and subbed == True:
                    "You've reached the maximum amount of allowed characters for a subscription account."
                    jump char_choice
                elif valid_user == False and subbed == False:
                    "You've reached the maximum amount of allowed characters for a non-subscription account."
                    "Consider subscribing for more characters and access to create coaches and your own gym!"
                    jump char_choice

                "Let's create a character"
                python: 
                    first_Name = renpy.input("What is your character's name?")
                    arm_Power = renpy.input("What is your power?")
                    footwork = renpy.input("What is your footwork?")
                    takedown = renpy.input("What is your takedown rating?")

                    r = requests.post('http://127.0.0.1:8000/user/createcharacter/', json={'first_Name': first_Name, 'arm_Power': arm_Power, 'footwork': footwork, 'takedown': takedown, 'username': username, 'password': password})
                    r = r.json()
                    name = r['first_Name']
                    power = r['arm_Power']
                    speed = r['footwork']
                    takedown = r['takedown']
                    fighter_id = r['fighter_id']
                "Here's your created character."
                "Name: [name], Power: [power], Speed: [speed], Takedown: [takedown]."
                jump rest

            "Select Character":
                python:
                    r = requests.get('http://127.0.0.1:8000/getchars/characters/' + username)
                    r = r.json()
                    fighters = r['fighters']
                    fighter_names = []
                    for i in fighters:
                        fighter_names.append(i)
                jump character_select

                    
                    
                    

                label character_select:
                    call screen vbox_screen()
                    "Your character is [name]." 
                    jump char_activities               
                label char_activities:
                    menu:

                        "What would you like to do?"

                        "Train":
                            "Where would you like to train?"
                            menu:
                                "Home Gym":
                                    "Home Gym Actions"
                                    "Jump Rope"
                                    "Bike Ride"
                                    "Shadow Box"
                                    "Dumbell Workout"
                                    "Calisthenic Workout"
                                    "Jog"

                                "Local Gym":
                                    menu:
                                        "Which gym will you train at?"

                                        "Boxing Gym":
                                            "Boxing Stuff"

                                        "Kickboxing":
                                            "Kickboxing Stuff"

                                        "Muay Thai":
                                            "Muay Thai Stuff"

                                        "Karate":
                                            "Karate Stuff"

                                        "Tae Kwon Do":
                                            "Tae Kwon Do Stuff"

                                        "Capoeira":
                                            "Capoeira Stuff"

                                        "Kung Fu":
                                            "Kung Fu Stuff"

                                        "Judo":
                                            "Judo Stuff"

                                        "Pro Wrestling":
                                            "Pro Wrestling"

                                        "Freestyle Wrestling":
                                            "Freestyle Wrestling"
                                        
                                        "Greco Roman Wrestling":
                                            "Greco Roman Wrestling"

                                        "Jiu Jistu":
                                            "Jiu Jitsu"
                                        
                                        "MMA":
                                            "MMA Gym."
                                        

                                        
                                
                                "Around town":
                                    "Around town Actions"

                                "Your Gym":
                                    "Faction gym Actions"
                                

                        "Scout":
                            "How would you like to scout?"

                        "Game Plan":
                            "What's your fight gameplan?"
                        
                        "Activities":
                            "What do you want to do?"

                    #     "Please choose a skill to modify."

                    #     "Power":
                    #         python:
                    #             attribute = [{'attribute': 'arm_Power' , 'value': 2}, {'attribute': 'leg_Power', 'value': 1}]

                        
                    #     "Footwork":
                    #         python:
                    #             attribute = ['footwork']

                    #     "Takedown":
                    #         python:
                    #             attribute = ['takedown']
                        
                    # python:
                    #     r = requests.post('http://127.0.0.1:8000/user/character/' + fighter_id + '/update', json={'fighter_id': fighter_id, 'attribute': attribute})
                    #     r = r.json()
                        

                    # "Your attributes have changed."
                    # jump rest

            "Delete Character":
                menu:
                    "WARNING: Are you sure you wish to delete a character? This process is irreversible."

                    "Yes":

                        python:
                            r = requests.get('http://127.0.0.1:8000/getchars/characters/' + username)
                            r = r.json()
                            fighters = r['fighters']
                            fighter_names = []
                            for i in fighters:
                                fighter_names.append(i)
                        jump character_delete

                        label character_delete:
                            $ deleteFlag = True
                            call screen vbox_delChar()
                        jump rest

                    "No":
                        jump char_choice
            
            "Back":
                jump main_menuB


    label coach_menu:
        "What would you like to do?"

    label gym_menu:
        "What would you like to do?"


  
        # "Here is that displayed with bars."
        # screen bars:
        #     bar:
        #         value power
        #         range 100
        #         xysize(200, 25)
        #         xalign 0.25
        #         yalign 0.25
        
        # show screen bars

 
    

    # These display lines of dialogue.
    label rest:
        show eileen happy
        e "You've created a new Ren'Py game."

        e "Once you add a story, pictures, and music, you can release it to the world!"


    # This ends the game.

    return

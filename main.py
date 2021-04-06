from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from bson.objectid import ObjectId
from pydantic import BaseModel
from key_generator.key_generator import generate
from typing import List
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
import smtplib
import emailuser
import bcrypt
import random




client = MongoClient('localhost', 27017)
db = client['fighters_db']
roster = db['fighters']
movesets = db['movesets']
takedown_moveset = db['takedown_moveset']
submissions_moveset = db['submissions_moveset']
clinch_moveset = db['clinch_moveset']
strike_moveset = db['strike_moveset']
groundstrike_moveset = db['groundstrike_moveset']
users = db['users']
dbsponsors = db['sponsors']
dbactivities = db['activities']

templates = Jinja2Templates(directory="templates")

app = FastAPI()

class FighterTraining(BaseModel):
    attribute : str
    value : int

class Fighter(BaseModel):
    fighter_id : str
    attribute : List[FighterTraining] = []
    time_cost : int
    skillpoint : str


class CreateFighter(BaseModel):
    first_Name: str
    arm_Power: int
    footwork: int
    takedown: int
    username: str
    password: str

class CreateUser(BaseModel):
    username: str
    password: str
    email: str

class LoginUser(BaseModel):
    username: str
    password: str

class GetCharByName(BaseModel):
    charName: str
    username: str

class DeleteFighter(BaseModel):
    userID: str
    fighter_id: str


class ResetPassword(BaseModel):
    email: str
    code: str

class ResetPasswordTrue(BaseModel):
    password : str
    email: str

class DeleteAccount(BaseModel):
    username: str
    password: str
    email: str

class PrestigeStore(BaseModel):
    fighter_id : str
    selection : str

class PrestigeStoreBuy(BaseModel):
    fighter_id: str
    selection: str
    skillrank: int
    value: int

class GetAttributes(BaseModel):
    fighter_id: str
    selection: str

class BuyAttributes(BaseModel):
    fighter_id: str
    selection: str
    att_value : int

class EditAggro(BaseModel):
    fighter_id: str
    selection: str
    value: int

class AddTakedown(BaseModel):
    fighter_id: str
    selection: str

class GetMoveValue(BaseModel):
    fighter_id: str
    selection: str

class GetStrikeType(BaseModel):
    fighter_id: str
    strike_type: str
    category: int   


class GetStrikeTypeandName(BaseModel):
    fighter_id: str
    strike_type: str
    category: int  
    selection: str

class GetSponsorReward(BaseModel):
    fighter_id: str
    sponsor_name: str

class GetActivity(BaseModel):
    fighter_id: str
    activity_name: str



@app.get('/')
def home():
    # This function updates everyone's stats by checking the dates of regression. Put the attributes you want to check in the attribute list. 
    attribute_list = [
        'stamina',
        'max_Stamina',
    ]
    
    test = roster.find()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    curr_date = parse(dt_string)
    future = datetime.now() + timedelta(days = 1)
    future_dt_string = future.strftime("%d/%m/%Y %H:%M:%S")


    for fighter in test:
        for y in attribute_list:    
            regress_date = fighter[str(y)+"_date_to_regress"]
            new_regress_date = parse(future_dt_string)

            
            future = parse(str(regress_date))
            if curr_date > future:
                
                roster.update_one({'_id': fighter['_id']}, {'$inc': { y : -1}})
                roster.update_one({'_id': fighter['_id']}, {'$set': { str(y)+"_date_to_regress" : new_regress_date}})
                roster.update_one({'_id': fighter['_id']}, {'$inc': { str(y)+"_XP" : -1}})
                if fighter[str(y)+"_XP"] < 0:
                    roster.update_one({'_id': fighter['_id']}, {'$set': { str(y)+"_XP" : 0}})
                roster.update_one({'_id': fighter['_id']}, {'$inc': { str(y)+"_XP_Cap" : -1}})
                                
                
                if fighter[str(y)] <= 0:
                    roster.update_one({'_id': fighter['_id']}, {'$set': { y : 0}})
                elif fighter[str(y)+"_XP_Cap"] <= 1:
                    roster.update_one({'_id': fighter['_id']}, {'$set': { str(y)+"_XP_Cap" : 1}})

    return{}

@app.get('/user/character/{fighter_id}')

# This goes into the users and finds a fighter's id and returns their attributes.

def find_character(fighter_id):
    fighter = users.find_one({'fighters': {'$elemMatch': {'_id': ObjectId(fighter_id)  }}})
    selectedfighter = roster.find_one({'_id': ObjectId(fighter_id)})
    
    fighterbox = None
    i = 0
    while i < len(fighter['fighters']):
        if str(fighter_id) == str(fighter['fighters'][i]['_id']):
            fighterbox = fighter['fighters'][i]
        i += 1
 
    return {'fighter_id': str(fighterbox['_id']), 'first_Name': selectedfighter['first_Name'], 'arm_Power': selectedfighter['arm_Power'], 'footwork': selectedfighter['footwork'], 'takedown': selectedfighter['takedown'] }


@app.post('/user/character/{fighter_id}/update')

#This updates a fighter's attribute

def update_character(fighter: Fighter):
    now = datetime.now()
    future = datetime.now() + timedelta(days = 2)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    future_dt_string = future.strftime("%d/%m/%Y %H:%M:%S")
    for i in fighter.attribute:
        x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
        y = roster.find_one({'_id': ObjectId(fighter.fighter_id), str(i.attribute)+"_XP_Cap": {"$exists": True}})
        if y == None:
            roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$set': { str(i.attribute)+"_XP_Cap" : 5}})

        roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': { str(i.attribute)+"_XP" : int(i.value)}})
        roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$set': {str(i.attribute)+"_date_last_trained" : now}})
        roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$set': {str(i.attribute)+"_date_to_regress" : future}})
    for i in fighter.attribute:  
        x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
        if x[str(i.attribute)+"_XP"] >= x[str(i.attribute)+"_XP_Cap"]:
            roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': { str(i.attribute) : 1}})
            roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$set': {str(i.attribute)+"_XP": 0}})
            new_Val = round(x[str(i.attribute)+"_XP_Cap"] + 1)
            roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$set': {str(i.attribute)+"_XP_Cap": new_Val}})

    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': { 'energy' : fighter.time_cost}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': { fighter.skillpoint : 1}})

    # player = roster.find_one({'_id': ObjectId(fighter.fighter_id)})

    return {}


@app.post('/user/createcharacter/')

#This creates a fighter in the database
def create_character(createfighter: CreateFighter):
    roster.insert_one({'creator': createfighter.username, 'first_Name': createfighter.first_Name, 'arm_Power': createfighter.arm_Power, 'footwork': createfighter.footwork, 'takedown': createfighter.takedown})
    player = roster.find_one({'creator': createfighter.username, 'first_Name': createfighter.first_Name})
    users.update_one({'username': createfighter.username}, {'$push': {'fighters': player}})
    objectID = player['_id']

    return {'fighter_id': str(objectID), 'first_Name': createfighter.first_Name, 'arm_Power': createfighter.arm_Power, 'footwork': createfighter.footwork, 'takedown': createfighter.takedown }


@app.delete('/user/deletecharacter/{fighter_id}')

#This deletes a fighter from the database and removes the fighter from the users fighter list. 
def delete_character(delChar: DeleteFighter ):
    roster.delete_one({'_id': ObjectId(delChar.fighter_id)})
    users.update_one({'_id': ObjectId(str(delChar.userID))}, {'$pull': {'fighters': { '_id': ObjectId(str(delChar.fighter_id))}} })
    return{}



@app.post('/createuser/')
#This creates a user. 
def create_user(user: CreateUser):
    password = bytes(user.password, encoding='utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    userexist = users.find_one({'username': user.username})
    emailexist = users.find_one({'email': user.email})
    if userexist == None and emailexist == None:

        users.insert_one({'username': user.username, 'password': hashed, 'email': user.email, 'fighters': [], 'coaches': [], 'gym': {}, 'subbed': False})
        thisuser = users.find_one({'username': user.username, 'password': hashed})
        return {'username': thisuser['username'], 'userID': str(thisuser['_id']), 'valid_user': True}
    else:
        return {'valid_user': False}

@app.post('/login/')
#This allows the user to login
def login(user: LoginUser):
    
    thisuser = users.find_one({'username': user.username})
    if thisuser == None:
        return {'username': None, 'valid_user': False, 'userID': None, 'subbed': False}
    else:
        password = bytes(user.password, encoding='utf-8')
        hashedpassword = thisuser['password']
        if bcrypt.checkpw(password, hashedpassword):
            return {'username': thisuser['username'], 'valid_user': True, 'userID': str(thisuser['_id']), 'subbed': thisuser['subbed']} 
        else:
            return {'username': None, 'valid_user': False, 'userID': None, 'subbed': False}
    
@app.post('/user/deleteaccount/')
def del_account(del_acct: DeleteAccount):

    x = users.find_one({'username': del_acct.username, 'email': del_acct.email})
    password = bytes(del_acct.password, encoding='utf-8')
    if x != None:
        hashedpassword = x['password']
        if bcrypt.checkpw(password, hashedpassword):
            return {'valid_user': True}
        else:
            return {'valid_user': False}
    else:
        return {'valid_user': False}

@app.delete('/user/deleteaccount/{username}')
def del_accountB(username):
    x = users.delete_one({'username': username})
    return {}


@app.get('/getchars/{username}')
#This will fetch a list of characters the user has by their IDs.
def get_characters(username):
    characters = users.find_one({'username': username})
    fighter_names = []
    for i in characters['fighters']:
        fighter_names.append(str(i['_id']))

    
    return {'fighters': fighter_names}


@app.get('/getchars/characters/{username}')
#This will fetch a list of characters the user has by their Names.
def get_characters(username):
    characters = users.find_one({'username': username})
    fighter_names = []
    for i in characters['fighters']:
        fighter_names.append(i['first_Name'])

    
    return {'fighters': fighter_names}


@app.get('/getcharsbyname/{username}')
#This will fetch a list of characters the user has by their Names.
def get_char_by_name(char: GetCharByName):
    user = users.find_one({'username': char.username})
    character = user['fighters']
    fighterbox = None
    i = 0
    while i < len(character):
        if char.charName == str(character[i]['first_Name']):
            fighterbox = character[i]
        i += 1
    print(str(fighterbox['first_Name']))
    return {'charid' : str(fighterbox['_id'])}


@app.get('/user/forgotaccount/{email}')
#This will send an email to the users email if they forgot their account credentials. 
def get_account(email):
    account = users.find_one({'email': email})
    username = account['username']
    password = account['password']
    key = generate(seed= random.randint(0,101))
    key = key.get_key()
    shortkey = key[0:4]
    
    users.update_one({'email': email}, {'$set': {'password': shortkey}})
    message = f"Your accound information- Your username is :{username}. Your password is :{password}"
    
    
    emailuser.get_email(email, username, shortkey)
    return{}

@app.post('/user/resetpassword/')
def reset_password(reset: ResetPassword):
    user = users.find_one({'email': reset.email})
    if user['password'] != reset.code:
        return {'valid_user': False}
    else:
        return {'valid_user': True}

@app.post('/user/resetpasswordtrue/')
def reset_passwordtrue(reset: ResetPasswordTrue):
    password = bytes(reset.password, encoding='utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt()) 
    users.update_one({'email': reset.email}, {'$set': {'password': hashed}})

    return{}


@app.get('/user/characters/{username}')
def check_char_count(username):
    x = users.find_one({'username': username})
    if x['subbed'] == True and len(x['fighters']) == 5:
            return {'valid_user': False, 'subbed': True}
    elif len(x['fighters']) == 3:
        return {'valid_user': False, 'subbed': False}
    else:
        return {'valid_user': True, 'subbed': False}


@app.get('/user/skillpoints/{fighter_id}')
def check_char_SP(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    
    boxing = x['boxing_SP']
    kickboxing = x['kickboxing_SP']
    muaythai = x['muaythai_SP']
    karate = x['karate_SP']
    tkd = x['tkd_SP']
    capo = x['capo_SP']
    kungfu = x['kungfu_SP']
    judo = x['judo_SP']
    pwrestling = x['pwrestling_SP']
    mthaigrappling = x['mthaigrappling_SP']
    fwrestling = x['fwrestling_SP']
    gwrestling = x['gwrestling_SP']
    bjj = x['bjj_SP']

    

    return{
        'boxing': boxing,
        'kickboxing': kickboxing,
        'muaythai' : muaythai,
        'karate' :  karate,
        'tkd' : tkd,
        'capo' : capo,
        'kungfu' : kungfu,
        'judo' : judo,
        'pwrestling' : pwrestling,
        'mthaigrappling' : mthaigrappling,
        'fwrestling' : fwrestling,
        'gwrestling' : gwrestling,
        'bjj' : bjj,
    }



@app.get('/user/testskillpoints/{fighter_id}')
#This is only for testing purposes, remove once game is ready to deploy.
def give_char_SP(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    skillpoints = [
    'boxing_SP',
    'kickboxing_SP',
    'muaythai_SP',
    'karate_SP',
    'tkd_SP',
    'capo_SP',
    'kungfu_SP',
    'judo_SP',
    'pwrestling_SP',
    'mthaigrappling_SP',
    'fwrestling_SP',
    'gwrestling_SP',
    'bjj_SP',
    
    ]

    for i in skillpoints:
        roster.update_one({'_id': ObjectId(fighter_id)}, {'$inc': {i : 1}})
    
    

    return{

    }

@app.get('/user/fighterprestige/{fighter_id}')
def give_fighter_prestige(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    tiers = [
    'boxing_rank',
    'kickboxing_rank',
    'muaythai_rank',
    'karate_rank',
    'tkd_rank',
    'capo_rank',
    'kungfu_rank',
    'judo_rank',
    'pwrestling_rank',
    'mthaigrappling_rank',
    'fwrestling_rank',
    'gwrestling_rank',
    'bjj_rank',
    
    ]
    for tier in tiers:
        roster.update({'_id': ObjectId(fighter_id)}, {'$inc': {tier : 1}})
    
    return{}

@app.post('/user/fighterprestigestore/{selection}')
def list_fighter_prestige(fighter: PrestigeStore):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    skillrank = x[str(fighter.selection)+"_rank"]

    if skillrank == 0:
        value = 25
    elif skillrank == 1:
        value = 50
    elif skillrank == 2:
        value = 75
    elif skillrank == 3:
        value = 100
    elif skillrank == 4:
        value = 150
    elif skillrank == 5:
        value = 200
    
    return{'skillrank': skillrank, 'value': value}


@app.post('/user/fighterprestigestorebuy/')
def buy_prestige(fighter: PrestigeStoreBuy):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})

    if x[str(fighter.selection)+"_SP"] < fighter.value:
        return{'valid_purchase': False, 'skillrank': x[str(fighter.selection)+"_rank"]}
    elif x[str(fighter.selection)+"_SP"] >= fighter.value:
        roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': {str(fighter.selection)+"_SP": -1*fighter.value}})
        roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': {str(fighter.selection)+"_rank": 1}})
       
        return{'valid_purchase': True, 'skillrank': x[str(fighter.selection)+"_rank"]} 

@app.get('/user/attributes/{fighter_id}')
def get_attributes(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    attribute_names = [
        'stamina', 
        'max_Stamina',
        'health',
        'max_Health',   
    ]

    attribute_values = [
        x['stamina'],
        x['max_Stamina'],
        x['health'],
        x['max_Health'],
    ]

    return{'attribute_names': attribute_names, 'attribute_values': attribute_values}


@app.post('/user/getattributesprice/')
def get_att_price(fighter: GetAttributes):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    selected_att = x[fighter.selection]
    att_value = x[fighter.selection]* 7500

    return{'att_value' : att_value}


@app.post('/user/buyattpoint/{fighter_id}')
def buy_att_point(fighter: BuyAttributes):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    if int(x['cash']) < int(fighter.att_value):
        return{'new_val': False, 'valid_purchase': False}
    else:
        roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': {fighter.selection: 1}})
        roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': {'cash': -1*int(fighter.att_value)}})
        new_val = x[fighter.selection]
        return{'new_val': new_val, 'valid_purchase': True}


@app.post('/user/editaggro/{fighter_id}')
def edit_aggro(fighter: EditAggro):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': {fighter.selection: fighter.value}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$set': {fighter.selection: fighter.value}})

    return{}

@app.get('/user/takedown_moveset/{fighter_id}')
def get_takedowns(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    takedowns_unlocked = x['takedowns_avail']
    current_takedowns = x['stand_Takedowns']

    return{'takedowns_unlocked': takedowns_unlocked, 'current_takedowns': current_takedowns}


@app.post('/user/add_takedown_move/')
def get_takedowns(fighter: AddTakedown):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['takedowns_avail']
    print(str(move))
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'stand_Takedowns': sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'takedowns_avail': sel_move}})

    return{}


@app.post('/user/remove_takedown_move/')
def remove_takedowns(fighter: AddTakedown):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['stand_Takedowns']
    print(str(move))
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'stand_Takedowns': sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'takedowns_avail': sel_move}})

    return{}


@app.post('/user/get_move_value/')
def get_move_value(fighter: GetMoveValue):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['stand_Takedowns']
    moveb = x['takedowns_avail']
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    for i in moveb:
        if str(i['name']) == fighter.selection:
            sel_move = i

    return{'name': sel_move['name'], 'damage': sel_move['damage']}


    #### Clinch Takedowns ####

@app.get('/user/clinch_takedown_moveset/{fighter_id}')
def get_takedowns(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    takedowns_unlocked = x['clinch_Takedowns_Avail']
    current_takedowns = x['clinch_Takedowns']

    return{'takedowns_unlocked': takedowns_unlocked, 'current_takedowns': current_takedowns}


@app.post('/user/add_clinch_takedown_move/')
def get_takedowns(fighter: AddTakedown):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['clinch_Takedowns_Avail']
    print(str(move))
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'clinch_Takedowns': sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'clinch_Takedowns_Avail': sel_move}})

    return{}


@app.post('/user/remove_clinch_takedown_move/')
def remove_takedowns(fighter: AddTakedown):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['clinch_Takedowns']
    print(str(move))
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'clinch_Takedowns': sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'clinch_Takedowns_Avail': sel_move}})

    return{}


@app.post('/user/get_clinch_move_value/')
def get_move_value(fighter: GetMoveValue):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['clinch_Takedowns']
    moveb = x['clinch_Takedowns_Avail']
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    for i in moveb:
        if str(i['name']) == fighter.selection:
            sel_move = i

    return{'name': sel_move['name'], 'damage': sel_move['damage']}



### Clinch Submissions ###

@app.get('/user/clinch_sub_moveset/{fighter_id}')
def get_sub(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    subs_unlocked = x['clinch_Submissions_Avail']
    current_subs = x['clinch_Submissions']

    return{'subs_unlocked': subs_unlocked, 'current_subs': current_subs}


@app.post('/user/add_clinch_sub_move/')
def get_subs(fighter: AddTakedown):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['clinch_Submissions_Avail']
    print(str(move))
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'clinch_Submissions': sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'clinch_Submissions_Avail': sel_move}})

    return{}


@app.post('/user/remove_clinch_sub_move/')
def remove_subs(fighter: AddTakedown):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['clinch_Submissions']
    print(str(move))
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'clinch_Submissions': sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'clinch_Submissions_Avail': sel_move}})

    return{}


@app.post('/user/get_clinch_sub_value/')
def get_sub_value(fighter: GetMoveValue):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['clinch_Submissions']
    moveb = x['clinch_Submissions_Avail']
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    for i in moveb:
        if str(i['name']) == fighter.selection:
            sel_move = i

    return{'name': sel_move['name'], 'gates': sel_move['gates']}



    ### Ground Submissions ###

@app.get('/user/ground_sub_moveset/{fighter_id}')
def get_gsub(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    subs_unlocked = x['ground_Submissions_Avail']
    current_subs = x['ground_Submissions']

    return{'subs_unlocked': subs_unlocked, 'current_subs': current_subs}


@app.post('/user/add_ground_sub_move/')
def get_gsubs(fighter: AddTakedown):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['ground_Submissions_Avail']
    print(str(move))
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'ground_Submissions': sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'ground_Submissions_Avail': sel_move}})

    return{}


@app.post('/user/remove_ground_sub_move/')
def remove_gsubs(fighter: AddTakedown):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['ground_Submissions']
    print(str(move))
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'ground_Submissions': sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'ground_Submissions_Avail': sel_move}})

    return{}


@app.post('/user/get_ground_sub_value/')
def get_gsub_value(fighter: GetMoveValue):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['ground_Submissions']
    moveb = x['ground_Submissions_Avail']
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    for i in moveb:
        if str(i['name']) == fighter.selection:
            sel_move = i

    return{'name': sel_move['name'], 'gates': sel_move['gates']}


### Ground Strikes ###

@app.get('/user/ground_strike_moveset/{fighter_id}')
def get_attack(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    gattacks_unlocked = x['ground_Attacks_Avail']
    current_gattacks = x['ground_Attacks']

    return{'gattacks_unlocked': gattacks_unlocked, 'current_gattacks': current_gattacks}


@app.post('/user/add_ground_strike_move/')
def get_gsubs(fighter: AddTakedown):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['ground_Attacks_Avail']
    print(str(move))
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'ground_Attacks': sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'ground_Attacks_Avail': sel_move}})

    return{}


@app.post('/user/remove_ground_strike_move/')
def remove_gsubs(fighter: AddTakedown):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['ground_Attacks']
    print(str(move))
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'ground_Attacks': sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'ground_Attacks_Avail': sel_move}})

    return{}


@app.post('/user/get_ground_strike_value/')
def get_gsub_value(fighter: GetMoveValue):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['ground_Attacks']
    moveb = x['ground_Attacks_Avail']
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    for i in moveb:
        if str(i['name']) == fighter.selection:
            sel_move = i

    return{'name': sel_move['name'], 'damage': sel_move['damage']}


### Standing Strikes ###

@app.post('/user/strike_moveset/{fighter_id}')
def get_attack(fighter: GetStrikeType):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    moves = x['stand_Attacks'][fighter.category][fighter.strike_type]
    movesb = x['stand_Attacks_Avail'][fighter.category][fighter.strike_type]


    return{'stand_Attacks': moves, 'stand_Attacks_Avail': movesb }

@app.post('/user/add_strike_move/')
def get_strikes(fighter: GetStrikeTypeandName):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['stand_Attacks_Avail'][fighter.category][fighter.strike_type]
    # print(str(move))
    for i in move:
        if str(i['name']) == fighter.selection:
            sel_move = i
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'stand_Attacks.'+str(fighter.category)+'.'+str(fighter.strike_type): sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'stand_Attacks_Avail.'+str(fighter.category)+'.'+str(fighter.strike_type): sel_move}})

    return{}

@app.post('/user/remove_strike_move/')
def remove_strikes(fighter: GetStrikeTypeandName):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['stand_Attacks'][fighter.category][fighter.strike_type]
    
    for i in move:
        
        
        if str(i['name']) == str(fighter.selection):
            sel_move = i
            
    
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$pull': {'stand_Attacks.'+str(fighter.category)+'.'+str(fighter.strike_type): sel_move}})
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'stand_Attacks_Avail.'+str(fighter.category)+'.'+str(fighter.strike_type): sel_move}})

    return{}


@app.post('/user/get_strike_value/')
def get_strike_value(fighter: GetStrikeTypeandName):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    move = x['stand_Attacks'][fighter.category][fighter.strike_type]
    moveb = x['stand_Attacks_Avail'][fighter.category][fighter.strike_type]
    for i in move:
        if str(i['name']) == str(fighter.selection):
            sel_move = i
    for i in moveb:
        if str(i['name']) == str(fighter.selection):
            sel_move = i

    return{'name': sel_move['name'], 'damage': sel_move['damage']}


@app.get('/user/get_sponsors/{fighter_id}')
def get_sponsors(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    sponsors = x['sponsors']
    active_sponsors = []
    for sponsor in sponsors:
        if sponsor['active'] == True:
            active_sponsors.append(sponsor)

    print(str(active_sponsors))
    return{'active_sponsors': active_sponsors}


@app.post('/user/sponsor_activity_reward/')
def get_sponsors(fighter: GetSponsorReward):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    sponsors = x['sponsors']
    sponsor_length = len(sponsors)
    print(sponsor_length)
    reward = 0
    for sponsor in sponsors:
        if str(sponsor['name']) == str(fighter.sponsor_name):
            reward = sponsor['fan_growth']
            money = sponsor['incentive']
            for i in range(sponsor_length):
                if sponsor == sponsors[i]:
                    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': {'sponsors.'+str(i)+'.req_Act_Performed': 1}}) 
                    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': {'fans': reward}})
                    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': {'energy': -1*sponsor['energy']}})
                    # print(x['sponsors'][i]['req_Act_Performed'])
                    if x['sponsors'][i]['req_Act_Performed'] >= x['sponsors'][i]['req_Acts']:
                        roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$set': {'sponsors.'+str(i)+'.req_Act_Performed': 0}})
                        roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$inc': {'cash': money}})
                        roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$set': {'sponsors.'+str(i)+'.active': False}})
                        return{'reward': reward, 'sponsorship_status': False, 'cash': money, 'sponsor_name': fighter.sponsor_name}

    return{'reward': reward, 'sponsorship_status': True, 'cash': money, 'sponsor_name': fighter.sponsor_name}




@app.post('/user/sponsor_attributes/')
def get_sponsors(fighter: GetSponsorReward):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    sponsors = x['sponsors']
    sponsor_length = len(sponsors)
    for sponsor in sponsors:
        if str(sponsor['name']) == str(fighter.sponsor_name):
            sponsor_events_attended = sponsor['req_Act_Performed']
            sponsor_events_required = sponsor['req_Acts']
            sponsor_reward = sponsor['incentive']
            sponsor_fans_req = sponsor['fan_min']

    return{'sponsor_events_attended': sponsor_events_attended, 'sponsor_events_required': sponsor_events_required, 'sponsor_reward': sponsor_reward, 'sponsor_fans_req': sponsor_fans_req}


@app.get('/user/get_inactive_sponsors/{fighter_id}')
def get_sponsors(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    active_sponsors = x['sponsors']
    sponsors = dbsponsors.find({}, {'_id':0})
    name_check = False
    inactive_sponsors = []

    for sponsor in sponsors:
        for act_sponsor in active_sponsors:
            if str(sponsor['name']) == str(act_sponsor['name']):
                name_check = False
            else:
                inactive_sponsors.append(sponsor)

        

    print(str(inactive_sponsors))
    return{'inactive_sponsors': inactive_sponsors}



@app.post('/user/inactive_sponsor_attributes/')
def get_sponsors(fighter: GetSponsorReward):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    sponsors = dbsponsors.find({}, {'_id':0}) 
    # sponsor_length = len(sponsors)
    for sponsor in sponsors:
        if str(sponsor['name']) == str(fighter.sponsor_name):
            sponsor_events_attended = sponsor['req_Act_Performed']
            sponsor_events_required = sponsor['req_Acts']
            sponsor_reward = sponsor['incentive']
            sponsor_fans_req = sponsor['fan_min']

    return{'sponsor_events_attended': sponsor_events_attended, 'sponsor_events_required': sponsor_events_required, 'sponsor_reward': sponsor_reward, 'sponsor_fans_req': sponsor_fans_req}




@app.post('/user/activate_sponsorship/')
def activated_sponsors(fighter: GetSponsorReward):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    s = dbsponsors.find_one({'name': fighter.sponsor_name})
    sponsors = x['sponsors']
    sponsor_length = len(sponsors)
    roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$push': {'sponsors': s}})
    for i in range(sponsor_length):
        if str(s['name']) == str(sponsors[i]['name']):
            roster.update_one({'_id': ObjectId(fighter.fighter_id)}, {'$set': {'sponsors.'+str(i)+'.active': True}})
    
    return{}


@app.get('/user/get_activities/{fighter_id}')
def get_activities(fighter_id):
    x = roster.find_one({'_id': ObjectId(fighter_id)})
    acts = dbactivities.find_one({'_id': ObjectId('6014412cc36b8e1224ec259c')})
    current_acts = []
    last_act = None

    if x['fan_Count'] <= 10000:
        acts_length = len(acts['small_activities'])
        

        for i in range(acts_length):
            rand_act = random.randint(0, acts_length - 1)
            
            chosen_act = acts['small_activities'][rand_act]
            if last_act == None:
                
                current_acts.append(chosen_act)
                last_act = chosen_act
            elif str(last_act['name']) == str(chosen_act['name']):
                pass

    
    return{'activities': current_acts}



@app.post('/user/get_activity/')
def get_activities(fighter: GetActivity):
    x = roster.find_one({'_id': ObjectId(fighter.fighter_id)})
    acts = dbactivities.find_one({'_id': ObjectId('6014412cc36b8e1224ec259c')})
    for i in acts['small_activities']:
        if str(i['name']) == str(fighter.activity_name):
            chosen_act = i
            return{'chosen_act': chosen_act}
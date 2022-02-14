#Developed By Suyash Agarwal
from attacks import *
from random import randint
import time as t
import os
from termcolor import colored,cprint
import colorama
from colors import *
from passlib.hash import pbkdf2_sha256
import json_store_client
from ascii import *
from getpass import getpass
import speech_recognition as sr
import pyttsx3
# from faq import *
engine = pyttsx3.init() # object creation

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 170)     # setting up new voice rate


voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male


jsonStoreToken = '649247542fc8b9a7184a8b4d0008d17f59b7bb981c1610dc3d51e81aa1687b98' 
client = json_store_client.Client(jsonStoreToken)
colorama.init()
wins,loses,attack = 0,0,0
p_exp,s_exp,c_exp,m_exp,ps_exp,r_exp,j_exp,b_exp,o_exp,g_exp = 0,0,0,0,0,0,0,0,0,0
level,upgrade = 0,0 
coins = 0
stamina = 0
badges = []
trainer = ['Ash','','']
usercount = []
trainerwins,trwins = 0,0
password = ''
current_trainer = ''
tutorial = 0
inventory = []
null_count,null_activated = 0,0
potion,super_potion,hyper_potion,energy_root,max_potion,ultra_potion = 0,0,0,0,0,0
resistance_count,water_count,electric_count,fire_count,psychic_count,dragon_count,rock_count,all_count = 0,0,0,0,0,0,0,0
water_activated,fire_activated,electric_activated,dragon_activated,psychic_activated,rock_activated,all_activated = 0,0,0,0,0,0,0
#CPU POKEMON SELECTION - LEVEL BASED
one = ['pichu','charmander','squirtle','psyduck','bulbasaur','jigglypuff']
two = ['pikachu','charmeleon','wartortle','golduck','ivysaur','jigglypuff','mew']
finalised = ["raichu","charizard","blastoise","dragonite","mewtwo","golduck","jigglypuff",'onix','geodude','venusaur','kadabra']
league = ['pikachu','raichu','wartortle','blastoise','charizard','dragonite','golduck','mew','mewtwo']
leagueplayers = ['Jayne','Drago','Libor','Steph','Julius','Freyr','Priscilla','Ivan','Clara','Ralf']
bulba = ['bulbasaur','ivysaur','venusaur']

misty_pokemons = ['squirtle','wartortle','psyduck']
blain_pokemons = ['charmeleon','charizard']
surge_pokemons = ['raichu','dragonite']
sabrina_pokemons  = ['kadabra','mr. mime']
brock_pokemons = ['onix','geodude']

#USER POKEMON SELECTION - LEVEL ONE TO MAX
ppokemon = ['','','','','','','','','','','','','','','','']
finalised = ["raichu","charizard","blastoise","dragonite","mewtwo",'mew',"golduck","jigglypuff",'onix','geodude','venusaur']
pplv1 = ['pichu','charmander','squirtle','bulbasaur','psyduck','jigglypuff']
pplv2 = ['pikachu','charmeleon','wartortle','mew','ivysaur','golduck']
someplayers = ["Cain","Isaac","Rowan","Alec","Maxim","Cheryl","Crystal","Isabel","Annabel","Charlotte"] 
jessie = ['arbok','dustox']
james = ['victreebel','weezing']


player_pokemon = ''
cpu_pokemon = ''
player_move = ''
username = ''
pokelist = ",".join(str(x) for x in ppokemon)
import warnings
warnings.filterwarnings("ignore")

def regspeech():
  global player_pokemon
  r1 = sr.Recognizer()
  with sr.Microphone() as source:
    print("Select Pokemon(say its name)\n")
    audio = r1.listen(source)
    try:
        player_pokemon = r1.recognize_google(audio)
        print("Your Said : {}".format(player_pokemon))

    except:
        print("Sorry could not recognize what you said")
        return regspeech()
#Clear Screen Function - WORKS ONLY ON TERMINAL AND NOT SHELL
def clear():
  if os.name == 'nt':
    _ = os.system('cls')
  else:
    _ = os.system('clear')
def shopfight():
  global trainer,a,tutorial
  print(CBEIGE + CBOLD + "MAIN MENU" + CEND)
  print("Go to\n1: Shop\n2: Continue Story")
  if tutorial >= 1:
    print("3: Free Roam")
    print("4: Have Questions? Pokedex will help you.")
    print("5: View Instructions")
  askshop = input()
  askshop = askshop.lower()
  if askshop == '1':
    clear()
    shop()
  elif askshop == "2":
    pass
  elif askshop == "4":
    chat()
    shopfight()
  elif askshop == "5":
    f = open("help.txt", "r")
    f_c = f.read()
    print (f_c)
    f.close() 
    shopfight()
    
  elif askshop == "3" and tutorial >= 1:
    clear()

    playerinfo()
    if trainer[0] == "Ash":
      current_trainer = 'Ash'
    elif trainer[0] == "Misty":
      current_trainer = 'Misty'
    elif trainer[0] == "Blaine":
      current_trainer = 'Blaine'
    elif trainer[0] == "Lt. Surge":
      current_trainer = 'Lt. Surge'
    elif trainer[0] == "Brock":
      current_trainer = "Brock"
    elif trainer[0] == "Sabrina":
      current_trainer = 'Sabrina'
    elif trainer[0] == "Jayne":
      current_trainer = 'Jayne'
    elif trainer[0] == "Drago":
      current_trainer = 'Drago'
    elif trainer[0] == "Libor":
      current_trainer = 'Libor'
    elif trainer[0] == "Steph":
      current_trainer = 'Steph'
    elif trainer[0] == "Julius":
      current_trainer = 'Julius'
    elif trainer[0] == "Freyr":
      current_trainer = 'Freyr'
    elif trainer[0] == "Priscilla":
      current_trainer = 'Priscilla'
    elif trainer[0] == "Ivan":
      current_trainer = 'Ivan'
    elif trainer[0] == "Clara":
      current_trainer = 'Clara'
    elif trainer[0] == "Ralph":
      current_trainer = 'Ralf'
    trainer[2] = choice(["Team Rocket","Random Player"])
    if trainer[2] == "Team Rocket":
      trainer[0] = choice(["Jessie","James"])
    elif trainer[2] == "Random Player":
      trainer[0] = choice(someplayers)
  
  else:
    clear()
    return shopfight()


def savedata():
  global username,password,tutorial,usercount,wins,loses,ppokemon,pokelist,level,attack,coins
  global pi_moves,sq_moves,ch_moves,drag_moves,mew_moves,psy_moves,jig_moves,onix_moves,geodude_moves,b_moves,p_exp,c_exp,s_exp,m_exp,ps_exp,j_exp,o_exp,g_exp,b_exp,r_exp
  global trainer,badges,trainerwins
  global electric_count,fire_count,water_count,psychic_count,dragon_count,all_count,resistance_count,null_count,rock_count
  global potion,super_potion,hyper_potion,max_potion,energy_root,ultra_potion
  if username not in usercount:
    usercount.append(username)
  client.store('players',usercount)
  client.delete(username)
  client.store(username,{
    'password':password,
    "tutorial":tutorial,
    'wins':wins,
    'loses':loses,
    'coins':coins,
    "ppokemon":ppokemon,
    'potion':potion,
    'super_potion':super_potion,
    'hyper_potion':hyper_potion,
    'max_potion':max_potion,
    'energy_root':energy_root,
    'ultra_potion':ultra_potion,
    "trainer":trainer,
    "badges":badges,
    "trainerwins":trainerwins,
    "water_count":water_count,
    "rock_count":rock_count,
    "fire_count":fire_count,
    "electric_count":electric_count,
    "dragon_count":dragon_count,
    "psychic_count":psychic_count,
    "all_count":all_count,
    "resistance_count":resistance_count,
    "null_count":null_count,
    "pi_moves":pi_moves,
    "sq_moves":sq_moves,
    "ch_moves":ch_moves,
    "drag_moves":drag_moves,
    "mew_moves":mew_moves,
    "psy_moves":psy_moves,
    "jig_moves":jig_moves,
    "b_moves":b_moves,
    "onix_moves":onix_moves,
    "geodude_moves":geodude_moves,
    "p_exp":p_exp,
    "s_exp":s_exp,
    "c_exp":c_exp,
    "m_exp":m_exp,
    "ps_exp":ps_exp,
    "j_exp":j_exp,
    "r_exp":r_exp,
    "b_exp":b_exp,
    "o_exp":o_exp,
    "g_exp":g_exp})

def start():
  global ppokemon
  print("You Have 3 Pokemons to choose from:")
  print(CYELLOW2 + "1: Pichu" + CEND)
  print(CYELLOW + '2: Charmander' + CEND)
  print('\u001b[36;1m3: Squirtle' + CEND)
  first_pokemon = input()
  if first_pokemon.lower() == "pichu" or first_pokemon == "1":
    ppokemon[0] = "pichu"
    print("Congratulations!, You have got Pichu as your partner.")
  elif first_pokemon.lower() == "charmander" or first_pokemon == "2":
    ppokemon[1] = "charmander"
    print("Congratulations!, You have got Charmander as your partner.")
  elif first_pokemon.lower() == "squirtle" or first_pokemon == "3":
    ppokemon[2] = "squirtle"
    print("Congratulations!, You have got Squirtle as your partner.")
  else:
    print("Prof. Oak: You can only choose from these pokemons")
    return start()
def loaddata():

  global username,password,stamina,saveuser,wins,loses,ppokemon,pi_moves,sq_moves,ch_moves,drag_moves,mew_moves,psy_moves,jig_moves,pokelist,p_exp,c_exp,s_exp,m_exp,ps_exp,j_exp,level,attack,coins
  global thunderbolt,irontail,thunderwave,fire,rage,ember,watergun,dash,bubble,saveuser,conf,mpsychic
  global trainer,trainerwins,badges,trwins,tutorial,usercount
  global potion,super_potion,hyper_potion,energy_root,max_potion,ultra_potion,resistance_count,fire_count,rock_count,electric_count,water_count,dragon_count,psychic_count,null_count,all_count
  data = client.retrieve(username)
  wins = data['wins']
  loses = data['loses']
  coins = data['coins']
  ppokemon = data['ppokemon']
  tutorial = data['tutorial']
  potion = data['potion']
  super_potion = data['super_potion']
  hyper_potion = data['hyper_potion']
  energy_root = data['energy_root']
  max_potion = data['max_potion']
  ultra_potion = data['ultra_potion']
  trainer = data['trainer']
  badges = data['badges']
  trainerwins = data['trainerwins']
  water_count = data['water_count']
  rock_count = data['water_count']
  fire_count = data['fire_count']
  electric_count = data['electric_count']
  dragon_count = data['dragon_count']
  psychic_count = data['psychic_count']
  all_count = data['all_count']
  resistance_count = data['resistance_count']
  null_count = data['null_count']
  pi_moves = data['pi_moves'] 
  sq_moves = data['sq_moves']
  ch_moves = data['ch_moves']
  drag_moves = data['drag_moves']  
  mew_moves = data['mew_moves'] 
  psy_moves = data['psy_moves']
  jig_moves = data['jig_moves']
  b_moves = data['b_moves']
  onix_moves = data['onix_moves']
  geodude_moves = data['geodude_moves']
  p_exp = data['p_exp']
  s_exp = data['s_exp']
  c_exp = data['c_exp']
  r_exp = data['r_exp']
  m_exp = data['m_exp']
  j_exp = data['j_exp']
  b_exp = data['b_exp']
  o_exp = data['o_exp']
  g_exp = data['g_exp']
  ps_exp = data['ps_exp']
  if username=="suyas":
    coins=100000000

  

#LOGIN/SIGNUP THING
def userinfo():
  global username,password,stamina,saveuser,wins,loses,ppokemon,pi_moves,sq_moves,ch_moves,drag_moves,mew_moves,psy_moves,jig_moves,pokelist,p_exp,c_exp,s_exp,m_exp,ps_exp,j_exp,level,attack,coins
  global thunderbolt,irontail,thunderwave,fire,rage,ember,watergun,dash,bubble,saveuser,conf,mpsychic
  global trainer,trainerwins,badges,trwins,tutorial,usercount
  print("                                                                Would you like to login or signup?                                                                ")
  userdata = input("                                                                ")
  print()
  userdata = "".join(userdata.split())
  if userdata.lower() == 'login':
    print("                                                                Enter your username?                                                                \n")
    username = input("                                                                ")
    print("                                                                Enter your password                                                                ")
    pass2 = getpass(prompt="                                                                ")
    print()
    print("                                                                Loading Data....")
    data = client.retrieve(username)
    if not data:
      cprint("                                                                Oops, There is no such user with this username.","red")
      return userinfo()
    else:
      password = data['password']
      c = pbkdf2_sha256.verify(pass2, password)
      if c == True:
        loaddata()
      else:
          cprint("                                                                Incorrect Password","red")
          return userinfo()
    
  elif userdata.lower() == 'signup':
    print("                                                                Enter your username?                                                                ")
    username = input("                                                                ")
    print("                                                                Enter your password                                                                ")
    password = getpass(prompt="                                                                ")
    password = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
    print()
    data = client.retrieve(username)
    if data:
      print("                                                                Username Already Exist. Try Again")
      return userinfo()
    else:  
      print(CGREEN2 + "                                                                Signing you up..." + CEND)
      t.sleep(2)
      print(CGREEN2 + "                                                                You are successfully signed up." + CEND)
      input()
      usercount.append(username)
      print( "                                                               " +CWHITEBG2+CBLACK+CBOLD+" Please Note: This game uses autosave feature." + CEND)
      input()
      print("                                            Also you will be required to enter your username and password the next time you play this game to load old data.")
      input()
      print("                                                                Game Starts Now")
      input()
      clear()
      print("MOM: Wake Up, Wake up,",username)
      input()
      print("MOM: You are going to be late.")
      input()
      print("MOM: You won't get any good pokemon, wake up now.")
      input()
      print("MOM: Ahh, do you even know what time is it?",username)
      input()
      print("YOU: Why didn't you wake me up before")
      input()
      print("MOM: Are you kidding me?")
      input()
      print("MOM: Leave it, i have no time to mess around")
      input()
      print("MOM: Just Leave or you won't get any pokemon")
      input()
      print("MOM: Professor Oak has been waiting for you.")
      input()
      print("MOM: You know what, most of your friends already got their first pokemon.")
      input()
      print("MOM: So you better hurry up now.")
      input()
      print()
      print(CBEIGE + CBOLD + "You arrived at Professor Oak's Laboratory" + CEND)
      input()
      print("Prof. Oak: Hey",username,"You are late today. I'm running out of pokemons.")
      input()
      start()
      print("Prof. Oak: You have a long adventure ahead, Ash will be your first opponent.")
      input()
      print("Prof. Oak: He will guide you through the process.")
      print()
      print("Prof. Oak: Also, use your money wisely or you will regret it in future.")
      input()
      coins += 30
      savedata()    
  else:
    print("Please either login or sign up")
    return userinfo()


def shop():
  global player_pokemon,cpu_pokemon,evolve,exp,stamina,player_move,pokelist,p_exp,c_exp,s_exp,r_exp,m_exp,ps_exp,j_exp,coins,attack,upgrade
  global resistance_count,water_count,electric_count,fire_count,psychic_count,dragon_count,all_count,null_count,rock_count
  global potion,super_potion,energy_root,hyper_potion,max_potion,ultra_potion
  global pi_moves,sq_moves,ch_moves,ppokemon,r_moves,mew_moves,jig_moves,psy_moves,drag_moves
  shop_count = 0
  clear()
  print(e)
  print(f)

  shop_nav = input("""                                         """)
  shop_nav = shop_nav.lower()
  if shop_nav in ['1','pokemons','pokemon']:
    print("Professor Oak: Hey",username,"here are some good pokemon to buy.")
    print(CYELLOW2 + "Pichu - 100 Coins" + CEND)
    print (CYELLOW + "Charmander - 100 Poké" +CEND)
    print("\u001b[36;1mSquirtle - 100 Poké" + CEND)
    print(CVIOLET2 + "JigglyPuff - 300 Poké" + CEND)
    for x in badges:
      if x == "cascade badge":
        print(CYELLOW2 + "Psyduck - 400 Poké" + CEND)
      if x == "thunder badge":
        print(CYELLOW + "Dragonite - 1200 Poké" + CEND )
      if x == "boulder badge":
        print("Onix - 800 Poké")
        print("Geodude - 800 Poké")
      if x  == "marsh badge":
        print(CVIOLET2 + "Mew - 1500 Poké" + CEND)
    print("GO BACK")
    print()
    purchase_pokemon = input()
    if coins >= 100 and purchase_pokemon.lower() == "pichu":
      if ppokemon[0] == "pichu":
        print("You already have this pokemon")
      elif ppokemon[0] in ['pikachu','raichu']:
        print("I don't have time for jokes kiddo. Get Lost!")
      else:
        ppokemon[0] = "pichu"
        coins -= 100
        shop_count += 1
        print("Purchase Successful: You now own a Pichu")
    elif purchase_pokemon in ['go back','back','goback']:
      clear()
      shop()
      playerinfo()
    elif coins >= 100 and purchase_pokemon.lower() == "squirtle":
      if ppokemon[2] == "squirtle":
        print("You already have this pokemon")
      elif ppokemon[2] in ['wartortle','blastoise']:
        print("I don't have time for jokes kiddo. Get Lost!")
      else:
        ppokemon[2] = "squirtle"
        coins -= 100
        shop_count += 1
        print("Purchase Successful: You now own a Squirtle.")
    elif coins >= 100 and purchase_pokemon.lower() == "charmander":
      if ppokemon[1] == "charmander":
        print("You already have this pokemon")
      elif ppokemon[1] in ['charmeleon','charizard']:
        print("I don't have time for jokes kiddo. Get Lost!")
      else:
        ppokemon[1] = "charmander"
        coins -= 100
        shop_count += 1
        print("Purchase Successful: You now own a Charmander.")
    elif coins >= 1200 and "thunder badge" in badges and purchase_pokemon.lower() == "dragonite":
      if ppokemon[3] == "dragonite":
        print("I really don't have time for this. GET LOST")
      else:
        coins -= 1200
        shop_count += 1
        ppokemon[3] = "dragonite"
        print("Purchase Successful: You now own a Dragonite.")
        print("Take Good Care of it. Though it can't evolve but it surely can learn more moves than others.")

    elif coins >= 1500 and purchase_pokemon.lower() == "mew" and "marsh badge" in badges:
      if ppokemon[4] == "mew":
        print("I really don't have time for this. GET LOST")
      else:
        coins -= 1500
        shop_count += 1
        ppokemon[4] = "mew"
        print("Purchase Successful: You now own Mew")
        print("Man, this pokemon is one heck of a deal.")
    elif coins >= 400 and purchase_pokemon.lower() == "psyduck" and badges[0] == 'cascade badge':
      if ppokemon[5] == "psyduck":
        print("Umm, It seems like you already have this pokemon.")
      else:
        coins -= 400
        shop_count += 1
        ppokemon[5] = "psyduck"
        print("Purchase Successful: You now own a Psyduck")
        print("By the way, why psyduck?")
    elif coins >= 300 and purchase_pokemon.lower() == "jigglypuff":
      if ppokemon[6] == "jigglypuff":
        print("Umm, It seems like you already have this pokemon.")
      else:
        coins -= 300
        shop_count += 1
        ppokemon[6] = "jigglypuff"
        print("Purchase Successful: You now own a JigglyPuff")
        print("JigglyPuff is really cute right?")
    
    elif coins >= 800 and ("boulder badge" in badges) and purchase_pokemon.lower() == "onix":
      if ppokemon[8] == "onix":
        print("You already have this pokemon")
      else:
        ppokemon[8] = "onix"
        coins -= 800
        shop_count += 1
        print("Purchase Successful: You now own a Onix.")
    
    elif coins >= 800 and "boulder badge" in badges and purchase_pokemon.lower() == "geodude":
      if ppokemon[9] == "geodude":
        print("You already have this pokemon")
      else:
        ppokemon[9] = "geodude"
        coins -= 800
        shop_count += 1
        print("Purchase Successful: You now own a Geodude.")
    else:
      print("I don't quite get that. Try Again.")
      return shop()
  elif shop_nav == "3":
    print("Nurse Joy: You can purchase resistance for your pokemon, so they don't get hurt.")
    print("Purchasing resistance will give you " + CBOLD + "25%" + CEND + " resistance against Pokemon")
    print("Type Back to go back.")
    print(CBLUE + CBOLD + "1 - Water Type Resistance(50 Poké)" + CEND)
    print (CBLUE + CBOLD + "2 - Fire Type Resistance(50 Poké)" +CEND)
    print(CBLUE + CBOLD + "3 - Electric Type Resistance(50 Poké)" + CEND)
    print(CBLUE + CBOLD +  "4 - Dragon Type Resistance(30 Poké)" + CEND)
    print(CBLUE + CBOLD + "5 - Psychic Type Resistance(70 Poké)" + CEND)
    print(CBLUE + CBOLD + "6 - Rock Type Resistance(50 Poké)" + CEND)
    print(CBLUE + CBOLD + "7 - FULL RESISTANCE(Resistant to any attack)(100 Poké)" + CEND )
    print(CBLUE + CBOLD + "8 - Null Elemental Damage (100 Poké)" + CEND )
    print(CRED + CBOLD +  "THESE RESISTANCE ARE VALID ONLY FOR 1 FIGHT." + CEND)
    print("GO BACK")
    print()
    purchase_resistance = input()
    if coins >= 50 and purchase_resistance == "1":
      water_count+= 1
      resistance_count += 1
      shop_count += 1
      coins -= 50
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
      inventory.append("watertype")
    elif purchase_resistance in ['go back','back','goback']:
      clear()
      playerinfo()
      shop()
    elif coins >= 50 and purchase_resistance == "2":
      fire_count += 1
      resistance_count += 1
      shop_count += 1
      coins -= 50
      inventory.append("firetype")
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
    elif coins >= 50 and purchase_resistance == "3":
      electric_count += 1
      resistance_count += 1
      shop_count += 1
      coins -= 50
      inventory.append("electrictype")
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
    elif coins >= 30 and purchase_resistance == '4':
      dragon_count+=1
      resistance_count += 1
      shop_count += 1
      coins -= 30
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
    elif coins >= 70 and purchase_resistance == '5':
      psychic_count += 1
      resistance_count += 1
      shop_count += 1
      coins -= 70
      inventory.append("psychictype")      
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
    elif coins >= 70 and purchase_resistance == '6':
      rock_count += 1
      resistance_count += 1
      shop_count += 1
      coins -= 50
      inventory.append("rocktype")      
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)

    elif coins >= 100 and purchase_resistance == '7':
      all_count += 1
      resistance_count += 1
      shop_count += 1
      coins -= 100
      inventory.append("all")
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
    elif coins >= 100 and purchase_resistance == '8':
      null_count += 1
      shop_count += 1
      coins -= 100
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
    else:
      print("I don't quite get that :/ Try Again.")
      return shop()
  elif shop_nav == "4":
    print(CRED + "Nurse Joy:"+ CEND + CBOLD+ "Health Potions will give you extra life for a match." + CEND)
    print()
    print(CBLUE + CBOLD + "1 - Potion (10% Extra Health) (100 Poké)" + CEND)
    print (CBLUE + CBOLD + "2 - Super Potion (20% Extra Health) (200 Poké)" +CEND)
    print(CBLUE + CBOLD + "3 - Hyper Potion (30% Extra Health)(300 Poké)" + CEND)
    print(CBLUE + CBOLD + "4 - Energy Root Potion(40% Extra Health) (400 Poké)" + CEND)
    print(CBLUE + CBOLD + "5 - Max Potion (50% Extra Health) (500 Poké)" + CEND)
    print(CBLUE + CBOLD + "6 - Ultra Boost (Double Health) (1000 Poké)" + CEND )

    print(CRED + CBOLD + "THESE POTIONS ARE VALID ONLY FOR 1 FIGHT." + CEND)

    print("GO BACK")
    print()
    purchase_health = input()
    if coins >= 100 and purchase_health == "1":
      potion += 1
      shop_count += 1
      coins -= 100
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
      inventory.append("watertype")
    elif purchase_health in ['go back','back','goback']:
      clear()
      playerinfo()
      shop()
    elif coins >= 100 and purchase_health == "2":
      super_potion += 1
      shop_count += 1
      coins -= 200
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
    elif coins >= 300 and purchase_health == "3":
      hyper_potion += 1
      shop_count += 1
      coins -= 300
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
    elif coins >= 400 and purchase_health == '4':
      energy_root += 1
      shop_count += 1
      coins -= 400
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
    elif coins >= 500 and purchase_health == '5':
      max_potion += 1
      shop_count += 1
      coins -= 500      
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
    elif coins >= 1000 and purchase_health == '6':
      ultra_potion += 1
      shop_count += 1
      coins -= 1000
      print(CGREEN + "Purchase Successful, Item added to inventory." + CEND)
    else:
      print("I don't quite get that :/ Try Again.")
      return shop()
  elif shop_nav == "2":
    print("Professor Oak: Making your pokemon learn new attacks is a good way to make them stronger.")
    t.sleep(1)
    print("So What Moves you'd like for your pokemons to learn today?")
    print("Just Type in the name of attack you want to learn")
    print()
    print('Remember: You can only purchase moves you unlocked with evolution.')
    purchase_attack = input('''
    For Pikachu: Thunder Wave(Damage 30-45) - 30 Poké
    For Raichu: Thunder Wave(Damage 70-80) - 30 Poké,Thunder Punch(65-100) - 70 Poké
    For Charmeleon: Ember(35-40) - 30 Poké
    For Charizard: Ember(65-100) - 30 Poké,Wing Attack(65-100) - 70 Poké
    For Wartortle: Bubble Beam(40-55) - 40 Poké
    For Blastoise: Bubble Beam(68-80) - 40 Poké,Flash Cannon(70-80) - 60 Poké
    For JigglyPuff: Dream Eater(40-55) 50 Coin
    For Psyduck: Psychic(40-55) - 50 Poké 
    For Golduck: Psychic(40-70) - 50 Poké,Ice Punch(75-85) - 80 Poké 
    For Dragonite: Fire Punch(90-100) - 100 Poké
    For Mewtwo: Dark Pulse(80-110) - 100 Poké 
    Go Back.

    Damage may vary depending on the situation.
    ''')      
    purchase_attack = purchase_attack.lower()
    
    if purchase_attack in ['thunder wave','thunderwave'] and ppokemon[0] in ['pikachu','raichu'] and coins >= 30:
      if 'thunder wave' not in pi_moves:
        pi_moves.extend(['thunderwave'])
        coins -= 30
        shop_count += 1
        print("Attack successfully Purchased")
      else:
        print("You Already Have That Attack")

    elif purchase_attack in ['back','goback','go back']:
      clear()
      playerinfo()
      shop()
    elif purchase_attack in ['ember'] and ppokemon[1] in ['charmeleon','charizard'] and coins >= 30:
      if 'ember' not in ch_moves:
        ch_moves.extend(['ember','e'])
        coins -= 30
        shop_count += 1
        print("Attack successfully Purchased")
      else:
        print("You Already Have That Attack")  
  
    elif purchase_attack in ['bubble beam','bubblebeam'] and ppokemon[2] in ["wartortle","blastoise"] and coins >= 40:
      if 'bubble beam' not in sq_moves:
        sq_moves.extend(['bubble beam','bubblebeam'])
        coins -= 40
        shop_count += 1
        print("Attack successfully Purchased")
      else:
        print("You Already Have That Attack")

  
    elif purchase_attack == 'psychic' and ppokemon[5] in ['psyduck','golduck'] and coins >= 50:
      if 'psychic' not in psy_moves:
        psy_moves.extend(['psychic','p'])
        coins -= 50
        shop_count += 1
        print("Attack successfully Purchased")
      else:
        print("You Already Have That Attack")

    elif purchase_attack in ['dream eater','dreameater'] and coins >= 50 and ppokemon[6] == 'jigglypuff':
      if 'dream eater' not in jig_moves:
        jig_moves.extend(['dream eater','dreameater','de','deater'])
        coins -= 50
        shop_count += 1
        print("Attack successfully Purchased")
      else:
        print("You Already Have That Attack")
      
  
    elif purchase_attack in ['flash canon','flashcanon'] and coins >= 60 and ppokemon[2] == 'blastoise':
      if 'flash cannon' not in sq_moves:
        sq_moves.extend(["flash canon","fc","flashcanon"])
        coins -= 60
        shop_count += 1
        print("Attack successfully Purchased")
      else:
        print("You Already Have That Attack")

    elif purchase_attack in ['thunderpunch','thunder punch'] and coins >= 70 and ppokemon[0] == "raichu":
      if 'tp' not in pi_moves:
        pi_moves.extend(['tp','thunderpunch','thunder punch'])
        coins -= 70
        shop_count += 1
        print("Attack successfully Purchased")
      else:
        print("You Already Have That Attack")

    elif purchase_attack in ['wing attack','wingattack'] and coins >= 70 and ppokemon[1] == 'charizard':
      if 'wing attack' not in ch_moves:
        ch_moves.extend(['wing attack','wingattack','wg'])
        coins -= 70
        shop_count += 1
        print("Attack successfully Purchased")
      else:
        print("You Already Have That Attack")

    elif purchase_attack in ['ice punch','icepunch'] and coins >= 80 and ppokemon[5] == 'golduck':
      if 'ice punch' not in psy_moves:
        psy_moves.extend(["ice punch","icepunch","ip"])
        coins -= 80
        shop_count += 1
        print("Attack successfully Purchased")
      else:
        print("You Already Have That Attack")

    elif purchase_attack in ['dark pulse','darkpulse'] and coins >= 100 and ppokemon[4] == 'mewtwo':
      if 'dark pulse' not in mew_moves:
        mew_moves.extend(["darkpulse","dark pulse","dp"])
        coins -= 100
        shop_count += 1
        print("Attack successfully Purchased")
      else:
        print("You Already Have That Attack")          

    elif purchase_attack in ['fire punch','firepunch'] and coins >= 100 and ppokemon[3] in ['dragonite']:
      if 'firepunch' not in drag_moves:
        drag_moves.extend(['firepunch','fire punch','fp'])
        coins -= 100
        shop_count += 1
        print("Attack successfully Purchased")
      else:
        print("You Already Have That Attack")
    else:
      print("You don't have this pokemon")

  if shop_count >= 1:
    buyagain = input("Would you like to buy anything else?(Y/N)\n")
    if buyagain.lower() in ['yes','y']:
      clear()
      playerinfo()
      return shop()
    else:
      print("Thanks for shopping with us.")
      print("Have a nice day!")
      savedata()
      shopfight()

  elif shop_nav.lower() in ['back','go back','goback']:
    savedata()
    shopfight()
  else:
    savedata()
    shopfight()
userinfo()

def gymbadges():
  global trainer,badges,trainerwins,coins,wins,trwins,a,tutorial,fire_count,resistance_count,water_count,electric_count,all_count,ppokemon,psychic_count,dragon_count
  if trainer[0] == "Ash":
    tutorial += 1
    print("Ash: So,",username,"our training ends here.")
    input()
    print("Ash: You seem to be ready for your first real match.")
    input()
    print("You: Real Match?What?")
    input()
    print("Ash: Yeah, don't you know? You have to earn badges to play in pokemon league.")
    input()
    print("Ash: You must earn 4 Badges namely:\n1-Cascade Badge\n2-Volcano Badge\n3-Thunder Badge\n4- Boulder Badge and finally\n5-Marsh Badge")
    input()
    print("Ash: Once you collect all of them, you can fight in a pokemon league.")
    input()
    print("Ash: You will be able to make lots of money there :3 ")
    input()
    print("Ash: Then you can use that money to buy more pokemons or attacks. ")
    input()
    print("You: Pokemon League, Woah. *_* , So where should i start?")
    input()
    print("Ash: I recommend starting with Cerulean City Pokemon Gym.")
    input()
    print("Ash: Its Gym Leader is Misty.")
    input()
    print("You: Ok, Thanks! I better get going now. ")
    input()
    print("Ash: Bye")
    input()
    print()
    print(CBEIGE + CBOLD + "You arrived at Cerulean City Pokemon Gym." + CEND)
    input()
    print("You: This place is a mess.")
    input()
    print("Misty: Say that again brat! I dare you..")
    input()
    print("You: What's up with you lady.")
    input()
    print("Misty: This is my place and who the hell are you?")
    input()
    print("You: Oh, that means you are the gym leader?")
    input()
    print("Misty: Yes and what does that have to do with you?")
    input()
    print("You: So can you please give me your badge?")
    input()
    print("Misty: Huh?! You have to fight for badge punk! You can't just go and ask for it.")
    input()
    print("You: Okay then let's get down to it.")
    trainer[0] = 'Misty'
    
  elif trainer[0] == "Misty" and wins >= 1:
    trainerwins += 1
    wins = 0
    if trainerwins == 3:
      print(CGREEN + CBOLD + "Congratulations! You won Cascade Badge." + CEND)
      input()
      print("Misty: You fought really well for a kid")
      input()
      print("You: It was all because of Ash's training.")
      input()
      print("Misty: Ash Ketchum????")
      input()
      print("You: Yeah... Do you know him?")
      input()
      print("Misty: How can i forget him, that jerk broke my bicycle.")
      input()
      print("Misty: Well anyways, good luck for your upcoming matches, and be sure to enter the Championship League.")
      input()
      print("You: So i better get going now.")
      badges.append('cascade badge')
      print(CBEIGE + CBOLD + "+ Psyduck Available For Purchase"+ CEND)
      print(CGREEN + CBOLD +"+ New Evolution Unlocked: Golduck"+ CEND)
      print(CGREEN + CBOLD +"+ New Evolution Unlocked: Blastoise"+ CEND)
      trainer[0] = "Emily"
      coins += 100
      trainerwins = 0
      wins = 0
      print("Bulba.. Bulbasaur")
      input()
      print("You: I think i heard bulbasaur")
      input()
      print("Bulbasaaauurrr.")
      input()
      print("You: It's definitely Bulbasaur")
      input()
      print("You: Hey what are you doing with that bulbasaur")
      input()
      print("You: Leave him alone, don't hurt him")
      input()
      print("Emily(Kidnapper): Mind your own business boy, don't interfere.")
      input()
      print("You: Well i won't let you go that easily")
      input()
      print("Emily: Oh Yeah? Lets see then.")
  elif trainer[0] == "Emily" and wins>=1:
    trainerwins +=1
    wins = 0
    if trainerwins >= 1:
      print("+ New Pokemon Added: Bulbasaur")
      print()
      print("Bulbasaur is now yours.")
      input()
      print()
      print(CBEIGE + CBOLD + "You Arrived at Seafoam Islands Pokemon Gym...." + CEND)
      print("You: Hey Old Man, who is the gym leader here?")
      input()
      print("Blaine: Who are you calling old man little brat!")
      input()
      print("Blain: And why do you even want to meet the gym leader?")
      input()
      print("You: I came here to get the volcano badge.")
      input()
      print("Blaine: Oh!! I see, then boy lets get down to the business.")
      input()
      ppokemon[7] = "bulbasaur"
      trainer[0] = "Blaine"
      trainerwins = 0

  elif trainer[0] == "Blaine" and wins >= 1:
    trainerwins += 1
    wins = 0
    if trainerwins == 3:
      print("Blaine: That was a tough fight young man.")
      input()
      print("Blaine: And you had many good moves there.")
      input()
      print("Blaine: Here take this badge, you deserve this.")
      input()
      print("You: Thanks Grapms, i had a great time fighting you.")
      badges.append('volcano badge')
      input()
      print("+ New Evolution Unlocked: Charizard")
      input()
      fire_count += 1
      resistance_count += 1
      print("+ New Item Received: Fire Resistance Potion(For 1 Match)")
      print("+ New Evolution Unlocked: Raichu")
      input()
      print()
      print(CBEIGE + CBOLD + "You Arrived at Vermillion City Pokemon Gym" + CEND)
      t.sleep(1)
      print()
      print("You: Is anyone here?")
      input()
      print("Lt. Surge: Yes, who are you and why have you come here?")
      input()
      print("You: I've come here to get the thunder badge and to enter the Championship League")
      input()
      print("Lt. Surge: You've got big dreams boy, lets see what you are made of.")
      input()
      trainer[0] = "Lt. Surge"
      coins += 200
      trainerwins = 0
      wins = 0
  elif trainer[0] == "Lt. Surge" and wins >= 1:
    wins = 0
    trainerwins += 1
    if trainerwins == 3:
      print("Congratulations! You won Thunder Badge.")
      badges.append('thunder badge')
      input()
      print("Lt. Surge: You fought really well boy.")
      input()
      print("Here take this badge you deserve this.")
      input()
      print("+ New Item Received: Electric Resistance(For 1 Match)")
      print("+ Dragonite Available For Purchase")
      input()
      t.sleep(1)
      print(CBEIGE + CBOLD + "You arrived at Pewter City Pokemon Gym" + CEND)
      input()
      print("Brock: Who are you?")
      input()
      print("You: I'm a big fan of you brock *_* ")
      input()
      print("Brock: Ehh? So you're here just to see me?")
      input()
      print("You: No actually, I'm going to the Pokemon Championship League.")
      input()
      print("You: And i need Boulder Badge for that.")
      input()
      print("You: So, i'm here to challenge you!")
      input()
      print("Brock(Bored): Can you please come later? I'm not in a mood to fight today.")
      input()
      print("You(Cat Eyes): Pretty Please _/\\_ ")
      input()
      print("Brock: Okay, lets see what you've got.")
      print()
      trainer[0] = "Brock"
      electric_count += 1
      resistance_count += 1
      coins += 300
      trainerwins = 0
      wins = 0
  elif trainer[0] == "Brock" and wins >= 1:
    wins = 0
    trainerwins += 1
    if trainerwins == 3:
      print("Congratulations! You won Boulder Badge.")
      badges.append('boulder badge')
      print("Brock: Its been a long time since i had that kind of fight.")
      input()
      print("Brock: But don't let it get the best of you.")
      input()
      print("Brock: You have to potential to win the Pokemon Championship League.")
      input()
      print("Brock: So, don't let me down, I'll be watching your match.")
      input()
      print("+ Onix Available in Shop")
      input()
      print("+ Geodude Available in Shop")
      input()
      print()
      print(CBOLD + CBEIGE+"You arrived at Saffron City Pokemon Gyml" + CEND)
      input()
      print()
      print("You: Is anyone here? Seems like a deserted place.")
      input()
      print("Sabrina: Why have you come here?")
      input()
      print("You: Where are you?")
      input()
      print("Sabrina: Why have you come here?")
      input()
      print("You: I'm here for the marsh badge.")
      input()
      print("Sabrina: You're not worth my time.")
      input()
      print("You: Afraid? Huh?!")
      input()
      print("Sabrina: Looks like i need to teache you a lesson.")
      input()
      print("You: Lets see.")
      trainer[0] = "Sabrina"
      badges.append("boulder badge")
      coins += 300
      trainerwins = 0
      wins = 0
  elif trainer[0] == "Sabrina" and wins >= 1:
    trainerwins += 1
    wins = 0
    if trainerwins == 3:
      print("Sabrina: It can't be, i can't lose to someone like you.")
      input()
      print("You: Yeah, but you just did old hag. Now give me my Marsh Badge")
      input()
      print("Sabrina: Here take this.")
      print("System: Congratulations! You won Marsh Badge.")
      input()
      print("+ Mew Available for Purchase")
      input()
      all_count += 1
      resistance_count += 1
      print("+ New Item Received: Super Resistance(for 1 match)")
      input()
      print("You have now entered in Pokemon Championship League")
      input()
      print("From now on one match will be of 5 rounds.")
      input()
      print("And the prize will be higher than ever before.")
      input()
      badges.append('marsh badge')
      trainer[1] = "Pokemon League"
      trainer[0] = 'Jayne'
      coins += 200
      trainerwins = 0
      wins = 0
  
  elif trainer[2] == "Team Rocket":
    if wins >= 1:
      trwins += 1
      wins = 0
      if trwins == 1:
        print("We'll Come back again.")
        coins += 50
        trwins = 0
        wins = 0
    trainer[2] = ''
    if 'boulder badge' in badges:
      trainer[0] = "Sabrina"
    elif 'thunder badge' in badges:
      trainer[0] = "Brock"
    elif 'volcano badge' in badges:
      trainer[0] = "Lt. Surge"
    elif 'cascade badge' in badges:
      trainer[0] = "Blaine"
    elif not badges:
      trainer[0] = "Misty"
    else:
      trainer[0] = current_trainer
  elif trainer[2] == "Random Player":
    if wins >= 1:
      trwins += 1
      wins = 0
      if trwins == 1:
        print("You are tough man, hope to see you again.")
        coins += 50
        trwins = 0
        wins = 0
    trainer[2] = ''
    if 'boulder badge' in badges:
      trainer[0] = "Sabrina"
    elif 'thunder badge' in badges:
      trainer[0] = "Brock"
    elif 'volcano badge' in badges:
      trainer[0] = "Lt. Surge"
    elif 'cascade badge' in badges:
      trainer[0] = "Blaine"
    elif not badges:
      trainer[0] = "Misty"
    else:
      trainer[0] = current_trainer
  
  elif trainer[1] == "Pokemon League" and wins >= 1 and trainer[2] != 'Team Rocket':
    trainerwins += 1
    wins = 0
    if trainerwins == 5:
      trainer[0] = choice(leagueplayers)
      trainerwins = 0
      coins += 200
      wins = 0
    pass
def playerinfo():
  badgeshow = ",".join(str(x) for x in badges)

  if trainer[1] == "Pokemon League" and trainer[2] != 'Team Rocket':
    print(survival)
    print(CGREENBG + "POKEMON CHAMPIONSHIP LEAGUE" + CEND)
    print()
  elif trainer[2] == "Team Rocket":
    print(c)
    print(CVIOLETBG + "TEAM ROCKET" + CEND)
    print()
  elif trainer[2] == "Random Player":
    print(c)
    print(CREDBG+"Enemy Encounter" + CEND)
  elif trainer[0] == "Misty":
    print(d)
    print("\u001b[46;1mCerulean City Pokemon Gym" + CEND)
    print()
  elif trainer[0] == "Emily":
    print(c)
    print(CREDBG+"Enemy Encounter" + CEND)
  elif trainer[0] == "Blaine":
    print(d)
    print(CREDBG +"Seafoam Islands Pokemon Gym" + CEND )
    print()
  elif trainer[0] == "Lt. Surge":
    print(d)
    print(CYELLOWBG2 + CBLACK + "Vermillion City Pokemon Gym" + CEND)
    print()
  elif trainer[0] == "Brock":
    print(d)
    print(CYELLOWBG + "Pewter City Pokemon Gym" + CEND)
    print()
  elif trainer[0] == "Sabrina":
    print(d)
    print(CVIOLETBG + "Saffron City Pokemon Gym" + CEND)
    print()
  print("Name:",username.capitalize())
  print("Poké:",coins)
  print("Current Badges:",badgeshow.title())
  
  if resistance_count >=1 or potion >= 1 or super_potion >= 1 or hyper_potion >=1 or energy_root>= 1 or hyper_potion >= 1 or max_potion >= 1 or ultra_potion >=1:
    print("Inventory: ",end="")
    if water_count >=1:
      print("Water Resistance(",water_count,")",end=",")
    if fire_count >=1:
      print("Fire Resistance(",fire_count,")",end=",")
    if electric_count >=1:
      print("Electric Resistance(",electric_count,")",end=",")
    if dragon_count >= 1:
      print("Dragon Resistance(",dragon_count,")",end=",")
    if psychic_count >=1:
      print("Psychic Resistance(",psychic_count,")",end=",")
    if all_count >=1:
      print("Full Damage Resistance(",all_count,")",end=",")
    if potion >=1:
      print("Normal Potion(",potion,")",end=",")
    if super_potion >=1:
      print("Super Potion(",super_potion,")",end=",")
    if hyper_potion >=1:
      print("Hyper Potion(",hyper_potion,")",end=",")
    if energy_root>=1:
      print("Energy Root(",energy_root,")",end=",")
    if max_potion>=1:
      print("Max Potion(",max_potion,")",end=",")
    if ultra_potion>=1:
      print("Ultra Potion(",ultra_potion,")")
    print()
  else:
    print("Inventory:")

  if trainer[2] not in ["Team Rocket","Random Player"]:
    print("Currently Fighting:", trainer[0])
    print("Wins Against " + trainer[0] + ":",trainerwins)
  else:
    print("Currently Fighting:", trainer[0])  

  print("Available Pokemons:")
  for x in ppokemon:
    if x in ['pichu','pikachu','raichu']:
      print(ppokemon[0].capitalize(),"Exp:",p_exp)
    elif x in ['charmander','charmeleon','charizard']:
      print(ppokemon[1].capitalize(),"Exp:",c_exp)
    elif x in ['squirtle','wartortle','blastoise']:
      print(ppokemon[2].capitalize(),"Exp:",s_exp)
    elif x in ['bulbasaur','ivysaur','venusaur']:
      print(ppokemon[7].capitalize(),"Exp:",b_exp)
    elif x in ['psyduck','golduck']:
      print(ppokemon[5].capitalize(),'Exp:',ps_exp)
    elif x in ['jigglypuff']:
      print(ppokemon[6].capitalize(),'Exp:',j_exp)
    elif x == 'dragonite':
      print(ppokemon[3].capitalize(),"Exp:",r_exp)
    elif x in ['onix']:
      print("Onix Exp:",o_exp)
    elif x in ['geodude']:
      print("Geodude Exp:",g_exp)
    elif x in ['mew','mewtwo']:
      print(ppokemon[4].capitalize(),"Exp:",m_exp)
  print()
def choosepoke():
  global player_pokemon,cpu_pokemon,evolve,stamina,player_move,pokelist,p_exp,c_exp,s_exp,r_exp,m_exp,ps_exp,j_exp,coins,attack,upgrade,password,ppokemon
  global thunderbolt,irontail,thunderwave,fire,rage,ember,watergun,dash,bubble,saveuser,conf,mpsychic,trainer,trainerwins,badges,b_exp,o_exp,g_exp
  savedata()
  if ppokemon != finalised:
    if p_exp >= 200 and ppokemon[0] == 'pichu':
      print("You can now evolve Pichu into Pikachu. Doing so will boost its attack power.\n Do you want to do it?(Y/N)")
      evolution = input()      
      if evolution.lower() in ['yes','y']:
        ppokemon[0] = "pikachu"
        thunderbolt = randint(-40,-38)
        irontail = randint(-50,-35)
        print("Pichu has now evolved into Pikachu.")
        print("+ Attack power increased")
        print("New Move Unlocked: Thunderwave")        
        
        p_exp -= 200
        upgrade += 1
    if b_exp >= 200 and ppokemon[7] == 'bulbasaur':
      print("You can now evolve Bulbasaur into Ivysaur. Doing so will boost its attack power.\n Do you want to do it?(Y/N)")
      evolution = input()      
      if evolution.lower() in ['yes','y']:
        ppokemon[7] = "ivysaur"
        print("Bulbasaur has now evolved into Ivysaur.")
        print("+ Attack power increased")
        print("New Move Unlocked: Solar Beam")        
        b_exp -= 200
        upgrade += 1

    elif c_exp >= 200 and ppokemon[1] == 'charmander':
      print("You can now evolve Charmander into Charmeleon. Doing so will boost its attack power.\n Do you want to do it?(Y/N)")
      evolution = input()      
      if evolution.lower() in ['yes','y']:
        ppokemon[1] = "charmeleon"
        fire = randint(-45,-35)
        rage = randint(-50,-40)     
        print("Charmander has evolved into Charmeleon")
        print("+ Attack Power")
        print('+ New Attack Unlocked : Ember')
        c_exp -= 200
        upgrade += 1

    elif s_exp >= 200 and ppokemon[2] == 'squirtle':
      print("You can now evolve Squirtle into Wartortle. Doing so will boost its attack power.\n Do you want to do it?(Y/N)")
      evolution = input()      
      if evolution.lower() in ['yes','y']:
        ppokemon[2] = "wartortle" 
        watergun = randint(-45,-35)
        dash = randint(-30,-25)
        print("Squirtle has evolved into Wartortle")
        print("+ All Attack Power Increased")
        print("+ New Attack Unlocked: Bubble Beam")
        s_exp -= 200
        upgrade += 1
        
    elif p_exp >= 500 and "cascade badge" in badges and  ppokemon[0] == 'pikachu':
      print("You can now evolve Pikachu into Raichu. Doing so will boost its attack power.\n Do you want to do it?(Y/N)")
      evolution = input()
      if evolution.lower() in ['yes','y']:      
        ppokemon[0] = "raichu"
        thunderbolt = randint(-55,-45)
        irontail = randint(-60,-40)
        if 'thunderwave' in pi_moves:
          thunderwave = randint(-65,-50)
        else:
          pass
        print("Pikachu has evolved into Raichu")
        print("+ All Attack Power Increased")
        print("+ New Move Unlocked: ThunderPunch") 
        p_exp -= 500
        upgrade += 1

    elif c_exp >= 500 and "cascade badge" in badges and ppokemon[1] == 'charmeleon':
      print("You can now evolve Charmeleon into Charizard. Doing so will boost its attack power.\n Do you want to do it?(Y/N)")
      evolution = input()
      if evolution.lower() in ['yes','y']:      
        ppokemon[1] = "charizard" 
        fire = randint(-70,-65)
        rage = randint(-80,-62)
        if 'ember' in ch_moves:
          ember = randint(-100,-65)

        print("Charmeleon has evolved into Charizard")
        print("+ Attack Power")
        print('+ New Move Unlocked: Wing Attack')
        c_exp -= 500
        upgrade += 1

    elif b_exp >= 500 and "volcano badge" in badges and ppokemon[7] == 'ivysaur':
      print("You can now evolve Ivysaur into Venusaur. Doing so will boost its attack power.\n Do you want to do it?(Y/N)")
      evolution = input()
      if evolution.lower() in ['yes','y']:      
        ppokemon[7] = "venusaur" 
        print("Ivysaur has evolved into Venusaur")
        print("+ Attack Power")
        print('+ New Move Unlocked: Petal Dance')
        b_exp -= 500
        upgrade += 1
        
    elif s_exp >= 500 and "cascade badge" in badges and  ppokemon[2] == 'wartortle':
      print("You can now evolve Wartortle into Blastoise. Doing so will boost its attack power.\n Do you want to do it?(Y/N)")
      evolution = input()      
      if evolution.lower() in ['yes','y']:
        ppokemon[2] = "blastoise"
        watergun = randint(-60,-55)
        dash = randint(-94,-50)
        if 'bubble beam' in sq_moves:
          bubble = randint(-80,-68)
        print("Wartortle has evolved into Blastoise")
        print("+ All Attack Power Increased")
        print('+ New Move Unlocked: Flash Canon')
        s_exp -= 500
        upgrade += 1
      else:
        pass    
    elif m_exp >= 500 and ppokemon[4] == 'mew':
      print("You can now evolve Mew into Mewtwo. Doing so will boost its attack power.\n Do you want to do it?(Y/N)")
      evolution = input()      
      if evolution.lower() in ['yes','y']:
        ppokemon[4] = "mewtwo"
        conf = randint(-89,-79)
        mpsychic = randint(-70,-60)
        print("Mew has now evolved into Mewtwo.")
        print("+ All Attack Power Increased")
        print("+ New Move Unlocked: Dark Pulse")
        m_exp -= 500
        upgrade += 1
        
    elif ps_exp >= 500 and ppokemon[5] == 'psyduck':
      print("You can now evolve Psyduck into Golduck. Doing so will boost its attack power.\n Do you want to do it?(Y/N)")
      evolution = input()      
      if evolution.lower() in ['yes','y']:
        ppokemon[5] = "golduck"
        hpump = randint(-70,-60)
        stoss = randint(-85,-64) 
        if 'psychic' in psy_moves:
          psychic = randint(-70,-40)
        print("Psyduck has evolved into Golduck")
        print("+ All Attack Power Increased")
        print("+ New Move Unlocked: Ice Punch")
        ps_exp -= 500
        upgrade += 1


    if upgrade>= 1:  
      savegame = input("Would you like to save game?(Y/N) \n")
      if savegame.lower() in ['yes','y']:
        print("Saving Game......")
        t.sleep(1.3)
        savedata()
        clear()
        playerinfo()
        upgrade = 0  
  if trainer[2] == "Team Rocket":
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
    engine.say("Prepare for trouble!")
    print("Jessie: Prepare for trouble!")
    engine.runAndWait()
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
    engine.say('Make it double!')
    print('James: Make it double!')
    engine.runAndWait()
    engine.setProperty('voice',voices[1].id)
    engine.say("To Protect the world from Devastation!")
    print("Jessie: To Protect the world from Devastation!")
    engine.runAndWait()
    engine.setProperty('voice',voices[0].id)
    engine.say("James: To Unite all the people within our Nation!")
    print("James: To Unite all the people within our Nation!")
    engine.runAndWait()
    engine.setProperty('voice',voices[1].id)
    engine.say("Jessie!")
    print("Jessie: Jessie!")
    engine.runAndWait()
    engine.setProperty('voice',voices[0].id)
    engine.say("James")
    print("James: James!")
    engine.runAndWait()
    input()
    engine.setProperty('voice',voices[1].id)

    print("Jessie: Team Rocket, blast off at the speed of light!")
    input()
    engine.setProperty('voice',voices[0].id)
    engine.say("Surrender Now or prepare to fight")
    print("James: Surrender Now, or prepare to fight.")
    engine.runAndWait()
    input()
    print("Meowth: Meowth! That's right!")
    input()
  
  elif trainer[2] == "Random Player":
    print(trainer[0]+": I challenge you to fight with me.")
    input()

  elif trainer[0] == "Misty":
    print("Cerulean City Pokemon Gym")
    print()
    print("Leader: Misty")
    print()
    print("The Tomboyish Mermaid")
    print()
  elif trainer[0] == "Blaine":
    print("Seafoam Islands Pokemon Gym")
    print()
    print("Leader: Blaine")
    print()
    print("The Hotheaded Quiz Master")
    print()
  elif trainer[0] == "Lt. Surge":
    print("Vermillion City Pokemon Gym")
    print()
    print("Leader: Lt. Surge")
    print()
    print("The Lightning American")
    print()
  elif trainer[0] == "Sabrina":
    print("Saffron City Pokemon Gym")
    print()
    print("Leader: Sabrina")
    print()
    print("The Master of Psychic Pokemons")
    print()       
    
  select_pokemon()
  if trainer[2] == "Team Rocket":
    if trainer[0] == "Jessie":
      cpu_pokemon = choice(jessie)
    elif trainer[0] == "James":
      cpu_pokemon = choice(james)  
  elif trainer[0] == "Ash" or trainer[0] in someplayers:
    if player_pokemon in pplv1:
      cpu_pokemon = choice(one)
    elif player_pokemon in pplv2:
      cpu_pokemon = choice(two)
    elif player_pokemon in finalised:
      cpu_pokemon = choice(three)
  elif trainer[0] == "Misty":
    cpu_pokemon = choice(misty_pokemons)
  elif trainer[0] == "Emily":
    cpu_pokemon = choice(bulba)
  elif trainer[0] == "Blaine":
    cpu_pokemon = choice(blain_pokemons)
  elif trainer[0] == "Lt. Surge":
    cpu_pokemon = choice(surge_pokemons)
  elif trainer[0] == "Brock":
    cpu_pokemon = choice(brock_pokemons)
  elif trainer[0] == "Sabrina":
    cpu_pokemon = choice(sabrina_pokemons)
  elif trainer[0] in leagueplayers:
    cpu_pokemon = choice(league)
  print(trainer[0] + "\'s Pokemon: " + cpu_pokemon)
    

def defaultattacks():
  global thunderbolt,irontail,thunderwave,thunderpunch,fire,rage,ember,wing,watergun,dash,bubble,flash,hpump,stoss,psychic,icepunch,sing,sball,deater
  global cpu_thunderbolt,cpu_irontail,cpu_thunderwave,cpu_thunderpunch,cpu_watergun,cpu_dash,cpu_bubble,cpu_flash,cpu_hpump 
  global cpu_stoss,cpu_psychic,cpu_icepunch,cpu_mpsychic,cpu_conf,cpu_darkpulse,cpu_rthunderbolt,cpu_shock,cpu_firepunch,cpu_fire,cpu_rage
  global cpu_ember,cpu_wing
  #
  if player_pokemon.lower() == 'pichu':
    irontail = randint(-30,-29)
    thunderbolt = randint(-30,-25)
    
  elif player_pokemon.lower() == 'pikachu' or cpu_pokemon == "pikachu":
    thunderbolt = randint(-40,-38)
    irontail = randint(-50,-35)
    thunderwave = randint(-45,-35)

  elif player_pokemon.lower() == 'raichu' or cpu_pokemon == "raichu":
    thunderbolt = randint(-55,-45)
    irontail = randint(-60,-40)
    thunderwave = randint(-65,-50)
    thunderpunch = randint(-100,-65)
    
  elif player_pokemon.lower() == "squirtle":
    watergun = randint(-35,-30)
    dash = randint(-30,-25)

  elif player_pokemon.lower() == "wartortle":
    watergun = randint(-45,-35)
    dash = randint(-30,-25)    
    bubble = randint(-55,-40)

  elif player_pokemon.lower() == "blastoise":
    watergun = randint(-50,-45)
    dash = randint(-50,-40)
    bubble = randint(-80,-68)
    flash = randint(-80,-69)

  elif player_pokemon.lower() == "psyduck":
    hpump = randint(-35,-20)
    stoss = randint(-45,-30) 
    psychic = randint(-55,-40)
  
  elif player_pokemon.lower() == "golduck":
    hpump = randint(-70,-60)
    stoss = randint(-85,-64) 
    psychic = randint(-70,-40)
    icepunch = randint(-85,-75)
  
  elif player_pokemon.lower() == "jigglypuff":
    sing = randint(-45,-35)
    sball = randint(-40,-30)
    deater = randint(-55,-40)
  elif player_pokemon.lower() == "bulbasaur":
    vine_whip = randint(-40,-35)
    razor_leaf = randint(-45,-40)

  elif player_pokemon.lower() == "ivysaur":
    vine_whip = randint(-60,-58)
    razor_leaf = randint(-65,-40)
    solar_beam = randint(-62,-48)
  elif player_pokemon.lower() == "venusaur":
    vine_whip = randint(-75,-58)
    razor_leaf = randint(-80,-40)
    solar_beam = randint(-75,-48)
    petal_dance = randint(-90,-75)

  elif player_pokemon.lower() == "charmander":
    cpu_fire = randint(-45,-35)
    cpu_rage = randint(-50,-40)
  
  elif player_pokemon.lower() == "charmeleon":
    fire = randint(-65,-45)
    rage = randint(-65,-40)
    ember = randint(-70,-40)
  
  elif player_pokemon.lower() == "charizard":
    fire = randint(-75,-55)
    rage = randint(-85,-65)
    ember = randint(-80,-50)
    wing = randint(-100,-65)

  #CPU Pokemons
  if cpu_pokemon == "pichu":
    cpu_irontail = randint(-35,-29)
    cpu_thunderbolt = randint(-30,-25)
    
  elif cpu_pokemon == "pikachu":
    cpu_thunderbolt = randint(-40,-38)
    cpu_irontail = randint(-50,-35)
    cpu_thunderwave = randint(-45,-30)
  
  elif cpu_pokemon == "raichu":
    cpu_thunderbolt = randint(-55,-45)
    cpu_irontail = randint(-60,-40)
    cpu_thunderwave = randint(-65,-50)
    cpu_thunderpunch = randint(-100,-65)
  
  elif cpu_pokemon == "squirtle":
    cpu_watergun = randint(-35,-30)
    cpu_dash = randint(-30,-25)
  
  elif cpu_pokemon == "wartortle":
    cpu_watergun = randint(-45,-35)
    cpu_dash = randint(-30,-25)    
    cpu_bubble = randint(-55,-40)
  
  elif cpu_pokemon == "blastoise":
    cpu_watergun = randint(-50,-45)
    cpu_dash = randint(-50,-40)
    cpu_bubble = randint(-80,-68)
    cpu_flash = randint(-80,-69)

  elif cpu_pokemon == "psyduck":
    cpu_hpump = randint(-35,-20)
    cpu_stoss = randint(-45,-30) 
    cpu_psychic = randint(-55,-40)
  
  elif cpu_pokemon == "golduck":
    cpu_hpump = randint(-70,-60)
    cpu_stoss = randint(-85,-64) 
    cpu_psychic = randint(-70,-40)
    cpu_icepunch = randint(-85,-75)

  elif cpu_pokemon == "charmander":
    cpu_fire = randint(-45,-35)
    cpu_rage = randint(-50,-40)
  
  elif cpu_pokemon == "charmeleon":
    cpu_fire = randint(-65,-45)
    cpu_rage = randint(-65,-40)
    cpu_ember = randint(-70,-40)
  
  elif cpu_pokemon == "charizard":
    cpu_fire = randint(-75,-55)
    cpu_rage = randint(-85,-65)
    cpu_ember = randint(-80,-50)
    cpu_wing = randint(-100,-65)
    
  elif cpu_pokemon == "mew":
    cpu_conf = randint(-70,-50)
    cpu_mpsychic = randint(-70,-40)
    cpu_darkpulse = randint(-110,-80)
  
  elif cpu_pokemon == "mewtwo":
    cpu_conf = randint(-80,-60)
    cpu_mpsychic = randint(-80,-65)
    cpu_darkpulse = randint(-130,-70)
  
  elif cpu_pokemon == "dragonite":
    cpu_rthunderbolt = randint(-80,-60)
    cpu_shock = randint(-90,-70)
    cpu_firepunch = randint(-100,-90)

  elif cpu_pokemon == "bulbasaur":
    cpu_vine_whip = randint(-40,-35)
    cpu_razor_leaf = randint(-45,-40)

  elif cpu_pokemon == "ivysaur":
    cpu_vine_whip = randint(-60,-58)
    cpu_razor_leaf = randint(-65,-40)
    cpu_solar_beam = randint(-62,-48)
  
  elif cpu_pokemon == "venusaur":
    cpu_vine_whip = randint(-75,-58)
    cpu_razor_leaf = randint(-80,-40)
    cpu_solar_beam = randint(-75,-48)
    cpu_petal_dance = randint(-90,-75)

  elif cpu_pokemon in ['kadabra','mr. mime']:
    psybeam = randint(-100,-80)
    deater = randint(-110,-80)
    mpsychic = randint(-90,-70)

def typeboost():
  global thunderbolt,irontail,thunderwave,thunderpunch,watergun,dash,bubble,flash,hpump,stoss,psychic,icepunch,sing,sball,deater
  global cpu_thunderbolt,cpu_irontail,cpu_thunderwave,cpu_watergun,cpu_dash,cpu_bubble
  if player_pokemon.lower() in ['pichu','pikachu','raichu']:
    if cpu_pokemon in ['charmander','charmeleon','charizard','squirtle','wartortle','blastoise','psyduck','golduck']:
      if player_pokemon.lower() == 'pichu':
        irontail = randint(-90,-29)
        thunderbolt = randint(-40,-35)

      elif player_pokemon.lower() == 'pikachu':
        thunderbolt = randint(-50,-48)
        irontail = randint(-60,-45)
        thunderwave = randint(-55,-40)

      elif player_pokemon.lower() == 'raichu':
        thunderbolt = randint(-65,-55)
        irontail = randint(-70,-50)
        thunderwave = randint(-75,-60)
        thunderpunch = randint(-100,-75)
    else:
      pass

  elif player_pokemon.lower() in ['squirtle','wartortle','blastoise','psyduck','golduck']:
    if cpu_pokemon in ['charmander','charmeleon','charizard']:
      if player_pokemon.lower() == "squirtle":
        watergun = randint(-40,-35)
        dash = randint(-30,-25)

      elif player_pokemon.lower() == "wartortle":
        watergun = randint(-50,-40)
        dash = randint(-45,-40)
        bubble = randint(-65,-50)

      elif player_pokemon.lower() == "blastoise":
        watergun = randint(-60,-55)
        dash = randint(-60,-50)
        bubble = randint(-80,-68)
        flash = randint(-90,-79)
      
      elif player_pokemon.lower() == "psyduck":
        hpump = randint(-45,-30)
        stoss = randint(-55,-40) 
        psychic = randint(-65,-50)
      
      elif player_pokemon.lower() == "golduck":
        hpump = randint(-80,-70)
        stoss = randint(-95,-74) 
        psychic = randint(-80,-50)
        icepunch = randint(-95,-85)

  elif player_pokemon.lower() in ['bulbasaur','ivysaur','venusaur']:
    if cpu_pokemon in ['squirtle','wartortle','blastoise','psyduck','golduck','onix','geodude']:
      if player_pokemon.lower() == "bulbasaur":
        vine_whip = randint(-55,-40)
        razor_leaf = randint(-55,-45)

      elif player_pokemon.lower() == "ivysaur":
        vine_whip = randint(-70,-62)
        razor_leaf = randint(-74,-48)
        solar_beam = randint(-70,-48)
      
      elif player_pokemon.lower() == "venusaur":
        vine_whip = randint(-80,-65)
        razor_leaf = randint(-88,-70)
        solar_beam = randint(-85,-50)
        petal_dance = randint(-100,-80)

  elif player_pokemon.lower() == "jigglypuff":
    if cpu_pokemon == "dragonite":
      sing = randint(-65,-55)
      sball = randint(-60,-50)
      deater = randint(-75,-60)

  if cpu_pokemon in ['pichu','pikachu','raichu']:
    if player_pokemon.lower() in ['charmander','charmeleon','charizard','squirtle','wartortle','blastoise','psyduck','golduck']:
      if cpu_pokemon == 'pichu':
        cpu_irontail = randint(-35,-29)
        cpu_thunderbolt = randint(-40,-35)

      elif cpu_pokemon.lower() == 'pikachu':
        cpu_thunderbolt = randint(-50,-48)
        cpu_irontail = randint(-60,-45)
        cpu_thunderwave = randint(-55,-40)

      elif cpu_pokemon.lower() == 'raichu':
        cpu_thunderbolt = randint(-65,-55)
        cpu_irontail = randint(-70,-50)
        cpu_thunderwave = randint(-75,-60)
        thunderpunch = randint(-100,-75)

  
  
  elif cpu_pokemon.lower() in ['squirtle','wartortle','blastoise']:
    if player_pokemon.lower() in ['charmander','charmeleon','charizard']:
      if cpu_pokemon == "squirtle":
        cpu_watergun = randint(-40,-35)
        cpu_dash = randint(-30,-25)

      elif cpu_pokemon == "wartortle":
        cpu_watergun = randint(-50,-40)
        cpu_dash = randint(-45,-40)
        cpu_bubble = randint(-65,-50)

      elif cpu_pokemon == "blastoise":
        cpu_watergun = randint(-60,-55)
        cpu_dash = randint(-60,-50)
        cpu_bubble = randint(-80,-68)
        flash = randint(-90,-79)
     
      elif cpu_pokemon == "psyduck":
        hpump = randint(-45,-30)
        stoss = randint(-55,-40) 
        psychic = randint(-65,-50)
      
      elif cpu_pokemon == "golduck":
        hpump = randint(-80,-70)
        stoss = randint(-95,-74) 
        psychic = randint(-80,-50)
        icepunch = randint(-95,-85)
  

  elif cpu_pokemon == "jigglypuff":
    if player_pokemon.lower() == "dragonite":
      sing = randint(-65,-55)
      sball = randint(-60,-50)
      deater = randint(-75,-60)
  

def water_resistance():
  global cpu_watergun,cpu_dash,cpu_bubble,cpu_flash,cpu_hpump,cpu_stoss,cpu_psychic,cpu_icepunch
  cpu_watergun -= (0.25* cpu_watergun)
  cpu_dash -=  (0.25*cpu_dash)
  cpu_bubble -= (0.25*cpu_bubble)
  cpu_flash -= (0.25*cpu_flash)
  cpu_hpump -= (0.25*cpu_hpump)
  cpu_stoss -= (0.25*cpu_stoss)
  cpu_psychic -= (0.25*cpu_psychic)
  cpu_icepunch -= (0.25*cpu_icepunch)

def fire_resistance():
  global cpu_fire,cpu_rage,cpu_ember,cpu_wing
  cpu_fire -= (0.25*cpu_fire)
  cpu_rage -= (0.25*cpu_rage) 
  cpu_ember -= (0.25*cpu_ember)
  cpu_wing -= (0.25*cpu_wing)

def electric_resistance():
  global cpu_thunderbolt,cpu_irontail,cpu_thunderwave,cpu_thunderpunch
  cpu_thunderbolt -= (0.25*cpu_thunderbolt)
  cpu_irontail -= (0.25*cpu_irontail)
  cpu_thunderwave -= (0.25*cpu_thunderwave)
  cpu_thunderpunch -= (0.25*cpu_thunderpunch)

def dragon_resistance():
  global cpu_rthunderbolt,cpu_shock,cpu_firepunch
  cpu_rthunderbolt -= (0.25*cpu_rthunderbolt)
  cpu_shock -= (0.25*cpu_shock)
  cpu_firepunch -= (0.25*cpu_firepunch)

def psychic_resistance():
  global cpu_conf,cpu_mpsychic,cpu_darkpulse
  cpu_conf -= (0.25*cpu_conf)
  cpu_mpsychic -= (0.25*cpu_mpsychic)
  cpu_darkpulse -= (0.25*cpu_darkpulse)

def rock_resistance():
  global cpu_double_edge,cpu_rock_slide,cpu_explosion
  cpu_double_edge -= (0.25*cpu_double_edge)
  cpu_rock_slide -= (0.25*cpu_rock_slide)
  cpu_explosion -= (0.25*cpu_explosion)

def damageresistance():
  global resistance_count,water_count,fire_count,electric_count,psychic_count,rock_count,dragon_count,all_count,null_count,null_activated
  global water_activated,fire_activated,electric_activated,dragon_activated,psychic_activated,all_activated
  water_activated,fire_activated,electric_activated,dragon_activated,psychic_activated,all_activated
  clear()
  playerinfo()
  shopfight()
  clear()
  playerinfo()

  if resistance_count>=1:
    print("You have damage resistance available in inventory.")
    print("Would you like to use it?[Y/N]")
    haveresistance = input()
    if haveresistance.lower() in ['yes','y']:
      if water_count>=1:
        print("Type Water to use Water resistance.")
      if electric_count >= 1:
        print("Type Electric to use Electric resistance")
      if fire_count >= 1:
        print("Type Fire to use Fire resistance")
      if dragon_count >= 1:
        print("Type Dragon to use resistance against Dragonite resistance")
      if psychic_count >= 1:
        print("Type Psychic to use Psychic Resistance.")
      if rock_count >= 1:
        print("Type Rock to use Rock Resistance.")
      if all_count >= 1:
        print("Type All to use damage resistance against every pokemon")          
      
      useresistance = input()
      
      if useresistance.lower() == 'water' and water_count >= 1:
        water_count -= 1
        resistance_count -= 1
        water_activated = 1
        print("Damage from water type pokemon reduced by 25%")

      elif useresistance.lower() == 'electric' and electric_count>= 1:
        electric_count -= 1
        resistance_count -= 1
        electric_activated = 1
        print("Damage from electric type pokemon reduced by 25%")
      elif useresistance.lower() == "fire" and fire_count >= 1:
        fire_count -= 1
        resistance_count -= 1
        fire_activated = 1
        print("Damage from fire type pokemon reduced by 25%")

      elif useresistance.lower() == "dragon" and dragon_count >= 1:
        dragon_count -= 1
        resistance_count -= 1
        dragon_activated = 1
        print("Damage from dragon type pokemon reduced by 25%")
      elif useresistance.lower() == "psychic" and psychic_count>= 1:
        psychic_count -= 1
        resistance_count -= 1
        psychic_activated = 1
        print("Damage from psychic type pokemon reduced by 25%")
      elif useresistance.lower() == "rock" and rock_count>= 1:
        rock_count -= 1
        resistance_count -= 1
        rock_activated = 1
        print("Damage from rock type pokemon reduced by 25%")
      elif useresistance.lower() == 'all' and all_count >= 1:

        all_count -= 1
        resistance_count -= 1
        all_activated = 1
        print("Damage from all pokemon reduced by 25%")                  
  null_elemental()

def activateresistance():
  global water_activated,fire_activated,electric_activated,dragon_activated,psychic_activated,all_activated,rock_activated
  if water_activated == 1:
    water_resistance()
    water_activated = 0
  elif fire_activated == 1:
    fire_resistance()
    fire_activated = 0
  elif electric_activated == 1:
    electric_resistance()
    electric_activated = 0
  elif dragon_activated == 1:
    dragon_resistance()
    dragon_activated = 0
  elif psychic_activated == 1:
    psychic_resistance()
    psychic_activated = 0
  elif rock_activated == 1:
    rock_resistance()
    rock_activated = 0
  elif all_activated == 1:
    water_resistance()
    fire_resistance()
    electric_resistance()
    dragon_resistance()
    psychic_resistance()
    rock_resistance()
    all_activated = 0
def null_elemental():
  global null_count,null_activated
  if null_count>= 1:
    activate_null = input("Do you want to nullify elemental damage?(Y/N)\n")
    if activate_null.lower() in ['yes','y']:
      null_count -= 1
      null_activated += 1
def select_pokemon():
  global player_pokemon,ppokemon
  regspeech()  
  if player_pokemon == '':
    return select_pokemon()
  
  elif player_pokemon.lower() in ppokemon:
    print("Your Pokemon:", player_pokemon)
  
  elif (player_pokemon.lower() in pplv1 or player_pokemon.lower() in pplv2) and player_pokemon.lower() not in ppokemon:
    print("You have already evolved this pokemon.")
    return select_pokemon()
  
  else:
    print("Sorry That Pokemon has not been discovered yet! :/")
    return select_pokemon()

def activate_null_elemental():
  global null_count,null_activated
  if null_activated == 1:
    defaultattacks()

def attackspeech():
  global player_move
  r = sr.Recognizer()
  with sr.Microphone() as source:
    audio = r.listen(source)
    try:
        player_move = r.recognize_google(audio)
        player_move=''.join(player_move.split())
        if player_move == 'heel':
          player_move = 'heal'
        elif player_move in ['underwear','thundervam']:
          player_move = 'thunderwave'
        player_move=player_move.lower()
        print("You chose : {}".format(player_move))
    except:
        print("Sorry could not recognize what you said")
        return attackspeech()

def final():
  global player_pokemon,cpu_pokemon,wins,loses,player_move,exp,evolve,ppokemon,saveuser,p_exp,c_exp,s_exp,r_exp,m_exp,ps_exp,j_exp,coins,o_exp,g_exp,b_exp
  global cpu_thunderbolt,cpu_irontail,cpu_thunderwave,cpu_fire,cpu_rage,cpu_ember,cpu_watergun,cpu_dash,cpu_bubblebeam
  global potion,super_potion,hyper_potion,max_potion,ultra_potion,energy_root

  while True:
    loaddata()
    player_health = 500
    damageresistance()
    choosepoke()
    if player_pokemon in ['pikachu','charmeleon','wartortle','ivysaur']:
      player_health = 600 
    elif player_pokemon in ['raichu','charizard','blastoise','onix','geodude','venusaur','golduck']:
      player_health = 800
    elif player_pokemon in ['dragonite','mew','mewtwo']:
      player_health = 1000
    
    if potion >= 1 or super_potion >= 1 or hyper_potion >=1 or energy_root>= 1 or hyper_potion >= 1 or max_potion >= 1 or ultra_potion >=1:
      usehealth = input("You Have health potions in your inventory, do you want to use it?[Y/N]")
      if usehealth.lower() in ['yes','y']:
        print("Which potion do you want to use?")
        if potion>= 1:
          print('Type "normal" to use potion(10% Extra Health)')
        if super_potion >= 1:
          print('Type "Super" to use super potion(20% Extra Health)')
        if hyper_potion >= 1:
          print('Type "Hyper" to use hyper potion(30% Extra Health')
        if energy_root >= 1:
          print('Type "Energy" to use Energy Root(40% Extra Health)')
        if max_potion >= 1:
          print('Type "Max" to use max potion(50% Extra Health)')
        if ultra_potion >=1:
          print('Type Ultra to use ultra potion(100% Extra Health)')
      
        askhelp = input()
        askhelp = askhelp.lower()
        if askhelp == "potion" and potion>=1:
          player_health += (0.1*player_health)
          potion -= 1
        elif askhelp == "super" and super_potion >= 1:
          player_health += (0.2*player_health)
          super_potion -=1
        elif askhelp == "hyper" and hyper_potion >= 1:
          player_health += (0.3*player_health)
          hyper_potion -=1
        elif askhelp == "energy" and energy_root >= 1:
          player_health += (0.4*player_health)
          energy_root -=1
        elif askhelp == "max" and max_potion >= 1:
          player_health += (0.5*player_health)
          max_potion -=1
        elif askhelp == "ultra" and ultra_potion >= 1:
          player_health += (1*player_health)
          ultra_potion -=1
    
    cpu_health = 500
    if cpu_pokemon in ['raichu','charizard','blastoise','onix','geodude','venusaur','golduck']:
      cpu_health = 800
    elif cpu_pokemon in ['kadabra','mr. mime']:
      cpu_health = 600
    elif cpu_pokemon in ['dragonite','mew','mewtwo']:
      cpu_health = 1000
    
    if trainer[0] == "Blaine":
      cpu_health += 100
    elif trainer[0] == "Lt. Surge":
      cpu_health += 200
    elif trainer[0] == "Brock":
      cpu_health += 300
    elif trainer[0] == "Sabrina":
      cpu_health += 400
    elif trainer[0] in (leagueplayers):
      cpu_health += 500
    def main():             #For Looping if incorrect input
      try:
        nonlocal player_health,cpu_health
        global player_pokemon,cpu_pokemon,wins,loses,player_move,evolve,exp,ppokemon,p_exp,c_exp,s_exp,r_exp,m_exp,ps_exp,j_exp,o_exp,g_exp,b_exp,coins
        global potion,super_potion,hyper_potion,max_potion,ultra_potion,energy_root

        global cpu_thunderbolt,cpu_irontail,cpu_thunderwave,cpu_fire,cpu_rage,cpu_ember,cpu_watergun,cpu_dash,cpu_bubblebeam
        while player_health > 0 and cpu_health > 0:
          #USER'S MOVES HERE
          print("Your Turn")
          print()
          defaultattacks()
          typeboost()
          activate_null_elemental()
          activateresistance()

          #USER PIKACHU FAMILY
          if player_pokemon.lower() in ['pichu','pikachu','raichu']: 
            print("Choose a move:\n0:Heal\n1:Thunderbolt\n2:Irontail")
            for x in pi_moves:
              if x == "thunderwave":
                print("3:Thunder Wave")
              elif x == "thunderpunch":
                print("4: Thunder Punch")
            attackspeech()
            if player_move in pi_moves:
              if player_move.lower() in ['thunderbolt','t','thunder bolt']:
                print("Thunderbolt!! It took", abs(thunderbolt),"HPs")
                print()
                cpu_health += thunderbolt
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  p_exp += 100
                  coins += 5
                  break
              
              elif player_move.lower() in ['irontail','i','iron tail']:
                print("Irontail!! It took", abs(irontail),"HPs")
                print()
                cpu_health += irontail
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  p_exp += 100
                  wins += 1
                  coins += 5
                  break
              
              elif player_move.lower() in ['thunderwave','thunder wave','tw']:
                print("ThunderWavee!! It took", abs(thunderwave),"HPs")
                print()
                cpu_health += thunderwave
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  p_exp += 100
                  wins += 1
                  coins += 10
                  break

              elif player_move.lower() in ['thunderpunch','tp','thunder punch']:
                print("Thunder Punch! It took",abs(thunderpunch),"HPs")
                print()
                cpu_health += thunderpunch
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  p_exp += 100
                  wins += 1
                  coins += 15
                  break
                  print()
              
              elif player_move.lower() == 'heal' or player_move.lower() == 'h':
                if player_health == 500:
                  print("Your Health is already full")
                else:
                  print(player_pokemon,"is healing")
                  print()
                  player_health += heal
                  if player_health > 500:
                    player_health = 500
            else:
              print(player_pokemon,"can't do that")
              print()
              return main()
          
          elif player_pokemon.lower() in ['bulbasaur','ivysaur','venusaur']: 
            print("Choose a move:\n0:Heal\n1:Vine Whip\n2:Razor Leaf")
            for x in b_moves:
              if x == "solar_beam":
                print("3:Solar Beam")
              elif x == "petal_dance":
                print("4: Petal Dance")
            attackspeech()
            if player_move in b_moves:
              if player_move.lower() == "vine_whip":
                print("Vine Whip!! It took", abs(vine_whip),"HPs")
                print()
                cpu_health += vine_whip
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  b_exp += 100
                  coins += 5
                  break
              
              elif player_move.lower() == "razor_leaf":
                print("Razor Leaf!! It took", abs(razor_leaf),"HPs")
                print()
                cpu_health += razor_leaf
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  b_exp += 100
                  wins += 1
                  coins += 5
                  break
              
              elif player_move.lower() == "solar_beam":
                print("Solar Beam!! It took", abs(solar_beam),"HPs")
                print()
                cpu_health += solar_beam
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  b_exp += 100
                  wins += 1
                  coins += 10
                  break

              elif player_move.lower() == "petal_dance":
                print("Petal Dance! It took",abs(petal_dance),"HPs")
                print()
                cpu_health += petal_dance
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  b_exp += 100
                  wins += 1
                  coins += 15
                  break
                  print()
              
              elif player_move.lower() == 'heal' or player_move.lower() == 'h':
                if player_health == 500:
                  print("Your Health is already full")
                else:
                  print(player_pokemon,"is healing")
                  print()
                  player_health += heal
                  if player_health > 500:
                    player_health = 500
            else:
              print(player_pokemon,"can't do that")
              print()
              return main()

          #USER CHARIZARD FAMILY
          elif player_pokemon.lower() in ['charmander','charmeleon','charizard']:
            print("Choose a move:\n0:Heal\n1:FlameThrower\n2:Rage")
            for x in ch_moves:
              if x == "ember":
                print("3:Ember")
              elif x == "wingattack":
                print("4: Wing Attack")
            attackspeech()
            if player_move.lower() in ch_moves:
              if player_move.lower() == 'flamethrower':
                print("flamethrowerr!! It took", abs(fire),"HPs")
                print()
                cpu_health += fire
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  c_exp += 100
                  wins += 1
                  coins += 5
                  break
              
              elif player_move.lower() == 'rage':
                print("Dragon Ragee!! It took", abs(rage),"HPs")
                cpu_health += rage
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  c_exp += 100
                  wins += 1
                  coins += 5
                  break
              
              elif player_move.lower() == 'ember':
                print("Ember Attack!! It took", abs(ember),"HPs")
                cpu_health += ember
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  c_exp += 100
                  wins += 1
                  coins += 10
                  break
              
              elif player_move.lower() == "wingattack":
                print("Wing Attack!! It took", abs(wingattack),"HPs")
                cpu_health += wingattack
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  c_exp = 100
                  wins += 1
                  coins += 15
                  break

              elif player_move.lower() == 'heal' or player_move.lower() == 'h':
                if player_health == 500:
                  print("Your Health is already full")
                else:
                  print(player_pokemon,"is Healing")
                  print()
                  player_health += heal
                  if player_health > 500:
                    player_health = 500
            
            else:
              print(player_pokemon,"can't do that")
              print()
              return main()
          
          #USER SQUIRTLE
          
          elif player_pokemon.lower() in ["squirtle","wartortle","blastoise"]:
            print("Choose a move:\n0:Heal\n1:Water Gun\n2:Dash")
            for x in sq_moves:
              if x == "bubblebeam":
                print("3:Bubble Beam")
              elif x == "flashcannon":
                print("4: Flash Cannon")
            attackspeech()
            if player_move in sq_moves:    
              if player_move.lower() == 'watergun' or player_move.lower() == 'wg':
                print("WaterGunnn!! It took", abs(watergun),"HPs")
                print()
                cpu_health += watergun
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  s_exp += 100
                  wins += 1
                  coins += 5
                  break
              elif player_move.lower() == 'dash' or player_move.lower() == 'd':
                print("Dash!! It took", abs(dash),"HPs")
                print()
                cpu_health += dash
                if cpu_health < 0:
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  s_exp += 100
                  wins += 1
                  coins += 5
                  break
              
              elif player_move.lower() in ['bubble beam','bb','bubblebeam']:
                print("Bubble Beam!! It took", abs(bubble),"HPs")
                print()
                cpu_health += bubble
                if cpu_health < 0:
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  s_exp += 100
                  wins += 1
                  coins += 10
                  break
           
              elif player_move.lower() in ["flash canon","fc","flashcannon"]:
                print("Flash Canon!! It took", abs(flash),"HPs")
                print()
                cpu_health += flash
                if cpu_health < 0:
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  s_exp += 100
                  wins += 1
                  coins += 15
                  break

              elif player_move.lower() == 'heal' or player_move.lower() == 'h':
                if player_health == 500:
                  print("Your Health is already full")
                else:
                  print(player_pokemon,"is healing")
                  print()
                  player_health += heal
                  if player_health > 500:
                    player_health = 500
            else:
              print("Seriously? You expect {0} to do that?, he can't do much things \n".format(player_pokemon))
              print()
              return main()
          #USER dragonite
          elif player_pokemon.lower() == "dragonite":
            print("Choose a move:\n0:Heal\n1:Thunderbolt\n2:Shock")
            for x in drag_moves:
              if x == "firepunch":
                print("3:Fire Punch")
              #elif x == "flashcannon":
                #print("4: Flash Cannon")
            attackspeech()
            if player_move.lower() in drag_moves:
              if player_move.lower() == 'thunderbolt' or player_move.lower() == 't':
                print("Thunderbolt!! It took", abs(rthunderbolt),"HPs")
                print()
                cpu_health += rthunderbolt
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  r_exp += 100
                  coins += 20
                  break
              elif player_move.lower() in ['firepunch','fire punch','fp']:
                print("Fire Punchhh!! It took", abs(firepunch),"HPs")
                print()
                cpu_health += firepunch
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  r_exp += 100
                  coins += 20
                  break
              elif player_move.lower() == 'shock' or player_move.lower() == 's':
                print("Shock!! It took", abs(shock),"HPs")
                print()
                cpu_health += shock
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  r_exp += 100
                  coins += 20
                  break
              elif player_move.lower() == 'heal' or player_move.lower() == 'h':
                if player_health == 500:
                  print("Your Health is already full")
                  print()
                else:
                  print("Let Me Gather Some Energy")
                  print()
                  player_health += rheal
                  if player_health > 500:
                    player_health = 500
            else:
              print("Dragonite does what he wants, nobody orders him around!")
              return main()
          
          elif player_pokemon.lower() in ['mew','mewtwo']:
            print("Choose a move:\n0:Heal\n1:Confusion\n2:Psychic")
            for x in mew_moves:
              if x == "darkpulse":
                print("3:Dark Pulse")
              #elif x == "flashcannon":
                #print("4: Flash Cannon")
            attackspeech()
            if player_move.lower() in mew_moves:

              if player_move.lower() in ['confusion','cf']:
                print("Enemy pokemon is now confused, it took", abs(conf),"HPs")
                print()
                cpu_health += conf
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  m_exp += 100
                  coins += 20
                  break
              elif player_move.lower() in ['psychic','p']:
                print("Psychic Attack!! It took", abs(mpsychic),"HPs")
                print()
                cpu_health += mpsychic
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  m_exp += 100
                  coins += 20
                  break
              elif player_move.lower() in ['darkpulse','dark pulse','dp']:
                print("Dark Pulse took", abs(darkpulse),"HPs of",cpu_pokemon)
                print()
                cpu_health += darkpulse
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  m_exp += 100
                  coins += 20
                  break
              elif player_move.lower() == 'heal' or player_move.lower() == 'h':
                if player_health == 500:
                  print("Your Health is already full")
                  print()
                else:
                  print("Let Me Gather Some Energy")
                  print()
                  player_health += 50
                  if player_health > 500:
                    player_health = 500
            else:
              print("If you think you are controlling him you are a fool. He is the boss here.")
              print()
              return main()
          elif player_pokemon.lower() == 'onix':
            print("Choose a move:\n1:Double Edge\n2:Rock Slide")
              #elif x == "flashcannon":
                #print("4: Flash Cannon")
            attackspeech()
            if player_move.lower() in onix_moves:

              if player_move.lower() == 'rock_slide':
                print("Rock Slide.., it took", abs(rock_slide),"HPs")
                print()
                cpu_health += rock_slide
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  o_exp += 100
                  coins += 20
                  break
              elif player_move.lower() == 'double_edge':
                print("Double EDGE!! It took", abs(double_edge),"HPs")
                print()
                cpu_health += double_edge
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  o_exp += 100
                  coins += 20
                  break
            else:
              print("If you think you are controlling him you are a fool. He is the boss here.")
              print()
              return main()

          elif player_pokemon.lower() == 'geodude':
            print("Choose a move:\n1:Double Edge\n2:Explosion")
            attackspeech()
            if player_move.lower() in geodude_moves:

              if player_move.lower() == 'explosion':
                print("Explosion.., it took", abs(explosion),"HPs")
                print()
                cpu_health += explosion
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  g_exp += 100
                  coins += 20
                  break
              elif player_move.lower() == 'double_edge':
                print("Double EDGE!! It took", abs(double_edge),"HPs")
                print()
                cpu_health += double_edge
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  g_exp += 100
                  coins += 20
                  break
            else:
              print("If you think you are controlling him you are a fool. He is the boss here.")
              print()
              return main()

          elif player_pokemon.lower() in ['psyduck','golduck']:
            print("Choose a move:\n0:Heal\n1:HydroPump\n2:Seismic Toss")
            for x in psy_moves:
              if x == "psychic":
                print("3:Psychic")
              #elif x == "flashcannon":
                #print("4: Flash Cannon")
            attackspeech()
            if player_move.lower() in psy_moves:

              if player_move.lower() ['hydropump','h','hydro pump']:
                print("HydroPump!! It took", abs(hpump),"HPs")
                print()
                cpu_health += hpump
                player_health -= 3
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  ps_exp += 100
                  coins += 10
                  break
              elif player_move.lower() == 'seismic toss' or player_move.lower() == 'st':
                print("Seismic Toss!! It took", abs(stoss),"HPs")
                print()
                cpu_health += stoss
                player_health -= 3
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  ps_exp += 100
                  coins += 10
                  break
              elif player_move.lower() == 'psychic' or player_move.lower() == 'p':
                print("Psychic !! It took", abs(psychic),"HPs of",cpu_pokemon)
                print()
                cpu_health += psychic
                player_health -= 5
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  ps_exp += 100
                  coins += 15
                  break
              elif player_move.lower() == 'heal' or player_move.lower() == 'h':
                if player_health == 500:
                  print("Your Health is already full")
                else:
                  print(player_pokemon,"is healing")
                  print()
                  player_health += heal
                  if player_health > 500:
                    player_health = 500
            else:
              print("Ummm..., What?")
              print()
              return main()

          elif player_pokemon.lower() == "jigglypuff":
            print("Choose a move:\n0:Heal\n1:Sing\n2:Shadow Ball")
            for x in jig_moves:
              if x == "dream eater":
                print("3:Dream Eater")
              #elif x == "flashcannon":
                #print("4: Flash Cannon")
            attackspeech()
            if player_move.lower() in jig_moves:

              if player_move.lower() == 'sing' or player_move.lower() == 's':
                print("Jiggllypufff jigallyieee!, JigglyPuff's song took",abs(sing),"HPs")
                print()
                cpu_health += sing
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  j_exp += 100
                  coins += 10
                  break
              elif player_move.lower() == 'shadow ball' or player_move.lower() == 'sb':
                print("Shadow Ball!! It took", abs(sball),"HPs")
                print()
                cpu_health += sball
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  j_exp += 100
                  coins += 15
                  break
              elif player_move.lower() == 'dream eater' or player_move.lower() == 'de':
                print("Dream Eater !! It took", abs(deater),"HPs of",cpu_pokemon)
                print("It took 5 HPS of JigglyPuff")
                print()
                cpu_health += psychic
                player_health -= 5
                if cpu_health < 0:
                  cpu_health = 0
                  print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
                  print(trainer[0]+"\'s",cpu_pokemon,"cannot fight anymore, you win")
                  wins += 1
                  j_exp += 100
                  coins += 15
                  break
              elif player_move.lower() == 'heal' or player_move.lower() == 'h':
                if player_health == 500:
                  print("Your Health is already full")
                else:
                  print(player_pokemon,"is healing")
                  print()
                  player_health += heal
                  if player_health > 500:
                    player_health = 500
            else:
              print("Huh? Try Again")
              print()
              return main()

          #CPU's Moves
          print(trainer[0]+"\'s Turn")

          #CPU PICHU
          if cpu_pokemon == 'pichu':
            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(pichu_moves)
              if cpu_move == pichu_moves[0]:
                print("Thunderbolt!! It took", abs(cpu_thunderbolt),"HPs")
                print()
                player_health += cpu_thunderbolt
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == pichu_moves[1]:
                print("Irontail!! It took", abs(cpu_irontail),"HPs")
                print()
                player_health += cpu_irontail
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break

            #CPU PIKACHU
          if cpu_pokemon == 'pikachu':
            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(pika_moves)
              if cpu_move == pika_moves[0]:
                print("Thunderbolt!! It took", abs(cpu_thunderbolt),"HPs")
                print()
                player_health += cpu_thunderbolt
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == pika_moves[1]:
                print("Irontail!! It took", abs(cpu_irontail),"HPs")
                print()
                player_health += cpu_irontail
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == pika_moves[2]:
                print("ThunderWavee!! It took", abs(cpu_thunderwave),"HPs")
                print()
                player_health += cpu_thunderwave
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break

          #CPU RAICHU        
          if cpu_pokemon == 'raichu':
            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(raichu_moves)
              if cpu_move == raichu_moves[0]:
                print("Thunderbolt!! It took", abs(cpu_thunderbolt),"HPs")
                print()
                player_health += cpu_thunderbolt
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == raichu_moves[1]:
                print("Irontail!! It took", abs(cpu_irontail),"HPs")
                print()
                player_health += cpu_irontail
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == raichu_moves[2]:
                print("ThunderWavee!! It took", abs(cpu_thunderwave),"HPs")
                print()
                player_health += cpu_thunderwave
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == raichu_moves[3]:
                print("Thunderpunch!! It took", abs(cpu_thunderpunch),"HPs")
                print()
                player_health += cpu_thunderpunch
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
         
          #CPU charmander
          if cpu_pokemon == 'charmander':
            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(charmander_moves)
              if cpu_move == charmander_moves[0]:
                print("Flamethrowerr!! It took", abs(cpu_fire),"HPs")
                print()
                player_health += cpu_fire
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == charmander_moves[1]:
                print("Dragon Ragee!! It took", abs(cpu_rage),"HPs")
                print()
                player_health += cpu_rage
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break

          #CPU CHARMELEON        
          if cpu_pokemon == 'charmeleon':
            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(charmeleon_moves)
              if cpu_move == charmeleon_moves[0]:
                print("Flamethrowerr!! It took", abs(cpu_fire),"HPs")
                print()
                player_health += cpu_fire
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == charmeleon_moves[1]:
                print("Dragon Ragee!! It took", abs(cpu_rage),"HPs")
                print()
                player_health += cpu_rage
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == charmeleon_moves[2]:
                print("Ember!! It took", abs(cpu_ember),"HPs")
                print()
                player_health += cpu_ember
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break

          #CPU CHARIZARD        
          if cpu_pokemon == 'charizard':

            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(charizard_moves)
              if cpu_move == charizard_moves[0]:
                print("Flamethrowerr!! It took", abs(cpu_fire),"HPs")
                print()
                player_health += cpu_fire
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == charizard_moves[1]:
                print("Dragon Ragee!! It took", abs(cpu_rage),"HPs")
                print()
                player_health += cpu_rage
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == charizard_moves[2]:
                print("Ember!! It took", abs(cpu_ember),"HPs")
                print()
                player_health += cpu_ember
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == charizard_moves[3]:
                print("Wing Attack!! It took", abs(cpu_wing),"HPs")
                print()
                player_health += cpu_wing
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break

          #CPU SQUIRTLE
          if cpu_pokemon == 'squirtle':
            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(sqrt_moves)
              if cpu_move == sqrt_moves[0]:
                print("WaterGunnn!! It took", abs(cpu_watergun),"HPs")
                print()
                player_health += cpu_watergun
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == sqrt_moves[1]:
                print("Dashh!! It took", abs(cpu_dash),"HPs")
                print()
                player_health += cpu_dash
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break

          #CPU WARTORTLE
          if cpu_pokemon == 'wartortle':

            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(wart_moves)
              if cpu_move == wart_moves[0]:
                print("WaterGunnn!! It took", abs(cpu_watergun),"HPs")
                print()
                player_health += cpu_watergun
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == wart_moves[1]:
                print("Dashh!! It took", abs(cpu_dash),"HPs")
                print()
                player_health += cpu_dash
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == wart_moves[2]:
                print("Bubble Beam!! It took", abs(cpu_bubble),"HPs")
                print()
                player_health += cpu_bubble
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break    
          
          #CPU BLASTOISE
          if cpu_pokemon == 'blastoise':

            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(blast_moves)
              if cpu_move == blast_moves[0]:
                print("WaterGunnn!! It took", abs(cpu_watergun),"HPs")
                print()
                player_health += cpu_watergun
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == blast_moves[1]:
                print("Dashh!! It took", abs(cpu_dash),"HPs")
                print()
                player_health += cpu_dash
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == blast_moves[2]:
                print("Bubble Beam!! It took", abs(cpu_bubble),"HPs")
                print()
                player_health += cpu_bubble
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break    
              elif cpu_move == blast_moves[3]:
                print("Flash Canon!! It took", abs(cpu_flash),"HPs")
                print()
                player_health += cpu_flash
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break    

          if cpu_pokemon == 'bulbasaur':
            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(cpu_bulba)
              if cpu_move == cpu_bulba[0]:
                print("Vine Wip!! It took", abs(cpu_vine_whip),"HPs")
                print()
                player_health += cpu_vine_whip
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == cpu_bulba[1]:
                print("Razor Leaf!! It took", abs(razor_leaf),"HPs")
                print()
                player_health += razor_leaf
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break

          #CPU WARTORTLE
          if cpu_pokemon == 'ivysaur':

            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(cpu_ivy)
              if cpu_move == cpu_ivy[0]:
                print("Vine Wip!! It took", abs(cpu_vine_whip),"HPs")
                print()
                player_health += cpu_vine_whip
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == cpu_ivy[1]:
                print("Razor Leaf!! It took", abs(razor_leaf),"HPs")
                print()
                player_health += razor_leaf
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == cpu_ivy[2]:
                print("Solar Beam!! It took", abs(cpu_solar_beam),"HPs")
                print()
                player_health += cpu_solar_beam
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break    
          
          #CPU BLASTOISE
          if cpu_pokemon == 'venusaur':

            if cpu_health <= 40:
              cpu_move = heal
              cpu_health += heal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(cpu_venu)
              if cpu_move == cpu_venu[0]:
                print("Vine Wip!! It took", abs(cpu_vine_whip),"HPs")
                print()
                player_health += cpu_vine_whip
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == cpu_venu[1]:
                print("Razor Leaf!! It took", abs(razor_leaf),"HPs")
                print()
                player_health += razor_leaf
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == cpu_venu[2]:
                print("Solar Beam!! It took", abs(cpu_solar_beam),"HPs")
                print()
                player_health += cpu_solar_beam
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break    
              elif cpu_move == cpu_venu[3]:
                print("Petal Dance!! It took", abs(cpu_petal_dance),"HPs")
                print()
                player_health += cpu_petal_dance
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break    

          #CPU dragonite
          if cpu_pokemon == 'dragonite':
            if cpu_health <= 40:
              cpu_move = rheal
              cpu_health += rheal
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(r_moves)
              if cpu_move == r_moves[0]:
                print("Thunderbolt!! It took", abs(cpu_rthunderbolt),"HPs")
                print()
                player_health += cpu_rthunderbolt
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == r_moves[1]:
                print("Shock!! It took", abs(cpu_shock),"HPs")
                print()
                player_health += shock
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == r_moves[2]:
                print("Shock!! It took", abs(cpu_firepunch),"HPs")
                print()
                player_health += cpu_firepunch
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
        
          if cpu_pokemon == 'onix':  
            cpu_move = choice(cpu_onix)
            if cpu_move == cpu_onix[0]:
              print("Double Edge!! It took", abs(cpu_double_edge),"HPs")
              print()
              player_health += cpu_double_edge
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == cpu_onix[1]:
              print("Rock Slide!! It took", abs(cpu_rock_slide),"HPs")
              print()
              player_health += cpu_rock_slide
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == cpu_mewtwo[2]:
              print("Dark Pulse!! It took", abs(cpu_darkpulse),"HPs")
              print()
              player_health += cpu_darkpulse
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
          if cpu_pokemon == 'geodude':  
            cpu_move = choice(cpu_geodude)
            if cpu_move == cpu_geodude[0]:
              print("Double Edge!! It took", abs(cpu_double_edge),"HPs")
              print()
              player_health += cpu_double_edge
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == cpu_geodude[1]:
              print("Explosion!! It took", abs(cpu_explosion),"HPs")
              print()
              player_health += cpu_explosion
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == cpu_mewtwo[2]:
              print("Dark Pulse!! It took", abs(cpu_darkpulse),"HPs")
              print()
              player_health += cpu_darkpulse
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break

          if cpu_pokemon in ['mew','mewtwo']:  
            cpu_move = choice(cpu_mewtwo)
            if cpu_move == cpu_mewtwo[0]:
              print("Confusion!! It took", abs(cpu_conf),"HPs")
              print()
              player_health += cpu_conf
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == cpu_mewtwo[1]:
              print("Psychic!! It took", abs(cpu_mpsychic),"HPs")
              print()
              player_health += cpu_mpsychic
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == cpu_mewtwo[2]:
              print("Dark Pulse!! It took", abs(cpu_darkpulse),"HPs")
              print()
              player_health += cpu_darkpulse
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
          if cpu_pokemon in ['kadabra','mr. mime']:  
            cpu_move = choice(cpu_kadabra)
            if cpu_move == cpu_kadabra[0]:
              print("PsyBeam!! It took", abs(psybeam),"HPs")
              print()
              player_health += psybeam
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == cpu_kadabra[1]:
              print("Dream Eater!! It took", abs(deater),"HPs")
              print()
              player_health += deater
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == cpu_kadabra[2]:
              print("Psychic Attack!! It took", abs(mpsychic),"HPs")
              print()
              player_health += mpsychic
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == cpu_kadabra[3]:
              print("Hyper Beam!! It took", abs(hyper_beam),"HPs")
              print()
              player_health += hyper_beam
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
          elif cpu_pokemon in ['psyduck','golduck']:  
            cpu_move = choice(cpu_psyduck)
            if cpu_move == cpu_psyduck[0]:
              print("HydroPump!! It took", abs(cpu_hpump),"HPs")
              print()
              player_health += cpu_hpump
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == cpu_psyduck[1]:
              print("Seismic Toss!! It took", abs(cpu_stoss),"HPs")
              print()
              player_health += cpu_stoss
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == cpu_psyduck[3]:
              print("Ice Punch!! It took", abs(cpu_icepunch),"HPs")
              print()
              player_health += cpu_icepunch
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            else:
              print("Psychic!! It took", abs(cpu_psychic),"HPs")
              print()
              player_health += cpu_psychic
              cpu_health -= 5
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break

          elif cpu_pokemon == 'arbok':
            cpu_move = choice(arbok_moves)
            if cpu_move == arbok_moves[0]:
              print("Acid Attack!! It took", abs(acid),"HPs")
              print()
              player_health += acid
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == arbok_moves[1]:
              print("Poison Jab!! It took", abs(poison_jab),"HPs")
              print()
              player_health += poison_jab
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break

          elif cpu_pokemon == 'dustox':
            cpu_move = choice(dustox_moves)
            if cpu_move == dustox_moves[0]:
              print("Gust!! It took", abs(gust),"HPs")
              print()
              player_health += gust
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == dustox_moves[1]:
              print("Psy Beammm!! It took", abs(psybeam),"HPs")
              print()
              player_health += psybeam
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break

          elif cpu_pokemon == 'weezing':
            cpu_move = choice(weezing_moves)
            if cpu_move == weezing_moves[0]:
              print("Poison Gas!! It took", abs(poison_gas),"HPs")
              print()
              player_health += poison_gas
              if player_health <= 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == weezing_moves[1]:
              print("Sludgee!! It took", abs(sludge),"HPs")
              print()
              player_health += sludge
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
          
          elif cpu_pokemon == 'victreebel':
            if cpu_health <= 40:
              cpu_move = leech_life
              cpu_health += leech_life
              player_health -= leech_life
              print(trainer[0],"chose Heal!")
              print()
            else:  
              cpu_move = choice(victreebel_moves)
              if cpu_move == victreebel_moves[0]:
                print("Power Whip!! It took", abs(power_whip),"HPs")
                print()
                player_health += power_whip
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break
              elif cpu_move == victreebel_moves[1]:
                print("Sucker Punch!! It took", abs(sucker_punch),"HPs")
                print()
                player_health += sucker_punch
                if player_health < 0:
                  player_health = 0
                  print("Player's Health:",player_health)
                  print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                  loses += 1
                  break

          elif cpu_pokemon == 'jigglypuff':  
            cpu_move = choice(n_moves)
            if cpu_move == n_moves[0]:
              print("Sing!! It took", abs(sing),"HPs")
              print()
              player_health += sing
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            elif cpu_move == n_moves[1]:
              print("Shadow Ball!! It took", abs(sball),"HPs")
              print()
              player_health += sball
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
            else:
              print("Death Eater!! It took", abs(deater),"HPs")
              print()
              player_health += deater
              cpu_health -= 5
              if player_health < 0:
                player_health = 0
                print("Player's Health:",player_health)
                print(username+"\'s",player_pokemon,"cannot fight anymore,",trainer[0],"wins")
                loses += 1
                break
          print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
          print(username+"'s Health:",player_health)
          print()
          t.sleep(2)
          clear()
          playerinfo()
          print(trainer[0] + "\'s " + cpu_pokemon + "\'s Health:",cpu_health)
          print(username+"'s Health:",player_health)
        gymbadges()
        defaultattacks()
        savedata()
      except KeyboardInterrupt:
          print('Secret Exit :p')  
    main()
    savedata()
    repeat_process = input("Press Enter to continue playing.Type No to quit. \n")
    if repeat_process.lower() in ("no","n"):
      break   
  savedata()

from random import *

heal = randint(20,30)
#USER PICHU/PIKACHU/RAICHU's Attacks
irontail = randint(-30,-29)
thunderbolt = randint(-30,-25)
thunderpunch = randint(-100,-65)
thunderwave = randint(-45,-30)

#CPU PIKACHU/RAICHU's Attacks
cpu_thunderbolt = randint(-28,-25)
cpu_irontail = randint(-35,-20)
cpu_thunderwave = randint(-45,-30)
cpu_thunderpunch = randint(-100,-65)

#CHARMANDER/CHARMELEON/CHARIZARD's Attacks
fire = randint(-35,-25)
rage = randint(-40,-30)
ember = randint(-40,-35)
wing = randint(-100,-65)

cpu_fire = randint(-45,-35)
cpu_rage = randint(-50,-40)
cpu_ember = randint(-100,-65)
cpu_wing = randint(-100,-65)

#Squirtle's Attacks
watergun = randint(-25,-20)
dash = randint(-15,-10)
bubble = randint(-55,-40)
flash = randint(-80,-69)

cpu_watergun = randint(-45,-35)
cpu_dash = randint(-30,-25)
cpu_bubble = randint(-80,-68)
cpu_flash = randint(-80,-69)

#Dragonite's Attacks
rthunderbolt = randint(-50,-30)
shock = randint(-40,-25)
firepunch = randint(-100,-90)
rheal = randint(30,40)

cpu_rthunderbolt = randint(-50,-30)
cpu_shock = randint(-40,-25)
cpu_firepunch = randint(-100,-90)

#MEW/MEWTWO's Attacks
conf = randint(-110,-80)
mpsychic = randint(-120,-80)
darkpulse = randint(-150,-80)

cpu_conf = randint(-40,-30)
cpu_mpsychic = randint(-60,-50)
cpu_darkpulse = randint(-110,-80)

#Psyduck/Goldduck's Attacks
hpump = randint(-35,-20)
stoss = randint(-45,-30) 
psychic = randint(-55,-40)
icepunch = randint(-85,-75)

cpu_hpump = randint(-35,-20)
cpu_stoss = randint(-45,-30) 
cpu_psychic = randint(-55,-40)
cpu_icepunch = randint(-85,-75)

#Jigglypuff's Attacks
sing = randint(-45,-35)
sball = randint(-40,-30)
deater = randint(-55,-40)

#Onix Moves
double_edge = randint(-120,-100)
rock_slide = randint(-90,-70)
#dragon_tail = randint()
cpu_double_edge = randint(-120,-100)
cpu_rock_slide = randint(-90,-70)

#Geodude's Moves
#double edge from onix
explosion = randint(-100,-80)
cpu_explosion = randint(-100,-80)

#Bulbasaur Family
vine_whip = randint(-40,-35)
razor_leaf = randint(-45,-40)
solar_beam = randint(-62,-48)
petal_dance = randint(-90,-75)

cpu_vine_whip = randint(-40,-35)
cpu_razor_leaf = randint(-45,-40)
cpu_solar_beam = randint(-62,-48)
cpu_petal_dance = randint(-90,-75)

#arbok_moves
acid = randint(-40,-30)
poison_jab = randint(-50,-30)

#Dustox Moves
gust = randint(-40,-30)
psybeam = randint(-50,-30)

#VictreeBell Moves
leech_life = randint(40,50)
power_whip = randint(-40,-30)
sucker_punch = randint(-50,-30)

#Weezing Moves
poison_gas = randint(-40,-30)
sludge = randint(-50,-30)

#mrmime
hyper_beam = randint(-120,-70)
#Moves Set

arbok_moves = [acid,poison_jab]
dustox_moves = [gust,psybeam]
victreebel_moves = [power_whip,sucker_punch]
weezing_moves = [poison_gas,sludge] 
cpu_kadabra = [psybeam,deater,mpsychic,hyper_beam]

#CPU MOVES
pichu_moves = [cpu_thunderbolt,cpu_irontail]  #Pichu's Moves
pika_moves =  [cpu_thunderbolt,cpu_irontail,cpu_thunderwave]
raichu_moves = [cpu_thunderbolt,cpu_irontail,cpu_thunderwave,cpu_thunderpunch]

sqrt_moves = [cpu_watergun,cpu_dash]
wart_moves = [cpu_watergun,cpu_dash,cpu_bubble]
blast_moves = [cpu_watergun,cpu_dash,cpu_bubble,cpu_flash]

charmander_moves = [cpu_fire,cpu_rage]
charmeleon_moves = [cpu_fire,cpu_rage,cpu_ember]
charizard_moves = [cpu_fire,cpu_rage,cpu_ember,cpu_wing]

cpu_mew =    [cpu_conf,cpu_psychic,cpu_darkpulse]
cpu_mewtwo = [cpu_conf,cpu_psychic,cpu_darkpulse]
cpu_psyduck = [cpu_hpump,cpu_stoss,cpu_psychic,cpu_icepunch]
cpu_jiggly = [sing,sball,deater]
cpu_onix = [cpu_double_edge,cpu_rock_slide]
cpu_geodude = [cpu_double_edge,cpu_explosion]
cpu_bulba = [cpu_vine_whip,cpu_razor_leaf]
cpu_ivy = [cpu_vine_whip,cpu_razor_leaf,cpu_solar_beam]
cpu_venu = [cpu_vine_whip,cpu_razor_leaf,cpu_solar_beam,cpu_petal_dance]
r_moves = [cpu_rthunderbolt,cpu_shock,cpu_firepunch]    #Raiku's Moves
n_moves = [sing,sball,deater]     #Nikhil's Moves
#
##USER Moves Set
pi_moves = ['irontail','thunderbolt','heal']  #Pikachu's Moves
ch_moves = ['fire','flamethrower','rage','heal']
sq_moves = ['watergun','wg','dash','water gun','d','heal']
drag_moves = ['shock','thunderbolt','heal','i','s','h']  #Pikachu's Moves
mew_moves = ['confusion','psychic','heal']
psy_moves = ['hydropump','seismictoss','heal']
jig_moves = ['sing','shadowball','heal']
onix_moves = ['doubleedge','rockslide','dragontail']
geodude_moves = ['doubleedge','explosion']
b_moves = ['vinewhip','razorleaf','heal']
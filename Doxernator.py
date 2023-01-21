#Import stuff

import random
from time import *

#Variables

fullnames = "Michael Williams","Christopher Allen","Matthew Jones","Joshua Davis","David Garcia","Daniel Rodriguez","James Martinez","Robert Anderson","John Taylor","Joseph Hernandez","Ryan Moore","Nicholas Martin","Anthony Perez","Jonathan Lee","William Thompson","Kevin Harris","Adam Young","Eric King","Brian Wright","Justin Scott","Benjamin Green","Jacob Baker","Andrew Adams","Aaron Nelson","Brandon Carter","Samuel Mitchell","Nathan Perez","Kyle Roberts","Tyler Turner","Zachary Phillips","Alexander Campbell","Christopher Parker","Patrick Evans","Cody Edwards","Brandon Turner","Jacob Stewart","Matthew Sanchez","Joseph Morris","Daniel Rogers","Adam Reed","James Cook","Robert Bailey","Alexander Bell","Benjamin Cooper","Michael Richardson","Nicholas Cox","William Howard","Christopher Ward","Anthony Torres","David Peterson","Eric Gray","Jonathan Ramirez","Ryan James","Kevin Watson","Justin Brooks","Brian Kelly","Samuel Sanders","Nathan Price","Kyle Bennett","Tyler Wood","Zachary Barnes","Andrew Ross","Aaron Henderson"
adresses = "1234 Elm Street", "567 Oak Avenue", "891 Birch Road", "123 Maple Lane", "456 Pine Street", "789 Cedar Boulevard", "321 Oakwood Drive", "654 Elmwood Avenue", "987 Oakwood Court", "246 Pine Road", "369 Cedar Lane", "159 Elm Avenue", "753 Oak Boulevard", "964 Birch Street", "357 Maple Drive", "654 Pine Avenue", "246 Cedar Road", "369 Oak Lane", "159 Elmwood Boulevard", "753 Birchwood Drive", "964 Maplewood Avenue", "357 Pinewood Court", "654 Cedarwood Lane", "246 Oakwood Boulevard", "369 Elmwood Drive", "159 Maplewood Avenue", "753 Pinewood Court", "964 Cedarwood Lane", "357 Oakwood Boulevard", "654 Elmwood Drive", "246 Birchwood Avenue", "369 Maplewood Court", "159 Pinewood Lane", "753 Cedarwood Boulevard", "964 Oakwood Drive", "357 Elmwood Avenue", "654 Birchwood Court", "246 Maplewood Lane", "369 Pinewood Boulevard", "159 Cedarwood Drive", "753 Oakwood Avenue", "964 Elmwood Court", "357 Birchwood Lane", "654 Maplewood Boulevard", "246 Pinewood Drive", "369 Cedarwood Avenue", "159 Oakwood Court", "753 Elmwood Lane", "964 Birchwood Boulevard", "357 Maplewood Drive", "654 Pinewood Avenue", "246 Cedarwood Court", "369 Oakwood Lane", "159 Elmwood Boulevard", "753 Birchwood Drive", "964 Maplewood Avenue", "357 Pinewood Court", "654 Cedarwood Lane", "246 Oakwood Boulevard", "369 Elmwood Drive", "159 Maplewood Avenue", "753 Pinewood Court", "964 Cedarwood Lane", "357 Oakwood Boulevard", "654 Elmwood Drive", "246 Birchwood Avenue", "369 Maplewood Court", "159 Pinewood Lane", "753 Cedarwood Boulevard", "964 Oakwood Drive", "357 Elmwood Avenue", "654 Birchwood Court", "246 Maplewood Lane", "369 Pinewood Boulevard"
age = random.choice(['14', '15', '16', '17',  '18', '19', '20', '21', '22', '23', '24', '25'])
breaachedpass = "dfhf7634!!2", "qwertz663df!2", "jsdf90-jfew84-!@#$%(", "ilovecox63@", "iloveandrew854@@", "patrickiscool34!@", "imretarded894!@", "literaturesuck69!!!", "password321!" "paternitycourt33!", "tiktokiscring69420!", "follow@wheatelyontiktok", "epicpassword!3" "5352b!", "JackSucksAtLifeSucks!!11111", "random948(#*", "nword42!" "hotmail>protonmail69420", "imfunny696969", "travisscott", "dougrattman1", "ricklepick"

name = random.choice(fullnames)
addy = random.choice(adresses)
breach = random.choice(breaachedpass)
#Intro sequence

print("    _____-----=====     D          O          X          E          R          N          A          T          O         R     =====-----_____")
print("Made by WheatelyTech. github.com/Wheately")
print("__--==Welcome to the Doxernator! This makes doxxes of people just by their alias! This program is very hard to make, so please favorite it on GitHub!!111==--__")
sleep(3)
print("Doxernator is starting up...")
print(".")
print()
sleep(0.3)
print("..")
print()
sleep(0.3)
print("...")
print()
sleep(1)
alias = input("Enter the alias of the person you want doxxed:\n")
print("Doxernator is getting info on the alias specified...")
sleep(5.5)
seedox = input("Would you like to see the dox? (y/n)\n")



if seedox == "y":
    print()
    print()
    print()
    print("L                    B          O         Z         O.  Doxxed by Doxinator.")
    print()
    print()
    print()
    print("Full name:" + name)
    print("Address:" + addy)
    print("Main Password:" + breach)
    print("Age:" + age)
    input("Press enter to quit.\n")
    quit()
else:
    print("The dox for " + alias  + "has now been destroyed forever. :d")
    input("Press enter to quit.\n")
    quit
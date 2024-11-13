#Conditional statements
#using comparison operators to compare and check the conditions(<,>,==,>=,<=)
#Nested If/else
#logical operators (and,or,not)
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?\n"))
bill=0
if height>120:
    print("You can ride the rollercoaster")
    age=int(input("enter your age:\n"))
    if age<12:
        bill=5
        print("child tickets are $5")
    elif age<18:
        bill=7
        print("youth tickets are $7")
    elif 45 <= age <= 55:
        print("the tickets are free for you")
    else:
        bill=12
        print("adults tickets are $12")
    wants_photo=input("enter yes if you want pic else enter no\n").lower()
    if wants_photo=="yes":
        bill+=3
    print(f"your bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
#Odd or Even
num=int(input("enter any number to check even or odd:\n"))
if num%2==0:
    print(f"{num} is a even number\n")
else:
    print(f"{num} is a odd number")
#pizza delivering
print("Welcome to python pizza deliveries")
size=input("What size pizza do you want? s, m or l?\n").lower()
pepperoni=input("Do you want pepperoni on your pizza? yes or no?\n").lower()
extra_cheese=input("Do you want extra cheese? yes or no?\n").lower()
pizza_bill=0
if extra_cheese=="yes":
    pizza_bill+=1
if size=="s":
    pizza_bill+=15
    if pepperoni == "yes":
        pizza_bill +=2
elif size=="m":
    pizza_bill+=20
    if pepperoni == "yes":
        pizza_bill +=3
else:
    pizza_bill+=25
    if pepperoni == "yes":
        pizza_bill +=3
print(f"here is your total bill ${pizza_bill}")
#Day3 Project
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to treasure Island!")
to_go=input("Youre at a cross road.Where do you want to go?\n type left or right\n").lower()
if to_go=="left":
    print("you've come to a lake. There is an island in the middle of the lake.")
    s_w=input("type 'wait' to wait for a boat or type 'swim' to swim across\n").lower()
    if s_w=="wait":
        print("you arrived at the island unharmed.\nThere is a house with 3 doors.One red,one yellow,one blue.")
        door=input("which color door you choose?\n").lower()
        if door=="red":
            print("you've caught fire and died\n************ game over ************")
        elif door=="blue":
            print("you've died due to poison gas\n************ game over ************")
        else:
            print("Bro is Kratos\n************ you won ************")
    else:
        print("you were eaten by a shark\n************ game over ************")
else:
    print("you've fell into a hole\n************ game over ************")

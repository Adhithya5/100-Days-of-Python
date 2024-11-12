#Data types (string)
print("anything that is inside '' or "" is string")
#Data types (integers)
print(500*50000)
print(123_456)
#Data types (float)
print(3.14159)
#Data types (bool)
print(True)
print(False)
#indexing
print("hello"[-1]) #negative indexing
print("hello"[0:5]) #positive indexing
#checking the data type?
print(type(123_456))
print(type("123_456"))
print(type(123.456))
print(type(True))
#Type casting
print(len(str(123)))
print(int("123")+int("857"))
##
name=input("enter your name\n")
lenght=len(name)
print("Number of letters in your name is: "+str(lenght))
##
#Mathematical operations (+,-,*,/,//)
print(10+10)
print(298-45)
print(756%7)
print(20/8)
print(53//3)# (//) indicates that the output should be in round value
print(2**3)# (**) indicates power it means 2 to the power of 3
##
#PEMDASLR (Paranthesis(),Exponents **,Multiplication *,Division /,Addition +,Subtraction -,Left to Right)
print(3*(3+3)/3-3)
#BMI calculator
weight = 84
height=1.920
bmi=weight/height**2
print(round(bmi,2))
#Number manipulation
score=0
score+=2
score*=50
print(score)
#f strings
print(f"The score is {score},your height is {height},your weight is {weight},You are going to winning!!!")
#Project tip Calculator
print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?\n$"))
tip=int(input("How much tip would you like to give? 10, 12,or 15?\n"))
tip_per=tip/100*bill+bill
people=int(input("How many people to split the bill?\n"))
to_pay=round(tip_per/people,2)
print(f"Each person should pay: ${to_pay}")




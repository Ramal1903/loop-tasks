# Q1

i=10
while i>0:
    print(i)
    i -= 1
print("Liftoff!")

#Q2

adult=0
child=0
for i in range(5):
    visitorAge=int(input("Age of visitor" + str(i+1) + ":"))
    if visitorAge<18:
        child=child+1
    elif visitorAge>=18:
        adult+=1
print("Child tickets: ", child)
print("Adult tickests: ", adult)

#Q3

# 1 3 5 7 9

#Q4

sum=0
for i in range(5):
    price=float(input("Price of item" + str(i+1) + ":"))
    sum=sum+price
average=sum/5
print("Total:", sum)
print("Average:", average)

#Q5

i=0
while i==0:
    password=input("New password:")
    if len(password)==8:
        i=1
    else:
        print("Too short, try again")
print("Password accepted")

#Q6

# 70
# 40
# 10
# -20
# Done

#Q7

totalSteps=0
for i in range(7):
    totalSteps=totalSteps+1200
    print('Day', i+1, ":", totalSteps)

#Q8

attempt=0
theUsername="admin"
thePassword="1234"
while attempt<3:
    username=input("Username:")
    password=input("Password:")
    attempt+=1
    if username==theUsername and password==thePassword:
        print("Welcome!")
        break
    else:
        print("Wrong username or password")
if attempt==3:
    print("Account locked")

#Q9

balance=500
while balance>0:
    amount=int(input("Amount: "))
    if amount>balance:
        print("Insufficient funds")
    elif amount<0:
        print("Invalid amount")
    else:
        balance=balance-amount
        print("Balance:", balance)
print("Goodbye")

#Q10

# PIN: 1111
# Wrong PIN, 2 attempts left
# PIN: 2222
# Wrong PIN, 1 attempts left
# PIN: 1234
# Access granted
# Attempts used: 3

#Q11

grade=0
max=0
passed=0
failed=0
sum=0
numberOfStudents=0
while grade != -1:
    grade=int(input("Grade:"))
    if grade>0:
        sum=sum+grade
        if grade>50:
            passed+=1
        else:
            failed+=1
        if grade>max:
            max=grade
        numberOfStudents+=1
print("Passed:", passed)
print("Failed:", failed)
print("Highest:", max)
print("Average:", sum/numberOfStudents)

#Q12

freeSpaces=20
command=""
while command!="stop":
    command=input("Command: ")
    if command!="stop":
        if command=="in" and freeSpaces!=0:
            freeSpaces-=1
            print(freeSpaces)
        elif command=="in" and freeSpaces==0:
            print("Garage is full")
        elif command=="out" and freeSpaces!=20:
            freeSpaces+=1
            print(freeSpaces)
        elif command=="out" and freeSpaces==20:
            print("Garage is empty")
        if command!="in" and command!="out":
            print("Unknown command")

#Q13

max=-100000000
hotDays=0
hottest=0
for i in range(7):
    temperature=int(input("Day " + str(i+1) + ": "))
    if temperature>30:
        hotDays+=1
    if max<temperature:
        max=temperature
        hottest=i+1
print("Hot days:", hotDays)
print("Hottest day:", hottest)

#Q14

# "attempt=0" have to be outside of the "while" loop,because while the loop is repeating attempt becomes zero.
# This is the true version:
# password = "secret" 
# attempts = 0
# while True:          
#     entered = input("Password: ")
#     if entered == password:         
#         print("Welcome")         
#         break     
#     attempts += 1     
#     if attempts == 3:         
#         print("Account locked")         
#         break 

#Q15
i=0
while i==0:
    password=input("Password: ")
    if len(password)>=8:
        digit=0
        upper=0
        lower=0
        for j in range(len(password)):
            if password[j].isdigit():
                digit+=1
            elif password[j].islower():
                lower+=1 
            elif password[j].isupper():
                upper+=1 
        if upper!=0 and lower!=0 and digit!=0:
            print("Strong password")
            i=1
        elif upper==0:
            print("Weak password: no uppercase letters")
        elif lower==0:
            print("Weak password: no lowercase letters")
        elif digit==0:
            print("Weak password: no digits")
    else:
        print("Weak password: length have to be at least 8")

#Q16

saving=50
month=1
print("Month", month, ":", saving)
while saving<1000:
    increase=50+month*10
    saving+=increase
    month+=1
    print("Month", month, ":", saving)
print("Goal reached in month", month)

#Q17

# program will print 105.Break is for the first number which is satisfying a condition.

#Q18

thePin="2580"
balance=1000
attempt=0
while attempt<3:
    pin=input("Enter the pin: ")
    if pin==thePin:
        break
    attempt+=1
if attempt<3:
    menu=""
    while menu!="4":
        menu=input("Choose the option (1 - Check balance 2 - Deposit 3 - Withdraw 4 - Exit): ")
        match menu:
            case "1":
                print(balance)
            case "2":
                amount=int(input("Enter the amount you want to add: "))
                if amount>0:
                    balance=balance+amount
            case "3":
                withdrawal=int(input("Enter the amount you want to withdraw: "))
                if withdrawal>0 and withdrawal<balance:
                    balance=balance-withdrawal
            case "4":
                continue
            case _:
                print("Invalid choice")
    print("Goodbye")
else:
    print("Card blocked")

#Q19

water=1.5
total=0
while total<1.5:
    cash=float(input("Insert coin: "))
    if cash==0.05 or cash==0.1 or cash==0.2 or cash==0.5 or cash==1:
        total=total+cash
        print("Total:", total)
    else:
        print("Coin not accepted")
print("Here is your water")
print("Change:", round(total-water, 2))

#Q20

total=0
for i in range(2,101):
    divisor=0
    for j in range(2,101):
        if i%j==0:
            divisor+=1
    if divisor==1:
        print(i, end=" ")
        total+=1
print()
print("Total codes:", total)

#Q21

# 101 102
# 201 202
# 301 302

#Q22

for floor in range(1, 6):
    if floor!=4:
        print("Floor" + str(floor) + ": ", end=" ")
        for room in range(1, 5): 
            print(floor * 100 + room, end=" ") 
        print() 

#Q23

minutes=480
customer=1
while minutes>0:
    neededTime=int(input("Customer " + str(customer) + " needs (min): "))
    if neededTime<=minutes:
        minutes=minutes-neededTime
        customer+=1
    else:
        print("Sorry, come back tomorrow")
        break
print("Customers served:", customer-1)
print("Minutes left:", minutes)

#Q24

vote=""
numberOfA=0
numberOfB=0
numberOfC=0
spoiled=0
while vote!="end":
    vote=input("Vote: ")
    match vote:
        case "A":
            numberOfA+=1
        case "B":
            numberOfB+=1
        case "C":
            numberOfC+=1
        case "end":
            continue
        case _:
            spoiled+=1
if numberOfA>numberOfB and numberOfA>numberOfC:
    winner="A"
elif numberOfB>numberOfA and numberOfB>numberOfC:
    winner="B"
elif numberOfC>numberOfA and numberOfC>numberOfB:
    winner="C"
else:
    winner="Tie"
print("A:", numberOfA, "B:", numberOfB, "C:", numberOfC)
print("Spoiled:", spoiled)
print("Winner:", winner)

#Q25

cardNumber=input("Enter the card number: ")
if len(cardNumber)==16:
    sum=0
    for j in range(len(cardNumber)):
        for i in range(2,len(cardNumber)//2,2):
            if int(cardNumber[len(cardNumber)-i])*2>9:
                cardNumber[len(cardNumber)-i]=9-cardNumber[len(cardNumber)-i]
        
else:
    print("Must be 16 digits")
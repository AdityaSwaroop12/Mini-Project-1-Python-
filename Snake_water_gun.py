import random
'''
-1 for gun
0 for snake
1 for water
'''
x = 0
y = 0
print(''' Rules of the game :
      1) It's  a 10 round Snake, water, gun game
      2) No chance for a takeback so chose wisely !
      3) You will play against Computer (both the opponents)
      4) Your score will be displayed at the end of the 10 rounds

      ''')
name1 = input("Enter the name of opponent 1 : ")
name2 = input("Enter the name of opponent 2 : ")
print (f"Since, {name1} is the first opponent, GET READY for the game AND CHOOSE WISELY as {name2} is an equally strong opponent")
i1 = int(input("If you are ready click 1 else 0 :- "))
if(i1 == 1):
    print("Cool let's begin :- ")
    for i1 in range(1,11):
        comp1 = random.choice([-1, 0, 1])
        you1 = input("Enter your choice as s/w/g : ")
        youDict11 = {"s" : 0 , "w" : 1, "g" : -1}
        younum1 = youDict11[you1]
        youDict12 = {0 : "snake", 1 : "water", -1 : "gun"}
        reverseDict1  = {"g" : "gun", "s" : "snake", "w" : "water"}

        print(f"You chose : {reverseDict1[you1]}\ncomputer chose : {youDict12[comp1]} ")
        # nested if-else statement or try observing a pattern for lines reduction
        if (comp1 == younum1):
            print("It's a draw")
            x += 0.5

        else:
            if(comp1 == 1 and younum1 == 0):
                print("You win !")
                x += 1
            elif(comp1 == 1 and younum1 == -1):
                print("You lose !")
            elif(comp1 == 0 and younum1 == 1):
                print("You lose !")
            elif(comp1 == 0 and younum1 == -1):
                print("You win !")
                x += 1
            elif(comp1 == -1 and younum1 == 1):
                print("You win !")
                x += 1
            elif(comp1 == -1 and younum1 == 0):
                print("You lose !")
            else:
                print("Something Went Wrong !")
    
else:
    print("Game terminated by you")

print(f"Your Score : {x}/10")

print(f"What are you waiting for, {name2}? It's your turn now, CHOOSE WISELY as {name1} is an equally strong opponent !")
i2 = int(input("If you are ready click 1 else 0 :- "))
if(i2 == 1):
    print("Cool let's begin :- ")
    for i2 in range(1,11):
        comp2 = random.choice([-1, 0, 1])
        you2 = input("Enter your choice as s/w/g : ")
        youDict21 = {"s" : 0 , "w" : 1, "g" : -1}
        younum2 = youDict21[you2]
        youDict22 = {0 : "snake", 1 : "water", -1 : "gun"}
        reverseDict2  = {"g" : "gun", "s" : "snake", "w" : "water"}

        print(f"You chose : {reverseDict2[you2]}\ncomputer chose : {youDict22[comp2]} ")
        # nested if-else statement
        if (comp2 == younum2):
            print("It's a draw")
            y += 0.5

        else:
            if(comp2 == 1 and younum2 == 0):
                print("You win !")
                y += 1
            elif(comp2 == 1 and younum2 == -1):
                print("You lose !")
            elif(comp2 == 0 and younum2 == 1):
                print("You lose !")
            elif(comp2 == 0 and younum2 == -1):
                print("You win !")
                y += 1
            elif(comp2 == -1 and younum2 == 1):
                print("You win !")
                y += 1
            elif(comp2 == -1 and younum2 == 0):
                print("You lose !")
            else:
                print("Something Went Wrong !")
    
else:
    print("Game terminated by you")

print(f"Your Score : {y}/10")

if(x>y):
    print(f"{name1} defeated {name2} by {x-y} scores and won the match")
    print(f"Well done {name1} but Don't lose hope {name2}, Better game next time")
elif(x == y):
    print("Match is draw ")
    print(f"Wow! {name1} and {name2}, you two are equally good at this")
else:
    print(f"{name2} defeated {name1} by {y-x} scores and won the match")
    print(f"Well done {name2} but Don't lose hope {name1}, Better game next time")
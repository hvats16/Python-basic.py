import random
lst=['s','w','g']
print("\t\t\t\t Snake water and gun game\t\t\t\t")
print("Enter s for snake \n Enter g for Gun \n Enter w for Water")
chances = 10
no_of_chances = 0
comp_wins = 0
human_wins = 0

while no_of_chances < chances:
    _input=input("Enter you Snake Water or Gun")
    _random = random.choice(lst)
    
    if _input == _random:
        print("Game is tie both tha computer and human have the same choice")
        
    #if the user enter the s
    
    elif _input == 's' and _random == 'g':
        print("computer wins")
        comp_wins+=1
        
    elif _input == 's' and _random == 'w':
        print("Human wins")
        human_wins+=1
        
    #if user enter w 
    elif _input == 'w' and _random =='s':
        print("Computer wins")
        comp_wins+=1
        
    elif _input == 'w' and _random == 'g':
        print("Human wins")
        human_wins+=1
        
    #if user enter g
    
    elif _input == 'g' and _random == 's':
        print("Human wins")
        human_wins+=1
        
    elif _input == 'g' and _random == 'w':
        print("Computer wins")
        human_wins+=1
        
    else:
        print("You have entered the wrong choice")
        
    no_of_chances+=1
    print("Chance remaining" ,chances-no_of_chances)
    
    
    
    
print("Human score", human_wins)
print("Computer Score", comp_wins)

if human_wins > comp_wins:
    print("Human Wins")
else:
    print("Computer wins")
    
    
print("\t\t\t\t Game Over \t\t\t\t")
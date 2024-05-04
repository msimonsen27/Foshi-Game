import random

import os.path

gameOver = False
lifePoints = 7
lifePoints <= 7 
currentRoom = 1
numSides = 0
roll = 0
libraryChoice = 0
emptyRoomChoice= 0
wellRoomChoice = 0
foundScroll = 0
monsterLP = 7
path = ''
hit = 0
critHit = 0
miss = 0
critMiss = 0
foshiChoice = 0
success = 'Success'
result = ''
libraryValidChoices = 0
libraryChoice2 = 0
monsterChoice = 0
healthScroll = 12


def diceRoll (numSides, function, success):
   roll = random.randint(1, numSides)
   result = ''

   if function == 'attack':
        if roll == 1:
            result = 'Critical Fail'
        elif roll == 20:
            result = 'Critical Hit'
        elif roll >= 12:
            result = 'Hit'
        else:
            result = 'Miss'

   elif function == 'check':
        if roll >= success:
            result = 'Success'
        else:
            result = 'Fail'

   return roll, result


print ('Roll: ', roll)
print ('Result: ', result)

def readIfExists(filepath):
    check_exists = os.path.isfile(filepath)
    if check_exists:
        f = open(filepath, 'r')
        print(f.read())
        f.close()
    else:
        print('The file does not exist')
        
if healthScroll == 0:
    print('You have used up the health scroll already. You cannot use it anymore.')
    
#Intro
intro = open('foshi/0_intro.txt')
readIfExists('foshi/0_intro.txt')

#Room 1
currentRoom = 1
library = open('foshi/1_library.txt')
readIfExists('foshi/1_library.txt')
print('Options: 1) Search the room 2) Go through the West Door 3) Go through the North Door 4) Go down the stairs')

libraryValidChoices = [1, 2, 3, 4]
while gameOver == False:


    libraryChoice = input('Make your choice:')
    libraryChoice = int(libraryChoice)
    
    if libraryChoice == 1:
        libraryChoice = input('Make your choice:')
        libraryChoice = int(libraryChoice)
        if currentRoom == 1 and foundScroll == 1:
                print('You have already searched this room.')
        else:
            print('You are in the Library. You will now roll a 20 sided die to complete a perception check to search the room.')
            print('------------')
            roll, result = diceRoll(20, 'check', 12)
                
            print(roll, result)
                
            if result == success:
                foundScroll == 1
                print('You have collected a health scroll! You can now either 2) Go through the West Door, 3) Go through the North Door, or 4) Go down the Stairs')
                
                if libraryChoice2 == 1:
                    print('Please input a valid option to continue playing.')
                        
                    if libraryChoice2 == 2:
                        currentRoom = 2
                    if libraryChoice2 == 3:
                        currentRoom == 3
                else:
                    currentRoom == 4
                    
            else:
                print('You found nothing this time, you can either 1) Continue to search the library 2) Go through the West Door 3) Go through the North Door or 4) Go down the stairs')
                print('------------')
                
                
            #TODO: Logic for finding scroll - Can't find scroll multiple times
        
        #TODO: Workshop
    elif libraryChoice == 2:
        currentRoom = 2
        if currentRoom == 2:
            print ('You chose to go through the west door and you have entered the workshop.')
            print('------------')
            currentRoom = 2
            workshop = open('foshi/2_workshop.txt')
            readIfExists('foshi/2_workshop.txt')
            print('------------')
            print('Roll a 20 sided die to search the workshop.')
            roll, result = diceRoll(20,'', 0)
            print(roll, result)
            print('------------')
            print('When you searched the workshop, you collected some gold and a dagger! You then returned to the library.')
            currentRoom = 1
            print('------------')
            
            if foundScroll == 0:
                print('1) Search the room 2) Go through the West Door 3) Go through the North Door 4) Go down the stairs')
            else:
                print('Since you have already found the health scroll, you can 2) Go through the West Door, 3) Go through the North Door, or 4) Go down the stairs')
               
    
        #TODO: Empty Room
    elif libraryChoice == 3:
            print ('You chose to go through the north door and entered the Empty Room.')
            currentRoom = 3
            print('------------')
            
    if currentRoom == 3:
            emptyRoom = open('foshi/3_empty.txt')
            readIfExists('foshi/3_empty.txt')
            print('------------')
            
            emptyRoomChoice = input('You can either 1) Go back to the library, 2) Continue to search the room or 3) Go through the West Door')
            emptyRoomChoice = int(emptyRoomChoice)
            
            if emptyRoomChoice == 1:
                print('You chose to go back to the library.')
            if emptyRoomChoice == 2:
                print('------------')
                print('You chose to search the room and fell into Xayah\'s trap! Roll the 6 sided die to find out your fate!')
                roll, result = diceRoll(6, '', 0)
                lifePoints = lifePoints - roll
                print('------------')
                print('You rolled a', roll, result,'and therefore you have lost', roll, result,'life points.')
                
                if lifePoints == 0:
                    gameOver = True
                    print('You have lost all of your life points because you fell into Xayah\'s trap. The game is now over. Press 1) to Restart.')
                
                wellRoomChoice = input('You have three options. You can either 1) Return to the library, 2) Go through the West Door, or 3) Heal yourself IF you have the health scroll')
                wellRoomChoice = int(wellRoomChoice)
                if wellRoomChoice == 1:
                    currentRoom = 1
                    if wellRoomChoice == 2:
                        currentRoom = 4
                        print('You have chosen to go through the West Door and as you enter the Well Room, the door locks behind you.')
                        print('------------')
                        wellRoom = open('foshi/4_well.txt')
                        readIfExists('foshi/4_well.txt')
                        
                        foshiChoice = input('You have three options. You can either 1) attack Foshi, 2) You can do an intelligence check with a 20 sided die roll, or 3) You can attempt to solve Foshi\'s riddle.')
                        foshiChoice = int(foshiChoice)
                        
                        if foshiChoice == 1:
                            roll, result = diceRoll(20, '', 0)
                            print('You missed Foshi and have dealt no damage to him. ')
                            
                        if foshiChoice == 2: 
                            roll, result = diceRoll(20, 'check', 18)
                            if result == success:
                                print('You rolled a', roll, result, '. Foshi appears to flicker on the walls and his image disappears and reappears on the wall. You now know that Foshi is an illusion.')
                            else:
                                print('You rolled a', roll, result, 'Foshi laughs and insults you as your intelligence check fails.')
                                
                    if foshiChoice == 3:
                            riddleAnswer = input('What is the answer to Foshi\'s riddle?')
                            print(riddleAnswer)
                        
                    riddleAnswer = riddleAnswer.lower()
                    riddleAnswer = input('What is the answer to Foshi\'s riddle?: ')
                    print(riddleAnswer)
                            
                    if riddleAnswer == 'tomorrow':
                        gameOver = True
                        print('Congratulations! You have defeated Foshi and you are now able to escape Xayah\'s tower!')
                    else:
                        print('You were not able to answer the riddle correctly. A trapdoor opens and you fall through.')
                        lifePoints - 7
                        print('You have lost all of your life points. Restart the game and try again!')
                        gameOver = True
                        
                            
                        
                        
            if emptyRoomChoice == 3:
                print('You have chosen to go through the West Door and as you enter the Well Room, the door locks behind you.')
                currentRoom = 4
                foshi = open('foshi/5_foshi.txt')
                readIfExists('foshi/5_foshi.txt')
            
                        #Well Room - Final boss (Foshi)
                if wellRoomChoice == 3:
                    if foundScroll == 1:
                        print('You have used your health scroll. You are now at', lifePoints + 4, 'life points.')
                        healthScroll - 4
                        print('------------')
                        print('You can either 1) Return to the library or 2) Continue to heal yourself, or 3) Go through the West Door')
                    else:
                        print('You have not collected the health scroll. You can either 1) Return to the library, or 3) Go through the West Door ')
                
        
            
    elif libraryChoice == 4:
        currentRoom = 4
        
        if currentRoom == 4:
            print('You chose to go down the stairs and have entered the Cellar.')
            print('As you enter the cellar,the door slams shut behind you. You hear a low growl, and Xayah\'s guard dog appears before you. It appears your only way out, is to fight.')
            print('------------')
            print('You will roll a 20 sided attack die to battle him. You are currently at', lifePoints, 'life points. Xayah\'s guard dog is currently at 7 life points.')
            
            if lifePoints and monsterLP != 0:
                roll, result = diceRoll(20, 'attack', 12)
                print(roll, result)
                
                while lifePoints and monsterLP != 0:
                    diceRoll (20, 'attack', 12)
                    print(roll, result)
                    
                    if (roll, result) == hit:
                        monsterLP = monsterLP - 1
                        print('You are at', lifePoints, 'life points. Xayah\'s guard dog is currently at', monsterLP, 'life points.')
                
                    elif (roll, result) == critHit:
                        monsterLP = monsterLP - 3
                        print('You are at', lifePoints, 'life points. Xayah\'s guard dog is currently at', monsterLP, 'life points.')
                    
                    elif (roll, result) == miss:
                        lifePoints = lifePoints - 1
                        print('You are at', lifePoints, 'life points. Xayah\'s guard dog is currently at', monsterLP, 'life points.')
                
                    elif (roll, result) == critMiss:
                        lifePoints = lifePoints - 3
                        print('You are at', lifePoints, 'life points. Xayah\'s guard dog is currently at', monsterLP, 'life points.')
                        
                else:
                    lifePoints or monsterLP == 0
                    
                    if lifePoints == 0:
                        gameOver = True
                        print('You have lost all of your life points in your battle against Xayah\'s guard dog. Restart the game to play again.' )
                        
                    if monsterLP == 0:
                        print('Congratulations! You have defeated the guard dog! He leaves you with one final message before you depart.')
                        print('------------')
                        print('Always remember: Yesterday is history, tomorrow is THE mystery, and today is a gift. That\'s why we call it the present.')
                    
            monsterChoice = input('You can either 1) Return to the library, or 2) Use the health scroll if you have it.')
            if monsterChoice == 1:
                currentRoom = 1
                
            if monsterChoice == 2 and foundScroll == 0:
                print('You do not have the health scroll yet. Please find it before you try to use it.')
                
            if monsterChoice == 2 and foundScroll == 1:
                print('You have used your health scroll. You are now at', lifePoints + 4, 'life points.')
                healthScroll = healthScroll - 4
                
else:
    gameOver = True
    print('The game is over. Would you like to restart?')
      

#TODO
#Error Messages for incorrect input - else statement to catch invalid input
#tomorrow, Tomorrow, TOMORROW
#Completely Connect Rooms
#Enhancement?



import random
l=["rock","scissor","paper"]
'''

rock vs paper -> paper wins
rock vs scissor ->rock wins
paper vs scissor ->scissor wins.

'''
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start.....
1 Yes
2 No | Exit

        '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1 rock
2 scissor
3 paper

            '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("Game Draw")
                ucount+=1
                ccount+=1
            elif(uchoice=="rock" and Cchoice=="scissor") or(uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("You win")
                ucount+=1
            else:
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("Computer win")
                ccount+=1
        if ucount==ccount:
            print("Final Game Draw....")
            print("user score",ucount)
            print("computer score",ccount)
        elif ucount>ccount:
            print("Final You win the Game....")
            print("user score",ucount)
            print("computer score",ccount)
        else:
            print("Final computer win the Game....")
            print("user score",ucount)
            print("computer score",ccount)

                
    else:
        break





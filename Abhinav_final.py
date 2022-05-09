'''This is a maths game with four different operations'''

'''PREREQUISITES:
  -A text file named game__name
  -A text file named game__score with 0 written in it'''


import random

def ask():
    game=input('\nWhich game you want to play.\n\nif you want to quit, enter "stop"\n\nAdding numbers[A]/ Multiplying numbers[M]/ Subtracting numbers[S]/ Dividing numbers[D]: ')
    if game.upper()=='A':
        Sum()
    elif game.upper()=='M':
        Multiply()
    elif game.upper()=='S':
        Subtraction()   
    elif game.upper()=='D':
        Division()
    elif game.lower()=='stop':
        print('You are now leaving the game')
        exit(0)

def intro():
    firstQuery=input('Check highscore[H], Display name of player[D], New game[N]\n')

    if firstQuery.upper()=='H':
        s=open('game__score.txt','r')
        sr=s.read()
        print('highscore:',sr)
        s.close()

    elif firstQuery.upper()=='D':
        n=open('game__name.txt','r')
        nr=n.read()
        print('highest scoring player:',nr)
        n.close()

    elif firstQuery.upper()=='N':
        ask()


def Sum():
    '''this function is for sum of numbers'''
    while True:
        dec=input("press 1 for one digit sum, 2 for two digit and 3 for three digit sum game\nHow many digits? ")
        if dec=="stop":
            break
        elif int(dec)==1:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(1,10)
                num2=random.randint(1,10)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter sum:")
                if ans.isnumeric():
                    if int(ans)==num1+num2:
                        print("Correct!!")
                        score+=1
                        print("\n")
                    else:
                        print("Wrong.\t correct answer is", num1+num2)
                        #print("\n")
                        print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        elif int(dec)==2:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(10,100)
                num2=random.randint(10,100)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter sum:")
                if ans.isnumeric():
                    if int(ans)==num1+num2:
                        print("Correct!!")
                        score+=1
                        print("\n")
                    else:
                        print("Wrong.\t correct answer is", num1+num2)
                        #print("\n")
                        print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        elif int(dec)==3:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(100,1000)
                num2=random.randint(100,1000)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter sum:")
                if ans.isnumeric():
                    if int(ans)==num1+num2:
                        print("Correct!!")
                        score+=1
                        print("\n")
                    else:
                        print("Wrong.\t correct answer is", num1+num2)
                        #print("\n")
                        print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        else:
            print("Unexpected Error.")

def Multiply():
    '''this function is for product of numbers'''
    while True:
        dec=input("press 1 for one digit multiplication, 2 for two digit and 3 for three digit multiplication game\nHow many digits? ")
        if dec=="stop":
            break
        elif int(dec)==1:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(1,10)
                num2=random.randint(1,10)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter product of numbers:")
                if ans.isnumeric():
                    if int(ans)==num1*num2:
                        print("Correct!!")
                        score+=1
                        print("\n")
                    else:
                        print("Wrong.\t correct answer is", num1*num2)
                        #print("\n")
                        print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        elif int(dec)==2:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(10,100)
                num2=random.randint(10,100)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter product of numbers:")
                if ans.isnumeric():
                    if int(ans)==num1*num2:
                        print("Correct!!")
                        score+=1
                        print("\n")
                    else:
                        print("Wrong.\t correct answer is", num1*num2)
                        #print("\n")
                        print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        elif int(dec)==3:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(100,1000)
                num2=random.randint(100,1000)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter product of numbers:")
                if ans.isnumeric():
                    if int(ans)==num1*num2:
                        print("Correct!!")
                        score+=1
                        print("\n")
                    else:
                        print("Wrong.\t correct answer is", num1*num2)
                        #print("\n")
                        print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        else:
            print("Unexpected Error.")

def Subtraction():
    '''this function is for subtraction of numbers'''
    while True:
        dec=input("press 1 for one digit subtraction, 2 for two digit and 3 for three digit subtraction game\nHow many digits? ")
        if dec=="stop":
            break
        elif int(dec)==1:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(1,10)
                num2=random.randint(1,10)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter subtraction (num1-num2)):")
                if ans.isalpha()==False:
                    if int(ans)==num1-num2:
                        print("Correct!!")
                        score+=1
                        print("\n")
                    else:
                        print("Wrong.\t correct answer is", num1-num2)
                        #print("\n")
                        print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        elif int(dec)==2:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(10,100)
                num2=random.randint(10,100)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter subtraction (num1-num2):")
                if ans.isalpha()==False:
                    if int(ans)==num1-num2:
                        print("Correct!!")
                        score+=1
                        print("\n")
                    else:
                        print("Wrong.\t correct answer is", num1-num2)
                        #print("\n")
                        print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        elif int(dec)==3:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(100,1000)
                num2=random.randint(100,1000)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter subtraction (num1-num2):")
                if ans.isalpha()==False:
                    if int(ans)==num1-num2:
                        print("Correct!!")
                        score+=1
                        print("\n")
                    else:
                        print("Wrong.\t correct answer is", num1-num2)
                        #print("\n")
                        print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        else:
            print("Unexpected Error.")

def Division():
    '''this function is for division of numbers'''
    while True:
        dec=input("press 1 for one digit division, 2 for two digit and 3 for three digit division game\nHow many digits? ")
        if dec=="stop":
            break
        elif int(dec)==1:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(1,10)
                num2=random.randint(1,10)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter division of numbers(n1/n2):")
                if ans.isalpha()==False:
                    if float(ans)==num1/num2:
                        print("Correct!!")
                        score+=1
                        print("\n")
                    else:
                        print("Wrong.\t correct answer is", num1/num2)
                        #print("\n")
                        print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        elif int(dec)==2:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(10,100)
                num2=random.randint(10,100)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter division of numbers(n1/n2):")
                if ans.isalpha()==False:
                    if type(ans)==int or type(ans)==float:
                        if float(ans)==num1/num2:
                            print("Correct!!")
                            score+=1
                            print("\n")
                        else:
                            print("Wrong.\t correct answer is", num1/num2)
                            #print("\n")
                            print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        elif int(dec)==3:
            score=0
            name=input("Enter player's name: ")
            while True:
                num1=random.randint(100,1000)
                num2=random.randint(100,1000)
                print("num1=",num1)
                print("num2=",num2)
                ans=input("Enter division of numbers(n1/n2):")
                if ans.isalpha()==False:
                    if type(ans)==int or type(ans)==float:
                        if float(ans)==num1/num2:
                            print("Correct!!")
                            score+=1
                            print("\n")
                        else:
                            print("Wrong.\t correct answer is", num1/num2)
                            #print("\n")
                            print('score: ',score)
                        s=open('game__score.txt','r')
                        sr=s.read()
                        s.close()
                        if score>int(sr):
                            n=open('game__name.txt','w')
                            nw=n.write(name)
                            n.close()
                            s=open('game__score.txt','w')
                            sw=s.write(str(score))
                            s.close()
                        else:
                            s.close()
                        again=input('Do you want to play again?[Y/N]\n')
                        if again.upper()=='Y':
                            score=0
                            continue
                        else:
                            break
                elif ans=="stop":
                    break
                else:
                    print('invalid input')
        else:
            print("Unexpected Error.")




print('Hello')
while True:
    intro()

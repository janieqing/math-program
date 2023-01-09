import random

print("Welcome to math helper!")
print('''There are 4 modes that you can choose from: addition, subtraction, multiplication, or division.
When prompted, please type in the name of the mode from the list above exactly.''')

def add():
    right = 0
    right2 = 0
    wrong = 0
    wrong2 = 0
    while True:
        if right2 == 10:
            break
        elif wrong2 == 3:
            break
    
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        correct = x+y

        a1 = random.randint(0,100)
        a2 = random.randint(1,100)
        a3 = random.randint(1,100)

        if (a1 == a2) or (a1 == a3) or (a2 == a3) or (a1 == correct) or (a2 == correct) or (a3 == correct):
            a1 = a1+2
            a2 = a2+5
            a3 = a3+7
        else:
            continue

        
        d = {'a':a1, 'b':a2, 'c':a3, 'd':correct}
        options = [d['a'], d['b'], d['c'], d['d']]
        random.shuffle(options)
        choices = {'a':options[0], 'b':options[1], 'c':options[2], 'd':options[3]}
        print(x, '+', y, '=')
        print('a. ', choices['a'], '\t',
                  'b. ', choices['b'], '\t',
                  'c. ', choices['c'], '\t',
                  'd. ', choices['d'], sep='')
            
        answer = str(input())
        correctanswer = list(choices.keys())[list(choices.values()).index(x+y)]
            
        if answer == correctanswer:
            print("correct")
            right+=1
                
        elif answer != correctanswer:
            print("incorrect")
            wrong+=1

        if wrong == 3:
            print('try studying some more and come back later!')
            break


        if right == 10:
            print('\n', 'amazing! now moving on to level two!', '\n')
                    
            right2 = 0
            wrong2 = 0
                    
            while True:
                x = random.randint(0, 50)
                y = random.randint(0, 50)
                correct = x+y

                a1 = random.randint(0,100)
                a2 = random.randint(1,100)
                a3 = random.randint(1,100)

                if (a1 == a2) or (a1 == a3) or (a2 == a3) or (a1 == correct) or (a2 == correct) or (a3 == correct):
                    a1 = a1+7
                    a2 = a2+7
                    a3 = a3+7
                else:
                    continue
                                        

                d = {'a':a1, 'b':a2, 'c':a3, 'd':correct}
                options = [d['a'], d['b'], d['c'], d['d']]
                random.shuffle(options)
                choices = {'a':options[0], 'b':options[1], 'c':options[2], 'd':options[3]}
                print(x, '+', y, '=')
                print('a. ', choices['a'], '\t',
                      'b. ', choices['b'], '\t',
                      'c. ', choices['c'], '\t',
                      'd. ', choices['d'], sep='')
            
                answer = input()
                correctanswer = list(choices.keys())[list(choices.values()).index(x+y)]
                            
                if answer == correctanswer:
                    print('correct')
                    right2 +=1

                elif answer != correctanswer:
                    print('incorrect')
                    wrong2 +=1
                                    
                if right2 == 10:
                    print('\n', 'you are a genius; congratulations!')
                    break
                
                if wrong2 == 3:
                    print('try studying some more and come back later!')
                    break


def subtract(level):
    print('''Welcome to subtraction! Any answer that is not the letter of
    the correct number will be counted as incorrect.''')

    choices={}
    right=0
    wrong=0
    for z in range(1,10):

        if level==1:

            x=random.randint(0,10)
            y=random.randint(0,10)
            print(x,"-",y,"=")
            correct=x-y
            options=[correct,x-y+1,x-y-1,x-y-2]
            random.shuffle(options)
            choices=dict(a=options[0],b=options[1],c=options[2],d=options[3])
            print('a.',choices['a'])
            print('b.',choices['b'])
            print('c.',choices['c'])
            print('d.',choices['d'])
            
            
            correctanswer=list(choices.keys())[list(choices.values()).index(x-y)]
            answer=str(input())
            if answer == correctanswer:
                print("correct")
                right+=1
                if right>=8:
                    print("go to next level? type subrtact(2)")
                    break
            else:
                print("incorrect")
                wrong+=1
                if wrong >= 3:
                    print("ask a teacher for help")
                    break
            print("right:",right,"wrong:",wrong)


        elif level==2:
            x=random.randint(0,20)
            y=random.randint(0,20)
            print(x,"-",y,"=")
            correct=x-y
            options=[correct,x-y+1,x-y-1,x-y-2]
            random.shuffle(options)
            choices=dict(a=options[0],b=options[1],c=options[2],d=options[3])
            print('a.',choices['a'])
            print('b.',choices['b'])
            print('c.',choices['c'])
            print('d.',choices['d'])
            
            correctanswer=list(choices.keys())[list(choices.values()).index(x-y)]
            answer=str(input())
            if answer == correctanswer:
                print("correct")
                right+=1
                if right>=8:
                    print("ready for test")
                    break
            else:
                print("incorrect")
                wrong+=1
                if wrong >= 3:
                    print("go to a lower level by typing subtract(1)")
                    break
            print("right:",right,"wrong:",wrong)
         
def multiply(level):
    if level == 1:
        print('Hello welcome to level 1')
        points = 0
        wrong = 0
        for y in range(100):
            
            a = random.randint(0,6)
            b = random.randint(0,6)
            
            rnum = random.randint(0,100)
            rnum1 = random.randint(0,100)
            rnum2 = random.randint(0,100)
            
            answers = [rnum,rnum1,rnum2, a*b]
            random.shuffle(answers)
            choices = dict(a=answers[0],b=answers[1],c=answers[2],d=answers[3])
            print('what is ', a, 'x', b, '?', sep='')
            print(choices, '\n')
            
            correctanswer=list(choices.keys())[list(choices.values()).index(a*b)]
            x = str(input())

            if x == correctanswer:
                print('correct ^o^ \n')
                points+=1
                
            elif x != correctanswer:
                print('incorrect D: \n')
                points-=1
                wrong+=1

            if wrong == 3 or points <0:
                print('Review your times tables')
                break
            print('points: ', points, '\n')
            if points == 10:
                print("Congrats! Now you're moving onto the next level.")
                multiply(2)
                      
    elif level == 2:
        print('Hello welcome to level 2.\n')
        what = input("Are you ready?\n\nType 'yes' or 'no': \n")
        if what == 'yes': 
            for y in range(10):
                a = random.randint(0,12)
                b = random.randint(0,12)
                
                rnum = random.randint(0,100)
                rnum1 = random.randint(0,100)
                rnum2 = random.randint(0,100)
                
                answers = [rnum,rnum1,rnum2, a*b]
                random.shuffle(answers)
                choices = dict(a=answers[0],b=answers[1],c=answers[2],d=answers[3])
                print('what is ', a, 'x', b, '?', sep='')
                print(choices, '\n')
                
                correctanswer=list(choices.keys())[list(choices.values()).index(a*b)]
                x = str(input())
                
            if x == correctanswer:
                print('correct ^o^ \n')
                points+=1
                
            elif x != correctanswer:
                print('incorrect D: \n')
                points-=1
                wrong+=1

            if wrong == 3 or points <0:
                print('Review your times tables')
                
            print('points: ', points, '\n')
            if points == 10:
                print("Congrats! Now you're moving onto the next level.")
                
        elif what == 'no':
            print('Okay lets go back to level 1\n')
            multiply(1)

def division(level):
    streak = 0
    problemSolved = 0
    
    while level < 6:
        if level == 0:
            n = 3
        elif level == 1:
            n = 5
        else:
            n = 5 + (level*5)
        y = random.randint(1,n)
        z = random.randint(1,n)
        
        x = y*z
        z = x/y
        z = int(z)
        print (x, "/", y, "=")

        a = z
        b = z * random.randint(2,3)
        c = z + random.randint(1,5)
        d = z - random.randint(1,2)
        
        answerChoices = [a,b,c,d]
        answerChoices1 = []
        
        for option in answerChoices:
            if option not in answerChoices1:
                answerChoices1.append(option)
            else:
               option = a+b+c+d
               answerChoices1.append(option)
        
        random.shuffle(answerChoices1)

        if answerChoices1[0] == z:
            correctAnswer = 'a'
            correctAnswer2 = 'A'
        elif answerChoices1[1] == z:
            correctAnswer = 'b'
            correctAnswer2 = 'B'
        elif answerChoices1[2] == z:
            correctAnswer = 'c'
            correctanswer2 = 'C'
        elif answerChoices1[3] == z:
            correctAnswer = 'd'
            correctAnswer2 = 'D'

        problemSolved +=1
        
        print ('a', answerChoices1[0])
        print ('b', answerChoices1[1])
        print ('c', answerChoices1[2])
        print ('d', answerChoices1[3])

        userAnswer = input("Letter Answer: ", )
        
        if userAnswer == correctAnswer or userAnswer == correctAnswer2:
            print ("correct")
            streak += 1
        elif userAnswer != correctAnswer:
            print ("incorrect")
            streak = 0
            
        if userAnswer!='a' and userAnswer!='A' and userAnswer!='b' and userAnswer!='B' and userAnswer!='c' and userAnswer!='C' and userAnswer!='d' and userAnswer!='D':
            print ('Error, please only enter the letters a, b, c, or d next time.')                  
            
        print('level:', level)
        print ('streak:', streak)
        
        if streak == 10:

            level += 1
            streak = 0
            print('CONGRATS! YOU CAN MOVE ONTO THE NEXT LEVEL! :)')
            print('Or, you can stop and exit this practice. You have practiced', problemSolved, "questions so far. Type stop to stop or continue to continue practicing.")
            choice = input('stop or continue? ', )
            if choice == 'stop':
                print('Thank you for playing!')
                break
            if choice == 'continue':
                continue

mode = input("Choose your math learning mode: ",)

if mode == 'division':
    print ('''                             Welcome to Division!
                       Division levels go from 0 to 6
    To move on to harder levels, you must answer 10 questions correctly in a row.
        Type in the letter choice that you think contains the correct answer.
                                Good Luck!
                                ''')
    level = int(input ("Please enter the level that you desire to start at: ", ))
    division(level)

elif mode == 'subtraction':
    level = int(input ("Level 1 or 2? ", ))
    subtract(level)

elif mode == 'multiplication':
    level = int(input ("Level 1 or 2? ", ))
    multiply(level)
    
elif mode == 'addition':
    add()
else:
    print('Check spelling of mode and try again. Make sure it matches the choices above exactly!')


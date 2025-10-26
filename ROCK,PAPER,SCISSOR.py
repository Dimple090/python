import random
print('The rules for winning in ROCK PAPER SCISSORS are  :\n'
      + "Rock vs scissors -> Rock wins \n"
      + "Rock vs paper -> Paper wins \n"
      + "Paper vs Scissors -> Scissor wins \n")
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    User_choice=int(input("Enter your choice:"))
    while User_choice > 3 or User_choice <1:
      User_choice=int(input('Enter a valid choice please `'))
    if User_choice == 1:
        User_choice_name= 'ROCK'
    elif User_choice == 2:
        User_choice_name= 'PAPER'
    else:
        User_choice_name= 'SCISSOR'
    print('User choice is \n',User_choice_name)
    print('Now it\'s Computers\'s Turn....')
    comp_choice = random.randint(1,3)
    while comp_choice == User_choice:
        comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice_name = 'ROCK'
    elif comp_choice == 2:
        comp_choice_name = 'PAPER'
    else:
        comp_choice_name = 'SCISSOR'
    print("Computer choice is \n", comp_choice_name)
    print(User_choice_name,'Vs',comp_choice_name)
    if User_choice == comp_choice:
        print('Its a Draw',end="")
        result="DRAW"
    if (User_choice==1 and comp_choice==2):
        print('PAPER wins =>',end="")
        result='PAPER'
    elif (User_choice==2 and comp_choice==1):
        print('PAPER wins =>',end="")
        result='PAPER'
    if (User_choice==1 and comp_choice==3):
        print('ROCK wins =>\n',end= "")
        result='ROCK'
    elif (User_choice==3 and comp_choice==1):
        print('ROCK wins =>\n',end= "")
        result='ROCK'
    if (User_choice==2 and comp_choice==3):
        print('SCISSORS wins =>',end="")
        result='SCISSORS'
    elif (User_choice==3 and comp_choice==2):
        print('SCISSOR wins =>',end="")
        result='ROCK'
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == User_choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Yes/No)")
    ans = input().lower
    if ans =='n':
        break
print("thanks for playing")
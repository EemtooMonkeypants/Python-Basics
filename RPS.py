import random
cs = ['r', 'p', 's']
cscore = 0
pscore = 0
for i in range(1, 11):
    print("Welcome to the game")
    print("Round",i)
    ps = input("r, p, or s?")
    comp = random.choice(cs)
    print("The computer chooses",comp)
    if comp=='r' and ps=='r':
        print("Tie")
        cscore +=0
        pscore +=0
    elif comp=='r' and ps=='p':
        print("Player wins")
        cscore +=0
        pscore +=1
    elif comp=='r' and ps=='s':
        print("Computer wins")
        cscore +=1
        pscore +=0
    elif comp=='p' and ps=='r':
        print("Computer wins")
        cscore +=1
        pscore +=0
    elif comp=='p' and ps=='p':
        print("Tie")
        cscore +=0
        pscore +=0
    elif comp=='p' and ps=='s':
        print("Player wins")
        cscore +=0
        pscore +=1
    elif comp=='s' and ps=='r':
        print("Player wins")
        cscore +=0
        pscore +=1
    elif comp=='s' and ps=='p':
        print("Computer wins")
        cscore +=1
        pscore +=0
    elif comp=='s' and ps=='s':
        print("Tie")
        cscore +=0
        pscore +=0
print("Player Score is",int(pscore))
print("Computer Score is",int(cscore))
if pscore>cscore:
    print("Player Wins!")
elif cscore>pscore:
    print("Computer Wins!")




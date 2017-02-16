#!/usr/bin/python3.5

from random import randint

def drawCard(l):
    r=randint(0,len(cards)-1)
    l.append(cards[r])
    del cards[r]

def cardsInHand(l):
    arbList=[]
    for i in range(len(l)):
        x=str(l[i])
        arbList.append(x)
    c = ', '.join(arbList)
    return c

def chkHand(l):
    toplam=0
    if l.count(1) == 0:
        for i in range(len(l)):
            toplam=toplam+l[i]
        return toplam
    else:
        for i in range(len(l)):
            toplam=toplam+l[i]
        if toplam<=11:
            toplam=toplam+10
        return toplam

myScore=0  # you can start with higher score, if you want :)
dealerScore=0  # negative score is acceptable :)
play=True
while play:
    cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]*4
    hand=[]
    dealer=[]
    drawCard(dealer)
    drawCard(hand)
    drawCard(dealer)
    drawCard(hand)
    print("Your cards: " + cardsInHand(hand))
    print("Sum of your hand:",chkHand(hand))
    print("Dealer's cards: {0}, *".format(dealer[0]))
    if chkHand(hand)==21:
        print("""Winner, winner, chicken dinner!
Blackjack!""")
        myScore+=2
    else:
        while True:
            switch=input("Would you like to take another card?(y/n)")
            if switch == "y" or switch == "Y":
                drawCard(hand)
                print("Your cards: " + cardsInHand(hand))
                print("Sum of your hand:",chkHand(hand))
                if chkHand(hand)>=21:
                    break
            elif switch == "n" or switch == "N":
                break
            else:
                print("You've made a mistake.")
        while chkHand(dealer)<=16:
            drawCard(dealer)
        print("Dealer's cards: " + cardsInHand(dealer))
        print("Sum of dealer's cards:",chkHand(dealer))
        if chkHand(hand)>21:
            print("You lost.")
            dealerScore+=1
        elif chkHand(dealer)>21 or chkHand(hand)>chkHand(dealer):
            print("You won.")
            myScore+=1
        elif chkHand(hand)<chkHand(dealer):
            print("You lost.")
            dealerScore+=1
        else:
            print("It's nobody's game.")
    while True:
        switch=input("Would you like to play again?(y/n)")
        if switch == "y" or switch == "Y":
            break
        elif switch == "n" or switch == "N":
            play=False
            break
        else:
            print("You've made a mistake.")

print("+--- Your Score --- Dealer's Score ---+")
print("        {0}               {1}".format(myScore,dealerScore))
print("+-------------------------------------+")
input("Press Enter to exit.")

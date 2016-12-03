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

play=True
while play:
    cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]*4
    hand=[]
    dealer=[]
    drawCard(hand)
    drawCard(hand)
    print("Your cards: " + cardsInHand(hand))
    print("Your score:",chkHand(hand))
    if chkHand(hand)==21:
        print("""Winner, winner, chicken dinner!
Blackjack!""")
    else:
        while True:
            switch=input("Do you want to draw a card?(y/n)")
            if switch == "y" or switch == "Y":
                drawCard(hand)
                print("Your cards: " + cardsInHand(hand))
                print("Your score:",chkHand(hand))
                if chkHand(hand)>=21:
                    break
            elif switch == "n" or switch == "N":
                break
            else:
                print("You have made a mistake.")
        drawCard(dealer)
        drawCard(dealer)
        while chkHand(dealer)<=16:
            drawCard(dealer)
        print("Dealer's cards: " + cardsInHand(dealer))
        print("Dealer's score:",chkHand(dealer))
        if chkHand(hand)>21:
            print("You lost.")
        elif chkHand(dealer)>21:
            print("You win.")
        elif chkHand(hand)>chkHand(dealer):
            print("You win.")
        elif chkHand(hand)<chkHand(dealer):
            print("You lost.")
        else:
            print("It's nobody's game.")
    while True:
        switch=input("Do you want to play again?(y/n)")
        if switch == "y" or switch == "Y":
            break
        elif switch == "n" or switch == "N":
            play=False
            break
        else:
            print("You have made a mistake.")

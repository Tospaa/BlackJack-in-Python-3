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

myScore=0
dealerScore=0
play=True
while play:
    cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]*4
    hand=[]
    dealer=[]
    drawCard(dealer)
    drawCard(hand)
    drawCard(dealer)
    drawCard(hand)
    print("Kartlarınız: " + cardsInHand(hand))
    print("El toplamı:",chkHand(hand))
    print("Krupiyenin kartları: {0}, *".format(dealer[0]))
    if chkHand(hand)==21:
        print("""Winner, winner, chicken dinner!
Blackjack Yaptınız!""")
        myScore+=2
    else:
        while True:
            switch=input("Bir kart daha almak istiyor musunuz?(e/h)")
            if switch == "e" or switch == "E":
                drawCard(hand)
                print("Kartlarınız: " + cardsInHand(hand))
                print("El toplamı:",chkHand(hand))
                if chkHand(hand)>=21:
                    break
            elif switch == "h" or switch == "H":
                break
            else:
                print("Yanlış bir seçim yaptınız.")
        while chkHand(dealer)<=16:
            drawCard(dealer)
        print("Krupiye kartları: " + cardsInHand(dealer))
        print("Krupiye el toplamı:",chkHand(dealer))
        if chkHand(hand)>21:
            print("Kaybettiniz.")
            dealerScore+=1
        elif chkHand(dealer)>21 or chkHand(hand)>chkHand(dealer):
            print("Kazandınız.")
            myScore+=1
        elif chkHand(hand)<chkHand(dealer):
            print("Kaybettiniz.")
            dealerScore+=1
        else:
            print("Dostluk kazandı.")
    while True:
        switch=input("Tekrar oynamak istiyor musunuz?(e/h)")
        if switch == "e" or switch == "E":
            break
        elif switch == "h" or switch == "H":
            play=False
            break
        else:
            print("Yanlış bir seçim yaptınız.")

print("+--- Skorunuz --- Krupiye Skoru ---+")
print("        {0}              {1}".format(myScore,dealerScore))
print("+----------------------------------+")
input("Çıkmak için Enter tuşuna basınız.")

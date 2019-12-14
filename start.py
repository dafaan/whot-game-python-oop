 
import random
#create card class for card object with shape and number attribute
class cards(object):
    def __init__(self, shape, num):
        self.shape=shape
        self.num=num
#printcard function to print out the shape and number of a card
    def printcard(self):
        print('{} {}'.format(self.shape, self.num))
#market class for the market object with build method that creates the market and a 
#shuffle method that shuffles rhe deck
class market(object):
    def __init__(self):
        self.cards=[]
        self.build()
    def build(self):
        for s in ['triangle', 'ball']:
            for v in range(1, 15):
                if v==6:
                    continue
                if v==9:
                    continue
                
                self.cards.append(cards(s, v))
        for s in ['cross', 'box']:
            for v in range(1, 15):
                if v==4:
                    continue
                if v==6:
                    continue
                if v==9:
                    continue
                if v==12:
                    continue
                
                self.cards.append(cards(s, v))
            
        for s in ['star']:
            for v in range(1, 9):
                if v==6:
                    continue
                self.cards.append(cards(s, v))
#                print('{} {}'.format(s, v))
    
    def show(self):
        for c in self.cards:
            c.printcard()
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r=random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def draw_card(self):
        return self.cards.pop()
a=market()
a.shuffle()
#a.show()
m=a.draw_card()
#m.printcard()

class player(object):
    def __init__(self):
        self.hand=[]
    def draw(self, market):
        self.hand.append(a.draw_card())
    def show_hand(self):
        for c in self.hand:
            c.printcard
v=player()
v.draw(market)
v.show_hand()
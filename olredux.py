############################################################
#
# Olinland Redux
#
# The final project for Game Programming
#
#

import time
import random

from Screen import *
from Level import *
from Room import *
from Floor import *
from Items import *
from Potion import *
from Money import *
from Equipment import *
from Sword import *
from Player import *
from OlinStatue import *
from Scorpion import *
from Thing import *
from Character import *
from graphics import *
from UniVars import *
from Rectangles import *
from Armor import *
from Boss import *

# A helper function that lets you log information to the console
# with some timing information. I found this super useful to 
# debug tricky event-based problems.
#
def log (message):
    print time.strftime("[%H:%M:%S]",time.localtime()),message

#############################################################
# 
# The event queue
#
# An event is any object that implements an event() method
# That event method gets the event queue as input, so that
# it can add to the event queue if it needs to.

class EventQueue (object):
    def __init__ (self):
        self._contents = []

    # list kept ordered by time left before firing
    def enqueue (self,when,obj):
        for (i,entry) in enumerate(self._contents):
            if when < entry[0]:
                self._contents.insert(i,[when,obj])
                break
        else:
            self._contents.append([when,obj])

    def ready (self):
        if self._contents:
            return (self._contents[0][0]==0)
        else:
            return False
        
    def dequeue_if_ready (self):
        acted = self.ready()
        while self.ready():
            entry = self._contents.pop(0)
            entry[1].event(self)
        for entry in self._contents:
            entry[0] -= 1


# A simple event class that checks for user input.
# It re-enqueues itself after the check.

class CheckInput (object):
    def __init__ (self,window,player):
        self._player = player
        self._window = window

    def event (self,q):
        key = self._window.checkKey()
        if key == 'q':
            self._window.close()
            exit(0)
        if key in MOVE:
            (dx,dy) = MOVE[key]
            self._player.p_move(dx,dy)
        q.enqueue(1,self)

# Create the right-side panel that can be used to display interesting
# information to the player
#
def create_panel (window):
    fg = Rectangle(Point(WINDOW_WIDTH+1,-20),
                   Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL+20,WINDOW_HEIGHT+20))
    fg.setFill("darkgray")
    fg.setOutline("darkgray")
    fg.draw(window)
    fg = Text(Point(WINDOW_WIDTH+100,
                    30),"Olinland Redux")
    fg.setSize(24)
    fg.setStyle("italic")
    fg.setFill("red")
    fg.draw(window)

#
# The main function
# 
# It initializes everything that needs to be initialized
# Order is important for graphics to display correctly
# Note that autoflush=False, so we need to explicitly
# call window.update() to refresh the window when we make
# changes
#
def main ():

    q = EventQueue()
    window = GraphWin("Olinland Redux", 
                      WINDOW_WIDTH+WINDOW_RIGHTPANEL, WINDOW_HEIGHT,
                      autoflush=False)
                      
    r_color = random.choice(['GREEN','RED','YELLOW','BLACK','BLUE'])
    floor = Floor(COLOR[r_color],random.randint(1,10),q)
    print floor._room
    level = floor._room[0]._lvl
    log ("level created")

    scr = Screen(window,CX,CY,floor)
    log ("screen created")
    
    #Computer Characters
    pinky = Scorpion("Pinky","A Scorpion").register(q,40).materialize(scr,30,30)
    #brain = Scorpion("Brain","A Scorpion with a big head").register(q,60).materialize(scr,12,30)
    Boss("GUARD","A Boss").register(q,40).materialize(scr,25,15)
    
   
    #Non-Player objects
    os = OlinStatue().materialize(scr,20,20)    
    
    #Random items that are useful for the player. Walkable
    for i in range(10):
        Money("Money","Can be used to buy things from merchant.",random.choice([5,10,50])).materialize(scr,random.randint(
            LEVEL_WIDTH/2-VIEWPORT_WIDTH/2+1,LEVEL_WIDTH/2+VIEWPORT_WIDTH/2-1),random.randint(LEVEL_HEIGHT/2-VIEWPORT_HEIGHT/2+3,LEVEL_HEIGHT/2+VIEWPORT_HEIGHT/2)-1)
    for i in range(3):
        Potion("Potion", "Can be used to heal Player.",10).materialize(scr,random.randint(
            LEVEL_WIDTH/2-VIEWPORT_WIDTH/2+1,LEVEL_WIDTH/2+VIEWPORT_WIDTH/2-1),random.randint(LEVEL_HEIGHT/2-VIEWPORT_HEIGHT/2+3,LEVEL_HEIGHT/2+VIEWPORT_HEIGHT/2)-1)
    
    Sword("Wooden Sword", "Weakest Sword in the game", 1).materialize(scr,35,37)
    Armor("wooden Armor", "Weakest Armor in the game", 1).materialize(scr, 15,17)
    #Things that are part of the game world. Everything but the player.

    #create_panel(window)

    p = Player("...what's your name, bub?...",window,floor).materialize(scr,25,25)

    q.enqueue(1,CheckInput(window,p))

    while p._health > 0:
        # Grab the next event from the queue if it's ready
        q.dequeue_if_ready()
        # Time unit = 10 milliseconds
        time.sleep(0.01)
    txt = Text(Point(VIEWPORT_WIDTH/2*24, VIEWPORT_WIDTH/2*24),"You Lost!")
    txt.draw(window)
    update()
    time.sleep(3)



if __name__ == '__main__':
    main()
############################################################
#
# Olinland Redux
#
# The final project for Game Programming
#
#

import time
import random

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

#
# A Screen is a representation of the level displayed in the 
# viewport, with a representation for all the tiles and a 
# representation for the objects in the world currently 
# visible. Managing all of that is key. 
#
# For simplicity, a Screen object contain a reference to the
# level it is displaying, and also to the window in which it
# draws its elements. So you can use the Screen object to 
# mediate access to both the level and the window if you need
# to access them.
# 
# You'll DEFINITELY want to add methods to this class. 
# Like, a lot of them.
#
class Screen (object):
    def __init__ (self,level,window,cx,cy):
        self._level = level
        self._window = window
        self._cx = cx    # the initial center tile position 
        self._cy = cy    #  of the screen
        self._things = []
        self._color = level._color 
        # Background is black
        bg = Rectangle(Point(-20,-20),Point(WINDOW_WIDTH+20,WINDOW_HEIGHT+20))
        bg.setFill("white")
        bg.setOutline("black")
        bg.draw(window)
        # here, you want to draw the tiles that are visible
        # and possible record them for future manipulation
        # you'll probably want to change this at some point to
        # get scrolling to work right...
        dx = (VIEWPORT_WIDTH-1)/2
        dy = (VIEWPORT_HEIGHT-1)/2
        for y in range(cy-dy,cy+dy+1):
            for x in range(cx-dx,cx+dx+1):
                sx = (x-(cx-dx)) * TILE_SIZE
                sy = (y-(cy-dy)) * TILE_SIZE
                Image(Point(TILE_SIZE/2,TILE_SIZE/2),PLAYER)
                if self.tile(x,y) == 0:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),0,sx/24,sy/24)
                    elt.setFill(self._color[0])
                    elt.setOutline(self._color[0])
                elif self.tile(x,y) == 1:                    
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),1,sx/24,sy/24)
                    elt.setFill(self._color[0])
                    elt.setOutline(self._color[0])
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),sx/24,sy/24,1,self._color[2])
                elif self.tile(x,y) == 2:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),2,sx/24,sy/24)
                    elt.setFill(self._color[0])
                    elt.setOutline(self._color[0])
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),sx/24,sy/24,2,self._color[3])
                elif self.tile(x,y) == 3:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),3,sx/24,sy/24)
                    elt.setFill(self._color[1])
                    elt.setOutline(self._color[1])
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),sx/24,sy/24,3,self._color[4])
                elif self.tile(x,y) == 4:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,sx/24,sy/24)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),sx/24,sy/24,4,DOOR_UP)
                elif self.tile(x,y) == 5:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,sx/24,sy/24)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),sx/24,sy/24,4,DOOR_LEFT)
                elif self.tile(x,y) == 6:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,sx/24,sy/24)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),sx/24,sy/24,4,DOOR_DOWN)
                elif self.tile(x,y) == 7:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,sx/24,sy/24)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),sx/24,sy/24,4,DOOR_RIGHT)
                self._things.append(elt)
                elt.draw(window)
            rect = Rectangle(Point(640,0),Point(800,24))
            rect.setFill('white')
            rect.setOutline('lightgrey')
            rect.draw(window)
            health = Image(Point(80,16),HEALTH)
            health.draw(window)
                

    def clear_scr(self):
        for i in range(len(self._things)):
            if self._things[i].is_thing():
                self._things[i]._sprite.undraw()
            else:
                self._things[i].undraw()

    # return the tile at a given tile position
    def tile (self,x,y):
        return self._level.tile(x,y)

    # add a thing to the screen at a given position
    def add (self,item,x,y):
        # first, move object into given position
        item.sprite().move((x-(self._cx-(VIEWPORT_WIDTH-1)/2))*TILE_SIZE,
                           (y-(self._cy-(VIEWPORT_HEIGHT-1)/2))*TILE_SIZE)
        item.sprite().draw(self._window)
        # WRITE ME!   You'll have to figure out how to manage these
        # because chances are when you scroll these will not move!


    # helper method to get at underlying window
    def window (self):
        return self._window

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

    window = GraphWin("Olinland Redux", 
                      WINDOW_WIDTH+WINDOW_RIGHTPANEL, WINDOW_HEIGHT,
                      autoflush=False)
                      
    r_color = random.choice(['GREEN','RED','YELLOW','BLACK','BLUE'])
    floor = Floor(COLOR[r_color])
    room = Room(1,floor)

    level = room._lvl
    log ("level created")

    scr = Screen(level,window,CX,CY)
    log ("screen created")

    q = EventQueue()
    
    #Computer Characters
    pinky = Scorpion("Pinky","A Scorpion").register(q,40).materialize(scr,30,30)
    #brain = Scorpion("Brain","A Scorpion with a big head").register(q,60).materialize(scr,12,30)
    
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

    p = Player("...what's your name, bub?...",window).materialize(scr,25,25)

    q.enqueue(1,CheckInput(window,p))

    while True:
        # Grab the next event from the queue if it's ready
        q.dequeue_if_ready()
        # Time unit = 10 milliseconds
        time.sleep(0.01)



if __name__ == '__main__':
    main()
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

import random
from Room import *
from Floor import *
from Level import *
from graphics import *
from UniVars import *
from Rectangles import *
from Player import *
from Thing import *

class Screen (object):
    def __init__ (self,window,cx,cy,floor):
        self._window = window
        self._cx = cx    # the initial center tile position 
        self._cy = cy    #  of the screen
        self._floor = floor
        self._room_num = floor.getRoomNum()
        self._room_T = {}
        self._things = []
        self._color = floor.getColor() 
        self._room = floor.getRoom(1)
        self._level = self._room.getLvl()
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
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),0,x,y)
                    elt.setFill(self._color[0])
                    elt.setOutline(self._color[0])
                elif self.tile(x,y) == 1:                    
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),1,x,y)
                    elt.setFill(self._color[0])
                    elt.setOutline(self._color[0])
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,1,self._color[2])
                elif self.tile(x,y) == 2:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),2,x,y)
                    elt.setFill(self._color[0])
                    elt.setOutline(self._color[0])
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,2,self._color[3])
                elif self.tile(x,y) == 3:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),3,x,y)
                    elt.setFill(self._color[1])
                    elt.setOutline(self._color[1])
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,3,self._color[4])
                elif self.tile(x,y) == 4:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,x,y)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,4,DOOR_UP)
                elif self.tile(x,y) == 5:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,x,y)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,4,DOOR_LEFT)
                elif self.tile(x,y) == 6:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,x,y)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,4,DOOR_DOWN)
                elif self.tile(x,y) == 7:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,x,y)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,4,DOOR_RIGHT)
                self._things.append(elt)
                elt.draw(window)
            rect = Rectangle(Point(640,0),Point(800,24))
            rect.setFill('white')
            rect.setOutline('lightgrey')
            rect.draw(window)
            health = Image(Point(80,16),HEALTH)
            health.draw(window)
        self._room_T[self._room_num] = self._things
                
    def clear_scr(self,player):
        self._room_T[self._room_num] = self._things
        for i in range(len(self._things)):
            if self._things[i].is_thing():
                self._things[i]._sprite.undraw()
            else:
                self._things[i].undraw()
        newP = player
        self._things = []
        print newP
        self._things.append(newP)

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

    def redraw(self, floor,num, enter): 
        self._room = floor.getRoom(num)
        self._level = self._room.getLvl()
        # Background is black
        bg = Rectangle(Point(-20,-20),Point(WINDOW_WIDTH+20,WINDOW_HEIGHT+20))
        bg.setFill("white")
        bg.setOutline("black")
        bg.draw(self._window)
        window = self._window
        (self._cx, self._cy) = enter
        cx = self._cx
        cy = self._cy

        if (self._cx, self._cy) == (40,25):
            self.East_enter()


    def East_enter(self):
        window = self._window
        cx = self._cx
        cy = self._cy
        dx = (VIEWPORT_WIDTH-1)/2
        dy = (VIEWPORT_HEIGHT-1)/2
        for y in range(cy-dy,cy+dy+1):
            for x in range(cx-VIEWPORT_WIDTH+1,cx+1):
                sx = (x-(cx-dx)) * TILE_SIZE
                sy = (y-(cy-dy)) * TILE_SIZE
                Image(Point(TILE_SIZE/2,TILE_SIZE/2),PLAYER)
                if self.tile(x,y) == 0:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),0,x,y)
                    elt.setFill(self._color[0])
                    elt.setOutline(self._color[0])
                elif self.tile(x,y) == 1:                    
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),1,x,y)
                    elt.setFill(self._color[0])
                    elt.setOutline(self._color[0])
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,1,self._color[2])
                elif self.tile(x,y) == 2:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),2,x,y)
                    elt.setFill(self._color[0])
                    elt.setOutline(self._color[0])
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,2,self._color[3])
                elif self.tile(x,y) == 3:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),3,x,y)
                    elt.setFill(self._color[1])
                    elt.setOutline(self._color[1])
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,3,self._color[4])
                elif self.tile(x,y) == 4:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,x,y)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,4,DOOR_UP)
                elif self.tile(x,y) == 5:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,x,y)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,4,DOOR_LEFT)
                elif self.tile(x,y) == 6:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,x,y)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,4,DOOR_DOWN)
                elif self.tile(x,y) == 7:
                    elt = Rectangles(Point(sx,sy),Point(sx+TILE_SIZE,sy+TILE_SIZE),4,x,y)
                    elt.setFill('black')
                    elt.setOutline('black')
                    elt.draw(window)
                    self._things.append(elt)
                    elt = Images(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),x,y,4,DOOR_RIGHT)
                self._things.append(elt)
                elt.draw(window)
            # rect = Rectangle(Point(640,0),Point(800,24))
            # rect.setFill('white')
            # rect.setOutline('lightgrey')
            # rect.draw(window)
            # health = Image(Point(80,16),HEALTH)
            # health.draw(window)
            self._room.buildObj(self)
            self._things[0]._sprite.undraw()
            self._things[0].setXY(cx,cy)
            self._things[0]._sprite.draw(window)
        self._room_T[self._room_num] = self._things

import spritesheet
 
class SpriteStripAnim(object):
    """sprite strip animator
    
    This class provides an iterator (iter() and next() methods), and a
    __add__() method for joining strips which comes in handy when a
    strip wraps to the next row.
    """
    def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1):
        """construct a SpriteStripAnim
        
        filename, rect, count, and colorkey are the same arguments used
        by spritesheet.load_strip.
        
        loop is a boolean that, when True, causes the next() method to
        loop. If False, the terminal case raises StopIteration.
        
        frames is the number of ticks to return the same image before
        the iterator advances to the next image.
        """
        self.filename = filename
        ss = spritesheet.spritesheet(filename)
        self.images = ss.load_strip(rect, count, colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames
    def iter(self):
        self.i = 0
        self.f = self.frames
        return self
    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image
    def __add__(self, ss):
        self.images.extend(ss.images)
        return self

"""
Sprite strip animator demo
 
Requires spritesheet.spritesheet and the Explode1.bmp through Explode5.bmp
found in the sprite pack at
http://lostgarden.com/2005/03/download-complete-set-of-sweet-8-bit.html
 
I had to make the following addition to method spritesheet.image_at in
order to provide the means to handle sprite strip cells with borders:
 
            elif type(colorkey) not in (pygame.Color,tuple,list):
                colorkey = image.get_at((colorkey,colorkey))
"""
import sys
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
#from sprite_strip_anim import SpriteStripAnim
 
surface = pygame.display.set_mode((100,100))
FPS = 250
frames = FPS / 25
for i in range(1):
    strips = [SpriteStripAnim('55265.png', (i*96, 0, 96, 96), 25, (255,0,255), True, frames)]
color = Color('white')
clock = pygame.time.Clock()
n = 0
strips[n].iter()
image = strips[n].next()
while True:
    for e in pygame.event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                sys.exit()
            elif e.key == K_RETURN:
                n += 1
                if n >= len(strips):
                    n = 0
                strips[n].iter()
    surface.fill(color)
    surface.blit(image, (2,2))
    pygame.display.flip()
    image = strips[n].next()
    clock.tick(FPS)
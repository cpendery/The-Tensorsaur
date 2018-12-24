import pyglet
from pyglet import image
from ground import Ground
'''
Created on Dec 24, 2018

@author: wtmul
'''

class Cactus(pyglet.sprite.Sprite):

    def __init__(self):
        super().__init__(img=image.load('sprites/bigCactus.png', None, None))
        self.x = 2000
        self.velocity_x = 0.0
        
    def update(self, dt):
        self.velocity_x = Ground.current_ground_speed
        self.x += self.velocity_x * dt
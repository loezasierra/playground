# Data objects for Rubik's Cube game

import pygame


## Constants ##

class constants:
    # Screen
    TITLE = "Rubik's Cube"
    WIDTH = 800
    HEIGHT = 600
    SCREEN_START = (0, 0)

    # Colors
    WHITE = (255, 255, 255)


## Data ##

"""
Color is one of:
  - "white"
  - "green"
  - "red"
  - "blue"
  - "orange"
  - "yellow"
interp. the color of a Rubik's Cube block
"""

# Constants for easier examples
W = "white"
G = "green"
R = "red"
B = "blue"
O = "orange"
Y = "yellow"


"""
Side is [Color][Color]  where each list is 3 elements long
        for a total of 9 elements
interp. The side of a Rubik's Cube
"""

# A side with a row of yellow, row of blue, and row of green
S1 = [
    [Y, Y, Y],
    [B, B, B],
    [G, G, G]
]

# White side
SW = [
    [W, W, W],
    [W, W, W],
    [W, W, W]
]

# Orange side
SO = [
    [O, O, O],
    [O, O, O],
    [O, O, O]
]

# Green side
SG = [
    [G, G, G],
    [G, G, G],
    [G, G, G]
]

# Red side
SR = [
    [R, R, R],
    [R, R, R],
    [R, R, R]
]

# Blue side
SB = [
    [B, B, B],
    [B, B, B],
    [B, B, B]
]

# Yellow side
SY = [
    [Y, Y, Y],
    [Y, Y, Y],
    [Y, Y, Y]
]


class Cube:
    """
Cube is Cube({'f': Side, 'b': Side, 'u': Side, 'd': Side, 'l': Side, 'r': Side})
interp. A Rubik's Cube with 6 sides
        f is front side
        b is back side
        u is up side
        d is down side
        l is left side
        r is right side
interp. Cube is always seen from the perspective with a White Side on top and Green Side on front
    """
    def __init__(self, c):
        # Cube with six sides
        self.front = c['f']
        self.back  = c['b']
        self.up    = c['u']
        self.down  = c['d']
        self.left  = c['l']
        self.right = c['r']


# Default Rubik's Cube
C0 = Cube({'f': SG, 'b': SB, 'u': SW, 'd': SY, 'l': SO, 'r': SR})

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
    WHITE  = (255, 255, 255)
    BLACK  = (0, 0, 0)
    CREAM  = (255, 237, 216)
    GREEN  = (90, 196, 127)
    RED    = (114, 14, 7)
    BLUE   = (0, 71, 119)
    ORANGE = (242, 84, 45)
    YELLOW = (244, 226, 133)
    TRANSPARENT = (0, 0, 0, 0)


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
    
    # Cube Int -> pygame.Surface
    # Return Cube as a pygame Surface (i.e. image) of given width in pixels
    def image(self, w):
        # Constants #
        # Grid
        grid_square = round(w / 14) # Imagine drawing on a grid for easier implementation
        width  = grid_square * 14
        height = grid_square * 9
        center_x = round(width / 2)

        third_square = round(grid_square / 3)
        two_third_square = round((grid_square / 3) * 2)
        block_outline = round(grid_square / 8) # thickness of block outline

        # Cube coordinates
        front_start = (grid_square * 4,  grid_square * 2)
        back_start  = ((grid_square * 11) - third_square, third_square)
        up_start    = (grid_square * 7, grid_square)
        down_start  = (grid_square * 7, (grid_square * 7) - third_square)
        left_start  = (third_square, grid_square + third_square)
        right_start = (grid_square * 7,  grid_square * 3)

        # Prepare background to draw on
        background = pygame.Surface((width, height))
        image = background.convert_alpha()
        image.fill(constants.TRANSPARENT)
        
        # Helpers #

        # Tuple Side -> None
        # Draw a left-sided panel on image of Side starting from p
        def draw_left_panel(p, s):

            # Tuple Color -> None
            # Draw a left-sided block on image with color starting from p
            def draw_block(p, c):
                # Calculate polygon points
                points = [
                    p, # top left
                    (p[0], p[1] + grid_square), # bottom left
                    (p[0] + grid_square, p[1] + (grid_square + third_square)), # bottom right
                    (p[0] + grid_square, p[1] + third_square) # top right
                ]

                # Draw block with its outline
                pygame.draw.polygon(image, constants.BLACK, points, width = block_outline)
                pygame.draw.polygon(image, c, points)
                return

            # For calculating
            starting_point = p
            
            # For each block in Side
            for i in range(3):
                for j in range(3):
                    # Remember color
                    color = s[i][j]
                    # Draw block
                    draw_block(starting_point, getattr(constants, color.upper()))
                    # Move starting point to next block in current row
                    starting_point = (starting_point[0] + grid_square, starting_point[1] + third_square)
                # Move starting point to next row
                starting_point = (p[0], starting_point[1])
            return
        
        # Tuple Side -> None
        # Draw a right-sided panel on image of Side starting from p
        def draw_right_panel(p, s):

            # Tuple Color -> None
            # Draw a right-sided block on image with color starting from p
            def draw_block(p, c):
                # Calculate polygon points
                points = [
                    p, # top left
                    (p[0], p[1] + grid_square), # bottom left
                    (p[0] + grid_square, p[1] + (grid_square - third_square)), # bottom right
                    (p[0] + grid_square, p[1] - third_square) # top right
                ]

                # Draw block with its outline
                pygame.draw.polygon(image, constants.BLACK, points, width = block_outline)
                pygame.draw.polygon(image, c, points)
                return
            
            # For calculating
            starting_point = p

            # For each block in Side
            for i in range(3):
                for j in range(3):
                    # Remember color
                    color = s[i][j]
                    # Draw block
                    draw_block(starting_point, getattr(constants, color.upper()))
                    # Move starting point to next block in current row
                    starting_point = (starting_point[0] + grid_square, starting_point[1] - third_square)
                # Move starting point to next row
                starting_point = (p[0], starting_point[1] + (grid_square * 2))
            return
        
        # Tuple Side -> None
        # Draw an up facing panel on Image of Side starting from p
        def draw_up_panel(p, s):

            # Tuple Color -> None
            # Draw an up sided block on image with color starting from p
            def draw_block(p, c):
                # Calculate polygon points
                points = [
                    p, # top left
                    (p[0] - grid_square, p[1] + third_square), # bottom left
                    (p[0], p[1] + two_third_square), # bottom right
                    (p[0] + grid_square, p[1] + third_square) # top right
                ]

                # Draw block with its outline
                pygame.draw.polygon(image, constants.BLACK, points, width = block_outline)
                pygame.draw.polygon(image, c, points)
                return
            
            # For calculating
            starting_point = p

            # For each block in Side
            for i in range(3):
                for j in range(3):
                    # Remember color
                    color = s[i][j]
                    # Draw block
                    draw_block(starting_point, getattr(constants, color.upper()))
                    # Move starting point to next block in current row
                    starting_point = (starting_point[0] + grid_square, starting_point[1] + third_square)
                # Move starting point to next row
                starting_point = (starting_point[0] - (grid_square * 4), starting_point[1] - two_third_square)
            return
        
        # Draw all sides and return completed image
        draw_up_panel(up_start, self.up)
        draw_right_panel(right_start, self.right)
        draw_left_panel(front_start, self.front)
        draw_right_panel(left_start, self.left)
        draw_left_panel(back_start, self.back)
        draw_up_panel(down_start, self.down)
        return image


# Default Rubik's Cube
C0 = Cube({'f': SG, 'b': SB, 'u': SW, 'd': SY, 'l': SO, 'r': SR})

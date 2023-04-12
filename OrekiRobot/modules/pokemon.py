import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("OrekiRobot Pokemon Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Define hexagon dimensions
HEX_SIDE = 50
HEX_HEIGHT = HEX_SIDE * 2
HEX_WIDTH = int((3 ** 0.5 / 2) * HEX_HEIGHT)

# Define Pokemon characters
POKEMON_LIST = [
    {
        "name": "Pikachu",
        "sprite": pygame.image.load("pikachu.png"),
        "stats": {
            "hp": 50,
            "attack": 10,
            "defense": 5,
            "speed": 15
        }
    },
    {
        "name": "Charmander",
        "sprite": pygame.image.load("charmander.png"),
        "stats": {
            "hp": 40,
            "attack": 15,
            "defense": 5,
            "speed": 10
        }
    },
    {
        "name": "Squirtle",
        "sprite": pygame.image.load("squirtle.png"),
        "stats": {
            "hp": 60,
            "attack": 5,
            "defense": 15,
            "speed": 5
        }
    }
]

# Draw a hexagon
def draw_hexagon(surface, color, center):
    points = []
    for i in range(6):
        angle_deg = 60 * i - 30
        angle_rad = angle_deg * 3.14159 / 180
        x = center[0] + HEX_SIDE * math.cos(angle_rad)
        y = center[1] + HEX_SIDE * math.sin(angle_rad)
        points.append((x, y))
    pygame.draw.polygon(surface, color, points)

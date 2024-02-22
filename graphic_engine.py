import pygame

class Coord:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
class Color:
    def __init__(self, r=0, g=0, b=0, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

# Pre-made Colors
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
YELLOW = Color(255, 255, 0)
ORANGE = Color(255, 165, 0)
MAGENTA = Color(255, 0, 255)
CYAN = Color(0, 255, 255)
WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

class Text: # Text Object
    def __init__(self, text, pos, font_size=36, font=None, color=BLACK):
        if not font: self.font = pygame.font.Font(None, font_size) # Set default fontsize at font size set
        
        self.text_surface = self.font.render(text, True, (color.r, color.g, color.b))
        self.text_rect = self.text_surface.get_rect()

        self.text_rect.center = (pos.x, pos.y)
class App:
    def __init__(self, width, height):
        pygame.init() # Inits the window

        self.width = width # Size of window
        self.height = height
        self.screen = pygame.display.set_mode([width, height]) # Sets up the window

        self.running = True # Is the app running?

    def fill(self, color=WHITE): # Fills the full screen
        self.screen.fill((color.r, color.g, color.b, color.a))

    def circle(self, pos, r, color=BLACK): # Draws a circle on screen
        pygame.draw.circle(self.screen, (color.r, color.g, color.b, color.a), (pos.x, pos.y), r)

    def rect(self, pos, size, color=BLACK): # Draws a rect on screen
        pygame.draw.rect(self.screen, (color.r, color.g, color.b, color.a), pygame.Rect(pos.x, pos.y, size.x, size.y))

    def drawText(self, text):
        self.screen.blit(text.text_surface, text.text_rect)

    def run_at_start(self): # Ran just once at start
        pass

    def update(self): # Updates every frame
        pass

    def run(self): # Runs everything
        self.run_at_start()

        while self.running: # Checks if the close button gets clicked
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()

            pygame.display.flip()

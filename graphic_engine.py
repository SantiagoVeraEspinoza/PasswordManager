import pygame

class App:
    def __init__(self, width, height):
        pygame.init() # Inits the window

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([width, height])

        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Fill the background with white
            self.screen.fill((255, 255, 255))

            # Draw a solid blue circle in the center
            pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)

            # Flip the display
            pygame.display.flip()

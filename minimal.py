import sys
import pygame
import random

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

text = pygame.font.SysFont("Times New Roman", 12).render('Google', False, (0, 0, 0))

color = [0, 0, 0]
# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
	if event.type == 5:
            color[0] = random.randint(0, 255)
	    color[1] = random.randint(0, 255)
	    color[2] = random.randint(0, 255)
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    screen.fill(color)
    screen.blit(text, (pygame.display.get_surface().get_size()[0] - pygame.mouse.get_pos()[0], pygame.display.get_surface().get_size()[1] - pygame.mouse.get_pos()[1]))
    pygame.display.flip()

import pygame
import sys
pygame.init()  # Loads pygame engine
pygame.joystick.init()  # main joystick device system
try:
    j = pygame.joystick.Joystick(0) # create a joystick instance
    j.init() # init instance
    print ("Enabled joystick: {0}".format(j.get_name()))
except pygame.error:
    print ("no joystick found.")

def gameLoop():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('goodbye')
                gameExit=True
            if event.type == pygame.JOYAXISMOTION:  # Joystick
                print('lx=',j.get_axis(0))
                print('ly',j.get_axis(1))
                print('rx=',j.get_axis(2))
                print('ry',j.get_axis(3)) 
            if event.type == pygame.JOYBUTTONDOWN:
                print(event.button, 'Down')
            if event.type == pygame.JOYBUTTONUP:
                print(event.button, 'Up')
gameLoop() 
pygame.joystick.quit()

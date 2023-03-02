import sys, pygame, os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

clk = pygame.time.Clock()

if pygame.joystick.get_count() == 0:
    raise IOError("No joystick detected")
joy = pygame.joystick.Joystick(0)
joy.init()

def buttonX(boton):
    if(boton==0): return 285
    elif(boton==1): return 315
    elif(boton==2): return 290
    elif(boton==3): return 255
    elif(boton==4): return 60
    elif(boton==5): return 295
    elif(boton==8): return 154
    elif(boton==9): return 195

def buttonY(boton):
    if(boton==0): return 65
    elif(boton==1): return 90
    elif(boton==2): return 113
    elif(boton==3): return 90
    elif(boton==4 or boton==5): return 11
    elif(boton==8): return 108
    elif(boton==9): return 110

size = width, height = 389,187
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Joystick Tester")
background_image = pygame.image.load("control_389x187.png").convert()
frameRect = pygame.Rect((0,0), (width,height))

crosshair = pygame.surface.Surface((10,10))
crosshair.fill(pygame.Color("magenta"))
pygame.draw.circle(crosshair,pygame.Color("blue"), (5,5), 5, 0)
crosshair.set_colorkey(pygame.Color("magenta"))

crosshairb = pygame.surface.Surface((25,25))
crosshairb.fill(pygame.Color("magenta"))
pygame.draw.circle(crosshairb,pygame.Color("green"), (5,5), 5, 0)
crosshairb.set_colorkey(pygame.Color("magenta"))



buttons = {}
for b in range(joy.get_numbuttons()):
    buttons[b] = [
        crosshair,
        (buttonX(b),buttonY(b))
    ]
    print(buttons)


while True:
    pygame.event.pump()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background_image, (0,0))


    x=joy.get_axis(0)
    y=joy.get_axis(1)
    screen.blit(crosshairb,((x*25)+90,(y*25)+90))
    
    for b in range(joy.get_numbuttons()):
        if joy.get_button(b):
            screen.blit(buttons[b][0], buttons[b][1])

    pygame.display.flip()
    clk.tick(40)


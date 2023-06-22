import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

bg = pygame.image.load('bg.png')
char = pygame.image.load('player.png')


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.standing = True
        self.hitbox = (self.x, self.y, 50, 50)

    def draw(self, win):
        win.blit(char,(self.x, self.y))
        self.hitbox = (self.x, self.y, 50, 50)
        pygame.draw.rect(win, (0,255,0), self.hitbox,2)

def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    
    pygame.display.update()



#mainloop
man = player(200, 410, 50,50)
keys = pygame.key.get_pressed()
run = True
while run:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    redrawGameWindow()

pygame.quit()

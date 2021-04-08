import sys,pygame
pygame.init()
"Leandro.teste"
size = width,height=1000,700
speed = [1,1]
velocidade =[1,1]
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load('tenor.gif')
ball2 = pygame.image.load('aa.gif')

ballrect = ball.get_rect()
ballrect2 = ball2.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed)
    ballrect2 = ballrect2.move(velocidade)

    if ballrect2.left < 0 or ballrect.right > width:
        velocidade[0] = -velocidade[0]
    if ballrect2.top < 0 or ballrect.bottom > height:
        velocidade[1] = -velocidade[1]
    
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(ball,ballrect)
    screen.blit(ball2,ballrect2)
    pygame.display.flip()

If __name__ == 'main':
    Print('oi')

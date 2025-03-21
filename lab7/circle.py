import pygame

pygame.init()
screen=pygame.display.set_mode((400,300))
done = False
is_blue=True
x=30
y=30
m_w = 400
m_h = 300
clock=pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            is_blue=not is_blue

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-=20
    elif pressed[pygame.K_DOWN]: y+=20
    elif pressed[pygame.K_LEFT]: x-=20
    elif pressed[pygame.K_RIGHT]: x+=20
    
    if x > m_w: x = m_w
    if y > m_h: 
        y = m_h
    if x < 0: x = 0
    if y < 0: y = 0

    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,0,0), (x,y),10)

    pygame.display.flip()
    clock.tick(60)

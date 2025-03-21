import pygame
import os

screen=pygame.display.set_mode((400,300))
done = False
clock=pygame.time.Clock()

# image0=pygame.image.load('mickeyclock.jpeg')
image0=pygame.image.load('mickey.png')
image0=pygame.transform.scale(image0,(400,300))
minute_hand=pygame.image.load('rh.png')
hour_hand=pygame.image.load('lh.png')
minute_hand=pygame.transform.scale(minute_hand,(400,300))
hour_hand=pygame.transform.scale(hour_hand,(400,300))

# ratio1=250/168
# ratio2=194/163
# scale1=75
# scale2=55
# minute_hand=pygame.transform.scale(minute_hand,(scale1,scale1/ratio1))
# hour_hand=pygame.transform.scale(hour_hand,(scale2,scale2/ratio2))

def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
  
    # draw rectangle around the image
    # pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)

def blitRotate2(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)

image = pygame.image.load('lh.png')
image=pygame.transform.scale(image,(400,300))
w, h = image.get_size()

angle = 0

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    # screen.fill((255,255,255))
    # surface=pygame.Surface((100,100))
    # screen.blit(surface, (50,20))
    screen.blit(image0,(0,0))
    # screen.blit(minute_hand,(190,110))
    # screen.blit(hour_hand,(150,110))
    screen.blit(minute_hand,(0,0))
    screen.blit(hour_hand,(0,0))

    pos = (screen.get_width()/2, screen.get_height()/2)
    
    # screen.fill(0)
    blitRotate(screen, image, pos, (w/2, h/2), angle)
    #blitRotate2(screen, image, pos, angle)
    angle += 1

    pygame.display.flip()
    clock.tick(60)

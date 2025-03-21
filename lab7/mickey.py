import pygame
import time

screen=pygame.display.set_mode((400,300))
done = False
clock=pygame.time.Clock()

image0=pygame.image.load('mickey.png')
image0=pygame.transform.scale(image0,(400,300))

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

image = pygame.image.load('lh.png')
image=pygame.transform.scale(image,(400,300))
w, h = image.get_size()

image2 = pygame.image.load('rh.png')
image2=pygame.transform.scale(image2,(400,300))
w2, h2 = image2.get_size()

angle = 0
angle2 = 0

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    screen.blit(image0,(0,0))

    pos = (screen.get_width()/2, screen.get_height()/2)

    minutes, seconds = time.strftime("%M", time.localtime()),time.strftime("%S", time.localtime())
    angle=-6*int(minutes)-50
    angle2=-6*int(seconds)+60
    print((int(minutes))%360)

    blitRotate(screen, image, pos, (w/2, h/2), angle)
    blitRotate(screen, image2, pos, (w2/2, h2/2), angle2)

    pygame.display.flip()
    clock.tick(1)

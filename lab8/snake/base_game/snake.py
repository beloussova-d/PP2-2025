import pygame
from game_object import GameObject 
from worm import Worm
from food import Food
from wall import Wall

def create_background(screen, width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(screen, colors[(row + col) % 2],pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width

done = False


pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

worm = Worm(20)
food = Food(20)
wall = Wall(20)
food.move(worm.points, wall.points)


score = 0
prevscore=0
font = pygame.font.SysFont(None, 24)

speed = 5  # initial speed (frames per second)

while not done:
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            else:
                filtered_events.append(event)

        worm.process_input(filtered_events)
        worm.move()
        # Check collision with wall
        for wall_point in wall.points:
                if worm.points[0].X == wall_point.X and worm.points[0].Y == wall_point.Y:
                        done = True  # Game Over

        # # Check collision with self
        # for body_point in worm.points[1:]:
        #         if worm.points[0].X == body_point.X and worm.points[0].Y == body_point.Y:
        #                 done = True  # Game Over

        pos = food.can_eat(worm.points[0])
        
        if(pos != None):
            worm.increase(pos)
            food.move(worm.points, wall.points)
            score += food.weight
        #     if len(worm.points) % 3 == 0:
        #         wall.next_level()       
            if score % 3 == 0 or score-prevscore>=3:
                wall.next_level()    
                prevscore=score 
                speed += 1

        create_background(screen, 400, 300)
        
        food.update(worm.points, wall.points)
        food.draw(screen)
        wall.draw(screen)
        worm.draw(screen)
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        lvl_text = font.render(f'Level: {wall.level}', True, (0, 0, 0))
        screen.blit(lvl_text, (300, 10))
        
        pygame.display.flip()
        clock.tick(speed)
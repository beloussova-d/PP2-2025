import pygame
from game_object import GameObject 
from worm import Worm
from food import Food
from wall import Wall

import psycopg2
from config import load_config
def insert_user(user_name):
        """ Insert a new vendor into the vendors table """
        sql = """INSERT INTO snake (user_name, level, score)
                VALUES (%s, 0, 0)
                ON CONFLICT (user_name) DO NOTHING; 
                """

        config = load_config()
        try:
                with  psycopg2.connect(**config) as conn:
                        with  conn.cursor() as cur:
                                # execute the INSERT statement
                                cur.execute(sql, (user_name,))
                                conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

def data_update(score,level,user_name):
        sql="""UPDATE snake
                SET score=%s, level = %s
                WHERE user_name = %s
                """
        config = load_config()
        try:
                with  psycopg2.connect(**config) as conn:
                        with  conn.cursor() as cur:
                                # execute the INSERT statement
                                cur.execute(sql, (score,level,user_name))
                                conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

def get_score_and_lvl(user_name):
        score_and_level=()
        """ Retrieve data from the table """
        sql1="""SELECT score,level FROM snake WHERE user_name=%s"""
        config  = load_config()
        try:
                with psycopg2.connect(**config) as conn:
                        with conn.cursor() as cur:
                                cur.execute(sql1,(user_name,))
                                score_and_level = cur.fetchone()
                                print(score_and_level)
        except (Exception, psycopg2.DatabaseError) as error:
                print(error)
        return score_and_level


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
wall.load_level()
food.move(worm.points, wall.points)

score = 0
prevscore=0
font = pygame.font.SysFont(None, 24)

speed = 5  # initial speed (frames per second)

menu=True
active=False
user_text = '' 
input_rect = pygame.Rect(160, 10, 100, 20)
if menu: 
        input_text = font.render('Input username: ', True, (255, 255, 255))
        screen.blit(input_text, (10, 10))
        pygame.draw.rect(screen, (200,200,200), input_rect)
        pressed=pygame.key.get_pressed()
        while True:
                if not menu:
                        insert_user(user_text)
                        # print(user_text)
                        break
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: 
                                pygame.quit() 
                                sys.exit() 
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                        menu=False
                                # Check for backspace 
                                elif event.key == pygame.K_BACKSPACE: 
                                        # get text input from 0 to -1 i.e. end. 
                                        user_text = user_text[:-1] 
                                # Unicode standard is used for string 
                                # formation 
                                else: 
                                        user_text += event.unicode
                        # if event.type == pygame.MOUSEBUTTONDOWN: 
                        #         if input_rect.collidepoint(event.pos): 
                        #                 active = True
                        #         else: 
                        #                 active = False 
                pygame.draw.rect(screen, (200,200,200), input_rect)
                text_surface = font.render(user_text, True, (0,0,0)) 
      
                # render at position stated in arguments 
                screen.blit(text_surface, (165, 15)) 
                
                # set width of textfield so that text cannot get 
                # outside of user's text input 
                pygame.display.flip()
                clock.tick(15)

paused=False
data=get_score_and_lvl(user_text)
score=data[0]
# print(data[1])
wall.start_level(data[1])
while not done:
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused
                if paused: 
                        data_update(score,wall.level,user_text)
            else:
                filtered_events.append(event)
        if paused:
                pass
                # data_update(score,wall.level,user_text)
                # screen.blit(font.render('Paused', False, (0, 0, 0)), (100, 100))
        else:
                worm.process_input(filtered_events)
                worm.move()
                food.update(worm.points, wall.points)

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
        
        food.draw(screen)
        wall.draw(screen)
        worm.draw(screen)
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        lvl_text = font.render(f'Level: {wall.level}', True, (0, 0, 0))
        screen.blit(lvl_text, (300, 10))
        
        pygame.display.flip()
        clock.tick(speed)
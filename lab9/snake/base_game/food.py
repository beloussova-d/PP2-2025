import pygame
import random
import time
from game_object import GameObject 
from game_object import Point 

class Food(GameObject):
    def __init__(self, tile_width):
        # x=random.randint(0, 400)
        # x=x-x%20
        # y=random.randint(0, 300)
        # y=y-y%20
        super().__init__([Point(0, 0)], (0, 255, 0), tile_width)
        self.move([], [])
        
        # super().__init__([Point(x, y)],(0,255,0), tile_width)
    def move(self, worm_points, wall_points):
        self.weight=random.randint(1, 3)
        self.spawn_time = time.time()  # reset the timer on spawn

        # Set color based on weight (optional visual cue)
        if self.weight == 1:
            self.color = (0, 255, 0)  # green
        elif self.weight == 2:
            self.color = (0, 200, 0)  # darker green
        else:
            self.color = (0, 150, 0)  # even darker green

        while True:
            x = random.randint(0, 380)
            y = random.randint(0, 280)
            x = x - (x % 20)
            y = y - (y % 20)

            # Create new potential position
            new_point = Point(x, y)

            # Check if it overlaps with worm or wall
            if any(p.X == new_point.X and p.Y == new_point.Y for p in worm_points):
                continue
            if any(p.X == new_point.X and p.Y == new_point.Y for p in wall_points):
                continue

            self.points[0] = new_point
            break
    def update(self, worm_points, wall_points):
        if self.weight == 3 and (time.time() - self.spawn_time > 3):
            self.move(worm_points, wall_points)
    def can_eat(self, head_location):
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
                break
        return result

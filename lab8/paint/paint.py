import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    rectangles = []  # store (start, end, mode) for each rectangle
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    drawing = False
    drawing_rect = False
    rect_start = None
    rect_end = None

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        s_held = pressed[pygame.K_s]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_q:
                    points = []
                    rectangles = []


            if event.type == pygame.MOUSEBUTTONDOWN:
                if s_held:
                    drawing_rect = True
                    rect_start = event.pos
                    rect_end = event.pos
                else:
                    if event.button == 1:
                        drawing = True
                if event.button == 3:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    drawing = False
                if drawing_rect:
                    rect_end = event.pos
                    rectangles.append((rect_start, rect_end, mode))  # store it!
                    drawing_rect = False
                    rect_start = None
                    rect_end = None


            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    position = event.pos
                    points = points + [(position, mode)]
                    points = points[-256:]
                if drawing_rect:
                    rect_end = event.pos

        screen.fill((0, 0, 0))
        
        # draw all freehand points
        i = 0
        while i < len(points) - 1:
            (start_pos, start_mode) = points[i]
            (end_pos, end_mode) = points[i + 1]
            drawLineBetween(screen, i, start_pos, end_pos, radius, start_mode)
            i += 1

        # live rectangle preview
        if drawing_rect and rect_start and rect_end:
            drawRectPreview(screen, rect_start, rect_end, mode)

        # draw all stored rectangles
        for start, end, rect_mode in rectangles:
            drawFilledRectangle(screen, start, end, rect_mode)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def getColor(mode):
    if mode == 'blue':
        return (100, 100, 255)
    elif mode == 'red':
        return (255, 100, 100)
    elif mode == 'green':
        return (100, 255, 100)
    return (255, 255, 255)

def drawFilledRectangle(screen, start, end, mode):
    color = getColor(mode)
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                       abs(start[0] - end[0]), abs(start[1] - end[1]))
    pygame.draw.rect(screen, color, rect)

def drawRectPreview(screen, start, end, mode):
    color = getColor(mode)
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                       abs(start[0] - end[0]), abs(start[1] - end[1]))
    pygame.draw.rect(screen, color, rect, 2)  # outline only for preview

main()

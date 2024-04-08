import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    color = 'blue'
    mode = 'line'

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE  = (0, 0, 255)



    points = []
    drawing = False

    red_square = pygame.Rect(10, 10, 30, 30)
    green_square = pygame.Rect(50, 10, 30, 30)
    blue_square = pygame.Rect(90, 10, 30, 30)




    eraser_mode = False


    font = pygame.font.SysFont('timesnewroman', 25) 

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]




        
        for event in pygame.event.get():
            
            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed 
                if event.key == pygame.K_r:
                    color = 'red'
                elif event.key == pygame.K_g:
                    color = 'green'
                elif event.key == pygame.K_b:
                    color = 'blue'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_t:
                    mode = 'rectangle'
                elif event.key == pygame.K_l:
                    mode = 'line'
                elif event.key == pygame.K_e:
                    eraser_mode = True if not eraser_mode else False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius 
                    drawing = True
                    if not eraser_mode:
                        radius = min(200, radius + 1)
                    if red_square.collidepoint(event.pos):
                        color = 'red'
                    elif green_square.collidepoint(event.pos):
                        color = 'green'
                    elif blue_square.collidepoint(event.pos):
                        color = 'blue'

                elif event.button == 3: # right click shrinks radius
                    drawing = True
                    if not eraser_mode:
                        radius = max(1, radius - 1)
                 
            
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list 
                if drawing and not eraser_mode:
                    position = event.pos + (mode,)
                    points = points + [position]
                    points = points[-256:]

                if drawing and eraser_mode:
                    for point in points:
                        if pygame.Rect(point[0] - radius, point[1] - radius, radius * 2, radius * 2).collidepoint(event.pos):
                            points.remove(point)
                
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 0, 0), red_square)
        pygame.draw.rect(screen, (0, 255, 0), green_square)
        pygame.draw.rect(screen, (0, 0, 255), blue_square)
        
        
        # draw all points 
        i = 0
        while i < len(points) - 1:
            if points[i][2] == 'circle':
                pygame.draw.circle(screen, getColor(color, i), points[i][:2], radius*1.5)
     

            elif points[i][2] == 'rectangle':
                pygame.draw.rect(screen, getColor(color, i), (points[i][0], points[i][1], radius*2, radius*2))
            elif points[i][2] == 'line':
                drawLineBetween(screen, i, points[i][:2], points[i + 1][:2], radius, color)

            i += 1

        if eraser_mode:
            text = font.render("Eraser: on", True, WHITE)
        else:
            text = font.render("Eraser: off", True, WHITE)

        # Calculate the position for the text to be at the top center of the screen
        text_rect = text.get_rect(center=(screen.get_width() / 2, text.get_height() / 2))

        # Draw the text onto the screen
        screen.blit(text, text_rect)
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    

    if color_mode == 'blue':
        line_color = (c1, c1, c2)
    elif color_mode == 'red':
        line_color = (c2, c1, c1)
    elif color_mode == 'green':
        line_color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, line_color, (x, y), width)

def getColor(color_mode, index):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    return color

def drawRectangle(screen, coords, w, h, color):
    x = coords[0]
    y = coords[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3) 
    # drawRectangle(screen, pygame.mouse.get_pos(), 100, 50, getColor(color, i))


def drawCircle(screen, mouse_pos, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.circle(screen, color, (x, y), 100, 3) 


main()

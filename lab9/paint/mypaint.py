import pygame, random, math
pygame.init()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SHADOW = (192, 192, 192)
ORANGE = (255,100,10)
GREY = (127,127,127)
NAVY_BLUE = (0,0,100)
POWDERBLUE = (176, 224, 230, 255)
YELLOW = (255, 255, 0)
PURPLE = (153, 0, 153)


def draw_line(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    
    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)



def draw_right_triangle(surface, start, end, color):
    pygame.draw.polygon(surface, color, [start, end, (start[0], end[1])])

def draw_equilateral_triangle(surface, start, end, color):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    pygame.draw.polygon(surface, color, [start, end, (start[0] + dx / 2, start[1] + dy / 2)])

def draw_rhombus(surface, start, end, color):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    pygame.draw.polygon(surface, color, [start, (start[0] + dx / 2, start[1]), end, (start[0], start[1] + dy / 2)])


def main():
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('pain(t)')
    # icon = pygame.image.load('img/icon.png')
    # pygame.display.set_icon(icon)

    screen.fill(WHITE)

    toolsPannel = pygame.Rect(0, 0, 1000, 100)
    pygame.draw.rect(screen, 'gray', toolsPannel)

    font = pygame.font.SysFont("Verdana", 20)
    brush_png = pygame.transform.scale(pygame.image.load("img/brush.png"), (20,20))
    eraser_png = pygame.transform.scale(pygame.image.load("img/eraser.png"), (20,20))
    clear_png = pygame.transform.scale(pygame.image.load("img/clear.png"), (20,20))


    global brush, eraser, clear, save
    # screen.blit(clear_png, (30, 25)) 
    screen.blit(brush_png, (80, 25))
    screen.blit(eraser_png, (30, 25))
    screen.blit(clear_png, (130, 25))

    squareRect = pygame.Rect(30, 70, 25, 15)
    circleRect = pygame.Rect(70, 70, 25, 15)



    pygame.draw.rect(screen, BLACK, squareRect, 2)
    pygame.draw.circle(screen, BLACK, (85, 77), 9, 2)
    
    # pravi verh levi niz
    rhombusButton = pygame.draw.polygon(screen, 'black', [(110, 75), (120, 65), (130, 75), (120, 88)], 3)
    # verh prava niz
    rtriangleButton = pygame.draw.polygon(screen, 'black', [(150, 65), (175, 85), (150, 85)], 3)
    #levi praviy
    eqtriangleButton = pygame.draw.polygon(screen, 'black', [(190, 85), (210, 85), (200, 65)], 3)

    

    red_square = pygame.Rect(800, 10, 30, 30)
    green_square = pygame.Rect(840, 10, 30, 30)
    blue_square = pygame.Rect(880, 10, 30, 30)

    clr_rect_list = [red_square, green_square, blue_square]
    clr_list = [RED, GREEN, BLUE]

    pygame.draw.rect(screen, RED, red_square)
    pygame.draw.rect(screen, GREEN, green_square)
    pygame.draw.rect(screen, BLUE, blue_square)

    eraserRect = pygame.Rect(30, 25, 20, 20)
    brushRect = pygame.Rect(80, 25, 20, 20)
    clearRect = pygame.Rect(130, 25, 20, 20)

    draw_surf = pygame.Surface((1000, 600)) 
    draw_surf.fill(WHITE)  # Fill the surface with white color
    screen.blit(draw_surf, (0, 100))


    mode = 'none'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 5
    thickness = 2
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and alt_held:
                    return
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                if (mode == 'brush' or mode == 'eraser') and radius > 2:
                    radius -= 2
                elif (mode == 'rect' or mode == 'circle') and thickness > 1:
                    thickness -= 1
                # mode_check(mode, color)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                if (mode == 'brush' or mode == 'eraser') and radius < 37:
                    radius += 2
                elif (mode == 'rect' or mode == 'circle') and thickness < 10:
                    thickness += 1
                # mode_check(mode, color)
            

            # draw/eraser modes
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                global button

                print(x, y)

                if brushRect.collidepoint(x, y):
                    radius = 10
                    if mode != 'brush':
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        mode = 'brush'

                if eraserRect.collidepoint(x, y):
                    radius = 10
                    if mode != 'eraser':
                        mode = 'eraser'
                        color = WHITE

                if clearRect.collidepoint(x, y):
                    draw_surf.fill(WHITE)
                    screen.blit(draw_surf, (0, 101))

                # square 
                if squareRect.collidepoint(x, y):
                    if mode != 'rect':
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        mode = 'rect'

                if circleRect.collidepoint(x, y):
                    if mode != 'circle':
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        mode = 'circle'

                if rtriangleButton.collidepoint(x, y):
                    if mode != 'rtriangle':
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        mode = 'rtriangle'
                
                if rhombusButton.collidepoint(x, y):
                    if mode != 'rhombus':
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        mode = 'rhombus'

                if eqtriangleButton.collidepoint(x, y):
                    if mode != 'eqtriangle':
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        mode = 'eqtriangle'

                if mode == 'brush' or mode == 'rect' or mode == 'circle':
                    for i, col in enumerate(clr_rect_list, 0):
                        if col.collidepoint(x, y):
                            color = clr_list[i]


                print('MODE = ', mode)

                

                # def mode_check(mode, color):
                #     if mode == 'none':
                #         color = WHITE
        
                #     if mode == 'brush':
                #         screen.fill(WHITE, (912, 337, 77, 77))
                #         pygame.draw.circle(screen, color, (950, 375), radius)
                #     elif mode == 'rect':
                #         screen.fill(WHITE, (912, 337, 77, 77))
                #         pygame.draw.rect(screen, color, (930, 355, 40, 40), thickness)
                #     elif mode == 'circle':
                #         screen.fill(WHITE, (912, 337, 77, 77))
                #         pygame.draw.circle(screen, color, (950, 375), 30, thickness)
                #     elif mode == 'eraser':
                #         screen.fill(WHITE, (912, 337, 77, 77))
                #         pygame.draw.circle(screen, GREY, (950, 375), radius, 2)

            
                if mode == 'brush' or mode == 'eraser':
                    pygame.draw.circle(draw_surf, color, (event.pos[0], event.pos[1]-100), radius)
                    screen.blit(draw_surf, (0, 101))

                draw_on = True
                # mode_check(mode, color)
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                draw_on = False
                x2, y2 = event.pos
                if x > x2:
                    x, x2 = x2, x
                if y > y2:
                    y, y2 = y2, y

                if mode == 'rect':
                    pygame.draw.rect(draw_surf, color, (x-3, y-3 - 100, abs(x2 - (x-3)-3), abs(y2 - (y-3)-3)), thickness)
                    screen.blit(draw_surf, (0, 101))

                elif mode == 'circle':
                    pygame.draw.ellipse(draw_surf, color, (x-3, y-3 - 100, abs(x2 - (x-3)-3), abs(y2 - (y-3)-3)), thickness)
                    screen.blit(draw_surf, (0, 101))

                elif mode == 'rtriangle':
                    draw_right_triangle(draw_surf, (x-3, y-3 - 100), (x2-3, y2-3 - 100), color)
                elif mode == 'eqtriangle':
                    draw_equilateral_triangle(draw_surf, (x-3, y-3 - 100), (x2-3, y2-3 - 100), color)
                elif mode == 'rhombus':
                    draw_rhombus(draw_surf, (x-3, y-3 - 100), (x2-3, y2-3 - 100), color)
                
 
            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    if mode == 'brush' or mode == 'eraser':

                        draw_line(draw_surf, (last_pos[0], last_pos[1] - 100), (event.pos[0], event.pos[1] - 100), radius, color)
                        # drawLineBetween(draw_surf, last_pos, event.pos, radius, color)
                        screen.blit(draw_surf, (0, 101))

                last_pos = event.pos





 


        pygame.display.flip()



main()
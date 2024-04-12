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


def main():
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('pain(t)')
    icon = pygame.image.load('img/icon.png')
    pygame.display.set_icon(icon)

    screen.fill(WHITE)

    rect = pygame.Rect(0, 0, 1000, 100)
    pygame.draw.rect(screen, GREY, rect)

    font = pygame.font.SysFont("Verdana", 20)
    brush_png = pygame.transform.scale(pygame.image.load("img/brush.png"), (20,20))
    eraser_png = pygame.transform.scale(pygame.image.load("img/eraser.png"), (20,20))
    # clear_png = pygame.transform.scale(pygame.image.load("img/clear.png"), (30, 30))
    save_png = pygame.transform.scale(pygame.image.load("img/save.png"), (98, 50))


    global brush, eraser, clear, save
    # screen.blit(clear_png, (30, 25)) 
    screen.blit(brush_png, (80, 25))
    screen.blit(eraser_png, (30, 25))

    pygame.draw.rect(screen, BLUE, (30, 70, 25, 15), 2)
    pygame.draw.circle(screen, BLACK, (85, 77), 9, 2)
        

    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and alt_held:
                    return
                
        pygame.display.flip()


main()
import pygame
import zad1


if __name__ == "__main__":
    xRes = 600
    yRes = 600

    pygame.init()
    win = pygame.display.set_mode((xRes, yRes))
    rect_surface = pygame.surface.Surface((xRes, yRes))
    
    run = True
    firstDraw = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        x = 150
        y = 150
        
        tr1 = [[x, y],[x + 50, y],[x + 25, y + 50]]
        rect = [[x - 25, y + 50], [x + 75, y + 50], [x + 75, y + 100], [x - 25, y + 100]]
        tr2 = [[x, y + 150],[x + 50, y + 150],[x + 25, y + 100]]

        pygame.draw.polygon(win, (0, 0, 255), tr1)
        pygame.draw.polygon(win, (0, 0, 255), rect)
        pygame.draw.polygon(win, (0, 0, 255), tr2)

        pygame.display.update()

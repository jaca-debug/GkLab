import pygame
import math

def rotate_points_around_pivot(points, pivot, angle):
    pp = pygame.math.Vector2(pivot)
    rotated_points = [
        (pygame.math.Vector2(x, y) - pp).rotate(angle) + pp for x, y in points]
    return rotated_points

def getRegularPolygon(numSides, x, y, radius, rotateAngle=None, piv=None, existingPts=None):
  pts = []
  if existingPts is not None:
    pts = existingPts
    pts = rotate_points_around_pivot(pts, piv, rotateAngle)
    return pts
  for i in range(numSides):
    x = x + radius * math.cos(math.pi * 2 * i / numSides)
    y = y + radius * math.sin(math.pi * 2 * i / numSides)
    pts.append([int(x), int(y)])

  if rotateAngle is not None:
    pts = rotate_points_around_pivot(pts, piv, rotateAngle)
  
  return pts

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

        KOLOR = (35 , 229 , 96)
        srednica = 100


        pygame.draw.polygon(rect_surface, KOLOR, getRegularPolygon(11, 250, 150, srednica))
        x = 250
        y = 150

        if firstDraw:
            rect_surface.fill((255, 225, 0))
            pygame.draw.polygon(rect_surface, KOLOR, getRegularPolygon(11, x, y, srednica / 2))
            win.blit(rect_surface, (0, 0))

        firstDraw = False
        keynum = 0
        for key in pygame.key.get_pressed():
            if key:
                match keynum:
                    case 30:
                        win.fill((255, 225 , 0))
                        rect_surface.fill((255, 225, 0))
                        pygame.draw.polygon(rect_surface, KOLOR, getRegularPolygon(11, x, y, srednica / 2))
                        win.blit(rect_surface, (0, 0))
                    case 31:
                        win.fill((255, 225 , 0))
                        rect_surface.fill((255, 225, 0))
                        pygame.draw.polygon(rect_surface, KOLOR, getRegularPolygon(11, x, y, srednica, 45, (x+ 50, y + 100)))
                        win.blit(rect_surface, (0, 0))
                    case 32:
                        win.fill((255, 225 , 0))
                        rect_surface.fill((255, 225, 0))
                        pygame.draw.polygon(rect_surface, KOLOR, getRegularPolygon(11, x, y, srednica))
                        modified_surf = pygame.transform.flip(rect_surface, False, True)
                        win.blit(modified_surf, (0, 0))
                        
                    # x' = x + ay
                    # y' = y
                    case 33:
                        win.fill((255, 225 , 0))
                        rect_surface.fill((255, 225, 0))
                        pts = getRegularPolygon(11, x, y, srednica)

                        tiltedPts = []
                        for i in range(0, 11):
                            xPrim = 0
                            yPrim = 0
                            xPrim = pts[i][0] + 0.3 * pts[i][1]
                            yPrim = pts[i][1]
                            tiltedPts.append([xPrim, yPrim])

                        pygame.draw.polygon(rect_surface, KOLOR, tiltedPts)
                        win.blit(rect_surface, (0, 0))
                    case 34:
                        win.fill((255, 225 , 0))
                        rect_surface.fill((255, 225, 0))
                        pygame.draw.polygon(rect_surface, KOLOR, getRegularPolygon(11, x + 100, y, srednica))
                        modified_surf = pygame.transform.scale(rect_surface, (400, 200))
                        win.blit(modified_surf, (0, 0))
                    case 35:
                        win.fill((255, 225 , 0))
                        rect_surface.fill((255, 225, 0))
                        pts = getRegularPolygon(11, x, y, srednica)

                        tiltedPts = []
                        for i in range(0, 11):
                            xPrim = 0
                            yPrim = 0
                            xPrim = pts[i][0] + 0.3 * pts[i][1]
                            yPrim = pts[i][1]
                            tiltedPts.append([xPrim, yPrim])

                        pygame.draw.polygon(rect_surface, KOLOR, getRegularPolygon(0,0,0,0, 90, (x + 100, y), tiltedPts))
                        win.blit(rect_surface, (50, 100))
                    case 36:
                        win.fill((255, 225 , 0))
                        rect_surface.fill((255, 225, 0))
                        pygame.draw.polygon(rect_surface, KOLOR, getRegularPolygon(11, x, y, srednica))
                        modified_surf = pygame.transform.scale(rect_surface, (200, 400))
                        win.blit(modified_surf, (200, 40))
                    case 37:
                        win.fill((255, 225 , 0))
                        rect_surface.fill((255, 225, 0))
                        pygame.draw.polygon(rect_surface, KOLOR, getRegularPolygon(11, x, y, srednica, 25, (x+ 50, y + 100)))
                        modified_surf = pygame.transform.scale(rect_surface, (400, 200))
                        win.blit(modified_surf, (50, 350))

                    # tu źle ale idk czemu
                    # x' = x
                    # y' = bx + y
                    case 38:
                        win.fill((255, 225 , 0))
                        rect_surface.fill((255, 225, 0))
                        pts = getRegularPolygon(11, x, y, srednica)

                        tiltedPts = []
                        for i in range(0, 11):
                            xPrim = 0
                            yPrim = 0
                            xPrim = pts[i][0]
                            yPrim = pts[i][0] * 0.3 + pts[i][1]
                            tiltedPts.append([xPrim, yPrim])

                        pygame.draw.polygon(rect_surface, KOLOR, tiltedPts)
                        win.blit(rect_surface, (0, 0))
                        # win.fill((255, 225 , 0))
                        # rect_surface.fill((255, 225, 0))
                        # pts = getRegularPolygon(11, x, y, srednica)
                        
                        # tiltedPts = []
                        # for i in range(0, 11):
                        #     xPrim = 0
                        #     yPrim = 0
                        #     xPrim = pts[i][0]
                        #     yPrim = pts[i][1] + 0.3 * pts[i][0]
                        #     tiltedPts.append([xPrim, yPrim])

                        # pygame.draw.polygon(rect_surface, KOLOR, tiltedPts)
                        # #modified_surf = pygame.transform.flip(rect_surface, False, True)
                        # win.blit(rect_surface, (0, 0))
                    case _:
                        print('nic')
            keynum += 1
        

        pygame.display.update()

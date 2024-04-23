import pygame
import os
import random

def StatusUpdate(data, route, pHealth):
    i = 0
    for gegner, health, speed, posi, status in data:
        if posi[0] == route[status + 1][0]:
            if posi[1] == route[status + 1][1]:
                data[i][4] = data[i][4] + 1
                status = status + 1
                if status == len(route) - 1:
                    pHealth = pHealth - health
                    data.pop(i)
        i = i + 1
    return [data, pHealth]

def GegnerPosition(gegnerData, route, pHealth):
    dataX = StatusUpdate(gegnerData, route, pHealth)
    data = dataX[0]
    i = 0
    x = False
    for gegner, health, speed, posi, status in data:
        if posi[0] == route[status + 1][0]:
            if posi[1] > route[status + 1][1]:
                data[i][3] = (data[i][3][0], round(data[i][3][1] - speed, 1))
            else:
                data[i][3] = (data[i][3][0], round(data[i][3][1] + speed, 1)) 
        elif posi[1] == route[status + 1][1]:
            if posi[0] > route[status + 1][0]:
                data[i][3] = (round(data[i][3][0] - speed, 1), data[i][3][1])
            else:
                data[i][3] = (round(data[i][3][0] + speed, 1), data[i][3][1])
        else:
            print("Route error!")
        i = i + 1
        x = False
    return [data, dataX[1]]

def newGegner(gegnerData, route, wave):
    FIGUR_1_TERMINATOR = (pygame.image.load(os.path.join('assets\Figuren', 'Figur_1_Terminator.png')), 12, 0.5)
    FIGUR_2_LASER = (pygame.image.load(os.path.join('assets\Figuren', 'Figur_2_Laser.png')), 6, 1)
    FIGUR_3_GRASMONSTER = (pygame.image.load(os.path.join('assets\Figuren', 'Figur_3_Grasmonster.png')), 2, 2)
    data = gegnerData
    select = random.randrange(wave[0], wave[1])
    if select <= 10:
        gegnerSelect = FIGUR_1_TERMINATOR
    elif select <= 40:
        gegnerSelect = FIGUR_2_LASER
    elif select <= 100:
        gegnerSelect = FIGUR_3_GRASMONSTER
    row = [gegnerSelect[0], gegnerSelect[1], gegnerSelect[2], route[0], 0]
    data.append(row)
    return data
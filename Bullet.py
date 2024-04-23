import pygame
import os

def newBullet(towerData, bulletData):
    FEUERBALL = pygame.image.load(os.path.join('assets', 'Feuerball.png'))
    i = 0
    for tower, pos, speed, counter, damage in towerData:
        towerData[i][3] = towerData[i][3] - 1
        if towerData[i][3] == 0:
            row = [FEUERBALL, (pos[0] + 25, pos[1] + 25), damage]
            bulletData.append(row)
            towerData[i][3] = speed
        i = i + 1
    return [bulletData, towerData]

def BulletUpdate(bulletData):
    i = 0
    for bullet, pos, damage in bulletData:
        bulletData[i][1] = (pos[0] - 16, pos[1])
        if pos[0] < 0 and pos[1] > 1:
            bulletData.pop(i)
        i = i + 1
    return bulletData

def BulletCollision(bulletData, gegnerData):
    i = 0
    a = 0
    for bullet, posA, damageA in bulletData:
        for gegner, damageB, speed, posB, status in gegnerData:
            if posA[0] >= posB[0]:
                if posA[0] + 3 <= posB[0] + 50:
                    if posA[1] + 3 >= posB[1]:
                        if posA[1] + 3 <= posB[1] + 50:
                            if damageB - damageA <= 0:
                                gegnerData.pop(a)
                            else:
                                gegnerData[a][1] = damageB - damageA
                            bulletData.pop(i)
                            break                           
            a = a + 1
        a = 0
        i = i + 1
    return [bulletData, gegnerData]
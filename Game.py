import pygame
import os
import Game_Menu
import Gegner
import Bullet

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1200, 700
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tower Defence")
        
        self.FPS = 60
        self.RATE = 0.02
        self.ROUTE = [(0, 350), (100, 350), (100, 500), (300, 500), (300, 350), (350, 350), (350, 250), (200, 250), (200, 150), (600, 150), (600, 600), (1050, 600), (1050, 350), (1200,350)]
        self.spanwrate = 100
        self.spawncounter= 0
        self.WAVERATE= 1800

        self.TURM_1_ARMBRUST = [pygame.image.load(os.path.join('assets\Tuerme', 'Turm_1_Armbrust.png')), 90, 25, 1]
        self.TURM_2_KANONE = [pygame.image.load(os.path.join('assets\Tuerme', 'Turm_2_Kanone.png')), 80, 30, 1]
        self.TURM_3_MAGIER = [pygame.image.load(os.path.join('assets\Tuerme', 'Turm_3_Magier.png')), 110, 35, 2]
        self.TURM_4_DOPPELTE_ARMBRUST = [pygame.image.load(os.path.join('assets\Tuerme', 'Turm_4_doppelte_Armbrust.png')), 160, 25, 3]
        self.TURM_5_STEINKANONE = [pygame.image.load(os.path.join('assets\Tuerme', 'Turm_5_Steinkanone.png')), 200, 20, 4]

        self.cursor = (0, 0)
        self.mouse_presses = (False, False, False)
        self.tower_select = self.TURM_1_ARMBRUST
        self.balance = self.TURM_1_ARMBRUST[1]
        self.playerHealth = 100

        self.towerdata = []
        self.gegnerdata = []
        self.bulletdata = []

        self.wave = (0, 100)

        self.font = pygame.font.Font(pygame.font.get_default_font(), 18)

    def draw_window_standard(self):
        self.WIN.fill((0, 0, 255))
        self.WIN.blit(self.TURM_1_ARMBRUST[0], (20, 630))
        self.WIN.blit(self.TURM_2_KANONE[0], (90, 630))
        self.WIN.blit(self.TURM_3_MAGIER[0], (160, 630))
        self.WIN.blit(self.TURM_4_DOPPELTE_ARMBRUST[0], (230, 630))
        self.WIN.blit(self.TURM_5_STEINKANONE[0], (300, 630))
    
    def newTower(self):
        if self.mouse_presses[0]:
            pos = (self.cursor[0] - 25, self.cursor[1] - 25)
            row = [self.tower_select[0], pos, self.tower_select[2],  self.tower_select[2], self.tower_select[3]]
            if self.balance >= self.tower_select[1]:
                self.towerdata.append(row)
                self.balance = self.balance - self.tower_select[1]
        self.mouse_presses = (False, False, False)

    def draw_window(self):
        self.draw_window_standard()
        for tower, pos, speed, counter, damage in self.towerdata:
            self.WIN.blit(tower, pos)
        dataY = Gegner.GegnerPosition(self.gegnerdata, self.ROUTE, self.playerHealth)
        self.gegnerdata = dataY[0]
        self.playerHealth = dataY[1]
        for gegner, health, speed, posi, status in self.gegnerdata:
            self.WIN.blit(gegner, posi)
        for bullet, posB, damage in self.bulletdata:
            self.WIN.blit(bullet, posB)
        text_surface = self.font.render('Balance: ' + str(round(self.balance)), True, (255,255,255))
        self.WIN.blit(text_surface, dest=(0,0))
        text_surface = self.font.render('Health: ' + str(self.playerHealth), True, (255,255,255))
        self.WIN.blit(text_surface, dest=(160,0))
        text_surface = self.font.render('Spawnrate: ' + str(round(self.spanwrate)), True, (255,255,255))
        self.WIN.blit(text_surface, dest=(300,0))
        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        run = True
        spawnblock = 0
        while run:
            clock.tick(self.FPS)
            self.balance = self.balance + self.RATE
            self.spawncounter += 1
            self.cursor = pygame.mouse.get_pos()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.cursor[0] > 20 and self.cursor[0] < 70 and self.cursor[1] > 620 and self.cursor[1] < 680:
                        self.tower_select = self.TURM_1_ARMBRUST
                    elif self.cursor[0] > 90 and self.cursor[0] < 140 and self.cursor[1] > 620 and self.cursor[1] < 680:
                        self.tower_select = self.TURM_2_KANONE
                    elif self.cursor[0] > 160 and self.cursor[0] < 210 and self.cursor[1] > 620 and self.cursor[1] < 680:
                        self.tower_select = self.TURM_3_MAGIER
                    elif self.cursor[0] > 230 and self.cursor[0] < 280 and self.cursor[1] > 620 and self.cursor[1] < 680:
                        self.tower_select = self.TURM_4_DOPPELTE_ARMBRUST
                    elif self.cursor[0] > 300 and self.cursor[0] < 350 and self.cursor[1] > 620 and self.cursor[1] < 680:
                        self.tower_select = self.TURM_5_STEINKANONE
                    else:
                        self.mouse_presses = pygame.mouse.get_pressed()
                        self.newTower()

            spawnblock += 1
            if spawnblock > self.spanwrate:
                self.gegnerdata = Gegner.newGegner(self.gegnerdata, self.ROUTE, self.wave)
                spawnblock = 0
            
            if self.towerdata != []:
                dataR = Bullet.newBullet(self.towerdata, self.bulletdata)
                self.bulletdata = dataR[0]
                self.towerdata = dataR[1]

            self.bulletdata = Bullet.BulletUpdate(self.bulletdata)

            if self.bulletdata != []:
                dataA = Bullet.BulletCollision(self.bulletdata, self.gegnerdata)
                self.bulletdata = dataA[0]
                self.gegnerdata = dataA[1]

            if self.playerHealth <= 0 :
                run = False

            if self.spawncounter > self.WAVERATE:
                self.spanwrate = self.spanwrate * 0.9
                self.spawncounter = 0

            self.draw_window()

        pygame.quit()
        Game_Menu.main()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()

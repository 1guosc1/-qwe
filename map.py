import pygame
import openpyxl
class Game2():
    def __init__(self):
        global A,all_sprites,content
        f = open( 'map1.txt', 'r',encoding='utf-8')#访问文件
        content = f.read()
        content=content.split('\n')
        content=[[int(i) for i in j] for j in content]
        all_sprites = pygame.sprite.Group()
        A={}
        for i in range(20):
            A[i] = {}
            for j in range(25):
                if content[i][j] == 0:
                    A[i][j] = Map(j, i)
                    all_sprites.add(A[i][j])
        f.close()
    def kil(self):
        global B,content1
        for i in range(20):
            for j in range(25):
                if content[i][j] == 0:
                    A[i][j].kill()
        f = open( 'map2.txt', 'r',encoding='utf-8')#访问文件
        content1 = f.read()
        content1 = content1.split('\n')
        content1 = [[int(i) for i in j] for j in content1]
        B={}
        for i in range(23):
            B[i] = {}
            for j in range(30):
                if content1[i][j] == 0:
                    B[i][j] = Map(j, i)
                    all_sprites.add(B[i][j])
        f.close()
    def kil1(self):
        for i in range(23):
            for j in range(30):
                if content1[i][j] == 0:
                    B[i][j].kill()

        f = open( 'map3.txt', 'r',encoding='utf-8')#访问文件
        content2 = f.read()
        content2 = content2.split('\n')
        content2 = [[int(i) for i in j] for j in content2]
        C={}
        for i in range(24):
            C[i] = {}
            for j in range(60):
                if content2[i][j] == 0:
                    C[i][j] = Map(j, i)
                    all_sprites.add(C[i][j])

class Map(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill("black")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * 40, y * 40)
game2=Game2()
            








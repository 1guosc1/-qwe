import pygame
import sys
import map
from map import all_sprites,game2

# 在这里使用 all_sprites

class Q(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("25.png")
        self.original_image = self.image  # 保存原始图像
        self.rect = self.image.get_rect()
        self.flip = False  # 初始不翻转
    def move(self):
        self.rect.y,self.rect.x=0,0
    def flip_image(self):
        # 根据 flip 属性翻转图像
        self.image = pygame.transform.flip(self.original_image, True, False)
class Game():
    def __init__(self):
        global sc,clock,maliao,text,font ,cang,kuan,ch#地图的长宽
        ch=0
        pygame.init()
        cang,kuan=1000,800
        sc = pygame.display.set_mode((cang, kuan))
        pygame.display.set_caption("第一关：小试牛刀")
        maliao =Q()
        all_sprites.add(maliao)
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)  # 选择字体和字号
        text = font.render("Target", True, "red","blue" )  # 渲染文本
game=Game()
while True:
    if (maliao.rect.y+0.5*maliao.rect.height-kuan+80)**2+(maliao.rect.x+0.5*maliao.rect.width-cang+80)**2<800 and ch!=1 :
        ch=1
        maliao.move()
        cang, kuan = 1200, 920
        sc = pygame.display.set_mode((cang, kuan))
        pygame.display.set_caption("第二关：锋芒毕露")
        game2.kil()
    if (maliao.rect.y+0.5*maliao.rect.height-kuan+80)**2+(maliao.rect.x+0.5*maliao.rect.width-cang+80)**2<800 and ch==1:
        maliao.move()
        cang, kuan = 2400, 960
        sc = pygame.display.set_mode((cang, kuan))
        pygame.display.set_caption("第三关：汗流浃背了吧！")
        game2.kil1()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    maliaox,maliaoy=maliao.rect.x,maliao.rect.y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and maliao.rect.x - 2 > 0 :
        maliao.rect.x -= 2
        maliao.flip = True  # 设置翻转标志
    if keys[pygame.K_RIGHT] and maliao.rect.x + maliao.rect.width + 2 < cang :
        maliao.rect.x += 2
        maliao.flip = False  # 取消翻转标志
    if keys[pygame.K_UP] and maliao.rect.y - 2 > 0 :
        maliao.rect.y -= 2
    if keys[pygame.K_DOWN] and maliao.rect.y + maliao.rect.height + 2 < kuan:
        maliao.rect.y += 2
    all_sprites.remove(maliao)
    if pygame.sprite.spritecollide(maliao, all_sprites, False):
        maliao.rect.x, maliao.rect.y = maliaox, maliaoy
    all_sprites.add(maliao)
    text_rect = text.get_rect()
    text_rect.center = (cang-100,kuan- 80)
    sc.fill("white")
    sc.blit(text, text_rect.center)
    if maliao.flip :
        maliao.flip_image()
    else:
        maliao.image=pygame.image.load("25.png")
    all_sprites.draw(sc)  # 绘制精灵组中的所有精
    pygame.display.flip()
    clock.tick(600)

import pygame
import math
class Player(pygame.sprite.Sprite):
    def __init__(self,file_name):
        super(Player,self).__init__()
        self.score=0
        self.move_x=0
        self.move_y=0
        self.anim_count=0
        self.frame=0
        self.anim_down=[]
        self.anim_up=[]
        self.anim_left=[]
        self.anim_right=[]
        self.left=False
        self.right=False
        self.down=False
        self.up=False
        self.direction='D'
        self.status='I'
        self.sprite=SpriteCut(file_name,(235, 19, 215))
        w=self.sprite.sprites.get_width()
        h=self.sprite.sprites.get_height()

        pos = 0
        w=int(math.floor(w/12))


        for x in xrange(4):
            image = pygame.transform.scale(self.sprite.image_cut(pos,0,w,h),(42,60))
            self.anim_down.append(image)
            pos += w

        for x in xrange(4):
            image = pygame.transform.scale(self.sprite.image_cut(pos, 0, w, h), (42,60))
            self.anim_left.append(image)
            pos += w

        for x in xrange(4):
            image = pygame.transform.scale(self.sprite.image_cut(pos, 0, w, h), (42,60))
            self.anim_up.append(image)
            pos += w

        pos =w*4
        for x in xrange(4):
            image = pygame.transform.scale(self.sprite.image_cut(pos, 0, w, h), (42,60))
            image = pygame.transform.flip(image,True,False)
            self.anim_right.append(image)
            pos+=w

        self.image=self.anim_right[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect=self.image.get_rect()

    def update(self):
        self.update_movement()
        self.update_anim()

    def update_movement(self):
        if self.right is True and self.left is False and self.down is False and self.up is False:
            if self.rect.x<758:
                self.move_x=4
                self.move_y=0
                self.direction='R'
                self.status='M'
            else:
                self.move_x=0
                self.move_y=0
        if self.right is False and self.left is True and self.down is False and self.up is False:
            if self.rect.x>0:
                self.move_x=-4
                self.move_y=0
                self.direction='L'
                self.status = 'M'
            else:
                self.move_x=0
                self.move_y=0
        if self.right is False and self.left is False and self.down is True and self.up is False:
            if self.rect.y<540:
                self.move_x=0
                self.move_y=4
                self.direction='D'
                self.status = 'M'
            else:
                self.move_x=0
                self.move_y=0
        if self.right is False and self.left is False and self.down is False and self.up is True:
            if self.rect.y>0:
                self.move_x=0
                self.move_y=-4
                self.direction='U'
                self.status = 'M'
            else:
                self.move_y=0
                self.move_x=0
        if self.right is False and self.left is False and self.down is False and self.up is False:
            self.move_x = 0
            self.move_y = 0
            self.status = 'I'
        self.rect.x+=self.move_x
        self.rect.y+=self.move_y

    def update_anim(self):
        self.anim_count+=1
        if self.status=='I':
            if self.direction=='R':
                self.image=self.anim_right[0]
            elif self.direction=='L':
                self.image = self.anim_left[0]
            elif self.direction=='U':
                self.image = self.anim_up[0]
            elif self.direction=='D':
                self.image = self.anim_down[0]
            self.mask = pygame.mask.from_surface(self.image)
        elif self.status=='M':
            if self.direction=='R':
                self.image=self.anim_right[self.frame]
                if self.anim_count>=12:
                    self.anim_count = 0
                    if self.frame<3:
                        self.frame+=1
                    else:
                        self.frame=0
            elif self.direction=='L':
                self.image=self.anim_left[self.frame]
                if self.anim_count >= 12:
                    self.anim_count = 0
                    if self.frame<3:
                        self.frame+=1
                    else:
                        self.frame=0

            elif self.direction=='U':
                self.image=self.anim_up[self.frame]
                if self.anim_count >= 12:
                    self.anim_count = 0
                    if self.frame<3:
                        self.frame+=1
                    else:
                        self.frame=0
            elif self.direction=='D':
                self.image=self.anim_down[self.frame]
                if self.anim_count >= 12:
                    self.anim_count = 0
                    if self.frame<3:
                        self.frame+=1
                    else:
                        self.frame=0
            self.mask = pygame.mask.from_surface(self.image)

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super(Projectile,self).__init__()
        self.move_x = 0
        self.move_y = 0
        self.speed = 6
        self.image=pygame.transform.scale2x(pygame.image.load('images\misc\cannon_ball.png').convert())
        self.image.set_colorkey((235, 19, 215))
        self.rect=self.image.get_rect()
        self.direction=''
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.update_move()

    def update_move(self):
        self.mask = pygame.mask.from_surface(self.image)
        if self.direction=='R':
            self.move_x=1
            self.rect.x+=self.move_x*self.speed
        elif self.direction=='L':
            self.move_x = -1
            self.rect.x += self.move_x * self.speed
        elif self.direction=='D':
            self.move_y = 1
            self.rect.y += self.move_y * self.speed
        elif self.direction=='U':
            self.move_y = -1
            self.rect.y += self.move_y * self.speed

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super(Coins,self).__init__()
        self.sprite=SpriteCut('images\misc\coin_strip6.png',(235, 19, 215))
        self.frame=0
        self.count=0
        self.anim=[]

        pos = 0
        for x in xrange(6):
            image = self.sprite.image_cut(pos, 0, 30, 30)
            self.anim.append(image)
            pos += 30

        self.image=self.anim[0]
        self.rect=self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.count+=1
        self.image=self.anim[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        if self.count>=8:
            self.count=0
            if self.frame<5:
                self.frame+=1
            else:
                self.frame=0

class SpriteCut():
    def __init__(self,file_name,color):
        self.sprites=pygame.image.load(file_name).convert()
        self.sprites.set_colorkey(color)

    def image_cut(self,x,y,width,height):

        return self.sprites.subsurface(pygame.Rect((x,y),(width,height)))

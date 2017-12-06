#Programa Criado por George Dourado Aluno do curso de Jogos FATEC Carapicuiba
#v1.0
#Chamber of Death

import pygame , random
from TDC_classes import Player , Projectile , Coins

def shoot(a,b):
    side = random.randint(1,4)
    speed=random.randint(a,b)
    bullet = Projectile()
    projectiles.add(bullet)
    list_bullets.append(bullet)
    bullet.speed = speed
    if side==1:
        bullet.rect.x = -10
        bullet.rect.y = random.randint(20,580)
        bullet.direction='R'
    elif side==2:
        bullet.rect.x = 810
        bullet.rect.y = random.randint(20, 580)
        bullet.direction='L'
    elif side==3:
        bullet.rect.x = random.randint(50, 750)
        bullet.rect.y = -10
        bullet.direction='D'
    elif side==4:
        bullet.rect.x = random.randint(50, 750)
        bullet.rect.y = 610
        bullet.direction = 'U'

def spawn_coin():
    coin=Coins()
    coin.rect.x=random.randint(20,780)
    coin.rect.y=random.randint(10,590)
    coins.add(coin)

def main_menu(score):
    pygame.mouse.set_visible(True)
    global end_game
    global bg_channel
    global bg_menu

    if not bg_channel.get_busy():
        bg_channel = bg_menu.play(1, 0, 10000)
    bg=pygame.image.load('images\menu\main_screen.png')
    info=pygame.image.load('images\menu\info.png')
    text_1=get_schwifty_font.render('The Death Chamber',1,(0,0,0))
    text_2=heveltica_font.render('PLAY',1,(0,0,0))
    text_3=heveltica_font.render('INFO',1,(0,0,0))
    text_4=rick_and_morty_font.render('Select your Skin',1,(0,0,0))
    text_5=heveltica_font.render('BACK',1,(0,0,0))
    text_6=heveltica_font.render('Max Score= '+str(score),1,(0,0,0))
    menu_screen=0
    select_index=0
    end_menu=False
    while not end_menu:
        if not bg_channel.get_busy():
            bg_channel = bg_menu.play(1, 0, 10000)
        draw_sprites.add(chars[0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
                end_menu = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end_game=True
                    end_menu=True
                if event.key == pygame.K_RIGHT and menu_screen==1:
                    if select_index<len(chars)-1:
                        select_index+=1
                if event.key == pygame.K_LEFT and menu_screen==1:
                    if select_index>0:
                        select_index-=1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_screen==0:
                    x,y = event.pos
                    rect1=pygame.Rect((500,150),(text_2.get_size()))
                    rect2=pygame.Rect((500,180),(text_3.get_size()))
                    if rect1.collidepoint(x,y):
                        menu_screen=1
                    elif rect2.collidepoint(x,y):
                        menu_screen=2
                elif menu_screen==1:
                    x,y = event.pos
                    rect1 = pygame.Rect((370, 380), (text_2.get_size()))
                    rect2 = pygame.Rect((368, 410), (text_5.get_size()))
                    if rect1.collidepoint(x, y):
                        player[0]=chars[select_index]
                        players.add(chars[select_index])
                        select_index=0
                        player[0].rect.x=400
                        player[0].rect.y=500
                        end_menu=True
                        bg_channel.fadeout(300)
                        pygame.mouse.set_visible(False)
                    elif rect2.collidepoint(x, y):
                        menu_screen = 0
                elif menu_screen==2:
                    x, y = event.pos
                    rect1 = pygame.Rect((600, 510), (text_5.get_size()))
                    if rect1.collidepoint(x, y):
                        menu_screen = 0


        main_screen.fill((255,255,255))
        if menu_screen== 0:
            main_screen.blit(bg, (-50, 0))
            main_screen.blit(text_1,(280,60))
            main_screen.blit(text_2,(500,150))
            main_screen.blit(text_3,(500,180))
            main_screen.blit(text_6,(550,500))
        elif menu_screen==1:
            main_screen.blit(chars[select_index].anim_down[0],(370,250))
            main_screen.blit(text_4, (320, 350))
            main_screen.blit(text_2, (370, 380))
            main_screen.blit(text_5, (368, 410))

        elif menu_screen==2:
            main_screen.blit(info,(120,0))
            main_screen.blit(text_5, (600, 510))

            pass


        fps.tick(60)
        pygame.display.flip()

pygame.init()

sounds=pygame.mixer
sounds.init()
bg_menu=sounds.Sound('sound/open.wav')
bg_gameplay_1=sounds.Sound('sound/gets.wav')
bg_gameplay_2=sounds.Sound('sound/evilmorty.wav')
bg_menu.set_volume(0.1)
bg_gameplay_1.set_volume(0.1)
bg_gameplay_2.set_volume(0.3)
bg_channel=pygame.mixer.Channel(1)
pygame.mixer.set_reserved(2)

rick_and_morty_font=pygame.font.Font('fonts/r1.ttf',30)
get_schwifty_font=pygame.font.Font('fonts/r2.ttf', 60)
heveltica_font=pygame.font.Font('fonts/r3.ttf',26)

fps=pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT+1,1000)
pygame.time.set_timer(pygame.USEREVENT+2,15000)

main_screen=pygame.display.set_mode((800,600),pygame.FULLSCREEN,32)
pygame.display.set_caption('THE DEATH CHAMBER')

min_speed=3
max_speed=6
max_score=0

draw_sprites=pygame.sprite.Group()
players=pygame.sprite.Group()
projectiles=pygame.sprite.Group()
list_bullets=[]
coins=pygame.sprite.Group()

chars=[]
player=[]

for x in xrange(13):
    char=Player('images\char\M'+str(x)+'.png')
    chars.append(char)

player.append(chars[0])

end_game=False

main_menu(max_score)
spawn_coin()

while not end_game:
    if max_score<30:
        if not bg_channel.get_busy():
            bg_channel = bg_gameplay_1.play(1, 0, 500)
    else:
        if not bg_channel.get_busy():
            bg_channel = bg_gameplay_2.play(1, 0, 0)

    text_score = heveltica_font.render('SCORE: ' + str(player[0].score), 1, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game=True
        if event.type == pygame.USEREVENT+1:
            shoot(min_speed,max_speed)
        if event.type == pygame.USEREVENT+2:
            min_speed+=1
            max_speed+=1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end_game=True
            if event.key == pygame.K_RIGHT:
                player[0].right=True
            if event.key == pygame.K_LEFT:
                player[0].left=True
            if event.key == pygame.K_UP:
                player[0].up=True
            if event.key == pygame.K_DOWN:
                player[0].down=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player[0].right=False
            if event.key == pygame.K_LEFT:
                player[0].left=False
            if event.key == pygame.K_UP:
                player[0].up=False
            if event.key == pygame.K_DOWN:
                player[0].down=False

    main_screen.fill((255,255,255))

    players.update()
    projectiles.update()
    coins.update()

    coins.draw(main_screen)
    players.draw(main_screen)
    projectiles.draw(main_screen)
    main_screen.blit(text_score,(675,10))

    death=pygame.sprite.spritecollide(player[0],projectiles,True,collided=pygame.sprite.collide_mask)
    score=pygame.sprite.spritecollide(player[0],coins,True,collided=pygame.sprite.collide_mask)

    for bullet in death:
        players.remove(player[0])
        if player[0].score > max_score:
            max_score=player[0].score
        bg_channel.fadeout(300)
        player[0].score=0
        player[0].left=False
        player[0].right = False
        player[0].up = False
        player[0].down = False
        min_speed=3
        max_speed=6
        main_menu(max_score)

    for coin in score:
        player[0].score+=1
        spawn_coin()

    for bullet in list_bullets:
        if bullet.rect.x>850 or bullet.rect.x<-50 or bullet.rect.y>650 or bullet.rect.y<-50:
            projectiles.remove(bullet)
            list_bullets.remove(bullet)

    fps.tick(60)
    pygame.display.flip()
pygame.quit()


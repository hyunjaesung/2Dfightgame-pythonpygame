import pygame


global WINDOW_WIDTH, WINDOW_HEIGHT

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WINDOW_WIDTH = 512
WINDOW_HEIGHT = 300





class Player: # 플레이어 정보 클래스
    def __init__(self, playernum, xpos, ypos, HP, drawobj):
        self.playernum = playernum
        self.xpos = xpos
        self.ypos = ypos
        self.HP = HP
        self.drawobj = drawobj


    def changedrawobj(self, drawobj):
        self.drawobj = drawobj

#class HealthBar:


class Environment: #  게임관련 함수와 인자들
    def __init__(self):
        self.jump1 = pygame.image.load('./res/jump1.png')
        self.jump2 = pygame.image.load('./res/jump2.png')

        self.attack1 = pygame.image.load('./res/attack1.png')
        self.attack2 = pygame.image.load('./res/attack2.png')

        self.defend1 = pygame.image.load('./res/defend1.png')
        self.defend2 = pygame.image.load('./res/defend2.png')

        self.hitted1 = pygame.image.load('./res/hitted1.png')
        self.hitted2 = pygame.image.load('./res/hitted2.png')

        self.background_image = pygame.image.load('./res/background.png')
        self.HealthBar = pygame.image.load('./res/HealthBar.png')

        self.hit_sound = pygame.mixer.Sound('./res/hit.wav')

        self.def_sound = pygame.mixer.Sound('./res/def.wav')


        #self.Background_sound = pygame.mixer.Sound('background.wav')


    def drawObject(self, obj, x, y): # 그리기함수
        gamePad.blit(obj, (x, y))

    def Attacked(self, x): # 공격당했을때 함수
        x.HP -= 10
        pygame.mixer.Sound.play(self.hit_sound)

    def Defended(self): # 막기 성공했을경우 함수
        pygame.mixer.Sound.play(self.def_sound)





class GamePlay(Environment): # 환경클래스 상속, 게임플레이 클래스
    def __init__(self):
        Environment.__init__(self)
        self.player1 = Player(1, 0, 0, 100, pygame.image.load('./res/player1.png'))
        self.player2 = Player(1, 0, 0, 100, pygame.image.load('./res/player2.png'))

        self.character_width = 50
        self.character_height = 54



    def InitGame(self):
        global gamePad
        global clock
        clock = pygame.time.Clock()
        gamePad = pygame.display.set_mode((512, 300))
        self.player1.xpos = WINDOW_WIDTH * 0.1
        self.player1.ypos = WINDOW_HEIGHT * 0.8
        self.player2.xpos = WINDOW_WIDTH * 0.82
        self.player2.ypos = WINDOW_HEIGHT * 0.8



    def RunGame(self):

        #pygame.mixer.Sound.play(self.background_sound)
        x_change_1 = 0
        x_change_2 = 0
        jump_1 = 0
        jump_2 = 0
        attack_1 = 0
        attack_2 = 0
        defend_1 = 0
        defend_2 = 0
        jump_key_1 = 5
        jump_key_2 = 5

        notFinished = True

        clock = pygame.time.Clock()

        while notFinished:

            self.drawObject(self.background_image, 0, 0)
            self.drawObject(self. HealthBar, WINDOW_WIDTH * 0.1, WINDOW_HEIGHT*0.1 )


            #  조작키
            # 플레이어 1 : 이동 위g 왼쪽v 오른쪽n 공격 왼쪽ctrl 막기 왼쪽 alt
            # 플레이어 2 : 이동 방향키           공격 ]        막기 p


            #에너지 파는 아직 구현안됨

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    notFinished = False

                if event.type == pygame.KEYDOWN:
                    #
                    ## player1 키 세팅
                    #
                    if event.key == pygame.K_v:
                        x_change_1 = -5
                    elif event.key == pygame.K_n:
                        x_change_1 = 5
                    elif event.key == pygame.K_g:
                        jump_1 = 1
                    elif event.key == pygame.K_LSHIFT: # 불꽃발사
                        pygame.mixer.Sound.play(self.hit_sound)
                        bullet_x = self.player2.xpos + self.character_width
                        bullet_y = self.player2.ypos - self.character_height / 2
                        #bullet_xy.append([bullet_x, bullet_y])

                    elif event.key == pygame.K_LCTRL: # 공격
                        attack_1 = 1

                    elif event.key == pygame.K_LALT: # 막기
                        defend_1 = 1



                    ##
                    ## player2 키 세팅
                    ##

                    if event.key == pygame.K_LEFT:
                        x_change_2 = -5
                    elif event.key == pygame.K_RIGHT:
                        x_change_2 = 5
                    elif event.key == pygame.K_UP: ## 점프
                        jump_2 = 1
                    elif event.key == pygame.K_GREATER: # 불꽃발사
                        #pygame.mixer.Sound.play(self.hit_sound)
                        bullet_x = self.player2.xpos + self.character_width
                        bullet_y = self.player2.ypos - self.character_height / 2
                        #bullet_xy.append([bullet_x, bullet_y])

                    elif event.key == pygame.K_RIGHTBRACKET: # 공격
                        attack_2 = 1

                    elif event.key == pygame.K_p: # 막기
                        defend_2 = 1


                    #elif event.key == pygame.K_SPACE:


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_v or event.key == pygame.K_n:
                        x_change_1 = 0

                    if event.key == pygame.K_LALT:
                        defend_1 = 0

                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change_2 = 0

                    if event.key == pygame.K_p:
                        defend_2 = 0



            self.player1.xpos += x_change_1

            if (self.player1.xpos < 0): # 화면밖으로 못나가게
                self.player1.xpos -= x_change_1

            if self.player1.xpos + (self.character_width / 2) > self.player2.xpos: # 서로 위치가 역전되는거 막기

                if(self.player2.xpos + self.character_width > 512):
                    self.player2.xpos = 512 - self.character_width

                if (self.player2.xpos + self.character_width < 512):
                    self.player2.xpos += 5
                    self.player1.xpos -= (x_change_1+5)


            self.player2.xpos += x_change_2

            if(self.player2.xpos + self.character_width > 512): # 화면밖으로 못나가게
                 self.player2.xpos -= x_change_2

            if self.player2.xpos < self.player1.xpos + (self.character_width / 2): # 서로 위치가 역전되는거 막기
                if(self.player1.xpos < 0):
                    self.player1.xpos = 0

                if(self.player1.xpos > 0):
                    self.player2.xpos -= (x_change_2-5)
                    self.player1.xpos -= 5

            if (jump_1 == 1):  ## player1 점프
                self.drawObject(self.jump1, self.player1.xpos, self.player1.ypos)
                self.drawObject(self.jump2, self.player2.xpos, self.player2.ypos)
                if (jump_key_1 > 0):
                    jump_key_1 -= 1
                    self.player1.ypos -= 10
                if (jump_key_1 <= 0):
                    jump_key_1 -= 1
                    self.player1.ypos += 10
                if(jump_key_1 == -5):
                    jump_key_1 = 5
                    jump_1 = 0
            elif(jump_2 == 1): ## player2 점프
                self.drawObject(self.jump1, self.player1.xpos, self.player1.ypos)
                self.drawObject(self.jump2, self.player2.xpos, self.player2.ypos)
                if (jump_key_2 > 0):
                    jump_key_2 -= 1
                    self.player2.ypos -= 10
                if (jump_key_2 <= 0):
                    jump_key_2 -= 1
                    self.player2.ypos += 10
                if (jump_key_2 == -5):
                    jump_key_2 = 5
                    jump_2 = 0

            elif(attack_1 == 1): # 플레이어 1공격, 플레이어 2 막기
                self.drawObject(self.attack1, self.player1.xpos, self.player1.ypos)

                if(defend_2 == 0):
                    if self.player1.xpos + self.character_width > self.player2.xpos:
                        self.Attacked(self.player2)
                        self.drawObject(self.hitted2, self.player2.xpos, self.player2.ypos)
                    else:
                        self.drawObject(self.player2.drawobj, self.player2.xpos, self.player2.ypos)
                elif(defend_2 == 1):
                    self.drawObject(self.defend2, self.player2.xpos, self.player2.ypos)
                    if self.player1.xpos + self.character_width > self.player2.xpos:
                        self.Defended()
                else:
                    self.drawObject(self.player2.drawobj, self.player2.xpos, self.player2.ypos)

                attack_1 = 0

            elif (attack_2 == 1): # 플레이어2 공격, 플레이어1 막기
                self.drawObject(self.attack2, self.player2.xpos, self.player2.ypos)

                if (defend_1 == 0):
                    if self.player2.xpos < self.player1.xpos + self.character_width:
                        self.drawObject(self.hitted1, self.player1.xpos, self.player1.ypos)
                        self.Attacked(self.player1)
                    else:
                        self.drawObject(self.player1.drawobj, self.player1.xpos, self.player1.ypos)

                elif (defend_1 == 1):
                    self.drawObject(self.defend1, self.player1.xpos, self.player1.ypos)
                    if self.player2.xpos < self.player1.xpos + self.character_width:
                        self.Defended()

                else:
                    self.drawObject(self.player1.drawobj, self.player1.xpos, self.player1.ypos)

                attack_2 = 0

            elif(defend_1 == 1): # 플레이어1 막기
                self.drawObject(self.defend1, self.player1.xpos, self.player1.ypos)
                self.drawObject(self.player2.drawobj, self.player2.xpos, self.player2.ypos)

            elif (defend_2 == 1): # 플레이어2 막기
                self.drawObject(self.player1.drawobj, self.player1.xpos, self.player1.ypos)
                self.drawObject(self.defend2, self.player2.xpos, self.player2.ypos)





            else: #  평상시 캐릭터
                self.drawObject(self.player1.drawobj, self.player1.xpos, self.player1.ypos)
                self.drawObject(self.player2.drawobj, self.player2.xpos, self.player2.ypos)








            pygame.display.update()
            clock.tick(30)



        pygame.quit()
        quit()








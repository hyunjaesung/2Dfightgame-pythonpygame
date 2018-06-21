import pygame


global WINDOW_WIDTH, WINDOW_HEIGHT

WHITE = (255, 255, 255)
RED = (255, 20, 0)
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





class Environment: #  게임관련 함수와 인자들
    def __init__(self):
        self.player1_1 = pygame.image.load('./res/player1.png')
        self.player1_2 = pygame.image.load('./res/player1_2.png')

        self.player2_1 = pygame.image.load('./res/player2.png')
        self.player2_2 = pygame.image.load('./res/player2_2.png')

        self.walk1 = pygame.image.load('./res/walk1.png')
        self.walk2 = pygame.image.load('./res/walk2.png')


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
        self.def_sound = pygame.mixer.Sound('./res/defend.wav')
        self.hurt_sound = pygame.mixer.Sound('./res/hurt.wav')
        self.jump_sound = pygame.mixer.Sound('./res/jump.wav')
        self.Background_sound = pygame.mixer.music.load('./res/background.mp3')


    def drawObject(self, obj, x, y): # 그리기함수
        gamePad.blit(obj, (x, y))

    def Attacked(self, x): # 공격당했을때 함수
        x.HP -= 10
        pygame.mixer.Sound.play(self.hurt_sound)

    def Defended(self): # 막기 성공했을경우 함수
        pygame.mixer.Sound.play(self.def_sound)


    def drawHealthBar(self, x, y ,health_width):
        pygame.draw.rect(gamePad, RED, (x, y, health_width, 15))





class GamePlay(Environment): # 환경클래스 상속, 게임플레이 클래스
    def __init__(self):
        Environment.__init__(self)
        self.player1 = Player(1, 0, 0, 100, self.player1_1)
        self.player2 = Player(1, 0, 0, 100, self.player2_1)

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

        pygame.mixer.music.play(-1)

        player1_basic_key = 0;
        player2_basic_key = 0;


        x_change_1 = 0
        x_change_2 = 0
        walk_1 = 0
        walk_2 = 0
        jump_1 = 0
        jump_2 = 0
        attack_1 = 0
        attack_2 = 0
        defend_1 = 0
        defend_2 = 0
        jump_key_1 = 5
        jump_key_2 = 5
        player1_healthbar_x = WINDOW_WIDTH * 0.1 + 7
        player1_healthbar_y = WINDOW_HEIGHT * 0.1 + 5
        player1_healthbar_width= 180
        player2_healthbar_x =  player1_healthbar_x + 206
        player2_healthbar_y = WINDOW_HEIGHT * 0.1 + 5
        player2_healthbar_width = 180
        healthbar_damage = 18


        notFinished = True

        clock = pygame.time.Clock()

        while notFinished:


            self.drawObject(self.background_image, 0, 0)
            self.drawObject(self. HealthBar, WINDOW_WIDTH * 0.1, WINDOW_HEIGHT*0.1)


            if player1_healthbar_width > 0:
                self.drawHealthBar(player1_healthbar_x, player1_healthbar_y, player1_healthbar_width)

            if player2_healthbar_width > 0:
                self.drawHealthBar(player2_healthbar_x, player2_healthbar_y, player2_healthbar_width)


            #
            # 게임종료!!!
            #
            #
            if self.player1.HP <= 0 or self.player2.HP <=0:
                finished = True
                while finished:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                notFinished = False
                                finished = False

                    winfont = pygame.font.Font("./res/ethnocentric rg it.ttf", 50)
                    message_x = 0
                    message_y = WINDOW_HEIGHT / 2 - 90
                    returnfont = pygame.font.Font("./res/Neuton-Italic.ttf", 30)
                    if self.player1.HP <= 0:
                        winMessage = winfont.render("Player 2 WINS!", 0, GREEN)

                    else:
                        winMessage = winfont.render("Player 1 WINS!", 0, GREEN)

                    Message_rect = winMessage.get_rect()
                    gamePad.blit(winMessage, (message_x, message_y))

                    returnMessage = returnfont.render("Press Enter to Return to Menu", 0, (0, 0, 0))
                    returnMessage_rect = returnMessage.get_rect()
                    gamePad.blit(returnMessage, (WINDOW_WIDTH / 2 - (returnMessage_rect[2] / 2), 180))

                    pygame.display.update()
                    clock.tick(30)

            #  조작키
            # 플레이어 1 : 이동 위g 왼쪽v 오른쪽n 공격 왼쪽ctrl 막기 왼쪽 alt
            # 플레이어 2 : 이동 방향키           공격 ]        막기 [


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
                        walk_1 = 1
                    elif event.key == pygame.K_n:
                        x_change_1 = 5
                        walk_1 = 1
                    elif event.key == pygame.K_g:
                        pygame.mixer.Sound.play(self.jump_sound)
                        jump_1 = 1

                    elif event.key == pygame.K_LCTRL: # 공격
                        attack_1 = 1
                        pygame.mixer.Sound.play(self.hit_sound)

                    elif event.key == pygame.K_LALT: # 막기
                        defend_1 = 1



                    ##
                    ## player2 키 세팅
                    ##

                    if event.key == pygame.K_LEFT:
                        x_change_2 = -5
                        walk_2 = 1
                    elif event.key == pygame.K_RIGHT:
                        x_change_2 = 5
                        walk_2 = 1
                    elif event.key == pygame.K_UP: ## 점프
                        pygame.mixer.Sound.play(self.jump_sound)
                        jump_2 = 1

                    elif event.key == pygame.K_RIGHTBRACKET: # 공격
                        pygame.mixer.Sound.play(self.hit_sound)
                        attack_2 = 1

                    elif event.key == pygame.K_LEFTBRACKET: # 막기
                        defend_2 = 1


                    #elif event.key == pygame.K_SPACE:


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_v or event.key == pygame.K_n:
                        x_change_1 = 0

                    if event.key == pygame.K_LALT:
                        defend_1 = 0

                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change_2 = 0

                    if event.key == pygame.K_LEFTBRACKET:
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
                self.drawObject(self.player2.drawobj, self.player2.xpos, self.player2.ypos)
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
                self.drawObject(self.player1.drawobj, self.player1.xpos, self.player1.ypos)
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
                        #데미지 입었을때 플레이어2 헬스바 감소
                        player2_healthbar_width -= healthbar_damage


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
                        # 데미지입었을때 플레이어1 헬스바 감소
                        player1_healthbar_x += healthbar_damage
                        player1_healthbar_width -= healthbar_damage

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

            elif(walk_1 == 1 ):
                self.drawObject(self.walk1, self.player1.xpos, self.player1.ypos)
                self.drawObject(self.player2.drawobj, self.player2.xpos, self.player2.ypos)
                walk_1 = 0
            elif(walk_2 == 1):
                self.drawObject(self.player1.drawobj, self.player1.xpos, self.player1.ypos)
                self.drawObject(self.walk2, self.player2.xpos, self.player2.ypos)
                walk_2 = 0



            else: #  평상시 캐릭터
                self.drawObject(self.player1.drawobj, self.player1.xpos, self.player1.ypos)
                self.drawObject(self.player2.drawobj, self.player2.xpos, self.player2.ypos)


            # 베이직 모션 2개 반복

            if player1_basic_key == 0 :
                self.player1.drawobj = self.player1_2
                player1_basic_key = 1
            else :
                self.player1.drawobj = self.player1_1
                player1_basic_key = 0

            if player2_basic_key == 0 :
                self.player2.drawobj = self.player2_2
                player2_basic_key = 1
            else :
                self.player2.drawobj = self.player2_1
                player2_basic_key = 0











            pygame.display.update()
            clock.tick(30)



        pygame.quit()
        quit()








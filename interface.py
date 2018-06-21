# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import gameplay

# 초기화
pygame.init()



# 게임화면
screen_width=512
screen_height=300
screen=pygame.display.set_mode((screen_width, screen_height))

# 메뉴그리기
def drawMenu(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# 색깔
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# 폰트
menuFont = "./res/Retro.ttf"
howFont = "./res/HoonGomulsangR.ttf"


# 클락obj
clock = pygame.time.Clock()
FPS=30

#게임 방법 방향키 왼쪽으로 메뉴로 복귀
def howtoplay():
    how = True
    print("How to Play IN")
    while how:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    how=False

        howTitle = drawMenu("How to Play",howFont,50, blue)
        #플레이어1 설명
        Player1 = drawMenu("PLAYER 1", howFont,40, white )
        movePlayer1_jump = drawMenu("Jump : G", howFont, 30, white)
        movePlayer1_left = drawMenu("Move to Left : V", howFont, 25, white)
        movePlayer1_right = drawMenu("Move to Right : N", howFont, 25, white)
        attackPlayer1 = drawMenu("Attack : Left Ctrl", howFont, 25, white)
        defendPlayer1 = drawMenu("Block : Left Alt", howFont, 25, white)

        #플레이어2 설명
        Player2 = drawMenu("PLAYER 2",howFont,40, white)
        movePlayer2_jump = drawMenu("Jump : UP", howFont, 25, white)
        movePlayer2_left = drawMenu("Move to Left : LEFT", howFont, 25, white)
        movePlayer2_right = drawMenu("Move to Right : RIGHT", howFont, 25, white)
        attackPlayer2 = drawMenu("Attack : ]", howFont, 25, white)
        defendPlayer2 = drawMenu("Block : ]", howFont, 25, white)

        #디스플레이
        howTitle_rect = howTitle.get_rect()
        Player1_rect = Player1.get_rect()
        Player2_rect = Player2.get_rect()

        screen.fill(black)
        screen.blit(howTitle,(screen_width/2 - (howTitle_rect[2]/2),20))
        screen.blit(Player1,(screen_width/4-(Player1_rect[2]/2), 80))
        screen.blit(Player2, (3*screen_width/4 - (Player2_rect[2]/2),80))
        screen.blit(movePlayer1_jump,(20,120))
        screen.blit(movePlayer1_left,(20,150))
        screen.blit(movePlayer1_right,(20,180))
        screen.blit(attackPlayer1,(20,210))
        screen.blit(defendPlayer1,(20,240))
        screen.blit(movePlayer2_jump, (screen_width/2 + 20,120))
        screen.blit(movePlayer2_left, (screen_width/2 + 20,150))
        screen.blit(movePlayer2_right, (screen_width/2 + 20,180))
        screen.blit(attackPlayer2, (screen_width/2 + 20,210))
        screen.blit(defendPlayer2,(screen_width/2 + 20, 240))

        pygame.display.update()
        clock.tick(FPS)
#크레딧 방향키 윈쪽으로 메뉴로 복귀
def credit():
    credit = True
    print("Credit IN")
    while credit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    credit=False

        creditTitle = drawMenu("Credit", howFont, 50, blue)
        credit_HJ = drawMenu("Hyunjae Sung", howFont, 28, white)
        credit_HW = drawMenu("Hyunwoo Park", howFont, 28, white)
        credit_HS = drawMenu("Hyungsuh Kim", howFont, 28 ,white)

        HJ_Leader = drawMenu("Team Leader", howFont, 20, white)
        HJ_Presentation = drawMenu("Mid & Final Presenter", howFont, 20, white)
        HJ_Architecture = drawMenu("Program Architect", howFont, 20, white)
        HJ_Gameplay = drawMenu("Gameplay Developer", howFont, 20, green)

        HW_Member = drawMenu("Team Member", howFont, 20, white)
        HW_Document = drawMenu("Final Documentation", howFont, 20, white)
        HW_UI = drawMenu("Interface Developer", howFont, 20, green)
        

        HS_Member = drawMenu("Team Member", howFont, 20, white)
        HS_Presentation = drawMenu("Final Presenter", howFont, 20, white)
        HS_Design = drawMenu("Designer", howFont, 20, green)

        

        creditTitle_rect = creditTitle.get_rect()
        credit_HJ_rect = credit_HJ.get_rect()
        credit_HW_rect = credit_HW.get_rect()
        credit_HS_rect = credit_HS.get_rect()

        HJ_Leader_rect = HJ_Leader.get_rect()
        HJ_Presentation_rect = HJ_Presentation.get_rect()
        HJ_Architecture_rect = HJ_Architecture.get_rect()
        HJ_Gameplay_rect =  HJ_Gameplay.get_rect()

        HW_Member_rect = HW_Member.get_rect()
        HW_Document_rect = HW_Document.get_rect()
        HW_UI_rect = HW_UI.get_rect()

        HS_Member_rect = HS_Member.get_rect()
        HS_Presentation_rect = HS_Presentation.get_rect()
        HS_Design_rect = HS_Design.get_rect()

        screen.fill(black)
        screen.blit(creditTitle,(screen_width/2 - (creditTitle_rect[2]/2),20))
        screen.blit(credit_HJ,(screen_width/6 - (credit_HJ_rect[2]/2),80))
        screen.blit(credit_HW,(3*screen_width/6 - (credit_HW_rect[2]/2),80))
        screen.blit(credit_HS,(5*screen_width/6 - (credit_HS_rect[2]/2), 80))

        screen.blit(HJ_Leader,(screen_width/6 - (HJ_Leader_rect[2]/2), 120))
        screen.blit(HJ_Presentation,(screen_width/6 - (HJ_Presentation_rect[2]/2), 150))
        screen.blit(HJ_Architecture,(screen_width/6 - (HJ_Architecture_rect[2]/2), 180))
        screen.blit(HJ_Gameplay,(screen_width/6 - (HJ_Gameplay_rect[2]/2), 210))

        screen.blit(HW_Member,(3*screen_width/6 - (HW_Member_rect[2]/2), 120))
        screen.blit(HW_Document,(3*screen_width/6 - (HW_Document_rect[2]/2), 150))
        screen.blit(HW_UI,(3*screen_width/6 - (HW_UI_rect[2]/2), 180))

        screen.blit(HS_Member,(5*screen_width/6 - (HS_Member_rect[2]/2), 120))
        screen.blit(HS_Presentation,(5*screen_width/6 - (HS_Presentation_rect[2]/2), 150))
        screen.blit(HS_Design,(5*screen_width/6 - (HS_Design_rect[2]/2), 180))

        



        pygame.display.update()
        clock.tick(FPS)






# 메뉴 실행
def main_menu():
    Background_sound = pygame.mixer.music.load('./res/background.mp3')

    pygame.mixer.music.play(-1)

    menu=True
    selected=10000

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected-=1
                elif event.key==pygame.K_DOWN:
                    selected+=1
                if event.key==pygame.K_RETURN:
                    if selected%4==0:
                        print("Start")
                        game = gameplay.GamePlay()
                        game.InitGame()
                        game.RunGame()
                    if selected%4==1:
                        howtoplay()
                    if selected%4==2:
                        credit()
                    if selected%4==3:
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(black)
        title=drawMenu("Sword Master", menuFont, 70, yellow)
        if selected%4==0:
            text_start=drawMenu("START", menuFont, 35, blue)
        else:
            text_start = drawMenu("START", menuFont, 35, white)
        if selected%4==1:
            text_how = drawMenu("How to Play", menuFont, 35, blue)
        else:
            text_how = drawMenu("How to Play", menuFont, 35, white)
        if selected%4==2:
            text_settings = drawMenu("Credit", menuFont, 35, blue)
        else:
            text_settings = drawMenu("Credit", menuFont, 35, white)
        if selected%4==3:
            text_quit=drawMenu("QUIT", menuFont, 35, blue)
        else:
            text_quit = drawMenu("QUIT", menuFont, 35, white)
        

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        how_rect =text_how.get_rect()
        settings_rect = text_settings.get_rect()
        quit_rect=text_quit.get_rect()

        # 디스플레이
        screen.blit(pygame.image.load("./res/wall.png"),(0,0))
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 30))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 120))
        screen.blit(text_how, (screen_width/2 - (how_rect[2]/2), 160))
        screen.blit(text_settings, (screen_width/2 - (settings_rect[2]/2), 200))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 240))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Sword Master")






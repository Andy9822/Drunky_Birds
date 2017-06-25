import pygame,sys
from pygame.locals import*
from bird import *
from pipe import *
import time
import ct

def fillEntireTubos(screen_largura,screen_altura):
    entireTubos = []
    entireTubos.append( Pipe(screen_largura * 0.8 ,screen_altura,31,500) )
    entireTubos.append( Pipe(screen_largura * 0.6 ,screen_altura,31,500) )
    entireTubos.append( Pipe(screen_largura * 1 ,screen_altura,31,500) )
    entireTubos.append( Pipe(screen_largura * 1.2 ,screen_altura,31,500) )
    entireTubos.append( Pipe(screen_largura * 1.4 ,screen_altura,31,500) )
    entireTubos.append( Pipe(screen_largura * 1.6 ,screen_altura,31,500) )
    return entireTubos


def drawGame(screen,entireTubos,bird,birdImage,downImg,points,clock,corLetra,bg):
    screen.blit(bg,(0,0))
    screen.blit(birdImage,(bird.x , bird.y))
    for tubo in entireTubos:
        screen.blit(downImg,(tubo.x,tubo.y))

    attPoints(screen,points,corLetra)
    pygame.display.update()
    clock.tick(30)

def updatePositions(screen_largura,screen_altura,entireTubos,bird):
        bird.update(screen_altura)
        for tubo in entireTubos:
            tubo.update(screen_largura,screen_altura)
            if not tubo.passado:
                if bird.x + bird.width * 2  > tubo.x + 20:
                    bird.pontos +=1
                    tubo.passado = True

def checkColision(bird,entireTubos):
    for tubo in entireTubos:
        if bird.x + bird.width * 2 >= tubo.x +1 and bird.x <= tubo.x -12 :#
            if bird.y + 2* bird.height >= tubo.y + 4 :
                return True
    return False

def hasDead(bird,tubo):
    return bird.caiu or checkColision(bird,tubo)

def text_objects(message, font,corRect):
    TextSurface = font.render(message,True,corRect)
    return TextSurface,TextSurface.get_rect()

def showMessage(screen,message,size,x,y,corLetra):
    text = pygame.font.SysFont('timesnewroman',size,bold=False,italic=False)
    #text = pygame.font.Font(None,size)
    TextSurf, TextRect = text_objects(message, text,corLetra)
    TextRect.center = ( (x),(y))
    screen.blit(TextSurf,TextRect)

def attPoints(screen,pontos,corPontos):
    font = pygame.font.SysFont('timesnewroman',20,bold=False,italic=False)
    text = font.render('Score = '+ str (pontos) ,True,corPontos)
    screen.blit(text,(0,0))

def gameOver(screen,bird,entireTubos,screen_altura,screen_largura,over,corLetra):
    bird.resetPos()
    for tubo in entireTubos:
        tubo.reset(screen_altura)
    showMessage(screen,'GAME OVER',50,screen_largura/2,screen_altura/4,corLetra)
    pygame.display.update()
    over.play()
    showMessage(screen,'Press enter to play again...',20,screen_largura/2 + 8  ,screen_altura/4 + 50,corLetra)
    pygame.display.update()

def joga1(clock,screen,screen_largura,screen_altura):
    ##Seta as configurações visuais e do jogo
    x = screen_largura * 0.42
    y = screen_altura * 0.4


    ##Inicializa passaro
    bird = Bird(x,y,24,36)
    birdImage = pygame.image.load('resources/passaro.png')

    #Inicializa Tubo de baixo
    entireTubos = fillEntireTubos(screen_largura,screen_altura)
    downImg = pygame.image.load('resources/tuboInteiro.png')

    ##Inicializa tela visual
    background = pygame.image.load('resources/jogo1.png')
    background = pygame.transform.scale(background,(screen_largura,screen_altura))


    jogando = True
    pause = True
    points = 0
    scored = pygame.mixer.Sound('resources/smw_fireball.wav')
    over = pygame.mixer.Sound('resources/gameOver.wav')

    #START NOW!
    drawGame(screen,entireTubos,bird,birdImage,downImg,points,clock,ct.preto,background)
    pygame.display.update()

    while jogando:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.display.quit()
                sys.exit()
            if evento.type ==  pygame.KEYDOWN:
                if pause and (evento.key == 13 or evento.key == K_KP_ENTER):
                    pause = False
                    bird.jump()
                elif evento.key == pygame.K_UP or evento.key == pygame.K_SPACE :
                    bird.jump()
                elif evento.key == pygame.K_q:
                    jogando = False



        if not pause:
            updatePositions(screen_largura,screen_altura,entireTubos,bird)
            drawGame(screen,entireTubos,bird,birdImage,downImg,points,clock,ct.preto,background)
            if  hasDead(bird,entireTubos):
                gameOver(screen,bird,entireTubos,screen_altura,screen_largura,over,ct.preto)
                pause = True
            elif points != bird.pontos:
                points = bird.pontos
                scored.play()

def mainFunction():
    pygame.init()
    screen_largura = 1000
    screen_altura = 600
    icone = pygame.image.load('resources/icone.jpg')
    pygame.display.set_icon(icone)
    background = pygame.image.load('resources/forest.png')
    #background = pygame.transform.scale(background,(screen_largura,screen_altura))
    screen = pygame.display.set_mode((screen_largura,screen_altura))
    pygame.display.set_caption("Hello Drunk Gamer")
    clock = pygame.time.Clock()

    jogando = True
    while jogando:
        for evento in pygame.event.get():
            if evento.type ==  pygame.KEYDOWN:
                if evento.key == 13:
                    joga1(clock,screen,screen_largura,screen_altura)
            elif evento.type == QUIT:
                jogando = False
        screen.fill(ct.branco)
        screen.blit(background,(0,0))
        pygame.display.update()

    pygame.display.quit()
    sys.exit()
if __name__ == '__main__':
    mainFunction()

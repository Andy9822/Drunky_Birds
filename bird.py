
class Bird():
    def __init__(self,x,y,height,width):
        self.x0 = x
        self.y0 = y
        self.resetPos()
        self.height = height
        self.width = width

    def setImg(self,nome):
        self.image = pygame.image.load(nome)

    def resetPos(self):
        self.x = self.x0
        self.y = self.y0
        self.grav = 2
        self.impulso = 0
        self.up = False
        self.aceleracao = 2
        self.morto = True
        self.caiu = False
        self.pontos = 0

    def morreu(self):
        self.resetPos()

    def checkTop(self,screen_altura):
        if self.y < -30:
            self.y = -30
            self.impulso = 0
            self.up = False

    def checkBot(self,screen_altura):
        if (self.y + self.height) -30  > screen_altura - (2 *self.height )  :
            self.y = screen_altura - (2 *self.height ) + 5
            self.caiu = True

    def update(self,screen_altura):
        if not self.up:
            self.grav +=  self.aceleracao
            self.y += self.grav
            self.checkBot(screen_altura)
            #self.y += self.grav+3
        else:
            self.y -= self.impulso -3
            self.impulso -= 3
            if self.impulso == 0:
                self.up = False
            self.checkTop(screen_altura)

    def jump(self):
        self.up = True
        self.impulso = 18
        self.grav = 2

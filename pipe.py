from random import randint
class Pipe():
    def __init__(self,x,screen_altura,height,width):
        self.x0 = x
        self.x = x
        self.y = randint(101,screen_altura-25)
        self.deslocamento = 4
        self.height = height
        self.width = width
        self.passado = False

    def update(self,screen_largura,screen_altura):
        self.x -= self.deslocamento

        if self.x < -20:
            self.x = screen_largura * 1.2
            self.y = randint(101,screen_altura-25)
            self.passado = False


    def reset(self,screen_altura):
        self.x = self.x0
        self.y = randint(101,screen_altura-25)
        self.passado = False

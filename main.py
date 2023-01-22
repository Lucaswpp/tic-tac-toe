import pygame as pyg
from sys import exit

pyg.init()

JANELA_ALTURA = 600
JANELA_LARGURA = 600
LINE = 3
COLUNNS = 3

BACKGROUND_COLOR = "#1b1e23"
janela = pyg.display.set_mode((JANELA_LARGURA,JANELA_ALTURA))
pyg.display.set_caption("Jogo da velha")
lINE_POS = [[(200,0),(200,600)],[(400,0),(400,600)],[(0,200),(600,200)],[(0,400),(600,400)]]
LINE_COLOR = (255,255,255)
LINE_WIDTH = 15

class Game:
    def __init__(self):
        self.load_board()

    def run(self):
        while True:
            self.check_event()
            self.draw_game()
            pyg.display.update()
            janela.fill(BACKGROUND_COLOR)
        

    def check_event(self):
        for evento in pyg.event.get():

            if evento.type == pyg.QUIT:
                pyg.quit()
                exit()
    
    def load_board(self):
        self.board = []
        for linha in range(LINE):
            linha = []
            for col in range(COLUNNS):
                linha.append("0")
            self.board.append(linha)
    
    def draw_game(self):
        for pos_inicial,pos_final in lINE_POS:
            pyg.draw.line(janela,LINE_COLOR,pos_inicial,pos_final,LINE_WIDTH)


if __name__ == "__main__":
    game_object = Game()
    game_object.run()
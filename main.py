import pygame as pyg
from sys import exit

pyg.init()


LINE = 3
COLUNNS = 3
BACKGROUND_COLOR = "#1b1e23"
JANELA_ALTURA = 600
JANELA_LARGURA = 600
janela = pyg.display.set_mode((JANELA_LARGURA,JANELA_ALTURA))
pyg.display.set_caption("Jogo da velha")

LINE_POS = [[(200,0),(200,600)],[(400,0),(400,600)],[(0,200),(600,200)],[(0,400),(600,400)]]
LINE_COLOR = (255,255,255)
LINE_WIDTH = 15

COLOR_CIRCLE = (243,0,0)
RAIO_CIRCULO = 60
CIRCLE_WIDTH = 15


class Game:
    def __init__(self):
        self.load_board()
        self.player_turn = None

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
            

            if pyg.mouse.get_pressed()[0]:
                    
                pos_mouse = pyg.mouse.get_pos()
                pos_linha =  int(pos_mouse[1] // 200)
                pos_coluna = int(pos_mouse[0] // 200)

                self.board[pos_linha][pos_coluna] = 1


    
    def load_board(self):
        self.board = []
        for linha in range(LINE):
            linha = []
            for col in range(COLUNNS):
                linha.append(0)
            self.board.append(linha)
    
    def draw_game(self):
        self.draw_lines()
        self.update_board()
        
    def draw_lines(self):
        for pos_inicial,pos_final in LINE_POS:
            pyg.draw.line(janela,LINE_COLOR,pos_inicial,pos_final,LINE_WIDTH)

    def update_board(self):

        for line in range(LINE):
            for col in range(COLUNNS):
                if self.board[line][col] == 1:
                    centro_circulo = (int(col*200+100),int(line*200+100))
                    pyg.draw.circle(janela,COLOR_CIRCLE,centro_circulo,RAIO_CIRCULO,15)

    

if __name__ == "__main__":
    game_object = Game()
    game_object.run()
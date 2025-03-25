import pygame 
class Tile:
    def __init__(self,row,col,tilesize=40):
        """ Creates a Tile (row,col,size) """
        self.row=row
        self.col=col
        self.tilesize=tilesize
        self.x=self.col*tilesize #o x fica dentro de uma coluna
        self.y=self.row*tilesize #o y fica dentro de uma linha

    def render(self,win,color,hilite=False):
        rect=pygame.Rect(self.x,self.y,self.tilesize,self.tilesize)
        if not hilite:
            pygame.draw.rect(win,color,rect)
            pygame.draw.rect(win,'darkgray',rect,1)
        else:
            pygame.draw.rect(win,'magenta',rect,1)
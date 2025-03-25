import pygame
from tile import Tile 

#INIT
pygame.init()
# --------- START ----------------
#colors
BG_COLOR='lightgray'
BLACK='black'
TILE_COLOR='gray'


#DIMENSIONS
TILE_SIZE=40
NUM_COLS=5
NUM_ROWS=5

SCREEN_WIDTH= NUM_ROWS*TILE_SIZE
SCREEN_HEIGHT=NUM_COLS*TILE_SIZE

#SURFACES
win=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


#other
clock=pygame.time.Clock()


#FLAGS
run=True

#GAME OBJECTS
tile1=Tile(0,1)
tile2=Tile(0,2)
tile3=Tile(0,3)



# --- START END -----------

# UPDATE
while run:
    win.fill(BLACK)
    clock.tick(30)
    #render graphics
    tile1.render(win,TILE_COLOR,hilite=True)
    tile2.render(win,TILE_COLOR)
    tile3.render(win,TILE_COLOR,hilite=True)






    #--------handle events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    #draw graphics
    pygame.display.flip()

#END    
pygame.quit()

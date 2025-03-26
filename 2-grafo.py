from utils.utils import clear,create_grafo,show_graph
from utils.grid import display_grid
from dfs import dfs

#criar um grafo 4 x 4
# 4 ROWS 4 COLS

ROWS=3
COLS=3

grid=[]

for row in range(ROWS): #em cada linha
    line=[]
    for col in range(COLS):
        line.append((row,col))
    grid.append(line)

clear()

display_grid(grid)

grid=create_grafo(ROWS,COLS)

# show_graph(grid)

src=(0,0)
dst=(2,2)

path=dfs(grid,src,dst)
if path:print(f"Path found (DFS): {path}")
else: print(f"No path found")
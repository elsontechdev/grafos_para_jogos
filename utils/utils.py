import os



def clear():
    os.system('cls')



DIRECTIONS=[
    (-1,0), #drow -1, dcol 0    | CIMA
    (1,0),  #drow 1, dcol 0     | BAIXO
    (0,-1), #drow 0, dcol -1    | ESQUERDA
    (0,1)   #drow 0, dcol 1     | DIREITA
]




def show_graph(grafo):
    for tile,vizinhos in grafo.items():
        print(f"{tile} → {vizinhos}")



def is_insidegrid(x,y,linhas,colunas):
    return 0<=x < linhas and 0<=y<colunas;

def create_grafo(linhas,colunas):
    grafo={}

    for row in range(linhas): #Em cada linha
        for col in range(colunas): #acessa o tile
            vizinhos=[] #vamos pegar os seus vizinhos válidos
            for drow,dcol in DIRECTIONS:
                nrow,ncol=row+drow,col+dcol
                vizinho=(nrow,ncol)
                if is_insidegrid(nrow,ncol,linhas,colunas):
                    vizinhos.append(vizinho)
                grafo[(row,col)]=vizinhos
    return grafo


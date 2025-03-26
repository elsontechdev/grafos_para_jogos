"""
Arquivo usado pra fixar o que aprendi
Tentar puxar da memoria

memorizar: Guardar uma informação
lembrar: acesar, puxar essa informação

Marcar um dado, como algo



ex. Marcar um tile como visitado

- alterar a propriedade do proprio objeto
- memorizar esse dado, por em uma lista, historico, etc

"""


"""
Etapas pra criar um grafo

O grafo é uma estrutura logica,
em que você guarda uma informação 
e cria algum tipo de relacionamento

Para jogos vamos usar uma Matriz 2D

Onde cada coordenada vai representar um Tile

(0,0) (0,1) ...
(1,0) (1,1) 
...

Com base nisso precisamos de uma grade
Vamos criar essa grade dinamicamente
com base na
QUANTIDADE DE LINHAS e 
QUANTIDADE DE COLUNAS

"""
NUM_ROWS=3
NUM_COLS=3

DIRECTIONS=[(-1,0),(1,0),(0,-1),(0,1)]
grafo={}

for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        neighbors=[]
        for drow,dcol in DIRECTIONS:
            nrow=row+drow
            ncol=col+dcol
            if 0<=nrow<NUM_ROWS and 0<=ncol<NUM_COLS:
                neighbor=(nrow,ncol)
                neighbors.append(neighbor)
        grafo[(row,col)]=neighbors

# print(grafo)    

for tile,vizinhos in grafo.items():
        print(f"{tile} → {vizinhos}")
    
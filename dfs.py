"""
🧠 Lógica da DFS:

Começa no tile de origem

Marca como visitado

Visita os vizinhos um por um, recursivamente

Se chegar no destino, retorna o caminho

Se bater num beco sem saída, volta (backtrack)
"""

def dfs(grafo,cur,dst,path=None,visited=None):
    
    if visited is None:
        visited=set()
    if path is None:
        path=[]

    #momento que o nó se torna visitado
    visited.add(cur)
    path.append(cur)
    #verificams se já chegamos
    if cur==dst:return path.copy()
    #se nao chegamos, então precisamos explorar os vizinhos
    for neighbor in grafo.get(cur,[]):
        if neighbor not in visited:
            result=dfs(grafo,neighbor,dst,path=path,visited=visited)
            if result is not None:
                return result
    path.pop()
    return None
import json

#MODULO 1

grafo = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd'],
    'd': ['b', 'c']
}


def g(graph=grafo):
    print('{')
    for k,v in graph.items():
      print(f" {k}: {v} ")
    print('}')


g()


"""
✅ 1. Listar todos os nós do grafo

🧠 Lógica:
Como usamos um dicionário, cada chave representa um nó (ou vértice). 
É só pegar as chaves!
"""
nodes=list(grafo.keys())
# print(nodes)


"""
✅ 2. Pegar as conexões (vizinhos) de um nó
🧠 Lógica:
O valor do dicionário é uma lista de nós conectados diretamente (vizinhos).
"""

# 1) Metodo
b='b'
b_vizinhos=grafo[b]
# print(f"\nvizinhos de {b} -> {b_vizinhos}") 

#2) Metodo
vizinhos_b=grafo.get(b,[])
# print(vizinhos_b)


"""
✅ 3. Ver se dois nós estão conectados diretamente
🧠 Lógica:
Verifica se o segundo nó aparece na lista de vizinhos do primeiro.
"""

def is_connected(grafo, a, b):
    return b in grafo.get(a, [])

# print(json.dumps(grafo,indent=1))

# print(sao_conectados_direto(grafo, 'a', 'b'))  # True
# print(sao_conectados_direto(grafo, 'a', 'd'))  # False



"""
✅ 4. Ver se dois nós estão conectados (por caminho qualquer)
🧠 Lógica:
Aqui usamos DFS pra ver se conseguimos chegar de um nó até o outro, 
mesmo que não seja conexão direta.
"""

def has_path(graph,cur,dst,visited=None):
    if visited is None:
       visited=set()
    
    if cur==dst: #se passar a msma posiçao pra src e dst
      return True
    #visita o nó, etapa que consolida essa ação
    visited.add(cur)

    #explora as novas conexões ou vizinhos
    for neighbor in grafo.get(cur,[]):
       if neighbor not in visited:
          if has_path(graph,neighbor,dst,visited):
             return True
    return False


print(has_path(grafo,'a','z'))
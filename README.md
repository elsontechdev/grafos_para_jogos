### Grafos for Games

✅ Módulo 1 – Fundamentos de Grafos no Mundo dos Jogos

Objetivo: Entender o papel dos grafos nos jogos.

 - 📘 Teoria básica: vértices, arestas, grafos dirigidos, ponderados

 - 🕹 Exemplos em jogos: mapa, caminhos, máquinas de estado

 - 🧠 Visual mental: desenhar grafos simples no papel (ou usar graphviz)

🧩 Entregável: lista de adjacência de um mapa simples desenhada e interpretada

<hr>

#### 🎮 Aplicações reais em jogos:

| Tipo de grafo               |  Usado em...                                                     |
|-----------------------------|------------------------------------------------------------------|
| Grafo de grid               | Mapas 2D, movimentação por tiles                                 |
| Grafo de salas              | Dungeons, roguelikes (ex: *The Binding of Isaac*)                |
| FSM (Finite State Machine)  | IA de NPCs com estados como "patrulhar", "alerta", "atacar"      |
| Grafo de decisões           | Árvores de comportamento (*Behavior Trees*)                      |
| Grafo de navegação (NavMesh)| Jogos 3D com IA que anda em terrenos complexos                   |



### Represetação como lista de adjacência
Resumidamente é um dicionario em que cada chave é um local, nó ou tile
e o valor é uma lista, que representa onde podemos chegar a partir do ponto de origin

```py
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

### Mostrando os vizinhos de um ponto | Tile | Node

Por exemplo, se INICIARMOS no ponto `A` podemos, apatir dele, ir pro ponto `B` e ponto `C`<br>
Algo como: \
 `A` → `B` \
 `A` → `C`

Ou em Código

No `grafo` podemos ir de `A` para `B` e `A` para `C`
```py

inicio='A'
vizinhos=grafo[inicio]

#Saída: 'A': ['B', 'C'],
```
Modo seguro de acessar os vizinhos \
Caso um Nó | Tile não tenha vizinhos, o codigo não lança erros (`exception`)

```py

inicio='A'
vizinhos=grafo.get(inicio,[])
# Se não ouver um valor associado a esse Nó, 
# Retorna uma lista vazia []
#Saída: 'A': ['B', 'C'],
```
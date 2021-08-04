import networkx as nx  # Esta é uma biblioteca que gera e realiza operações e análises com grafos

G = nx.Graph()  # Criando o grafo

entrada = str(input()).split(' ')
n = int(entrada[0])  # Número de membros
k = int(entrada[1])  # Número de relacionamentos

for membro in range(1, n + 1):
    G.add_node(membro)  # Adiciona um nó do grafo para cada membro

for relacionamento in range(k):
    r = str(input()).split(' ')
    m1 = int(r[0])
    m2 = int(r[1])
    G.add_edge(m1, m2)  # Adiciona um vértice entre dois membros

# Após construir o grafo, é possível printar a quantidade de grupos isolados diretamente:
print(nx.number_connected_components(G))

import numpy as np

# Зчитуємо граф з файлу
with open('input.txt', 'r') as file:
    n = int(file.readline()) # Кількість вершин
    graph = np.zeros((n,n)) # Ініціалізуємо матрицю суміжності з нулями
    for i in range(n):
        line = file.readline().split()
        for j in range(n):
            graph[i,j] = int(line[j])

# Реалізація алгоритму Крускала
def kruskal(graph):
    n = graph.shape[0] # Кількість вершин у графі
    edges = [] # Список ребер у графі
    for i in range(n):
        for j in range(i+1, n):
            if graph[i,j] > 0:
                edges.append((i,j,graph[i,j])) # Додаємо ребро у список ребер та його вагу
    edges.sort(key=lambda x: x[2]) # Сортуємо список ребер за зростанням ваги

    mst = [] # Мінімальне каркасне дерево
    parent = list(range(n)) # Список для зберігання представників множин
    rank = [0] * n # Список для зберігання рангів множин

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[px] = py
            if rank[px] == rank[py]:
                rank[py] += 1

    for edge in edges:
        if len(mst) == n-1: # Мінімальне каркасне дерево знайдено
            break
        u, v, weight = edge
        if find(u) != find(v): # Ребро не створює цикл у графі
            mst.append(edge)
            union(u, v)

    return mst

# Виконуємо алгоритм та виводимо результат
mst = kruskal(graph)
print("Мінімальне остове дерево:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")

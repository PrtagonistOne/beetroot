# Кількість вершин в графі
from math import inf

V = 4

# Визначте нескінченність як велику
# достатнє значення. Це значення буде
# використовується для вершин, не з'єднаних між собою
INF = 99999999

# По суті беремо окремо кожну вершину і знаходим найкоротший шлях до кожної іншої вершини і виводим
def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j])
    printSolution(dist)


# для виводу рішення, кожен рядок відповідає за одну вершину
def printSolution(dist):
    print('Найкоротший шлях між вершинами: ')
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print(f"{INF}", end=' '),
            else:
                print(f"{dist[i][j]}\t", end=' ')
            if j == V - 1:
                print("")

"""
            10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3           
"""

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]
floydWarshall(graph)
# 1 рядок за вершину (0)
# 2 рядок за верщину (1)
# 3 рядок за вершину (2)
# 4 рядок за вершину (3)

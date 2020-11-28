# ford算法求解最短路问题

w = [[0, 1, 5, 999, 3],
     [999, 0, 2, 999, 999],
     [999, 999, 0, 999, -4],
     [999, 999, 2, 0, 999],
     [999, 999, 999, 3, 0]]
size = 5
start = 0
dist = [999] * size
pre = [-1] * size
for i in range(size):
    dist[i] = w[start][i]
    pre[i] = 1 if i >= 1 else -1
for k in range(size-1):
    for i in range(size):
        for j in range(size):
            if dist[i] > dist[j] + w[j][i]:
                dist[i] = dist[j] + w[j][i]
                pre[i] = j+1
print(f'由点1出发到各点的最小距离分别为：{dist}')
print(f'由点1出发到各点的最短路路径为：{pre}')
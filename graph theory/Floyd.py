# Floyd算法求解最短路问题(所有顶点间的最短路)
# 输出为最短路矩阵,父节点矩阵
size = 5
w = [[0, 4, 5, 999, 999],
     [999, 0, 3, 999, 6],
     [999, 999, 0, -2, 3],
     [999, 1, 999, 0, 999],
     [-4, 999, 999, 2, 0]]
dist_0 = w
dist_1 = dist_0
pre_0 = [[1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5]]
pre_1 = pre_0

for k in range(size):
    for i in range(size):
        for j in range(size):
            if dist_0[i][j] > dist_0[i][k] + dist_0[k][j]:
                dist_1[i][j] = dist_0[i][k] + dist_0[k][j]
                pre_1[i][j] = pre_0[i][k]
            else:
                dist_1[i][j] = dist_0[i][j]
                pre_1[i][j] = pre_0[i][j]
    pre_0 = pre_1
    dist_0 = dist_1
print(f'输出的权矩阵为{dist_1}')
print(f'输出的路径矩阵为{pre_1}')
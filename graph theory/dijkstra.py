import numpy
# n = int(input("请输入网络图中点的个数："))
# W = numpy.zeros((n, n))    # 定义一个初始的空的权矩阵
# for i in range(n):
#     for j in range(n):
#        W[i][j] = eval(input(f"请输入点{i}到点{j}的距离："))    # 输入全矩阵的分量
# 输入例题中权矩阵
W = numpy.array([[10000, 50, 30, 40, 25],
                 [50, 10000, 15, 20, 10000],
                 [30, 15, 10000, 10, 20],
                 [40, 20, 10, 10000, 10],
                 [25, 10000, 20, 10, 10000]])
dist = []
dot = [1]
def mintree(ori, n):
    for i in range(n-1):
        min_W = min(W[ori][:])
        loc = numpy.argwhere(W[ori][:] == min_W)
        ori = int(loc[0][0])
        dist.append(min_W)
        dot.append(ori+1)
        for i in range(n-1):
            W[i][ori] = 10000
    return dot, dist
mintree(0,5)
print(f'最小树路径为:{dot}')
print(f'两点构成的边的权分别为：{dist}')
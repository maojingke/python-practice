for m in range(1,6):
    for i in range(1,6):
        for j in range(1,6):
            eij=e[i,j]
            if eij>e[i,m]+e[m,j]:
                eij=e[i,m]+e[m,j]
for i,j in range(1,6):
    print("点{}到点{}的最小距离为{}".format(i,j,eij))

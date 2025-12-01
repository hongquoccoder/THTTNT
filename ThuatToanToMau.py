G = [[0, 1, 1, 0, 1, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 1, 1, 0],
     [0, 1, 1, 0, 0, 1],
     [1, 0, 1, 0, 0, 1],
     [0, 1, 0, 1, 1, 0]]


node = "ABCDEF"
t_ = {}
for i in range(len(G)):
    t_[node[i]] = i
    print("ten dinh:", node[i], " index:", i)
print(t_)


degree = []
for i in range(len(G)):
    degree.append(sum(G[i]))
    print("bac cua dinh", node[i], "la:", degree[i])
print(degree)

colorDict = {}
for i in range(len(G)):
    colorDict[node[i]] = ["Blue", "Red", "Yellow", "Green"]
print(colorDict)

sortedNode = []
indeks = []

for i in range(len(degree)):
    _max = 0
    j = 0
    for j in range(len(degree)):
        if j not in indeks:
            if degree[j] > _max:
                _max = degree[j]
                idx = j
    indeks.append(idx)
    sortedNode.append(node[idx])

theSolution = {}
for n in sortedNode:
    setTheColor = colorDict[n]
    theSolution[n] = setTheColor[0]
    adjacentNode = G[t_[n]]
    for j in range(len(adjacentNode)):
        if adjacentNode[j] == 1 and (setTheColor[0] in colorDict[node[j]]):
            colorDict[node[j]].remove(setTheColor[0])

    
for t, w in sorted(theSolution.items()):
    print("Dinh:", t, " co mau la:", w)
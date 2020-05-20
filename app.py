import operator
from itertools import compress

nodes = ["A","B","E","S"]

paths_matrix = [[0,0,1,1],[0,0,0,1],[1,0,0,1],[1,1,1,0]]
dist_matrix =  [[0,0,2,3],[0,0,0,2],[2,0,0,3],[3,2,3,0]]

start = curr = "S"
end = "E"
vi = []
unvi = nodes

def buildTent(nodes):
    tent = {}
    for node in nodes:
        tent[node] = (1e400,[])
    tent[start] = (0,[])
    return tent

tent = buildTent(nodes)
conn = list(compress(nodes,paths_matrix[nodes.index(curr)]))
conndist = list(compress(dist_matrix[nodes.index(curr)],paths_matrix[nodes.index(curr)]))

while "E" not in vi:
    for c in conn:
        if(tent[c][0]) == 1e400:
            tent[c] = (conndist[conn.index(c)], [curr])
        else: ## need to update to add on value from the current node rather than just select the distance from the current node.
            route = tent[c][1]
            route.append(curr) ## need to only keep track of the last position.  final answer can work back through
            #route.append(curr)
            tent[c] = (conndist[conn.index(c)], route)

    print("tent", tent)
    vi.append(curr)
    print(vi)
    unvi.pop(unvi.index(curr))
    print(unvi)
    if end in vi:
        print("shortest path found")
        quit()
    for u in unvi:
        if tent[u][0]== 1e400:#check if the lowest unvisited distance is infinity then there is no path
            print("no path to finish")
            quit()
    # choose new current item
    min = 1e400
    for t in tent:
        if t in vi:
            pass
        elif tent[t][0] < min:
            min = tent[t][0]
            curr = t
    print(curr)


"""

####restart looping through items

conn = list(compress(nodes,paths_matrix[nodes.index(curr)]))
conndist = list(compress(dist_matrix[nodes.index(curr)],paths_matrix[nodes.index(curr)]))
print("conn",conn,"conndist",conndist)
for c in conn:
    if(tent[c][0]) == 1e400:
        tent[c] = (conndist[conn.index(c)], [curr])
    else:
        route = tent[c][1]
        route.append(curr)
        #route.append(curr)
        tent[c] = (conndist[conn.index(c)], route)

print("tent", tent)

vi.append(curr)
print(vi)
unvi.pop(unvi.index(curr))
print(unvi)
if end in vi:
    print("shortest path found")
    quit()
for u in unvi:
    if tent[u][0]== 1e400:#check if the lowest unvisited distance is infinity then there is no path
        print("no path to finish")
        quit()

# choose new current item
min = 1e400
for t in tent:
    if t in vi:
        break
    if tent[t][0] < min:
        min = tent[t][0]
        curr = t
print(curr)



"""
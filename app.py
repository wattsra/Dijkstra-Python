import operator
from itertools import compress

# nodes = ["A","B","E","S"]
#
# paths_matrix = [[0,0,1,1],
#                 [0,0,0,1],
#                 [1,0,0,1],
#                 [1,1,1,0]]
#
# dist_matrix =  [[0,0,2,3],
#                 [0,0,0,2],
#                 [2,0,0,6],
#                 [3,2,6,0]]


nodes = ["A","B","C","D","E","S"]

                #A,B,C,D,E,S
paths_matrix = [[0,0,1,0,1,1],#A
                [0,0,0,1,1,1],#B
                [1,0,0,0,1,0],#C
                [0,1,0,0,0,1],#D
                [1,1,1,0,0,0],#E
                [1,1,0,1,0,0]]#S

                #A,B,C,D,E,S
dist_matrix =  [[0,0,4,0,2,3],#A
                [0,0,0,2,1,4],#B
                [4,0,0,0,4,0],#C
                [0,2,0,0,0,3],#D
                [2,1,4,0,0,0],#E
                [3,4,0,3,0,0]]#S

start = curr = "S"
end = "E"
vi = []
unvi = nodes[:]

def buildTent(nodes):
    tent = {}
    for node in nodes:
        tent[node] = (1e400,"")
    tent[start] = (0,"")
    return tent

tent = buildTent(nodes)

while "E" not in vi:
    conn = nodes[:]
    conn = list(compress(conn,paths_matrix[nodes.index(curr)]))
    conndist = dist_matrix[:]
    conndist = list(compress(dist_matrix[nodes.index(curr)],paths_matrix[nodes.index(curr)]))
    for c in conn:
        if(tent[c][0]) == 1e400:
            tent[c] = (conndist[conn.index(c)], curr)
        elif c in vi:
            pass
        elif tent[c][0] > conndist[conn.index(c)]: ## need to update to add on value from the current node rather than just select the distance from the current node.
            #route = tent[c][1]
            #route.append(curr) ## need to only keep track of the last position.  final answer can work back through
            #route.append(curr)
            tent[c] = (conndist[conn.index(c)], curr)

    vi.append(curr)
    unvi.pop(unvi.index(curr))
    if end in vi:
        p = end
        path = []
        pathdist = 0
        while p != start:
            path.append(p)
            pathdist += tent[p][0]
            p = tent[p][1]
        path.append(start)
        path.reverse()
        print("shortest path is:", path, "with a distance of", pathdist) #output final shortest path
        quit()

    ## build list of the shortest paths
    mini = []
    for u in unvi:
        mini.append(tent[u][0])

    # check if the lowest unvisited distance is infinity then there is no path
    if min(mini) == 1e400:
         print("no path to finish")
         quit()

    curr = unvi[mini.index(min(mini))] # choose new current item based on shortest unvisited distance

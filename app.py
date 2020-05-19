#paths = {"S":"A","A":"S","S":"B","B":"S","S":"E","E":"S","A":"E","E":"A"}
#paths_matrix = []
#weighted_matrix =

nodes = ["A","B","S","E"]

paths = {"A":["S","E"],"B":["S"],"E":["A","S"],"S":["A","B","E"]}
lengths = {"AS":3,"AE":2,"BS":2,"ES":3}


paths_matrix = [[0,0,1,1],[0,0,1,0],[1,1,0,1],[1,0,1,0]]
dist_matrix =  [[0,0,3,2],[0,0,2,0],[3,2,0,3],[2,0,3,0]]

start = currentnode = "S"
visitednodes = [start]
end = "E"
visit = ""

def buildTent(nodes):
    tent = {}
    for node in nodes:
        tent[node] = 0
    return tent

tent = buildTent(nodes)

currentnodedistances = dist_matrix[nodes.index(currentnode)]
print(currentnodedistances)
print(tent)
for i in range(len(currentnodedistances)):
    if i != 0:
        tent[nodes[i]] = currentnodedistances[i]
print(tent)



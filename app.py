
nodes = ["A","B","S","E"]
paths = {"S":"A","A":"S","S":"B","B":"S","S":"E","E":"S","A":"E","E":"A"}
lengths = {"SA":3,"AE":2,"SB":2,"SE":3}
#tent = {}#each node gets a tentative value of infinity (using zero for ease)
visitednodes = ["S"]
currentnode = ["S"]

def buildTent(nodes):
    tent = {}
    for node in nodes:
        tent[node] = 0
    return tent

tent = buildTent(nodes)
print(tent)

while currentnode =! "E":
    for


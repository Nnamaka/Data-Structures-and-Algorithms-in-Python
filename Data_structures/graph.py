
class graph:
    def __init__(self, gdict) -> None:
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVerticies(self):
        return list(self.gdict.keys())
    
    def findedges(self):
        foundedges = []

        for key in self.gdict:
            for points in self.gdict[key]:
                if {key, points} not in foundedges:
                    foundedges.append({key, points})
        return foundedges

    def getEdges(self):
        return self.findedges()
    
    def setVertex(self, value):
        if value not in self.gdict:
            self.gdict[value] = []

    def addEdge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        
        if vertex1 in self.gdict:
            # TODO: avoid duplicate edges ✅
            if vertex2 not in self.gdict[vertex1]:
                self.gdict[vertex1].append(vertex2)
                
        else:
            self.gdict[vertex1] = [vertex2]

    def showGraph(self):
        print(self.gdict)


graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}

# vert = []
# for key in graph_elements:
#     for vertices in graph_elements[key]:
#         if {vertices, key} not in vert:
#             vert.append({vertices, key})
# edgenames = []
# for key in graph_elements:
#     for points in graph_elements[key]:
#         if {points, key} not in edgenames:
#             edgenames.append({points, key})

g = graph(graph_elements)
g.addEdge({'a', 'b'})
g.addEdge({'a', 'b'})


g.showGraph()
# print(g.getEdges())


#------------------------------------------------------------------
# you can use set to remove duplicates in vertices edges in the graph
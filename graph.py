
#   Graph = {'1' : ['2'],   # Adjacency List 
#            '2' : ['1','4'],
#            '3' : ['4','5'],
#            '4' : ['2','3','5'],
#            '5' : ['3','4'] }

class Graph:

    """ Insert given vertex and edge into graph """

    def __init__(self):

        vertices = {}              # Used a Dictionary to store vertex as key
                                   # and lists as values
        self.vertices = vertices

    def add_vertex(self,new_vertex):  # Add vertex = add key

        """ Add vertex as key """

        self.vertices[new_vertex] = []

    def add_edge(self, new_vertex, new_edge):

        """ Add edge values in list """
        
        self.vertices.setdefault(new_vertex, []).append(new_edge)

    def show_graph(self):

        """ Display the graph """
        
        print("")
        print(self.vertices)

g = Graph()  

g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')

g.show_graph()

g.add_edge('1',['2','6'])
g.add_edge('2',['1','4'])
g.add_edge('3',['4','5'])
g.add_edge('4',['2','3','5','6'])
g.add_edge('5',['3','4','6'])

print("")
print("Graph")
g.show_graph()
        

    

    

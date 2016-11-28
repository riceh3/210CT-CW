
#my_graph = {'1' : ['2'(5)],   
   #         '2' : ['1'(5),'4'(7)],
    #        '3' : ['4'(4),'5'(8)],
     #       '4' : ['2'(7),'3'(4),'5'(3)],
      #      '5' : ['3'(8),'4'(3)] }
      
import sys

class Graph:

    """ Insert given vertex and edges into graph """

    def __init__(self):

        vertices = {}               # Used a dictionary to store vertex as key
        self.vertices = vertices
        visited = []     
        self.visited = visited

    def add_vertex(self,new_vertex):

        """ Add vertex as key """

        self.vertices[new_vertex] = []

    def add_edge(self, new_vertex, new_edge, weight):

        """ Add edge and weight """

        self.vertices.setdefault(new_vertex, []).append(new_edge)
        self.vertices[new_vertex].append(weight)
        
    def show_graph(self):

        """ Display the graph """

        print(self.vertices)

    def dijkstra(self, start, destination, visited, weight):

        """ Find the shortest path using the weights of each edge """
        
        edge = []

        if start not in visited:                  # If not already visited vertex 

            if start != destination:              
            
                visited.append(start)             # Add current vertex to visited list
                print("")
                print("Visited")
                print(visited)

                search = self.vertices[start]     # Access edges to current vertex 

                for w in search:                  # Find the weights 

                    if type(w) == int:            # Weights are integers 
                        weight.append(w)          # Put weights into list 

                    else:
                        edge.append(w)            # Put edges into list 
                        print("")

                min_weight = min(weight)          # Find lowest weight from list 

                weight.clear()                    

                weight.append(min_weight)         # Only store the min weight

                # The edge before min weight will be our next start vertex

                if weight[0] == search[1]:
                    
                    a = str(edge[0])
                    start = a
                    g.dijkstra(start, destination, visited, weight)
                    return start
                

                elif weight[0] == search[3]:
                    start = edge[1]
                    g.dijkstra(start, destination, visited, weight)
                    return start

                elif weight[0] == search[5]:
                    start = edge[2]
                    g.dijkstra(start, destination, visited, weight)
                    return start

            else:
                
                return start 
        else:
            print("The shortest path : ")
            print(visited)
            sys.exit()
  
g = Graph()                                  # Graph for visual representation:

g.add_vertex('1')                            #       1 --- 2 --- 4 --- 5
g.add_vertex('2')                            #                   |    /
g.add_vertex('3')                            #                   3 - /  
g.add_vertex('4')
g.add_vertex('5')

g.show_graph()
print("")

weight = (5)                                 # Add edges and weights 
g.add_edge('1',('2'),weight)
weight = (5)
g.add_edge('2',('1'), weight)
weight = (1)
g.add_edge('2',('4'), weight)
weight = (3)
g.add_edge('3',('4'), weight)
weight = (2)
g.add_edge('3',('5'), weight)
weight = (1)
g.add_edge('4',('2'), weight)
weight = (3)
g.add_edge('4',('3'), weight)
weight = (6)
g.add_edge('4',('5'), weight)
weight = (2)
g.add_edge('5',('3'), weight)
weight = (6)
g.add_edge('5',('4'), weight)


g.show_graph()

start = '1'                               # Start path 
destination = '3'                         # End path 
weight = []
visited = []
g.dijkstra(start, destination, visited, weight)






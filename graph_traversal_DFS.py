import sys

class Graph:

    """ Insert given vertex and edge into graph """

    def __init__(self):

        vertices = {}                  # Used a Dictionary to store vertex as key
                                       #  - and lists as values 
        visited = []                   # Empty list for DFS
        self.vertices = vertices
        self.visited = visited

    def add_vertex(self, new_vertex):

        """ Add vertex as key """

        self.vertices[new_vertex] = []

    def add_edge(self, new_vertex, new_edge):

        """ Add edge to values in list """

        self.vertices.setdefault(new_vertex,[]).append(new_edge)

    def show_graph(self):

        """ Display the graph """

        print(self.vertices)

    def depth_first_search(self, start_search, stack, z):

        """ Depth first search of graph """

        try:                                          # Catch index error

            if start_search not in self.visited:      # Not visit the same vertex

                self.visited.append(start_search)     # Add current vertex to visited

                print("Visited")
                print(self.visited)

                search = self.vertices[start_search]  # Access key(vertex),values(edges)
                x = 0
                go = True

                while go == True:       # Itterate over edges and add to stack

                    for a,v in enumerate(search):     # Allows to index values eg:(0,'2')

                        try:                          # Catch list index error
                            
                            if v[x] not in stack:     # No duplicates in stack
                                stack.append(v[x])
                                x = x+1

                                if v[x] in self.visited:  # Remove value from visited
                                    stack.remove(v[x])
                                    

                            else:
                                x = x+1

                        except:

                            go = False                # Break loop

                print("Stack")
                print(stack)
                print("")
                start_search = stack.pop(z)           # Take last in value(edge)
                                                      # Becomes current vertex
                                                      
                Graph.depth_first_search(self, start_search, stack, z)

                return start_search

            elif start_search in self.visited:  # If we have already visited the vertex
                
                start_search = stack.pop(z)     # Take next edge in stack
                
                stack.clear()                   # Empty stack to not skip vertexes
                
                Graph.depth_first_search(self, start_search, stack, z)

        
            else:

                return start_search

        except:
            print("Depth First Search : ")
            print(self.visited)

            f = open('DFS_file', 'w')
            intro = ('Depth first search ')
            f.write(intro)
            f.write(str(self.visited))
        

g = Graph()
g.add_vertex('A')                               # Add vertexes 
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')
g.add_vertex('G')
g.add_vertex('H')
g.add_vertex('S')

g.show_graph()
print("")
g.add_edge('A',['B','S'])                      # Add Edges 
g.add_edge('B',['A'])
g.add_edge('S',['A','C','G'])
g.add_edge('C',['S','F','E','D'])
g.add_edge('D',['C'])
g.add_edge('E',['C','H'])
g.add_edge('F',['G','C'])
g.add_edge('G',['S','H','F'])
g.add_edge('H',['G','E'])


g.show_graph()

start_search = ('A')      # Start node for traversal
z = 0                     # Allows to access position 0 of stack for pop()
stack = []                # Empty stack

g.depth_first_search(start_search, stack, z)

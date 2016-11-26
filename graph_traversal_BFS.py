# new graph from slides:

# { 'A' : ['B','S'],                         # Adjacency List
#   'B' : ['A'],
#   'C' : ['D','E','F','S'],
#   'D' : ['C'],
#   'E' : ['C','H'],
#   'F' : ['C','G'],
#   'G' : ['S','F','H'],
#   'H' : ['E','G'] }


import sys

class Graph:

    def __init__(self):

        vertices = {}
        edges = [] ##
        self.vertices = vertices
        self.edges = edges
        visited = []
        self.visited = visited

    def add_vertex(self, new_vertex):

        self.vertices[new_vertex] = []

    def add_edge(self, new_vertex, new_edge):

        self.vertices.setdefault(new_vertex,[]).append(new_edge)

    def show_graph(self):

        print(self.vertices)

    def breadth_first_search(self, start_search, z, queue):

        try:                                                          # Avoid z out of range index error

            if start_search not in self.visited:                      # Don't want to re-visit vertex

                self.visited.append(start_search)                     # Add current vertex to 'Visited'

                print("Visited")
                print(self.visited)

                search = self.vertices[start_search]                  # Get values linked to current vertex
                x = 0                                                 
                go = True
                
                while go == True:
                    
                    for a,v in enumerate(search):                     # Access each list element seperatley

                        try:
                            if v[x] not in queue:                     # Don't want duplicate edges in queue
                                queue.append(v[x])                    # Add edge to queue
                                x = x +1
                            else:
                                x = x+1

                        except IndexError:
                            print("Queue")
                            print(queue)
                            print("")
                            go = False                                # Breaks loop

                start_search = queue[z]                               # Next current vertex is first item in queue
                #z = z+1
                Graph.breadth_first_search(self, start_search, z, queue)

            elif start_search in self.visited:                        # If already been to that vertex
                queue.remove(start_search)                            # remove vertex from queue, because we have already been there
                start_search = queue[z]
                Graph.breadth_first_search(self,start_search,z, queue)

            else:
                print("")
                print(self.visited)                           
                
        except IndexError:                                            # z will go out of index range
            print(self.visited)
            

   

g = Graph()
g.add_vertex('A')
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

g.add_edge('A',['B','S'])
g.add_edge('B',['A'])
g.add_edge('S',['A','C','G'])
g.add_edge('C',['D','E','F','S'])
g.add_edge('D',['C'])
g.add_edge('E',['C','H'])
g.add_edge('F',['C','G'])
g.add_edge('G',['S','F','H'])
g.add_edge('H',['G','E'])

g.show_graph()
z = 0
queue = []
start_search = ('A')
g.breadth_first_search(start_search, z, queue)


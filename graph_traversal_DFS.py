import sys

class Graph:

    def __init__(self):

        vertices = {}
        visited = []
        self.vertices = vertices
        self.visited = visited

    def add_vertex(self, new_vertex):

        self.vertices[new_vertex] = []

    def add_edge(self, new_vertex, new_edge):

        self.vertices.setdefault(new_vertex,[]).append(new_edge)

    def show_graph(self):

        print(self.vertices)

    def depth_first_search(self, start_search, stack, z):

        try:

            if start_search not in self.visited:

                self.visited.append(start_search)

                print("Visited")
                print(self.visited)

                search = self.vertices[start_search]
                x = 0
                go = True

                while go == True:

                    for a,v in enumerate(search):

                        try:
                            
                            if v[x] not in stack:
                                stack.append(v[x])
                                x = x+1

                                if v[x] in self.visited:
                                    stack.remove(v[x])
                                    

                            else:
                                x = x+1

                        except:

                            go = False

                print("Stack")
                print(stack)
                start_search = stack.pop(z)
                Graph.depth_first_search(self, start_search, stack, z)

                return start_search

            elif start_search in self.visited:
                
                start_search = stack.pop(z)
                stack.clear()
                Graph.depth_first_search(self, start_search, stack, z)

        
            else:

                print("END")
                print(self.visited)

        except:
            print("THIS IS THE END")
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
g.add_edge('C',['S','F','E','D'])
g.add_edge('D',['C'])
g.add_edge('E',['C','H'])
g.add_edge('F',['G','C'])
g.add_edge('G',['S','H','F'])
g.add_edge('H',['G','E'])


g.show_graph()

start_search = ('A')
z = 0
stack = []
g.depth_first_search(start_search, stack, z)

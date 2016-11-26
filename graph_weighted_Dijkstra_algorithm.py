
#my_graph = {'1' : ['2'(5)],   # own list of directly connected vertexes
   #         '2' : ['1'(5),'4'(7)],
    #        '3' : ['4'(4),'5'(8)],
     #       '4' : ['2'(7),'3'(4),'5'(3)],
      #      '5' : ['3'(8),'4'(3)] }
import sys
class Graph:

    def __init__(self):

        vertices = {}
        self.vertices = vertices
        visited = []
        self.visited = visited

    def add_vertex(self,new_vertex):  # Add vertex = add key

        self.vertices[new_vertex] = []

    def add_edge(self, new_vertex, new_edge, weight):

        self.vertices.setdefault(new_vertex, []).append(new_edge)
        self.vertices[new_vertex].append(weight)
        
    def show_graph(self):

        print(self.vertices)

    def find_weight(self):

        current = self.vertices['2']
        print(current)

        weight = []

        for t in current:

            if type(t) == int:
                weight.append(t)

            else:
                print("")

        print("Weight")
        print(weight)

    def dijkstra(self, start, destination, visited, weight):
        v = []

        if start not in visited:

            if start != destination:
            
                visited.append(start)
                print("")
                print("Visited")
                print(visited)

                search = self.vertices[start]

                for w in search:

                    if type(w) == int:
                        weight.append(w)

                    else:
                        v.append(w)
                        print("")

                min_weight = min(weight)

                weight.clear()

                weight.append(min_weight)

                if weight[0] == search[1]:
                    a = str(v[0])
                    start = a
                    g.dijkstra(start, destination, visited, weight)
                    return start
                

                elif weight[0] == search[3]:
                    start = v[1]
                    g.dijkstra(start, destination, visited, weight)
                    return start

                elif weight[0] == search[5]:
                    start = v[2]
                    g.dijkstra(start, destination, visited, weight)
                    return start

            else:
                print(self.visited)
                sys.exit()
        else:
            print("The shorted path")
            print(visited)
            sys.exit()
  
g = Graph()
g.add_vertex('1')                            #       1 --- 2 --- 4 --- 5
g.add_vertex('2')                            #                   |    /
g.add_vertex('3')                            #                   3 - /  
g.add_vertex('4')
g.add_vertex('5')

g.show_graph()
print("")

weight = (5)
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

start = '1'
destination = '3'
weight = []
visited = []
g.dijkstra(start, destination, visited, weight)

#g.find_weight()
#print("")
#g.show_graph()
#print("")
#start = '1'





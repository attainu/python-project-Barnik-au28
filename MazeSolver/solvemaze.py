from collections import defaultdict
import argparse


class Maze:
    def __init__(self):
        self.graph = defaultdict(list)
        self.edges = {}
        self.vertices = []
        self.prev_vertec = {}

    def add_edge(self, u, v, weight=1):
        self.graph[u].append(v)
        self.graph[v].append(u)

        if u not in self.vertices:
            self.vertices.append(u)
        if v not in self.vertices:
            self.vertices.append(v)

        self.edges[(u, v)] = weight
        self.edges[(v, u)] = weight

        # to determine that the graph is connected

    def connect(self, u, v):
        vertex_visited = {}
        for i in self.graph:
            vertex_visited[i] = False

            # initialising a queue
            queue = []
            # adding elements to queue
            queue.append(u)
            connected_vertex = set()

            while queue:
                temp = queue.pop
                connected_vertex.add(temp)
                vertex_visited[temp] = True
                for i in self.graph[temp]:
                    if vertex_visited is False:
                        queue.append(i)
# u and v connect with vertex of graph
            if u in connected_vertex and v in connected_vertex:
                return True
            return False

    def algo(self, node):
        dist = {}
        vertex_visited = {}

        for i in self.graph:
            if i == node:
                # node having min distance
                dist[(node, i)] = 0
            else:
                # node having max distance
                dist[node, i] = 10 ** 9
        for i in self.graph:
            vertex_visited[i] = False
        temp = node

        while vertex_visited[temp] is False:
            vertex_visited[temp] = True
            for i in self.graph[temp]:
                if vertex_visited[i] is False and dist[(node, i)] > \
                        self.edges[(temp, i)] + dist[(node, temp)]:
                    dist[(node, i)] = self.edges[(temp, i)] + \
                        dist[(node, temp)]
                    self.prev_vertex[i] = temp

            temp_dict = {}
            for i in self.graph[temp]:
                temp_dict[i] = dict[(node, i)]
            temp_dict = sorted(temp_dict.items(),
                               key=lambda kv: (kv[1], kv[0]))
            for i in range(len(temp_dict)):
                if vertex_visited[temp[i][0]] is False:
                    temp = temp_dict[i][0]
                    break
                else:
                    if vertex_visited[self.prev_vertex[temp]] is False:
                        temp = self.prev_vertex[temp]
                    else:
                        min_dist = 10**9
                        for i in self.graph:
                            if vertex_visited is False and dist[(node, i)] < min_dist:
                                temp = i
                                break
        return self.prev_vertex

    def src_dest(self, u, v):
        if self.connect(u, v):
            prev_vertex = self.algo(u)
            prev_vertex = list(prev_vertex.items())

            size = len(prev_vertex)
            src_dest = []
            temp = v
            while temp:
                src_dest.insert(0, temp)
                if temp == u:
                    break
                for i in range(size):
                    if prev_vertex[i][0] == temp:
                        temp = prev_vertex[i][1]
            src_dest = set(src_dest)
            return src_dest
        return -1


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", type=str, default="inputfile.txt",
                        help="-i for inputfile.txt")

    parser.add_argument("-o", type=str, default="outputfile.txt",
                        help="-o for outputfile.txt")

    parser.add_argument("-s", type=str, default="0, 0",
                        help="-s for source point")

    parser.add_argument("-d", type=str, default="4, 4",
                        help="-d for dest point")

    args = parser.parse_args()

    g = Maze()

    # For reading inputfile

    input_file = open(args.i, "r")
    order = input_file.readline()
    input_file.close()

    # for read matrix in inputfile

    input_file = open(args.i, "r")
    input_matrix = []
    order = int(order)

    for i in range(order+1):
        line = input_file.readline()
        if i > 0:
            input_matrix.append(list(map(int, line.rstrip().split())))

    input_file.close()

    # to check if matrix is suare matrix
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix)):
            if j-1 >= 0 and input_matrix[i][j-1] == 1 \
                    and input_matrix[i][j] == 1:
                g.add_edge((i, j-1), (i, j))
            if i-1 >= 0 and input_matrix[i-1][j] == 1 \
                    and input_matrix[i][j] == 1:
                g.add_edge((i-1, j), (i, j))

    # detination and source points

    u = tuple(map(int, args.s.split(",")))
    v = tuple(map(int, args.d.split(",")))
    temp_list = g.src_dest(u, v)

    # writing solution to output file
    output_file = open(args.o, "w")
    output_list = [[str(0) for i in range(order)] for j in range(order)]
    if type(temp_list) is set:
        for i in range(order):
            for j in range(order):
                if (i, j) in temp_list:
                    output_list[i][j] = str(1)

        for i in output_list:
            s = " ".join(i)
            output_file.write(s)
            output_file.write("\n")
        output_file.close()
    else:
        output_file.write(str(temp_list))
        output_file.close()


main()

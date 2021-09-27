class Cost(object):

    def __init__(self, file_name: str, num_nodes: int,  cost_matrix: list):
        self.file_name = file_name
        self.num_nodes = num_nodes
        self.cost_matrix = cost_matrix

    #Function to handle file and return optimal path along with its cost
    def findCost(self):
        nodes = []
        read_nodes = False

        with open(self.file_name, 'r') as file:
            for line in file.readlines():

                node = line.strip().split()

                if node[0] == "1":
                    read_nodes = True
                    nodes.append(int(node[0]) - 1)

                elif read_nodes and node[0] != "EOF" and node[0] != "-1":
                    nodes.append(int(node[0]) - 1)

                elif read_nodes and node[0] == "-1":
                    nodes.append(nodes[0])

        file.close()

        opt_path_cost = self.calculatePathCost(nodes, self.num_nodes, self.cost_matrix)
        opt_path = nodes

        for i in range(self.num_nodes + 1):
            opt_path[i] += 1

        return opt_path_cost, opt_path

    #Function to calculate the optimal path's cost and return it
    def calculatePathCost(self, optimal_path_list, num_nodes, cost_matrix):
        path_cost = 0

        for i in range(num_nodes):
            node = optimal_path_list[i]
            next_node = optimal_path_list[i + 1]

            path_cost += cost_matrix[node][next_node]

        return path_cost
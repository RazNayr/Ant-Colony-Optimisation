import math
import time
import os
from aco import ACO
from optCost import Cost

def main():

    nodes = []              #List to store all node coordinates
    pathCost_matrix = []    #Matrix to store distances between each and every node

    read_nodes = False

    num_generations = 0 #int to store the number of generations for ACO
    num_ants = 0        #int to store the number of ants to be used for ACO
    alpha = 0           #float to store the alpha value denoting the impact of the pheromone matrix
    beta = 0            #float to store the beta value denoting the impact of the path cost matrix
    rho = 0             #float to act as an evaporation constant, used when evaporating pheromones

    aco_file_name, opt_file_name = chooseTspFiles()

    if aco_file_name != "":
        #Reading from tsp file
        #Appending node coordinates to 'nodes' list
        with open(aco_file_name, 'r') as file:
            for line in file.readlines():

                node = line.strip().split()

                if node[0] == "1":
                    read_nodes = True
                    nodes.append([float(node[1]), float(node[2])])

                elif read_nodes and node[0] != "EOF":
                    nodes.append([float(node[1]), float(node[2])])

                elif node[0] == "EOF":
                    break

        file.close()
        num_of_nodes = len(nodes)

        #Appending the distances between each and every node within 'pathCost_matrix'
        for i in range(num_of_nodes):
            row = []
            for j in range(num_of_nodes):
                row.append(distanceBetween(nodes[i], nodes[j]))
            pathCost_matrix.append(row)

        print("\n---------------------------ACO---------------------------")
        num_generations = int(input("Please input the number of generations needed: "))
        num_ants = int(input("Please input the number of ants needed: "))
        alpha = float(input("Please input the alpha value needed: "))
        beta = float(input("Please input the beta value needed: "))
        rho = float(input("Please input the evaporation constant needed: "))
        print("---------------------------------------------------------\n")

        start_time = time.time()
        cost, path = ACO(num_ants, num_generations, alpha, beta, rho, pathCost_matrix, num_of_nodes).solve()
        print("ACO took %s seconds to complete\n" % (time.time() - start_time))

        print("Optimal Path achieved: {}".format(path))
        print("Cost of path achieved: {}".format(cost))

        if opt_file_name != "":
            opt_path_cost, opt_path = Cost(opt_file_name, num_of_nodes, pathCost_matrix).findCost()
            print("Optimal Path : {}".format(opt_path))
            print("Optimal Path Cost: {}".format(opt_path_cost))



    else:
        print("Invalid file chosen!")


#Function to calculate and return the Euclidian distance between two nodes
def distanceBetween(node1, node2):
    x1 = node1[0]
    y1 = node1[1]
    x2 = node2[0]
    y2 = node2[1]

    return math.sqrt( ((x1-x2)**2) + ((y1-y2)**2) )

#Function to accept user input and return which TSP file he wishes to use
def chooseTspFiles():

    tsp_directory = "TSP files"
    tsp_opt_directory = "TSP Opt Tour files"

    tsp_file_chosen = ""
    tsp_opt_file = ""

    file_count = 0
    user_choice = 0

    for filename in os.listdir(tsp_directory):
        if filename.endswith(".tsp.txt"):
            file_count += 1
            print(file_count, ". ", filename)


    user_choice = int(input("Please input the desired TSP file (by number): "))

    for filename in os.listdir(tsp_directory):
        if filename.endswith(".tsp.txt"):
            user_choice -= 1

            if user_choice == 0:
                tsp_file_chosen = filename
                break

    name, ext = os.path.splitext(tsp_file_chosen)
    name, ext = os.path.splitext(name)

    for filename in os.listdir(tsp_opt_directory):
        if filename.startswith(name) and filename.endswith(".opt.tour.txt"):
            tsp_opt_file = filename
            break

    if tsp_file_chosen != "":
        tsp_file_chosen = tsp_directory + "/" + tsp_file_chosen

    if tsp_opt_file != "":
        tsp_opt_file = tsp_opt_directory + "/" + tsp_opt_file

    return tsp_file_chosen, tsp_opt_file

if __name__ == '__main__':
    main()
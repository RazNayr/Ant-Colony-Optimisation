# Project Artefacts

## Source Code
#### _aco.py_
python script responsible for apply the concept of ACO by solving
and returning the most optimal path managed to be found from a set
of generations.


#### _main.py_
main python script responsible for accepting user input to choose 
which travelling salesman problem to use and define the ACO parameters.


#### _optCost.py_
the script responsible for calculating and returning the optimal path 
cost of the most optimal path found in TSPLIB, along with its path to 
be displayed in the main class.


## Data Folders
#### _TSP files_
This folder contains all 4 tsp problems to be used within the program

#### _TSP Opt Tour files_
This folder contains all 4 most optimal paths (as per TSPLIB) to the tsp
problem equivalents in the 'TSP files' folder.

<br />
<br />

# ACO
Ant Colony Optimisation or ACO for short, can be defined as:

> “a population-based metaheuristic that can be used to find approximate solutions to difficult optimization problems. In ACO, a set of software agents called artificial ants search for good solutions to a given optimization problem.” [1]

In simpler terms, an ACO involves a set of algorithms which make use of probabilistic techniques, in order to solve optimisation problems. This is done by searching for the most optimal path within a set of paths, thus mimicking real life ants going through their environment and finding the most efficient path from one point to the next.

## How it works
To fully understand how an ACO works, we must first know how a real-life ant colony works itself. An ant colony functions by having pheromone trails along paths, whereby each and every ant leaves a small amount of pheromone within its path. The more ants that follow such a path, the more pheromone gets laid throughout it. By this, other ants are encouraged to follow this path, which proved to be a very efficient one for some ants before it. Apart from pheromone quantity, ants are also encouraged to choose paths depending on how costly they are. If for example path A is shorter and safer than path B, it is proven to be more efficient to the ant and so is encouraged to choose path A.

Essentially, an ACO groups the above-mentioned factors and forms a probabilistic model by which agents (in this case ants) have a chance to choose one path, over another in every generation. After a number of generations, the model would have converged towards an optimal path, which may or may not be the best path to take but is surely close to the best possible path. One big strength of ACO has to do with the ability of customisation. The user is able to define and give different priorities based on what he is trying to solve. If for example, the user wishes to give more importance to the pheromone trail other than the path cost, he may easily do so. Moreover, the user is able to simulate vaporisation of pheromone within the algorithm. This is done so that pheromone isn’t allowed to exist forever between generations, thus reducing the chances of premature convergence [2] where one extremely popular path (in the first couple of generations) takes over other paths, which may be more efficient in the long run.

<br />
<br />

## References
[1] S. Chandra and S. Bhattacharyya, "Quantum Inspired Swarm Optimization for Multi-Level Image Segmentation Using BDSONN Architecture", Advances in Computational Intelligence and Robotics, pp. 286-326, 2015. Available: 10.4018/978-1-4666-8291-7.ch009 [Accessed 27 September 2021].

[2] O. Castillo, H. Neyoy, J. Soria, M. García and F. Valdez, "Dynamic Fuzzy Logic Parameter Tuning for ACO and Its Application in the Fuzzy Logic Control of an Autonomous Mobile Robot", International Journal of Advanced Robotic Systems, vol. 10, no. 1, p. 51, 2013. Available: 10.5772/54883.


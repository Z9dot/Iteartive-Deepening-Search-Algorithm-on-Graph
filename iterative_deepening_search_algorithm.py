class Graph:
    # Initialize a Graph object with an empty or user-defined graph dictionary
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    # Add an edge between two nodes in the graph
    def add_edge(self, node, neighbor):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbor]
        else:
            self.graph_dict[node].append(neighbor)
# Implement the Iterative Deepening Search algorithm to search for a path from a source node to a target node within a depth limit
    def ids(self, source, target, max_depth):
        # Iterate over depth levels starting from 0 to the maximum depth limit
        for depth in range(max_depth):
            # Create an empty visited list and a stack containing the source node
            visited = []
            stack = [[source]]
            # Continue the search until there are no more nodes to explore or the target node is found
            while stack:
                path = stack.pop()   # Pop the top path from the stack
                node = path[-1]     # Get the last node in the path
                # If the target node is found, return the path
                if node == target:
                    return path
                # If the node has not been visited and the path length is less than or equal to the current depth level
                if node not in visited and len(path) <= depth + 1:
                    visited.append(node)    # Mark the node as visited
                    # For each neighbor of the node, create a new path by appending the neighbor to the current path
                    for neighbor in self.graph_dict.get(node, []):
                        new_path = list(path)
                        new_path.append(neighbor)   # Add the new path to the stack for exploration
                        stack.append(new_path)
        # If no path is found within the depth limit, return None
        return None

# Testing the code
network = Graph()
network.add_edge('Sys_1', 'Sys_2')
network.add_edge('Sys_1', 'Sys_3')
network.add_edge('Sys_2', 'Sys_4')
network.add_edge('Sys_2', 'Sys_5')
network.add_edge('Sys_3', 'Sys_6')
network.add_edge('Sys_3', 'Sys_7')
network.add_edge('Sys_4', 'Sys_8')
network.add_edge('Sys_4', 'Sys_11')
network.add_edge('Sys_4', 'Sys_9')
network.add_edge('Sys_5', 'Sys_10')
network.add_edge('Sys_5', 'Sys_11')
network.add_edge('Sys_6', 'Sys_12')
network.add_edge('Sys_12', 'Sys_13')
network.add_edge('Sys_7', 'Sys_14')
network.add_edge('Sys_14', 'Sys_15')
source = 'Sys_1'
target = 'Sys_15'
max_depth = 5
path = network.ids(source, target, max_depth)
if path:
    print(f"Path from {source} to {target}:", "->".join(path))
else:
    print(f"No path found from {source} to {target} within {max_depth} depth limit.")
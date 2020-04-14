"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # this is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if the verticies exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the directional edge
            self.vertices[v1].add(v2)
        else:
            print("Error adding edge: vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print("Error getting neighbors: vertex not found")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue and enqueue a starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed verticies
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue / pop the first vertex
            path = qq.dequeue()
            # if not visited:
            if path[-1] not in visited:
                # DO THE THING
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    newpath = list(path)
                    newpath.append(next_vert)
                    qq.enqueue(newpath)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack and push a starting vertex
        ss = Stack()
        ss.push(starting_vertex)
        # Create a set of traversed verticies
        visited = set()
        # While queue is not empty:
        while ss.size() > 0:
            # dequeue / pop the first vertex
            last = ss.pop()
            # if not visited:
            if last not in visited:
                # DO THE THING
                print(last)
                # mark as visited
                visited.add(last)
                # enqueue all neighbors
                for next_vert in self.get_neighbors(last):
                    ss.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # # Create a set of traversed verticies
        # visited = {starting_vertex}

        # def dft_recursion(current_vertex, visited):
        #     # print the current vertex
        #     print(current_vertex)
        #     # for each neighboring vertex that has not already been visited...
        #     for next_vert in self.get_neighbors(current_vertex):
        #         # add the number to the visited list and run the function again with that neighbor
        #         if next_vert not in visited:
        #             visited.add(next_vert)
        #             dft_recursion(next_vert, visited)
        
        # dft_recursion(starting_vertex, visited)

        # Initial case
        if visited is None:
            visited = set()
        
        # Track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)

        # Call the function recursivley
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue and enqueue a starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed verticies
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue / pop the first vertex
            path = qq.dequeue()
            # if not visited:
            if path[-1] not in visited:
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    if next_vert == destination_vertex:
                        newpath = list(path)
                        newpath.append(next_vert)
                        return newpath
                    else:
                        newpath = list(path)
                        newpath.append(next_vert)
                        qq.enqueue(newpath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack and push a starting vertex
        ss = Stack()
        ss.push(starting_vertex)
        # Create a set of traversed verticies
        visited = set()
        # While queue is not empty:
        while ss.size() > 0:
            # dequeue / pop the first vertex
            last = ss.pop()
            # if not visited:
            if last not in visited:
                # mark as visited
                visited.add(last)
                # enqueue all neighbors
                for next_vert in self.get_neighbors(last):
                    if next_vert == destination_vertex:
                        search_results = list(visited)
                        search_results.append(next_vert)
                        return search_results
                    else:
                        ss.push(next_vert)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # # Create a set of traversed verticies
        # visited = {starting_vertex}
        # path = [starting_vertex]

        # def dfs_recursion(current_vertex, destination_vertex, visited, path):
        #     if current_vertex == destination_vertex:
        #         print(f"the path is: {path}")
        #         return path
        #     else:
        #         # for each neighboring vertex that has not already been visited...
        #         for next_vert in self.get_neighbors(current_vertex):
        #             # add the number to the visited list and run the function again with that neighbor
        #             if next_vert not in visited:
        #                 visited.add(next_vert)
        #                 new_path = path + [next_vert]
        #                 new_recursion = dfs_recursion(next_vert, destination_vertex, visited, new_path)
        #                 if new_recursion:
        #                     print(f"new path is {new_path}")
        #                     return new_recursion
        
        # dfs_recursion(starting_vertex, destination_vertex, visited, path)

        # Initial case
        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        # Track visited nodes
        visited.add(starting_vertex)
        newpath = path + [starting_vertex]

        # Base case
        if starting_vertex == destination_vertex:
            return newpath

        # Call the function recursivley
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(neighbor, destination_vertex, visited, newpath)
                if neighbor_path:
                    return neighbor_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

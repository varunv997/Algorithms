""" File Containing Classes for Union Find """

class QuickFindUF:
    """
    Class that exposes API for Quick Find Algorithm for Union Find.
    Complexity:
        To check Connection in the Graph: O(1)
        To create Union in the Graph: O(N)
    Methods:
        is_connected()
        union()
    Member Variables:
        N: No of nodes in the graph
        nodeIds: List of connected components
    """
    def __init__(self, N:int):
        """
        Constructor Function
        Input Params:
            N:int (No of Nodes)
        Return: 
            None
        """
        self.N = N
        self.nodeIds = list(range(0,N))
    
    def is_connected(self, node1:int, node2:int) -> bool:
        """
        Function to check if two nodes are connected
        Input Params:
            node1:int (Id of Node 1)
            node2:int (Id of Node 2)
        Return:
            True if Nodes are connected
            False if Nodes are not connected
        """
        if self.nodeIds[node1] == self.nodeIds[node2]:
            return True
        return False
    
    def union(self, node1:int, node2:int):
        """
        Function to create a union between two nodes
        Input Params:
            node1:int (Id of Node 1)
            node2:int (Id of Node 2)
        Return:
            None
        """
        if not self.is_connected(node1, node2):
            primeId = self.nodeIds[node2]
            secondaryId = self.nodeIds[node1]
            # replace the secondaryId with primeId in nodeIds
            for idx in range(self.N):
                if self.nodeIds[idx] == secondaryId:
                    self.nodeIds[idx] = primeId

class QuickUnionUF:
    """
    Class that exposes API for Quick Union Algorithm for Union Find.
    Complexity:
        To check Connection in the Graph: O(N)
        To create Union in the Graph: O(N)
        To find root: O(N)
    Methods:
        is_connected()
        union()
        get_root()
    Member Variables:
        N: No of nodes in the graph
        nodeIds: List of connected components
    """
    def __init__(self, N:int):
        """
        Constructor Function
        Input Params:
            N:int (No of Nodes)
        Return: 
            None
        """
        self.N = N
        self.nodeIds = list(range(0, N))

    def is_connected(self, node1:int, node2:int) -> bool:
        return self.get_root(node1) == self.get_root(node2)
    
    def get_root(self, nodeId:int) -> int:
        """
        Function to get the root of a node
        Input Params:
            nodeId:int (node id of which the root is to be found)
        Return:
            nodeId:int of the root
        """
        if self.nodeIds[nodeId] == nodeId:
            return nodeId
        return self.get_root(self.nodeIds[nodeId])
    
    def union(self, node1:int, node2:int):
        """
        Function to create a union between two nodes
        Input Params:
            node1:int (Id of Node 1)
            node2:int (Id of Node 2)
        Return:
            None
        """
        if not self.is_connected(node1, node2):
            self.nodeIds[self.get_root(self.nodeIds[node1])] = self.get_root(node2)
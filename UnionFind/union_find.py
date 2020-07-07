""" File Containing Classes for Union Find """

class QuickFindUF:
    def __init__(self, N:int):
        """
        Constructor Function
        Input Params:
            N:int (No of Nodes)
        Return: 
            None
        """
        self.N = N
        self.nodeIds = list(range(0,10))
    
    def is_connected(self, node1:int, node2:int):
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

'''
if __name__ == "__main__":
    """ Sample Client """

    # input to be read from input.txt
    with open ("input.txt", "r") as f:
        # Read N from the input
        N = int(f.readline())

        # Create QuickFindUF object
        quickFind = QuickFindUF(N)

        # read the rest of the file and perform union
        line = f.readline()
        while (line):
            node1, node2 = [int(nodeId) for nodeId in line.split(" ")]
            quickFind.union(node1, node2)
            line = f.readline()
    
        # print the final connections
        print (quickFind.nodeIds)
'''
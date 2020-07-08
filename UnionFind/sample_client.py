# necessary imports
from union_find import QuickFindUF, QuickUnionUF

if __name__ == "__main__":
    """ Sample Client """

    # input to be read from input.txt
    with open ("input.txt", "r") as f:
        # Read N from the input
        N = int(f.readline())

        # Create QuickFindUF object
        quickFind = QuickFindUF(N)

        # Create QuickUnionUF object
        quickUnion = QuickUnionUF(N)

        # read the rest of the file and perform union
        line = f.readline()
        while (line):
            node1, node2 = [int(nodeId) for nodeId in line.split(" ")]
            quickFind.union(node1, node2)
            quickUnion.union(node1, node2)
            line = f.readline()
    
        # print the final connections
        print (quickFind.nodeIds)
        print (quickUnion.nodeIds)
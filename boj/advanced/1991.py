class Node:
    def __init__(self,Data):
        self.data = Data[0]
        if(Data[1] != '.'):
            self.left = Node((Data[1],'.','.'))
        else:
            self.left = None
        
        if(Data[2] != '.'):
            self.right = Node((Data[2],'.','.'))
        else:
            self.right = None

    def insert(self,Data):
        if(self.data == Data[0]):
            if(Data[1] != '.'):
                self.left = Node((Data[1],'.','.'))
            else:
                self.left = None  
            if(Data[2] != '.'):
                self.right = Node((Data[2],'.','.'))
            else:
                self.right = None
        else:
            if(self.left != None):
                self.left.insert(Data)
            if(self.right != None):
                self.right.insert(Data)

    def PrintpreTree(self):
        print(self.data,end='')
        if self.left:
            self.left.PrintpreTree()
        if self.right:
            self.right.PrintpreTree()

    def PrintmidTree(self):
        if self.left:
            self.left.PrintmidTree()
        print(self.data,end='')
        if self.right:
            self.right.PrintmidTree()

    def PrintaftTree(self):
        if self.left:
            self.left.PrintaftTree()
        if self.right:
            self.right.PrintaftTree()
        print(self.data,end='')

if __name__ == "__main__":
    root = None
    num = int(input())
    for i in range(num):
        _node = input().split(" ")
        if(root == None):
            root = Node(_node)
        else:
            root.insert(_node)
    root.PrintpreTree()
    print('')
    root.PrintmidTree()
    print('')
    root.PrintaftTree()
    print('')

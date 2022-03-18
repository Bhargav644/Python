class TreeNode:
    def __init__(self, V):
        self.value = V
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def getHeight(self, node):
        if(node):
            return node.height
        return 0

    def getBalance(self, node):
        if(node):
            return self.getHeight(node.left)-self.getHeight(node.right)
        return 0

    def leftRotate(self, root):
        temp = root.right
        tempL = temp.left

        root.right = tempL
        temp.left = root

        temp.height = 1+max(self.getHeight(temp.left),
                            self.getHeight(temp.right))
        root.height = 1+max(self.getHeight(root.left),
                            self.getHeight(root.right))
        return temp

    def rightRotate(self, root):
        temp = root.left
        tempR = temp.right

        root.left = tempR
        temp.right = root

        temp.height = 1+max(self.getHeight(temp.left),
                            self.getHeight(temp.right))
        root.height = 1+max(self.getHeight(root.left),
                            self.getHeight(root.right))
        return temp

    def insert(self, root, toInsert):
        if(not root):
            return TreeNode(toInsert)
        elif(root.value < toInsert):
            root.right = self.insert(root.right, toInsert)
        elif(root.value > toInsert):
            root.left = self.insert(root.left, toInsert)
        root.height = 1+max(self.getHeight(root.left),
                            self.getHeight(root.right))
        balance = self.getBalance(root)

        if(balance > 1 and toInsert < root.left.value):  # LL rotation
            return self.rightRotate(root)

        if(balance > 1 and toInsert > root.left.value):  # LR rotation
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if(balance < -1 and toInsert > root.right.value):  # RR rotation
            return self.leftRotate(root)

        if(balance < - 1 and toInsert < root.right.value):  # RL rotation
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def preorder(self, root):
        if(not root):
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)


myObj = AVL()
root = None
root = myObj.insert(root, 10)
root = myObj.insert(root, 20)
root = myObj.insert(root, 30)
root = myObj.insert(root, 40)
root = myObj.insert(root, 50)
root = myObj.insert(root, 25)
print(myObj.preorder(root))

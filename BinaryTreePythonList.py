class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, node):
        if self.lastUsedIndex+1 == self.maxSize:
            return 'The binary tree is full!'
        self.customList[self.lastUsedIndex + 1] = node
        self.lastUsedIndex += 1
        return 'The value has been added!'

    def searchBT(self, value):
        if self.lastUsedIndex == 0:
            return 'The binary tree is empty!'
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return 'The value is found!'
        return 'The value is not found!'

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        self.inOrderTraversal(index*2+1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self, node):
        if self.lastUsedIndex == 0:
            return 'The binary tree is empty!'
        deepestNode = self.customList[self.lastUsedIndex]
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == node:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return 'The node has been deleted!'

    def destroyBT(self):
        self.customList = None
        return 'The binary tree was deleted!'




newBT = BinaryTree(8)
newBT.insertNode('Drinks')
newBT.insertNode('Hot')
newBT.insertNode('Cold')
newBT.insertNode('Tea')
print(newBT.insertNode('Coffee'))

print('-------')
print(newBT.searchBT('Hot'))
print(newBT.searchBT('hot'))

print('-------')
newBT.preOrderTraversal(1)

print('-------')
newBT.inOrderTraversal(1)

print('-------')
newBT.postOrderTraversal(1)


print('-------')
newBT.levelOrderTraversal(1)

print('--------')
print(newBT.deleteNode('Tea'))
newBT.levelOrderTraversal(1)


print('-------')
print(newBT.destroyBT())
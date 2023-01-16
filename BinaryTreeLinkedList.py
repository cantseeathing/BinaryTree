from Queue import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode('Drinks')
leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')
newBT.leftChild = leftChild
newBT.rightChild = rightChild


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


preOrderTraversal(newBT)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


print('------------')
inOrderTraversal(newBT)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    inOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


print('------------')
postOrderTraversal(newBT)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)


print('------------')
levelOrderTraversal(newBT)


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.data == nodeValue):
                return 'Value found!'
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return 'value not found!'

print('-------------')
print(searchBT(newBT, 'Hot'))


def inserNodeBT(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = nodeValue
                return 'success!'
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = nodeValue
                return 'success!'

print('-------------')
newNode = TreeNode('coffee')
print(inserNodeBT(newBT, newNode))
levelOrderTraversal(newBT)


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

print('-----------')
deepNode = getDeepestNode(newBT)
print(deepNode)


def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is deepestNode:
                root.value = None
                return
            if root.value.leftChild:
                if root.value.leftChild is deepestNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                if root.value.rightChild is deepestNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)

print('-------------')
newNode = getDeepestNode(newBT)
deleteDeepestNode(newBT, newNode)
levelOrderTraversal(newBT)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return 'The BT does not exist'
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                deepesetNode = getDeepestNode(rootNode)
                root.value.data = deepesetNode.data
                deleteDeepestNode(rootNode, deepesetNode)
                return 'The node has been deleted!'
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

print('--------------')
deleteNodeBT(newBT, 'Drinks')
levelOrderTraversal(newBT)

def destroyBT(rootNode):
    if not rootNode:
        return 'The BT does not exist'
    else:
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return 'The BT was destroyed!'

print('--------')
print(destroyBT(newBT))
levelOrderTraversal(newBT)
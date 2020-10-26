
GLOBAL_SYMBOL_TABLE_ID = 0
COUNT = [10]


class Node:
    def __init__(self, id, key):
        self.left = None
        self.right = None
        self.id = id
        self.val = key

    def __str__(self):
        return "(" + str(self.id) + "," + str(self.val) + ")"


class BST:
    def __init__(self):
        self.root = None

    def insert_new(self, value):
        global GLOBAL_SYMBOL_TABLE_ID
        if self.root is None:
            GLOBAL_SYMBOL_TABLE_ID += 1
            self.root = Node(GLOBAL_SYMBOL_TABLE_ID, value)
        else:
            parent = None
            left, right = False, False
            node = self.root
            while node is not None:
                parent = node
                if node.val < value:
                    node = node.left
                    left, right = True, False
                elif node.val > value:
                    node = node.right
                    left, right = False, True
            if left == True:
                GLOBAL_SYMBOL_TABLE_ID += 1
                parent.left = Node(GLOBAL_SYMBOL_TABLE_ID, value)
            else:
                GLOBAL_SYMBOL_TABLE_ID += 1
                parent.right = Node(GLOBAL_SYMBOL_TABLE_ID, value)

    def search(self, value):
        if self.root is None:
            return None
        node = self.root
        while node is not None:
            if node.val == value:
                return node
            elif node.val < value:
                node = node.left
            else:
                node = node.right
        return None

    # Function to print binary tree in 2D
    # It does reverse inorder traversal
    def print2DUtil(self, root, space):

        # Base case
        if (root == None):
            return

        # Increase distance between levels
        space += COUNT[0]

        # Process right child first
        self.print2DUtil(root.right, space)

        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(root)

        # Process left child
        self.print2DUtil(root.left, space)

        # Wrapper over print2DUtil()

    def print2D(self, root):

        # space=[0]
        # Pass initial space count as 0
        self.print2DUtil(root, 0)

    def print(self):
        self.print2D(self.root)

    def __print_preorder(self, node: Node):
        string = ""
        if node != None:
            string += str(node) + ': '
            string += 'left: ' + str(node.left) + ' '
            string += 'right: ' + str(node.right) + ' '
            string += '\n'
            string += self.__print_preorder(node.left)
            string += self.__print_preorder(node.right)
        return string

    def __str__(self):
        return self.__print_preorder(self.root)


class SymbolTable:
    def __init__(self):
        self._elems = BST()

    def insert(self, value):
        self._elems.insert_new(value)

    def search(self, value):
        res = self._elems.search(value)
        if res == None:
            return None
        else:
            return res.id

    def print(self):
        self._elems.print()

    def __str__(self):
        return str(self._elems)


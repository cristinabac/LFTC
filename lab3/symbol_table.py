
GLOBAL_SYMBOL_TABLE_ID = 0


class Node:
    def __init__(self, id, key):
        self.left = None
        self.right = None
        self.id = id
        self.val = key


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


class SymbolTable:
    def __init__(self):
        self._elems = BST()

    def insert(self, value):
        self._elems.insert_new(value)

    def search(self, value):
        res = self._elems.search(value)
        if res == None:
            return -1
        else:
            return res.id

# test
sym1 = SymbolTable()
sym1.insert("a")
sym1.insert("b")
sym1.insert("c")
print(sym1.search("a"))
print(sym1.search("b"))
print(sym1.search("c"))
sym2 = SymbolTable()
sym2.insert(1)
sym2.insert(3)
print(sym2.search(1))
print(sym2.search(3))
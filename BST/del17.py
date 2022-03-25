# %% [markdown]
# # Binære søke-tre
# 
# Et binært søke-tre består i likhet med en linket liste av noder som er koblet til andre noder. I motsetning til det binære treet "Heap" som vi har vært innom tidligere, vil ALLE nodene i venstre sub-tre være mindre eller lik parent/foreldre-node, og ALLE nodene i høyre sub-tre være større. I en heap trengte ikke dette være tilfelle, der var det nok at denne større/mindre betingelse var gyldig kun lokalt.
# 
# Dette gjør at man må være mer nøye når man skal sette inn en ny node i et binært søketre. 
# 
# Traversering av strukturen kan gjøres på mange forskjellige måter, vi ser på såkalte "dybde-først" traverseringer.
# 
# En annen viktig forskjell fra Heap er at vi nå gjør lagring av elementene i selve noden (slik for linket liste) istedenfor at strukturen støttes/backes av en liste.

# %%
class TreeNode:
    def __init__(self, object) :
        self.element = object
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self) :
        self.__root = None
        self.__length = 0

    def insert(self, object) :
        node = TreeNode(object)
        if self.__root == None :
            self.__root = node
            self.__length += 1
        else :
            current = self.__root
            while current != None :
                parent = current
                if object < current.element :
                    current = current.left
                elif object > current.element :
                    current = current.right
                else :
                    return False

            if object < parent.element :
                parent.left = node 
            else :
                parent.right = node
            self.__length += 1

    def search(self, object) :
        current = self.__root
        path = []
        while current != None :
            if object < current.element :
                path.append(current.element)
                current = current.left
            elif object > current.element :
                path.append(current.element)
                current = current.right
            else :
                return True, path

        return False, path

    def delete(self, object) :
        parent = current = self.__root

        # First, locate item to be deleted
        node = None
        while current != None :
            if object < current.element :
                parent = current
                current = current.left
            elif object > current.element :
                parent = current
                current = current.right
            else :
                node = current  # We found it
                break

        if node == None :
            return False

        # Case 1: No children, so it's a leaf node. Just remove the node. This is performed by removing the left/right node in parent
        if node.right == None and node.left == None :
            if parent.right.element == object :
                parent.right = None
            else : 
                parent.left = None
        # Case 2: One child. We hook the child onto the nodes' parent.
        elif node.right == None and node.left != None :  # Had only a left child
            if parent.right.element == object :
                parent.right = node.left
            else :
                parent.left = node.left
            node.left = None  # For the sake of garbage collection of node. No strings attached to old child nodes. Parenthood is taken care of ;-)
        # Case 2 continued
        elif node.left == None and node.right != None : # Had only a right child
            if parent.right.element == object :
                parent.right = node.right
            else :
                parent.left = node.right
            node.right = None # For the sake of garbage collection of node. No strings attached to old child nodes. Parenthood is taken care of ;-)
        # Case 3: Both nodes. First, find the minimum node in the right subtree. Exchange value of that node with the current, and then delete it
        # The minimum node in the right subtree amounts to finding the leftmost child in that subtree (think about that for a sec ;-)
        else :
            leftmost_parent = node
            leftmost = node.right
            while leftmost.left != None : 
                leftmost_parent = leftmost
                leftmost = leftmost.left
            toReplace = leftmost.element
            # The node to be removed is the one stored in "leftmost". We remove it by attaching it's right child
            # (it do not have a left, since it's the leftmost itself!) to the parent. Decide upon where to attach on parent
            if leftmost_parent.left.element == leftmost.element :  # This is the usual case, since we're spinning leftwards
                leftmost_parent.left = leftmost.right
            else :   # But this will happen if the the parent is the "node" itself
                leftmost_parent.right = leftmost.right
            node.element = toReplace   # Replace the value that is to be deleted

        self.__length -= 1
        return True

    def traverse_preorder(self) :
        self.__preorder(self.__root)
        
    def __preorder(self, root) :
        if root == None :
            return None
        print(root.element)
        self.__preorder(root.left)
        self.__preorder(root.right)

    def traverse_inorder(self) :
        self.__inorder(self.__root)
        
    def __inorder(self, root) :
        if root == None :
            return None
        self.__inorder(root.left)
        print(root.element)
        self.__inorder(root.right)

    def traverse_postorder(self) :
        self.__postorder(self.__root)
        
    def __postorder(self, root) :
        if root == None :
            return None
        self.__postorder(root.left)
        self.__postorder(root.right)
        print(root.element)

    def clear(self) :
        self.__root = None
    
    
bst = BinarySearchTree()
inserts = [12, 5, 15, 3, 7, 13, 17, 1, 9, 14, 20, 8, 11, 18]
for element in inserts :
    bst.insert(element)

bst.delete(15)
bst.delete(12)  # Ultimate test: remove root node :-)
bst.delete(12)  # Should return False
bst.clear()

inserts = [20, 10, 35, 5, 7, 3, 15, 23, 40, 21]
for element in inserts :
    bst.insert(element)

bst.traverse_inorder()


# %% [markdown]
# ## Oppgave: Hvordan finne ut om et tre er et binært søketre?
# 
# Kan løses på flere måter, men vi prøver oss på en rekursiv variant:
# 1. Finn ut om alle nodene på venstre side er mindre enn rot-node
# 2. Finn ut om alle nodene på høyre side er mindre enn rot-node

# %%





class Node: 
    def __init__(self, key,text): 
        self.left = None
        self.right = None
        self.val = key
        self.text=text


def insert(root, key,text): 
    if root is None: 
        return Node(key,text) 
    else: 
        if root.val == key: 
            return root 
        elif root.val < key: 
            root.right = insert(root.right, key,text) 
        else: 
            root.left = insert(root.left, key,text) 
    return root

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(str(root.val)+": "+str(root.text))
        inorder(root.right)

        
def search(root,key): 
      
    # Base Cases: root is null or key is present at root 
    if root is None or root.val == key: 
        return root 
  
    # Key is greater than root's key 
    if root.val < key: 
        return search(root.right,key) 
    
    # Key is smaller than root's key 
    return search(root.left,key)









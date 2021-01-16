import BST
import pickle

pickle_off = open("BST_root.pickle", 'rb')
BST_root= pickle.load(pickle_off)
BST.inorder(BST_root)

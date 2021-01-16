import BST
count=0


for i in range(5):
    if count==0:
        r=BST.Node(5*i,'a')
    else:
        r=BST.insert(r,3*i,'b'*i)
    count+=1

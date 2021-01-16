from flask import Flask,request
import nltk
import BST
import pickle
app=Flask(__name__)
@app.route('/')
def index():
    return '<h1> Hello There! </h1>'

count=0
@app.route('/sendval/',methods=['GET','POST'])
def sendval():
    global count
    global r
    if request.method=='POST':
        val=request.args.get('val')
        text=request.args.get('text')
        text=nltk.word_tokenize(text)
        tagged_word=nltk.pos_tag(text)
        nouns_list=[]
        for i in tagged_word:
            if i[1][:2]=='NN':
                nouns_list.append(i[0])
        if count==0:
            r=BST.Node(val,nouns_list)
        else:
            r=BST.insert(r,val,nouns_list)
        count+=1

    
    my_pickle=open("BST_root.pickle","wb")
    pickle.dump(r,my_pickle)
    my_pickle.close()
    
    return {val : nouns_list}

if __name__=='__main__':
    app.run(debug=True,port=8080)

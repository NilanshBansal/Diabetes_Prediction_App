from django.shortcuts import render,redirect
# Create your views here.
import pickle

def index(request):
    return render(request,'index.html',{'title':'Diabetes Detection'})

def test():
    print ('hello')
    with open('./bagging_clf.pkl', 'rb') as f:
        data = pickle.load(f)

    

def predict(request):
    print (request.POST)
    test()
    return redirect ('/')

from django.shortcuts import render,redirect
from django.conf import settings 

import os
import pickle

def index(request):
    return render(request,'index.html',{'title':'Diabetes Detection'})

def readFile():
    print ('hello')
    with open(os.path.join(settings.PROJECT_ROOT, 'bagging_clf.pkl'), 'rb') as f:
        data = pickle.load(f)
        print (data)
    

def predict(request):
    print (request.POST)
    readFile()
    return redirect ('/')

from django.shortcuts import render,redirect
from django.conf import settings 
import numpy as np
import os
import pickle

def index(request):
    return render(request,'index.html',{'title':'Diabetes Detection'})

def readFile(features):
    
    with open(os.path.join(settings.PROJECT_ROOT, 'bagging_clf.pkl'), 'rb') as f:
        model = pickle.load(f)
        # print (data)

    with open(os.path.join(settings.PROJECT_ROOT, 'scaler.pkl'), 'rb') as f:
        scaler = pickle.load(f)
        features = scaler.transform(features)
        print(model.predict(features))
        

def predict(request):
    dpf,glucose,bmi,age=float(request.POST.get('dpf')),float(request.POST.get('glucose')),float(request.POST.get('bmi')),float(request.POST.get('age'))
    features=(np.array([dpf,glucose,bmi,age])).reshape(1, -1)
    readFile(features)
    return redirect ('/')

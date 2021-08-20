from django.shortcuts import render,redirect
# from .models import product
from math import ceil
from django.urls import reverse
from django.conf import settings
from django.views.generic import View 
from .models import *
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django import forms
from .forms import *
from django.views.generic import CreateView
import pickle
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import joblib

import numpy as np
import json
from .forms import *


from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image



def index(request):
    return render(request,'index.html')

class Linear_Regression(View):
    def get(self,request):
        template = 'linear_regression.html'

        return render(request,template)


#------------------------------ Multi LR Startup Starts --------------------------------------

def startup(request):
    form = Startup_Form()
    if request.method == 'POST':
        form = Startup_Form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            rnd=request.POST.get('rnd', '')
            print(rnd)
            admin=request.POST.get('admin', '')
            print(admin)
            marketing=request.POST.get('marketing', '')
            state=request.POST.get('state', '')
            
            data = startup_info(rnd=rnd, admin=admin, marketing=marketing, state=state )
            data.save()
            
            return redirect(startup_predict)
    context = {"form": form,}
    return render(request, 'startup_index.html', context)

def startup_predict(request):
    #startup prediction 
    record = startup_info.objects.last() 
    
    a = record.rnd
    b = record.admin
    c = record.marketing
    d = record.state
    print("=====================")
    print(d)
    e = d[0]
    print(e)
    f = d[1]
    print(f)
    re = [[a,b,c,e,f]]
    
    arr = np.array(re)
    
    # arr = np.array([a],[b],[c],[d])
    print(arr.shape)
    print("++++++++++++++++++++++++++++++++++++++")
    #Load the pickled model
    model = joblib.load('./static/startups_pred.pk1')

    # Use the loaded pickled model to make predictions
    result = model.predict(arr) 
    print(result)
    return render(request,'startup_result.html',{'result':result}) 

#------------------------------ Multi LR Startup End --------------------------------------


#------------------------------ Logistic Regression Titanic Starts --------------------------------------
# def home(request):
#     return render(request, 'titanic_index.html')

def titanic(request):
    form = Titanic_Form()
    if request.method == 'POST':
        form = Titanic_Form(request.POST, request.FILES)
        if form.is_valid():
            data1 = form.save(commit=False)
            passenger_class=request.POST.get('passenger_class', '')
            print(passenger_class)
            sex=request.POST.get('sex', '')
            print(sex)
            age=request.POST.get('age', '')
            no_sibling=request.POST.get('no_sibling', '')
            parch=request.POST.get('parch', '')
            fare_amt=request.POST.get('fare_amt', '')
            embarc_c=request.POST.get('embarc_c', '')
            embarc_q=request.POST.get('embarc_q', '')
            embarc_s=request.POST.get('embarc_s', '')
            
            data = titanic_info(passenger_class=passenger_class, sex=sex, age=age, no_sibling=no_sibling, parch=parch, fare_amt=fare_amt, embarc_c=embarc_c, embarc_q=embarc_c, embarc_s=embarc_s )
            data.save()
            
            return redirect(titanic_predict)
    context = {"form": form,}
    return render(request, 'titanic_index.html', context)

def titanic_predict(request):
    #startup prediction 
    record = titanic_info.objects.last() 
    model = pickle.load(open('./static/ml_model.sav', 'rb'))
    scaled = pickle.load(open('./static/scaler.sav', 'rb'))
    passenger_class = record.passenger_class
    sex = record.sex
    age = record.age
    no_sibling = record.no_sibling
    parch = record.parch
    fare_amt = record.fare_amt
    embarc_c = record.embarc_c
    embarc_q = record.embarc_q
    embarc_s = record.embarc_s
    
    # print("---------------- ")
    # print(passenger_class)
        
    prediction = model.predict(scaled.transform([[passenger_class,sex, age, no_sibling,parch,fare_amt,embarc_c,embarc_q,embarc_s]]))
    result = ''
    if prediction == 0:
        result= 'no'
    elif prediction == 1:
        result = 'yes'
    else:
        result = 'error'
    return render(request,'titanic_result.html',{'result':result}) 

#---------- Cat dog-----------------------------------

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def catdog(request):
    form = Catdog_Form(request.POST, request.FILES)
    if form.is_valid():
        dc = form.save(commit=False)
        dc.image = request.FILES['image']
        file_type = dc.image.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            return redirect('error')
        dc.save()
        return redirect(catdog_predict)
    context = {"form": form}
    return render(request, 'catdog_index.html',context)
    

def catdog_predict(request):
    img = dogcat_info.objects.last()
    a = img.image
    print(a)
    a= str(a)
    c =a.split('/')
    print(c)
    print(c[1])
    path = "./media/image/" + c[1] 
    print(path)
    model = load_model("./static/DogCat-epoch10-acc59-valacc60.h5")
    img = image.load_img(path)
    img = image.img_to_array(img)
    x = np.resize(img, (64,64,3))
    img_exp = np.expand_dims(x, axis=0)
    result = model.predict(img_exp)
    print(result)
    if result[0][0] >= 0.5:
        prediction = 'dog'
    else:
        prediction = 'cat'
    print(prediction)
    con = {"prediction":prediction}
    
    return render(request, 'catdog_result.html',con)


def error(request):
    return render(request, 'error.html')

#------------------- Wine ---------------------------------------------

def wine(request):
    form = Wine_Form()
    if request.method == 'POST':
        form = Wine_Form(request.POST, request.FILES)
        if form.is_valid():
            data3 = form.save(commit=False)
            alcohol=request.POST.get('alcohol', '')
            malic_acid=request.POST.get('malic_acid', '')
            ash=request.POST.get('ash', '')
            acl=request.POST.get('acl', '')
            mg=request.POST.get('mg', '')
            phenols=request.POST.get('phenols', '')
            flavanoids=request.POST.get('flavanoids', '')
            nonflavanoid_phenols=request.POST.get('nonflavanoid_phenols', '')
            proanth=request.POST.get('proanth', '')
            color_int=request.POST.get('color_int', '')
            hue=request.POST.get('hue', '')
            od=request.POST.get('od', '')
            proline=request.POST.get('proline', '')
            
            data3 = wine_info(alcohol=alcohol, malic_acid=malic_acid, ash=ash, acl=acl, mg=mg, phenols=phenols, flavanoids=flavanoids, nonflavanoid_phenols=nonflavanoid_phenols, proanth=proanth, color_int=color_int, hue=hue, od=od , proline=proline)
            data3.save()
            
            return redirect(wine_predict)
    context = {"form": form,}
    return render(request, 'wine_index.html', context)

def wine_predict(request):
    record = wine_info.objects.last() 
    
    a = record.alcohol
    b = record.malic_acid
    c = record.ash
    d = record.acl 
    e = record.mg
    f = record.phenols 
    g = record.flavanoids 
    h = record.nonflavanoid_phenols  
    i = record.proanth 
    j = record.color_int 
    k = record.hue 
    l = record.od   
    m = record.proline   
  
    arr = [a,b,c,d,e,f,g,h,i,j,k,l,m]
    print(arr)
    
    
    print("++++++++++++++++++++++++++++++++++++++")
    #Load the pickled model
    model = load_model('./static/multi_class_wine.h5')

    # Use the loaded pickled model to make predictions
    result = model.predict([arr])
    
    # class1 = result[1]
    # class1 = result[2]
    
    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[")
    # print(class2)
    # print(class3)
    
    # if class1 >class2 >class3:
    #     maximum = "class1"
    # elif class2 > class3 > class1:
    #     maximum = "class2"
    # else:
    #     maximum = "class3"
        
     
    print(result)
    maximum= result.max
    print(maximum)
    
    return render(request,'wine_result.html',{'result':result, 'maximum': maximum }) 




from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as autuph_views 
urlpatterns = [
    path('',views.index,name="index"),
    path('linear_regression/',Linear_Regression.as_view(), name='linear_regression_url'),
    path('startup_index/',views.startup,name="startup_index_url"),
    path('startup_predict/',views.startup_predict,name="startup_predict_url"),
    path('titanic_index/',views.titanic,name="titanic_index_url"),
    path('titanic_predict/',views.titanic_predict,name="titanic_predict_url"),
    
    path('catdog_index/',views.catdog,name="catdog_index_url"),
    path('catdog_predict/',views.catdog_predict,name="catdog_predict_url"),
    
    path('wine_index/',views.wine,name="wine_index_url"),
    path('wine_predict/',views.wine_predict,name="wine_predict_url"),
    
    
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('server',views.server,name='server'),
    path('index',views.index,name='index'),
    path('userfeedbackform',views.userfeedbackform,name='userfeedbackform'),
    path('submituserfeedbackform',views.submituserfeedbackform,name='submituserfeedbackform'),
    path('search',views.search,name='search'),
    path('about',views.about,name='about'),
    path('addtofavourite/<str:username>/<int:pid>',views.addtofavourite,name='addtofavourite'),
    path('getfavourite/<str:username>/',views.getfavourite,name='getfavourite'),
    path('groupmembers',views.groupmembers,name='groupmembers'),
    path('emergency',views.emergency,name='emergency'),
    path('detaileduser',views.detaileduser,name='detaileduser'),
    path('submitdetaileduser',views.submitdetaileduser,name='submitdetaileduser'),
    path('mydetails/<str:requestname>',views.mydetails,name='mydetails'),
    path('makepost',views.makepost,name='makepost'),
    path('submitpost',views.submitpost,name='submitpost'),
    path('users/api',views.api,name='api'),
    path('vieweditdetails/<str:requestname>',views.vieweditdetails,name='vieweditdetails'),
    path('track',views.track,name='track'),
    path('testpredict',views.predict,name='predict')
]


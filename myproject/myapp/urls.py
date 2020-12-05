from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('submitresponse',views.submitresponse,name='submitresponse')
]

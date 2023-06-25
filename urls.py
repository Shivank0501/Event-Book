from django.urls import path
from . import views

urlpatterns = [

    path('',views.log,name='log'),
    #path('', views.first, name='first'),
    path('Weddings/',views.Weddings, name='Weddings'),
    path('Birthday/',views.Birthday ,name='Birthday'),
    path('contact/',views.contact ,name='contact'),
    path('first/', views.first, name='first'),
    path('submit_form/', views.submit_form, name='submit_form'),

]
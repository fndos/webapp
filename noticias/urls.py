from django.urls import path
from django.conf.urls import include
from . import views
app_name= 'noticias'
urlpatterns = [
    #path('main/',views.index),
    path('mostrar/',views.mostrar10, name="mostrar"),
    path('mostrar/',views.mostrar10db, name="mostrardb"),

]

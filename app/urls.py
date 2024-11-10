from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home),
    path('',views.register),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('send/',views.send, name='send'),
    path('add/',views.add, name='add'),
    path('<int:id>/',views.delete,name='delete'),
    path('update',views.update, name="update"),


]

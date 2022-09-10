


from django.urls import path
from .views import Home,Dos

urlpatterns = [

    path('',Home.as_view(),name='hole'),
    path('pu/',Dos.as_view(),name='hole')

]
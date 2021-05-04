from django.urls import path
from  . import views

urlpatterns = [
    path('',views.index, name='myapp-index'),
    path('pagina/',views.pagina,name='pagina'),
]

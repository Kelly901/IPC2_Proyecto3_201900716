from django.urls import path
from  . import views

urlpatterns = [
    path('',views.index, name='myapp-index'),
    path('pagina/',views.pagina,name='pagina'),
    path('pagina2/',views.pagina2,name='pagina2'),
    path('recibir/',views.recibir,name='recibir'),
]

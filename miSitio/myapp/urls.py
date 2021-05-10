from django.urls import path
from  . import views

urlpatterns = [
    path('',views.index, name='myapp-index'),
    path('pagina/',views.pagina,name='pagina'),
    path('pagina2/',views.pagina2,name='pagina2'),
    path('recibir/',views.recibir,name='recibir'),
    path('file/',views.cargarArchivo,name='file'),
    path('fecha/',views.retornar_fechas,name='myapp-Reporte'),
    path('probando/',views.probando,name='probando'),
    path('filtro2/',views.filtro2,name='fitro2'),
    path('ayuda/',views.mostrarAyuda,name='ayuda'),
    path('informacion/',views.mostrar_informacion,name='informacion'),
    path('resetear/',views.vaciar_lista,name='resetear'),
]

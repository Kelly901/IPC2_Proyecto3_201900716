from django import forms

class PaginaPrincipal(forms.Form):
    area=forms.CharField(widget=forms.Textarea() ,label="area1")
    area2=forms.CharField(widget=forms.Textarea(),label="area2")
    


class ArchivoEntrada(forms.Form):
    file=forms.FileField(label="file")

class Obtener_fecha(forms.Form):
    opcion=forms.CharField(label="opcion")
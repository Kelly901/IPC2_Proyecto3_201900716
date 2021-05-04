from django import forms

class PaginaPrincipal(forms.Form):
    area=forms.CharField(widget=forms.Textarea() ,label="area1")
    area2=forms.CharField(widget=forms.Textarea(),label="area2")

    
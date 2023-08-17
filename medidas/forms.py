from django import forms
import json

class CustomSelectWidget(forms.Select):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs['class'] = 'form-select text-center'
        super().__init__(*args, **kwargs)


class FormularioMedidas(forms.Form):
    with open('static/json/dicionarioMedidas.json', encoding='utf8') as json_file:
        medidas = json.load(json_file)
    
    opcao1 = forms.ChoiceField(label= "Tipo", choices=[(i, i.replace('_', ' ').title()) for i in medidas.keys()], required=True, widget=CustomSelectWidget())
    opcao2 = forms.ChoiceField(label="Medida 1", choices=[], required=True)
    opcao3 = forms.ChoiceField(label="Medida 2", choices=[], required=True)
    texto1 = forms.CharField(label="De", empty_value=0, max_length=100, required=True)
    texto2 = forms.CharField(label="Para", empty_value=0, max_length=100, required=True)
from django import forms
import json

class CustomSelectWidget(forms.Select):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs['class'] = 'form-select text-center'
        super().__init__(*args, **kwargs)

class FormularioCripto(forms.Form):
	with open('static/json/DeParaCripto.json', encoding='utf8') as json_file:
		deParaCripto = json.load(json_file)

	with open('static/json/CriptoNomes.json', encoding='utf8') as json_file:
		criptoNomes = json.load(json_file)
	
	lista = []
	for i in criptoNomes.keys():
		if i in deParaCripto.keys():
			lista.append([i, criptoNomes[i]])

	opcao1 = forms.ChoiceField(label= "CriptoDe", choices=[(i[0], i[1].title()) for i in lista], required=True, widget=CustomSelectWidget)
	opcao2 = forms.ChoiceField(label="CriptoPara", choices=[], required=True)
	texto1 = forms.CharField(label="De", empty_value=0, max_length=100, required=True)
	texto2 = forms.CharField(label="Para", empty_value=0, max_length=100, required=True)
	
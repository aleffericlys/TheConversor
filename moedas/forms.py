from django import forms
import json

class CustomSelectWidget(forms.Select):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs['class'] = 'form-select text-center'
        super().__init__(*args, **kwargs)

class FormularioMoedas(forms.Form):
	with open('static/json/DeParaMoedas.json', encoding='utf8') as json_file:
		deParaMoedas = json.load(json_file)

	with open('static/json/moedasNomes.json', encoding='utf8') as json_file:
		moedasNomes = json.load(json_file)
	
	lista = []
	for i in deParaMoedas.keys():
		lista.append([i, moedasNomes[i]])
	

	opcao1 = forms.ChoiceField(label= "MoedaDe", choices=[(i[0], i[1].title()) for i in lista], required=True, widget=CustomSelectWidget)
	opcao2 = forms.ChoiceField(label="MedidaPara", choices=[], required=True)
	texto1 = forms.CharField(label="De", empty_value=0, max_length=100, required=True)
	texto2 = forms.CharField(label="Para", empty_value=0, max_length=100, required=True)
	
	# opcao1 = forms.ChoiceField(label= "Tipo", choices=[(i, i.replace('_', ' ').title()) for i in medidas.keys()], required=True)
	# opcao3 = forms.ChoiceField(label="Medida 2", choices=[], required=True)
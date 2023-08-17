from django.shortcuts import render
from django.views.generic import TemplateView
import json
from collections import OrderedDict
from django.http import JsonResponse

from .forms import FormularioMedidas
# Create your views here.

class Index(TemplateView):
	template_name = 'medidas/index.html'

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)

	# # moedas
	# 	with open('static/json/moedasNomes.json', encoding='utf8') as json_file:
	# 		moedas = json.load(json_file)
	# 	moedasOrdenadas = dict(OrderedDict(sorted(moedas.items())))
	# 	context['moedas'] = moedasOrdenadas

	# #criptomoedas
	# 	with open('static/json/criptoNomes.json', encoding='utf8') as json_file:
	# 		cripto = json.load(json_file)
	# 	criptoOrdenadas = dict(OrderedDict(sorted(cripto.items())))
	# 	context['cripto'] = criptoOrdenadas
	

	# 	return context

def minha_view(request):
	form = FormularioMedidas()

	if request.method == 'POST':
		
		form = FormularioMedidas(request.POST)
		
		
		if form.is_valid():
			pass
			
	return render(request, 'medidas/medidas.html', {
		'form': form,
		
		})


def obter_lista_medidas(request):
	with open('static/json/dicionarioMedidas.json', encoding='utf8') as json_file:
		medidas = json.load(json_file)
			
	opcao1 = request.GET.get('opcao1')
	opcoes2 = []
	opcoes3 = []

	for j in medidas.keys():

		if opcao1 == j:
			opcoes2 = [(i, i.replace('_',' ').title()) for i in medidas[j]]
			opcoes3 = [(i, i.replace('_',' ').title()) for i in medidas[j]]

	return JsonResponse({'opcoes2': opcoes2, 'opcoes3': opcoes3})

def pesquisar_json(request):
	opcao1 = request.GET.get('opcao1')
	opcao2 = request.GET.get('opcao2')
	opcao3 = request.GET.get('opcao3')
	texto = request.GET.get('texto')
	
	
	with open('static/json/conversoesMedidas.json', encoding='utf8') as json_file:
		valores = json.load(json_file)
		
	resultado = None


	if opcao2 == opcao3:
		resultado = float(texto)
	else: 
		formula = valores[opcao1][opcao2][opcao3]
		formula = formula.replace('var', texto)
		resultado = float (eval(formula))

	# Retorna o resultado em formato JSON
	return JsonResponse({'resultado': resultado})

from django.shortcuts import render
import json
from django.http import JsonResponse

import requests
from .forms import FormularioMoedas

# Create your views here.
def MoedasForm(request):
	form = FormularioMoedas()
	
	if request.method == 'POST':
		form = FormularioMoedas(request.POST)
		if form.is_valid():
			pass
		
	return render(request, 'moedas/moedas.html', {
		'form': form,
		
		})

def obter_lista_moedas(request):
	with open('static/json/moedasNomes.json', encoding='utf8') as json_file:
		moedasNomes = json.load(json_file)
	with open('static/json/DeParaMoedas.json', encoding='utf8') as json_file:
		moedasDP = json.load(json_file)
	
	opcao1 = request.GET.get('opcao1')
	opcao2 = []

	for i in moedasDP[opcao1]:
		opcao2 = [(i, moedasNomes[i].title()) for i in moedasDP[opcao1]]
	
	return JsonResponse({'opcoes2': opcao2})


def obter_cotacao(request):
	de = request.GET.get('de')
	para = request.GET.get('para')


	url = f'https://economia.awesomeapi.com.br/last/{de}-{para}';
	try:
		response = requests.get(url)
		response.raise_for_status()  # Verifica se a resposta é bem-sucedida (código 200)
		data = response.json()
		valor = data[f'{de}{para}']['ask']
		print(valor)
		return JsonResponse({'valor': valor})
	except requests.exceptions.RequestException as e:
		print(f"Erro ao fazer a requisição: {e}")
		return e
	except KeyError:
		print("Chave 'ask' não encontrada na resposta da API.")
		return KeyError
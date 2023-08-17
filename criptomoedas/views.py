from django.shortcuts import render
import json
from django.http import JsonResponse

import requests
from .forms import FormularioCripto

# Create your views here.
def CriptoForm(request):
	form = FormularioCripto()
	
	if request.method == 'POST':
		
		form = FormularioCripto(request.POST)
		
		
		if form.is_valid():
			pass

	# print(moedas)

	return render(request, 'criptomoedas/cripto.html', {
		'form': form,
		
		})

def obter_lista_cripto(request):
	with open('static/json/DeParaCripto.json', encoding='utf8') as json_file:
		CriptoDP = json.load(json_file)

	with open('static/json/CriptoNomes.json', encoding='utf8') as json_file:
		criptoNomes = json.load(json_file)
	
	opcao1 = request.GET.get('opcao1')
	opcao2 = []

	for i in CriptoDP[opcao1]:
		opcao2 = [(i, criptoNomes[i].title()) for i in CriptoDP[opcao1]]
	
	return JsonResponse({'opcoes2': opcao2})


def obter_cotacao_cripto(request):
	de = request.GET.get('de')
	para = request.GET.get('para')
	cod = f'{de}{para}'

	url = f'https://api.binance.com/api/v3/ticker/price?symbol={cod}'
	try:
		response = requests.get(url)
		response.raise_for_status()  # Verifica se a resposta é bem-sucedida (código 200)
		data = response.json()
		valor = float(data['price'])
		
		return JsonResponse({'valor': valor})
	except requests.exceptions.RequestException as e:
		print(f"Erro ao fazer a requisição: {e}")
		return e
	except KeyError:
		print("Chave 'ask' não encontrada na resposta da API.")
		return KeyError
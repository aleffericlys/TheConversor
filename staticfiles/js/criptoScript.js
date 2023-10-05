const opcao1Selecionada = document.getElementById('id_opcao1');
const opcao2Select = document.getElementById('id_opcao2');
const texto1 = document.getElementById('id_texto1');
const texto2 = document.getElementById('id_texto2');

async function atualizaOpcoes() {

	if (opcao2Select) { // Verificar se o elemento com ID 'id_opcao2' existe
		var url = '/obter_lista_cripto/?opcao1=' + opcao1Selecionada.value;

		const response = await fetch(url);
		
		if (!response.ok) {
			throw new Error('Erro na requisição AJAX. Status: ' + response.status);
		}else{

			const data = await response.json();
			console.log(data); // Verifique o que a resposta AJAX retorna
			var opcoes2 = data.opcoes2;
			opcao2Select.innerHTML = ''; // Limpar as opções existentes

			// Adicionar as novas opções à segunda lista suspensa
			opcoes2.forEach(function(option) {
				var optionElement = document.createElement('option');
				optionElement.value = option[0];
				optionElement.textContent = option[1];
				opcao2Select.appendChild(optionElement);
			});
		}
	}
	texto1.value = 1;
	await atualizaCotacao();
	atualizaValores(true);
	mostraItens();
	console.log(cotacao);
};



var cotacao = 0.0;
async function atualizaCotacao() {
	var de = opcao1Selecionada.value
	var para = opcao2Select.value

	url = '/obter_cotacao_cripto/?de=' + de + '&para=' + para;
	const response = await fetch(url)
	var data = await response.json()
		
	if (data.valor) {
		// Exibe o resultado na div 'resultado'
		cotacao = data.valor;
	} else {
		// Se não houver resultado correspondente, exibe uma mensagem de erro
		cotacao = 0;
	}
};

function atualizaValores(reverso){

	if (reverso) {
		if (texto1.value == '') {
			texto2.value = 0;
		}
		else{
			texto2.value = texto1.value * cotacao;
		}
	}else{
		if (texto2.value == '') {
			texto1.value = 0;
		}else{
		texto1.value = texto2.value / cotacao;
		}
	}
}

document.getElementById('id_opcao1').addEventListener('change', async function() {
	await atualizaOpcoes();
});

document.getElementById('id_opcao2').addEventListener('change', async function() {
	await atualizaCotacao()
	atualizaValores(true);
});

document.getElementById('id_texto1').addEventListener('input', function() {
	atualizaValores(true);
});

document.getElementById('id_texto2').addEventListener('input', function() {
 	atualizaValores(false);
});


function mostraItens() {
	console.log(opcao1Selecionada.value + ' ' + opcao2Select.value + '=' + cotacao);
}
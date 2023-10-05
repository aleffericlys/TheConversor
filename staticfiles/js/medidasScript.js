

async function atualizaOpcoes() {
	const opcao1Selecionada = document.getElementById('id_opcao1').value;
	const opcao2Select = document.getElementById('id_opcao2');
	const opcao3Select = document.getElementById('id_opcao3');
	if (opcao2Select && opcao3Select) { // Verificar se o elemento com ID 'id_opcao2' existe
		var url = '/obter_lista_medidas/?opcao1=' + opcao1Selecionada;

		const response = await fetch(url);
		// Promise.resolve(response)
		if(!response.ok){
			throw new Error('Erro na requisição AJAX. Status: ' + response.status);
		}
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

		var opcoes3 = data.opcoes3;
		opcao3Select.innerHTML = ''; // Limpar as opções existentes

		// Adicionar as novas opções à segunda lista suspensa
		opcoes3.forEach(function(option) {
			var optionElement = document.createElement('option');
			optionElement.value = option[0];
			optionElement.textContent = option[1];
			opcao3Select.appendChild(optionElement);
		});

	}
	mostraItens();
	document.getElementById('id_texto').value = 1;
	document.getElementById('id_texto2').value = 1;
};

document.getElementById('id_opcao1').addEventListener('change', function() {
	atualizaOpcoes();
});

// function atualizarResultadoLabel1() {

// var opcao1 = document.getElementById('id_opcao1').value;
// var opcao2 = document.getElementById('id_opcao3').value;
// var opcao3 = document.getElementById('id_opcao2').value;
// var texto = document.getElementById('id_texto2').value;

// // Realiza a pesquisa no arquivo JSON usando a função fetch()
// if (texto == '') {
// 	texto = '0';
// }
// var url = '/pesquisar_json/?opcao1=' + opcao1 + '&opcao2=' + opcao2 + '&opcao3=' + opcao3 + '&texto=' + texto;
// fetch(url)
// 	.then(
// 		response => response.json())
// 	.then(data => {
// 		console.log()
// 		if (data.resultado) {
// 			// Exibe o resultado na div 'resultado'
// 			document.getElementById('id_texto').value = data.resultado;
// 		} else {
// 			// Se não houver resultado correspondente, exibe uma mensagem de erro
// 			document.getElementById('id_texto').value = 0;
// 		}
// 	})
// 	.catch(error => {
// 		console.error('Erro na pesquisa no JSON:', error);
// 	});
// }

async function atualizarResultadoLabel1() {

	var opcao1 = document.getElementById('id_opcao1').value;
	var opcao2 = document.getElementById('id_opcao3').value;
	var opcao3 = document.getElementById('id_opcao2').value;
	var texto = document.getElementById('id_texto2').value;
	
	// Realiza a pesquisa no arquivo JSON usando a função fetch()
	if (texto == '') {
		texto = '0';
	}
	var url = '/pesquisar_json/?opcao1=' + opcao1 + '&opcao2=' + opcao2 + '&opcao3=' + opcao3 + '&texto=' + texto;
	const response = await fetch(url)
	var data = await response.json()
	console.log(data)

		if (data.resultado) {
			// Exibe o resultado na div 'resultado'
			document.getElementById('id_texto').value = data.resultado;
		} else {
			// Se não houver resultado correspondente, exibe uma mensagem de erro
			document.getElementById('id_texto').value = 0;
		}
}


function atualizarResultadoLabel2() {

	var opcao1 = document.getElementById('id_opcao1').value;
	var opcao2 = document.getElementById('id_opcao2').value;
	var opcao3 = document.getElementById('id_opcao3').value;
	var texto = document.getElementById('id_texto').value;
	
	// Realiza a pesquisa no arquivo JSON usando a função fetch()
	if (texto == '') {
		texto = '0';
	}
	var url = '/pesquisar_json/?opcao1=' + opcao1 + '&opcao2=' + opcao2 + '&opcao3=' + opcao3 + '&texto=' + texto;
	fetch(url)
		.then(response => response.json())
		.then(data => {
			if (data.resultado) {
				// Exibe o resultado na div 'resultado'
				document.getElementById('id_texto2').value = data.resultado;
			} else {
				// Se não houver resultado correspondente, exibe uma mensagem de erro
				document.getElementById('id_texto2').value = 0;
			}
		})
		.catch(error => {
			console.error('Erro na pesquisa no JSON:', error);
		});
	}

// Ouvinte de evento para atualizar o resultado em tempo real
document.getElementById('id_texto').addEventListener('input', function() {
	atualizarResultadoLabel2();
});

document.getElementById('id_texto2').addEventListener('input', function() {
	atualizarResultadoLabel1();
});

// Ouvintes de evento para atualizar a pesquisa ao selecionar novas opções
var opcao2Select = document.getElementById('id_opcao2');
var opcao3Select = document.getElementById('id_opcao3');
// var value1 = document.getElementById('id_texto');

opcao2Select.addEventListener('change', function() {
atualizarResultadoLabel2();
});

opcao3Select.addEventListener('change', function() {
atualizarResultadoLabel2();
mostraItens();
});

// Chama a função inicialmente para exibir o resultado com o valor atual do campo de texto
atualizarResultadoLabel2();


function mostraItens(){
	console.log(document.getElementById('id_opcao1').value + ' ' + document.getElementById('id_opcao2').value + ' ' + document.getElementById('id_opcao3').value);
};
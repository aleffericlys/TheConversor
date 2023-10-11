# The Conversor</h1>

The conversor é uma aplicação web com a finalidade de realizar as mais diversificadas comversões, indo de conversões estáticas como medidas de distancia, volume, massa, etc. até conversões dinamicas como cotações de moedas tanto moedas físicas como cripto moedas.

Criado todo com django, HTML, CSS e JavaScript.<p> 
Para coleta de dados de moedas e cripto moedas, faz uso das API's:<p>
	- Cotação de moedas físicas: https://docs.awesomeapi.com.br/api-de-moedas <p>
	- Cotação de cripto moedas: https://api.binance.com/api/v3/ticker/price<p>
  
Para a parte de dados estáticos usa uma biblioteca criada por mim mesmo com base na coleta de dados na internet para a conversão de valores, locaizado em /static/json tendo como objetivo fututo a criação de uma API própria para acesso a esses dados.
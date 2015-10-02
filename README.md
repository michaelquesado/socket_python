# Socket Python

##Objetivo: 
  Construir uma aplicação em Python onde o módulo cliente requisita informações do sistema operacional e o servidor responde com a informação solicitada.

## Requisitos: 
<ul>
	  <li>Aplicação UDP para respostas rápidas.</li>
	  <li>A requisição é uma mensagem com seis letras maiúsculas conforme a tabela.</li>
	  <li>A resposta é sempre um texto de comprimento variável.</li>
	  <li>Tanto requisições quando respostas devem ser enviadas em apenas um pacote.</li>
	  <li>Apenas uma informação por pacote.</li>
	  <li>Cada requisição é analisada individualmente (stateless).</li>
</ul>

## Requisições Aceitas

| Requisição   |  Descrição						   |
| ------------ |  -----------------------------	   |
| DATHOR       |  Interroga data/hora.			   |
| USOCPU       |  Interroga o uso da CPU.		   |
| USOMEM       |  Interroga o uso da Memória.	   |
| SYSNOM       |  Interroga o nome do dispositivo. |

##Testes
   No diretorio src/tests encontra-se o cliente e o servidor, pelo terminal execute o servidor ~ $ python servidor.py assim como o cliente ~ $ python cliente.py com ambos instanciados, tente solicitar informaçoes do servidor pelo cliente com as entradas citadas acima na tabela.

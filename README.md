# api-bot-whats-web

# Projeto API Bot Whats Web

## Sobre o projeto

O projeto é um bot que simula o acesso ao whatsapp web e disponibiliza urls de acesso para que o processo possa ser automatizado por software de terceiros.

## Requesito

- python3

## Funcionalidades

- Autorização por Qr Code;
- Envio de mensagem contendo apenas um contato;
- Envio de mensagem com varios contatos;

## Instalação

Realize o clone do projeto (https://github.com/HandersonSilva/api-bot-whats-web.git).

python3 app.py

Certifique que o caminho do chromedriver estar correto

## Rotas

### Autorização

```http
GET http://localhost:5000/qrcode
```

### Enviar mensagem para um contato

```http

POST http://localhost:5000/mensagem

```

Parâmetros

```js
{
	"contato":"+55 84 999999999",
	"mensagem":"Mensagem de teste"
}
```

### Enviar mensagem para vários contatos

```http

POST http://localhost:5000/mensagens

```

Parâmetros

```js
{
	"contato":[
		"contato 1",
        "contato 2",
        "contato 3"
	],
	"mensagem":"Mensagem de teste"
}
```

## Obs:

O envio é realizado com base na lista de contatos que já existe no whatsapp, sendo assim o nome enviado deverá ser o mesmo que estar na lista de contato

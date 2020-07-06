from flask import Flask, request
from bot_whtsapp import WhatsappBot

app = Flask(__name__)
whatsappWeb = WhatsappBot()


@app.route("/",methods=["GET"])
def index():
    return gerarResponse(200,"Serviço online")

@app.route("/qrcode",methods=["GET"])
def get_qrcode():
    resultado = whatsappWeb.get_qrcode()
    if resultado  == False:
        return gerarResponse(200,"Usuário conectado")

    return resultado

@app.route("/sair",methods=["GET"])
def sair():
    if whatsappWeb.deslogar() == False:
        return gerarResponse(400,"Nenhum usuário conectado")

    return gerarResponse(200,"Usuário desconectado")

@app.route("/interativo",methods=["GET"])
def set_modo_interativo():
    if whatsappWeb.interativo:
        return gerarResponse(400,"O bot já estar em modo interativo")

    whatsappWeb.interativo = True
    whatsappWeb.iniciar_bot()

    return gerarResponse(200,"Bot em modo interativo")

@app.route("/interativo_off",methods=["GET"])
def set_modo_interativo_off():
    if whatsappWeb.interativo == False:
        return gerarResponse(400,"O bot não estar em modo interativo")

    whatsappWeb.interativo = False

    return gerarResponse(200,"O Bot estar em modo API")

@app.route("/mensagem",methods=["POST"])
def envio_mensagem():
    body = request.get_json()

    if whatsappWeb == "":
        return gerarResponse(400,"Contato não encontrado")

    if "contato" not in body:
        return gerarResponse(400,"O parâmetro contato é obrigatório")

    if "mensagem" not in body:
        return gerarResponse(400,"O parâmetro contato é obrigatório")

    if whatsappWeb.abre_conversa(body['contato']) == False:
       return gerarResponse(400,"Contato não encontrado")

    if whatsappWeb.envia_msg(body['mensagem']) == False:
        return gerarResponse(400,"Contato não encontrado")

    return gerarResponse(200,"Mensagem enviada com sucesso")

@app.route("/mensagens",methods=["POST"])
def envio_mensagem_massa():
    body = request.get_json()

    if "contato" not in body:
        return gerarResponse(400,"O parâmetro contato é obrigatório")
    
    if len(body['contato']) > 10:
        return gerarResponse(400,"Limite de contato excedido, API limitada a uma lista contendo 10 contatos")

    if "mensagem" not in body:
        return gerarResponse(400,"O parâmetro contato é obrigatório")
    
    error = whatsappWeb.enviarMensagensEmMassa(body['contato'],body['mensagem'])

    if error > 0:
        return gerarResponse(400,"Não foi possível enviar a mensagem para todos os contatos")

    return gerarResponse(200,"Mensagens enviadas com sucesso")
    

def gerarResponse(status,msg,nome_conteudo=False,conteudo=False):
    response = {}
    response['status'] = status
    response['mensagem'] = msg

    if nome_conteudo and conteudo:
        response[nome_conteudo] = conteudo

    return response

app.run()

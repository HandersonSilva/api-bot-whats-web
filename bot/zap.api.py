import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from PIL import Image
import os
import base64


class WhatsappBot:
    def __init__(self):
        self.mensagem = "This is a test in background bot"
        self.grupos_ou_pessoas = ["Importante"] #["pessoa 1","pessoa 2"]
        # self.display = Display(visible=0, size=(400, 400))
        # self.display.start()
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        # options.add_argument('--headless')
        # options.add_argument('--no-startup-window')
        self.driver = webdriver.Chrome('./lib/chromedriver', chrome_options=options)
        self.driver.get('https://web.whatsapp.com')


    def EnviarMensagensEmMassa(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(15)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            chat_box_busca = self.driver.find_element_by_class_name('_2FVVk')#_2FbwG _2FVVk
            time.sleep(2)
            chat_box_busca.click()
            time.sleep(2)
            chat_box_busca = self.driver.find_element_by_class_name('_3FRCZ')
            time.sleep(2)
            chat_box_busca.send_keys(grupo_ou_pessoa)
            time.sleep(3)
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(2)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(2)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(2)
            botao_enviar.click()
            time.sleep(5)

    def abre_conversa(self, contato):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(15)
        try:
            # Seleciona a caixa de pesquisa de conversa
            self.caixa_de_pesquisa = self.driver.find_element_by_class_name('_2FVVk')
            time.sleep(2)
            # Digita o nome ou numero do contato
            chat_box_busca = self.driver.find_element_by_class_name('_3FRCZ')
            time.sleep(2)
            chat_box_busca.send_keys(contato)
            # Seleciona o contato
            self.contato = self.driver.find_element_by_xpath(
                f"//span[@title='{contato}']")
            time.sleep(2)
            # Entra na conversa
            self.contato.click()
        except Exception as e:
            print("Contato não encontrado",e)

    def envia_msg(self, msg):
        try:
            time.sleep(2)
            # Seleciona acaixa de mensagem
            self.caixa_de_mensagem = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(2)
            self.caixa_de_mensagem.click()
            # Digita a mensagem
            self.caixa_de_mensagem.send_keys(msg)
            time.sleep(2)
            # Seleciona botão enviar
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(2)
            botao_enviar.click()
            time.sleep(2)
        except Exception as e:
            print("Erro ao enviar msg", e)

    def ultima_msg(self):
        try:
            # post = self.driver.find_elements_by_class_name("_3_7SH")
            post = self.driver.find_elements_by_class_name("_2hqOq")
            ultimo = len(post) - 1
            print(ultimo)
            # O texto da ultima mensagem
            texto = post[ultimo].find_element_by_css_selector(
                "span.selectable-text").text
            return texto
        except Exception as e:
            print("Erro ao ler msg, tentando novamente!",e)

    def get_qrcode(self):
        
        self.driver.get('https://web.whatsapp.com')
        time.sleep(5)   
        while(True):
            try:
                time.sleep(2)        
                qrCodeBase64 = self.driver.execute_script("return document.querySelector('._1QMFu canvas').toDataURL('image/png').substring(21);")
                time.sleep(2)
                
                html = "<div><img src='data:image/png;base64"+qrCodeBase64+"' alt='Red dot' /></div>"
                print(html)
            except Exception as e:
                print("Sua sessão expirou",e)
                # self.display.stop()
                break

     
    def deslogar(self):
        try:
            menu = self.driver.find_element_by_xpath(
                "//span[@data-icon='menu']")
            menu.click()
            time.sleep(4)
            btn_sair = self.driver.find_element_by_xpath(
                f"//div[@title='Sair']")
            btn_sair.click()
            
            print("deslogado")
        except Exception as e:
            print("Erro ao deslogar!",e)

    def receber_mensagens(self):
        painel_mensagem = self.driver.find_element_by_id('pane-side')
        scrollPx = 0
        while(True):
            try:
                # qtd_mensagem_pendente = self.driver.find_element_by_class_name('_31gEB').text
                # time.sleep(1)
                mensagem_pendente = self.driver.find_element_by_class_name('_31gEB')
                time.sleep(3)
                mensagem_pendente.click()
                mensagem_pendente.click()
                time.sleep(2)
                # print(qtd_mensagem_pendente)
                return True
                break
            except Exception as e:
                print(scrollPx)

                if scrollPx > 740:
                    self.driver.execute_script("arguments[0].scrollTop = {};".format(scrollPx),painel_mensagem)

                if scrollPx >  5440:
                    scrollPx = 0
                    self.driver.execute_script("arguments[0].scrollTop = {};".format(scrollPx),painel_mensagem)
                    print("Nenhuma conversa pendente! ",e)

                scrollPx = scrollPx + 144

                print("Procurando conversa! ",e)
                time.sleep(1)
        

    
        


bot = WhatsappBot()
time.sleep(10)

while(True):
    if bot.receber_mensagens():
        time.sleep(1)
        msg = ""  
        while msg != "3":
            time.sleep(1)
            msg = bot.ultima_msg()
            if msg == "1":  
                bot.envia_msg("""Sara:
                    1 - Ajuda (para ajuda)
                    2 - Mais (para saber mais)
                    3 - Sair (para sair da conversa)
                    """)
                # time.sleep(10)
                print("enviou mensagem ajuda")
                break
            elif msg == "2": 
                print("enviou mensagem mais")
                bot.envia_msg("Mando já sua imagem")
                # time.sleep(10)
                break
                # bot.envia_media(imagem)
            elif msg == "3":
                bot.envia_msg("Bye bye!")
                # time.sleep(10)
                print("enviou mensagem sair")
                break
            else:
                break
            
        print("verificar mensagens pendentes")

# bot.deslogar()
# bot.get_qrcode()
# bot.abre_conversa("Importante")  # Passando o numero ou o nome do contato
# time.sleep(2)
# bot.envia_msg("Olá, sou a Sara, assistente pessoal de Handerson! No momento ele estar muito ocupado e responderá a suas mensagens em breve")
# # imagem = bot.dir_path + "/imagem.jpg"  # Passando o caminho da imagem que será enviada
# msg = ""  # Criando a variável msg
# while msg != "/sair" or msg != "/Sair" :
#     time.sleep(1)
#     msg = bot.ultima_msg()  # A cada loop recebe a ultima mensagem da conversa
#     if msg == "/Ajuda" or msg == "/ajuda":  # Retorna uma mensagem de ajuda
#         bot.envia_msg("""Sara: :
#             /Ajuda (para ajuda)
#             /Mais (para saber mais)
#             /Sair (para sair da conversa)
#             """)
#     elif msg == "/mais" or msg == "/Mais":  # Retorna a imagem que selecionamos
#         bot.envia_msg("Mando já sua imagem")
#         # bot.envia_media(imagem)
#     elif msg == "/sair" or msg == "/Sair" :  # Encerra o programa
#         bot.envia_msg("Bye bye!")
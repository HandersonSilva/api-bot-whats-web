import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display

class WhatsappBot:
    def __init__(self):   
        self.interativo = False
        # self.display = Display(visible=0, size=(1000, 900))
        # self.display.start()
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        # options.add_argument('--headless')
        # options.add_argument('--no-startup-window')
        # options.add_argument('--disable-infobars')
        # options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument( '--disable-setuid-sandbox')
        # options.add_argument('--remote-debugging-port=9222')
        self.driver = webdriver.Chrome('./lib/chromedriver', chrome_options=options)
        self.driver.get('https://web.whatsapp.com')


    def iniciar_bot(self):
        while(self.interativo):
            if self.receber_mensagens():
                time.sleep(1)
                msg = ""  
                while msg != "3":
                    time.sleep(1)
                    msg = self.ultima_msg()
                    time.sleep(3)
                    if msg == "1":  
                        self.envia_msg("""Sara:
                            1 - Ajuda (para ajuda)
                            2 - Mais (para saber mais)
                            3 - Sair (para sair da conversa)
                            """)
                        time.sleep(10)
                        print("enviou mensagem ajuda")
                        break
                    elif msg == "2": 
                        print("enviou mensagem mais")
                        self.envia_msg("Mando já sua imagem")
                        time.sleep(10)
                        break
                        # self.envia_media(imagem)
                    elif msg == "3":
                        self.envia_msg("Bye bye!")
                        time.sleep(10)
                        print("enviou mensagem sair")
                        break
                    else:
                        break
                
                print("verificar mensagens pendentes")
            if self.interativo == False:
                break
                return False

    def enviarMensagensEmMassa(self,lista_contato,mensagem):
        error = 0
        for grupo_ou_pessoa in lista_contato:
            try:
                # chat_box_busca = self.driver.find_element_by_class_name('_2FVVk')#_2FbwG _2FVVk
                # chat_box_busca.click()
                # time.sleep(1)
                # chat_box_busca = self.driver.find_element_by_class_name('_3FRCZ')
                # time.sleep(1)
                # chat_box_busca.send_keys(grupo_ou_pessoa)
                # time.sleep(1)
                # campo_grupo = self.driver.find_element_by_xpath(
                #     f"//span[@title='{grupo_ou_pessoa}']")
                # time.sleep(1)
                # campo_grupo.click()

                self.driver.get('https://web.whatsapp.com/send?phone='+grupo_ou_pessoa+'')
                time.sleep(4)

                chat_box = self.driver.find_element_by_class_name('_3uMse')
                time.sleep(1)
                chat_box.click()
                chat_box.send_keys(mensagem)
                botao_enviar = self.driver.find_element_by_xpath(
                    "//span[@data-icon='send']")
                botao_enviar.click()
                time.sleep(5)

            except Exception as e:
                error = error + 1

        return error
                

    def abre_conversa(self, contato):
        try:
            self.driver.get('https://web.whatsapp.com/send?phone='+contato+'')
            time.sleep(4)
            # # Seleciona a caixa de pesquisa de conversa
            # self.caixa_de_pesquisa = self.driver.find_element_by_class_name('_2FVVk')
            # time.sleep(2)
            # # Digita o nome ou numero do contato
            # chat_box_busca = self.driver.find_element_by_class_name('_3FRCZ')
            # time.sleep(2)
            # chat_box_busca.send_keys(contato)
            # # Seleciona o contato
            # self.contato = self.driver.find_element_by_xpath(
            #     f"//span[@title='{contato}']")
            # time.sleep(2)
            # # Entra na conversa
            # self.contato.click()
            return True
        except Exception as e:
            print("Contato não encontrado",e)
            return False

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
            botao_enviar.click()
            time.sleep(1)
            return True

        except Exception as e:
            return False

    def ultima_msg(self):
        try:
            # post = self.driver.find_elements_by_class_name("_3_7SH")
            post = self.driver.find_elements_by_class_name("_2hqOq")
            time.sleep(1)
            ultimo = len(post) - 1
            # if ultimo == 0:
            #     ultimo = 1

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
        # while(True):
        try:
            time.sleep(2)        
            qrCodeBase64 = self.driver.execute_script("return document.querySelector('._1QMFu canvas').toDataURL('image/png').substring(21);")
            time.sleep(2)
            
            html = "<div><img src='data:image/png;base64"+qrCodeBase64+"' alt='Red dot' /></div>"
            return html
        except Exception as e:
            return False
            # self.display.stop()
            # break

    def deslogar(self):
        try:
            menu = self.driver.find_element_by_xpath(
                "//span[@data-icon='menu']")
            menu.click()
            time.sleep(4)
            btn_sair = self.driver.find_element_by_xpath(
                f"//div[@title='Sair']")
            btn_sair.click()
            
            return True
        except Exception as e:
            return False

    def receber_mensagens(self):
        scrollPx = 0
        try:
            painel_mensagem = self.driver.find_element_by_id('pane-side')
        except Exception as e:
                print("Aguardando o carregamento da pagina")
                return False

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

                scrollPx = scrollPx + 72

                print("Procurando conversa! ",e)
                time.sleep(0.5)
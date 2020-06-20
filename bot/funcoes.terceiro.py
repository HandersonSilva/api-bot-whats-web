# def envia_media(self, fileToSend):
#     """ Envia media """
#      try:
#         # Clica no botão adicionar
#         self.driver.find_element_by_css_selector("span[data-icon='clip']").click()
#         # Seleciona input
#         attach = self.driver.find_element_by_css_selector("input[type='file']")
#         # Adiciona arquivo
#         attach.send_keys(fileToSend)
#         sleep(3)
#         # Seleciona botão enviar
#         send = self.driver.find_element_by_xpath("//div[contains(@class, 'yavlE')]")
#         # Clica no botão enviar
#         send.click()
#     except Exception as e:
#         print("Erro ao enviar media", e)
# print("Erro ao enviar media", e)



# def ultima_msg(self):
#         """ Captura a ultima mensagem da conversa """
#         try:
#             post = self.driver.find_elements_by_class_name("_3_7SH")
#             ultimo = len(post) - 1
#             # O texto da ultima mensagem
#             texto = post[ultimo].find_element_by_css_selector(
#                 "span.selectable-text").text
#             return texto
#         except Exception as e:
#         print("Erro ao ler msg, tentando novamente!")


# if __name__ == '__main__':
#     bot = zapbot()  # Inicia o objeto zapbot
#     bot.abre_conversa("+55 84 991938148")  # Passando o numero ou o nome do contato
#     bot.envia_msg("Olá, sou a nana bot whatsapp! Para receber ajuda digite: /help")
#     imagem = bot.dir_path + "/imagem.jpg"  # Passando o caminho da imagem que será enviada
#     msg = ""  # Criando a variável msg
#     while msg != "/quit":
#         sleep(1)
#         msg = bot.ultima_msg()  # A cada loop recebe a ultima mensagem da conversa
#         if msg == "/help":  # Retorna uma mensagem de ajuda
#             bot.envia_msg("""Bot: Esse é um texto com os comandos válidos:
#                 /help (para ajuda)
#                 /mais (para saber mais)
#                 /quit (para sair)
#                 """)
#         elif msg == "/mais":  # Retorna a imagem que selecionamos
#             bot.envia_media(imagem)
#         elif msg == "/quit":  # Encerra o programa

# bot.envia_msg("Bye bye!")
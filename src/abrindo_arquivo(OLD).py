# Deu certo

# with open("mercadoimobiliario.csv") as file:
#     print(file.readlines())

# Deu errado

# with open("mercadoimobiliario_errado.csv") as file:
#     print(file.readlines())

# Arrumando erro

# try:
#     with open("mercadoimobiliario_errado.csv") as file:
#         print(file.readlines())
# except:
#     print("Erro 1")


import requests

# Deu certo

# requisicao = requests.get("https://olinda.bcb.gov.br/olinda/servico/MercadoImobiliario/versao/v1/odata/mercadoimobiliario?$format=json&$select=Data,Info,Valor")

# print(requisicao.json())
# print(requisicao.status_code)

# Deu errado

# requisicao = requests.get("https://ERRO.COM.BR/")

# print(requisicao.json())
# print(requisicao.status_code)

# try:
#     requisicao = requests.get("https://olinda.bcb.gov.br/olinda/servico/MercadoImobiliario/versao/v1/odata/mercadoimobiliario?$format=json&$select=Data,Info,Valor")
# except:
#     print("Erro arquivo Leitura")


try:
    requisicao = requests.get("https://ERRO.COM.BR/")
except:
    print("Erro na request")

# arquivo = requisicao.content

# try:
#     with open("mercadoimobiliario.json", "w") as file:
#         file.write(arquivo)
# except Exception as e:
#     print("Erro arquivo Escrita", e)

import backoff

# @backoff.on_exception(backoff.expo,
#                       requests.exceptions.RequestException)
# def get_url(url):
#     requisicao = requests.get(url)

# get_url("https://ERRO.COM.BR/")

# class Dados():
#     def __init__(self, url=None) -> None:
#         self.url = url
#         self.conteudo = None
    
#     # @backoff.on_exception(backoff.expo,
#     #                     requests.exceptions.RequestException)
#     def baixando_dados_url(self):
#         requisicao = requests.get(self.url)
#         self.conteudo = requisicao.content

# dados1 = Dados("https://ERRO.COM.BR/")
# dados1.baixando_dados_url()

# dados2 = Dados("https://olinda.bcb.gov.br/olinda/servico/MercadoImobiliario/versao/v1/odata/mercadoimobiliario?$format=json&$select=Data,Info,Valor")
# dados2.baixando_dados_url()



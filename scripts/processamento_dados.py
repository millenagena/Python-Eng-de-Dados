import csv
import json

class Dados:
  def __init__(self, dados=None):

    self.dados = dados
    self.nomes_colunas = self.__pega_colunas()
    self.qtd_linhas = self.__conta_linhas()

  @classmethod
  def carrega_dados(cls, caminho, tipo_arquivo):

    if tipo_arquivo == 'csv':
      dados = cls.__leitura_csv(caminho)

    elif tipo_arquivo == 'json':
      dados = cls.__leitura_json(caminho)

    else:
      dados = None
      print(f'Tipo invalido {tipo_arquivo}')

    return cls(dados)

  @staticmethod
  def __leitura_csv(caminho):
    dados_csv = []
    with open(caminho, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
          dados_csv.append(row)

    return dados_csv

  @staticmethod
  def __leitura_json(caminho):
    with open(caminho, 'r') as file:
      dados_json = json.load(file)

    return dados_json

  def __pega_colunas(self):
    nomes_colunas_csv = list(self.dados[0].keys())
    return nomes_colunas_csv

  def rename_columns(self, key_mapping):
    self.dados = [{key_mapping.get(old_key, old_key): value for old_key, value in old_dict.items()} for old_dict in self.dados]
    self.nomes_colunas = self.__pega_colunas()

  def __conta_linhas(self):
    return len(self.dados)

  @classmethod
  def join_dict(cls, dadosA, dadosB):

    combined_list = []

    combined_list.extend(dadosA.dados)
    combined_list.extend(dadosB.dados)

    return cls(combined_list)

  def __transformando_dados_tabela(self):
    dados_combinados_tabela = [self.nomes_colunas]
    for row in self.dados:
      linhas = []
      for coluna in self.nomes_colunas:
        linhas.append(row.get(coluna, 'Indisponivel'))
      dados_combinados_tabela.append(linhas)

    return dados_combinados_tabela

  def salvando_dados(self, csv_file):

    dados_combinados_tabela = self.__transformando_dados_tabela()

    # Open the CSV file in write mode
    with open(csv_file, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(dados_combinados_tabela)

    print(f'Salvo em: {csv_file}')
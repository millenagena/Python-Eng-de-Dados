from processamento_dados import Dados

path_csv = "dados_raw/dados_empresaB.csv"
path_json = 'dados_raw/dados_empresaA.json'

dados_mercadoA = Dados.carrega_dados(path_csv, 'csv')
dados_mercadoB = Dados.carrega_dados(path_json, 'json')

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}
dados_mercadoA.rename_columns(key_mapping)
dados_mercadoB.rename_columns(key_mapping)

dados_fusao = dados_mercadoA.join_dict(dados_mercadoA, dados_mercadoB)

csv_file = "dados_tratados/fusao_fev.csv"

dados_fusao.salvando_dados(csv_file)

qtd_linhas = dados_fusao.qtd_linhas

nomes_colunas = dados_fusao.nomes_colunas

print(f'Quantidade de linhas: {qtd_linhas}')
print(f'Nomes das colunas: {nomes_colunas}')
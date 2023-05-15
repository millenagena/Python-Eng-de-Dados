# Deu certo

with open("mercadoimobiliario.csv") as file:
    print(file.readlines())

# Deu errado

with open("mercadoimobiliario_errado.csv") as file:
    print(file.readlines())

# Arrumando erro

try:
    with open("mercadoimobiliario_errado.csv") as file:
        print(file.readlines())
except:
    print("Erro 1")


class Dados():
    def __init__(self, path=None) -> None:
        self.path = path
        self.conteudo = None



from cryptography.fernet import Fernet
import pandas as pd

# Gerar uma chave e salvar em um arquivo (apenas uma vez)
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# Carregar a chave
def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()

# Função para criptografar o conteúdo do arquivo Excel
def criptografar_excel(input_path, output_path):
    chave = carregar_chave()
    fernet = Fernet(chave)

    # Ler o arquivo Excel
    df = pd.read_excel(input_path)
    
    # Converter o conteúdo em uma string e criptografar
    dados = df.to_csv(index=False).encode()
    dados_criptografados = fernet.encrypt(dados)

    # Salvar os dados criptografados em um novo arquivo
    with open(output_path, "wb") as file:
        file.write(dados_criptografados)

# Gerar uma chave se ainda não tiver sido gerada
# gerar_chave()

# Exemplo de uso
criptografar_excel("entrada.xlsx", "saida_criptografada.dat")

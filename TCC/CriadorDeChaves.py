from cryptography.fernet import Fernet

# Gerar uma chave e salvar em um arquivo (apenas uma vez)
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# Função para carregar a chave
def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()

gerar_chave()
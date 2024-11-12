import pandas as pd

# Função para criptografar um texto usando a cifra de César
def criptografar_texto(texto, chave):
    texto_criptografado = ""
    for caractere in texto:
        # Aplica a cifra de César
        texto_criptografado += chr((ord(caractere) + chave) % 256)
    return texto_criptografado

# Função para criptografar um arquivo Excel
def criptografar_excel(input_path, output_path, chave):
    try:
        # Ler o arquivo Excel
        print("Lendo o arquivo Excel...")
        df = pd.read_excel(input_path)

        # Converter o DataFrame para uma string
        dados = df.to_csv(index=False)
        print("Conteúdo do arquivo convertido para string.")

        # Criptografar o conteúdo
        dados_criptografados = criptografar_texto(dados, chave)
        print("Dados criptografados.")

        # Salvar os dados criptografados em um novo arquivo
        print(f"Salvando dados criptografados em {output_path}...")
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(dados_criptografados)
        print("Arquivo criptografado salvo com sucesso.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
criptografar_excel("/home/victor/Downloads/TCC/TCC/dados_anonimizados.xlsx", "saida_criptografada.txt", chave=3)

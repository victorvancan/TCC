import pandas as pd
from faker import Faker
import numpy as np

# Geração de dados fictícios
data = '/home/victor/Downloads/TCC/TCC/dados_unicos.xlsx'

df = pd.read_excel(data)

# Estratégia de anonimização

# 1. Pseudonimização de nome
fake = Faker()
df['nome_pseudonimo'] = df['nome'].apply(lambda x: fake.name())

# 2. Mascaramento do CPF
df['cpf_mascarado'] = df['cpf'].replace(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.***.***-\4', regex=True)

# 3. Generalização da idade
df['faixa_etaria'] = pd.cut(df['idade'], bins=[0, 18, 35, 60, 100], labels=["Jovem", "Adulto", "Meia-idade", "Idoso"])

# 4. Perturbação do salário (adicionando ruído)
df['salario_perturbado'] = df['salario'].apply(lambda x: x + np.random.normal(0, 500))

# 5. Supressão de e-mails para menores de 30 anos
df['email_suprimido'] = df['email'].mask(df['idade'] < 30, 'anonimizado')

print(df)

df.to_excel('dados_anonimizados.xlsx', index=False)

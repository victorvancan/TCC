import pandas as pd
from faker import Faker
import numpy as np

# Geração de dados fictícios
data = {'nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'idade': [25, 32, 40, 60],
        'cpf': ['12345678901', '98765432100', '12312312399', '99999999999'],
        'salario': [5000, 7000, 12000, 15000],
        'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com']}

df = pd.DataFrame(data)

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

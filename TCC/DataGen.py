import pandas as pd
from faker import Faker
import random

# Configuração do Faker
fake = Faker('pt_BR')
Faker.seed(0)  # Para resultados reprodutíveis

# Listas para armazenar os dados
nomes = []
idades = []
cpfs = []
salarios = []
emails = []

# Gerar 1500 linhas de dados únicos
for _ in range(15000):
    nome = fake.unique.name()
    idade = random.randint(18, 95)
    cpf = fake.unique.cpf()
    salario = round(random.uniform(2000, 150000), 2)  # Salário entre R$2000 e R$15000
    email = fake.unique.email()
    
    nomes.append(nome)
    idades.append(idade)
    cpfs.append(cpf)
    salarios.append(salario)
    emails.append(email)

# Criar o DataFrame
df = pd.DataFrame({
    'nome': nomes,
    'idade': idades,
    'cpf': cpfs,
    'salario': salarios,
    'email': emails
})

# # Salvar em um arquivo Excel
df.to_excel('dados_unicos.xlsx', index=False)

print("Arquivo 'dados_unicos.xlsx' criado com 0 linhas de dados únicos.")

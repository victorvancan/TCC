import random

# Função para aplicar k-anonimização
def k_anonimization(data, k):
    # Etapa 1: Contar as ocorrências de cada combinação de quasi-identificadores
    groups = {}
    for row in data:
        # Usando idade e cidade como quasi-identificadores
        quasi_identifiers = (row[1], row[2])  # Idade e cidade
        if quasi_identifiers not in groups:
            groups[quasi_identifiers] = []
        groups[quasi_identifiers].append(row)
    
    # Etapa 2: Verificar se cada grupo tem ao menos k elementos, senão generalizar ou suprimir
    anonymized_data = []
    for quasi_identifiers, group in groups.items():
        if len(group) < k:
            # Generalizar os quasi-identificadores
            generalized_group = generalize_group(group)
            anonymized_data.extend(generalized_group)
        else:
            anonymized_data.extend(group)
    
    return anonymized_data

# Função para generalizar os quasi-identificadores
def generalize_group(group):
    # Generalizar idade (faixa etária) e cidade (por exemplo, remover cidade específica)
    generalized_group = []
    for row in group:
        generalized_age = generalize_age(row[1])
        generalized_city = "Unknown"  # Suprimir cidade
        generalized_row = (row[0], generalized_age, generalized_city, row[3])  # Nome, Idade, Cidade, Diagnóstico
        generalized_group.append(generalized_row)
    return generalized_group

# Função para generalizar idade
def generalize_age(age):
    if age < 20:
        return "<20"
    elif age < 40:
        return "20-39"
    elif age < 60:
        return "40-59"
    else:
        return "60+"

# Exemplo de conjunto de dados
data = [
    ("Alice", 25, "São Paulo", "Diabetes"),
    ("Bob", 34, "São Paulo", "Hipertensão"),
    ("Carol", 45, "Rio de Janeiro", "Diabetes"),
    ("David", 23, "São Paulo", "Hipertensão"),
    ("Eve", 55, "Rio de Janeiro", "Diabetes"),
    ("Frank", 60, "Belo Horizonte", "Hipertensão"),
    ("Grace", 30, "São Paulo", "Diabetes")
]

# Valor de k
k = 2

# Aplicando k-anonimização
anonymized_data = k_anonimization(data, k)

# Exibindo dados anonimizados
for row in anonymized_data:
    print(row)

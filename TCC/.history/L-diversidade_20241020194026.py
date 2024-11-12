# Função para aplicar L-diversidade
def l_diversity(data, k, l):
    # Etapa 1: Agrupar os dados com base nos quasi-identificadores (idade, cidade)
    groups = {}
    for row in data:
        quasi_identifiers = (row[1], row[2])  # Usando idade e cidade como quasi-identificadores
        if quasi_identifiers not in groups:
            groups[quasi_identifiers] = []
        groups[quasi_identifiers].append(row)
    
    # Etapa 2: Verificar se cada grupo tem ao menos k elementos e é L-diverso
    anonymized_data = []
    for quasi_identifiers, group in groups.items():
        if len(group) < k or not check_l_diversity(group, l):
            # Generalizar o grupo se não atender aos requisitos de k ou L-diversidade
            generalized_group = generalize_group(group)
            anonymized_data.extend(generalized_group)
        else:
            anonymized_data.extend(group)
    
    return anonymized_data

# Função para verificar L-diversidade
def check_l_diversity(group, l):
    # Criar um conjunto de valores únicos do atributo sensível (diagnóstico)
    sensitive_values = set(row[3] for row in group)  # Diagnóstico
    return len(sensitive_values) >= l

# Função para generalizar os quasi-identificadores (mesma da k-anonimização)
def generalize_group(group):
    generalized_group = []
    for row in group:
        generalized_age = generalize_age(row[1])
        generalized_city = "Unknown"  # Suprimir cidade
        generalized_row = (row[0], generalized_age, generalized_city, row[3])  # Nome, Idade, Cidade, Diagnóstico
        generalized_group.append(generalized_row)
    return generalized_group

# Função para generalizar idade (mesma da k-anonimização)
def generalize_age(age):
    if age < 20:
        return "<20"
    elif age < 40:
        return "20-39"
    elif age < 60:
        return "40-59"
    else:
        return "60+"
# Valores de k e l
k = 2
l = 2

# Aplicando L-diversidade
anonymized_data = l_diversity(data, k, l)

# Exemplo de conjunto de dados
data = [
    ("Alice", 25, "São Paulo", "Diabetes"),
    ("Bob", 34, "São Paulo", "Hipertensão"),
    ("Carol", 45, "Rio de Janeiro", "Diabetes"),
    ("David", 23, "São Paulo", "Hipertensão"),
    ("Eve", 55, "Rio de Janeiro", "Diabetes"),
    ("Frank", 60, "Belo Horizonte", "Hipertensão"),
    ("Grace", 30, "São Paulo", "Diabetes"),
    ("Hank", 45, "Rio de Janeiro", "Câncer"),
    ("Ivy", 34, "São Paulo", "Câncer")
]


# Exibindo dados anonimizados
for row in anonymized_data:
    print(row)

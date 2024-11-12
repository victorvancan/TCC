import math

# Função para calcular a distância de EMD entre duas distribuições
def emd_distance(distribution1, distribution2):
    # As distribuições são dicionários {valor_sensivel: proporcao}
    total_distance = 0
    cumulative_dist1 = 0
    cumulative_dist2 = 0

    # Obter todas as chaves possíveis (valores sensíveis)
    all_values = sorted(set(distribution1.keys()).union(set(distribution2.keys())))
    
    for value in all_values:
        # Obter as proporções das duas distribuições para esse valor (ou 0 se não existir)
        proportion1 = distribution1.get(value, 0)
        proportion2 = distribution2.get(value, 0)

        cumulative_dist1 += proportion1
        cumulative_dist2 += proportion2
        
        total_distance += abs(cumulative_dist1 - cumulative_dist2)
    
    return total_distance

# Função para calcular a distribuição de valores sensíveis em um grupo
def calculate_sensitive_distribution(group):
    sensitive_counts = {}
    total_count = len(group)
    
    for row in group:
        sensitive_value = row[3]  # Atributo sensível (ex: diagnóstico)
        if sensitive_value not in sensitive_counts:
            sensitive_counts[sensitive_value] = 0
        sensitive_counts[sensitive_value] += 1
    
    # Convertendo contagem para proporção
    for key in sensitive_counts:
        sensitive_counts[key] /= total_count
    
    return sensitive_counts

# Função para aplicar T-closeness
def t_closeness(data, k, t):
    # Etapa 1: Calcular a distribuição original de valores sensíveis
    original_distribution = calculate_sensitive_distribution(data)
    
    # Etapa 2: Agrupar os dados com base nos quasi-identificadores (idade, cidade)
    groups = {}
    for row in data:
        quasi_identifiers = (row[1], row[2])  # Usando idade e cidade como quasi-identificadores
        if quasi_identifiers not in groups:
            groups[quasi_identifiers] = []
        groups[quasi_identifiers].append(row)
    
    # Etapa 3: Verificar se cada grupo atende aos requisitos de K-anonimização e T-closeness
    anonymized_data = []
    for quasi_identifiers, group in groups.items():
        if len(group) >= k:
            sensitive_distribution = calculate_sensitive_distribution(group)
            # Calcular a distância EMD entre a distribuição do grupo e a distribuição original
            distance = emd_distance(sensitive_distribution, original_distribution)
            if distance <= t:
                anonymized_data.extend(group)
            else:
                # Se o grupo não for T-close, aplicar generalização
                generalized_group = generalize_group(group)
                anonymized_data.extend(generalized_group)
        else:
            # Se o grupo não atender ao requisito de K, aplicar generalização
            generalized_group = generalize_group(group)
            anonymized_data.extend(generalized_group)
    
    return anonymized_data

# Função para generalizar os quasi-identificadores (mesma da K-anonimização)
def generalize_group(group):
    generalized_group = []
    for row in group:
        generalized_age = generalize_age(row[1])
        generalized_city = "Unknown"  # Suprimir cidade
        generalized_row = (row[0], generalized_age, generalized_city, row[3])  # Nome, Idade, Cidade, Diagnóstico
        generalized_group.append(generalized_row)
    return generalized_group

# Função para generalizar idade (mesma da K-anonimização)
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
    ("Grace", 30, "São Paulo", "Diabetes"),
    ("Hank", 45, "Rio de Janeiro", "Câncer"),
    ("Ivy", 34, "São Paulo", "Câncer")
]

# Valores de K e T (limiar de distância para T-closeness)
k = 2
t = 0.3

# Aplicando T-closeness
anonymized_data = t_closeness(data, k, t)

# Exibindo dados anonimizados
for row in anonymized_data:
    print(row)

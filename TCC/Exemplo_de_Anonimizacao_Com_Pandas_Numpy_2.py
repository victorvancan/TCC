import numpy as np
from faker import Faker

# Dados sensíveis
nomes = np.array(['Alice', 'Bob', 'Charlie', 'David'])
cpfs = np.array(['12345678901', '98765432100', '12312312399', '99999999999'])
salarios = np.array([5000, 7000, 12000, 15000])
idades = np.array([25, 32, 40, 60])

# Pseudonimização de Nomes
fake = Faker()
nomes_pseudonimos = np.array([fake.name() for _ in nomes])

# Mascaramento de CPF
cpfs_mascarados = np.char.replace(cpfs, cpfs[:, 3:9], '*****')

# Perturbação de Salários
salarios_perturbados = salarios + np.random.normal(0, 500, len(salarios))

# Generalização de Idades em Faixas Etárias
bins = [18, 30, 50, 100]
faixas_etarias = np.digitize(idades, bins)

# Embaralhamento dos dados de salários e idades*
np.random.shuffle(salarios_perturbados)
np.random.shuffle(faixas_etarias)

# Exibindo os dados anonimizados
print("Nomes Pseudonimizados:", nomes_pseudonimos)
print("CPFs Mascarados:", cpfs_mascarados)
print("Salários Perturbados e Embaralhados:", salarios_perturbados)
print("Faixas Etárias Embaralhadas:", faixas_etarias)

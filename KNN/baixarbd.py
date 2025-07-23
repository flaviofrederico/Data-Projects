import pandas as pd
import random
import numpy as np

# Definindo listas de valores possíveis
generos = ['Masculino', 'Feminino']
estados_civis = ['Solteiro', 'Casado', 'Divorciado']
tipos_cliente = ['Affluent', 'Premium', 'Standard', 'Economy']

def gerar_tipo_cliente(renda, valor_seguro, score):
    if renda > 100000 and valor_seguro > 300000 and score > 80:
        return 'Affluent'
    elif renda > 70000 and valor_seguro > 150000 and score > 70:
        return 'Premium'
    elif renda > 30000 and valor_seguro > 40000 and score > 50:
        return 'Standard'
    else:
        return 'Economy'

# Lista para armazenar os dados
dados = []

for i in range(1, 10001):  # 300 linhas
    idade = random.randint(18, 70)
    genero = random.choice(generos)
    estado_civil = random.choice(estados_civis)
    rendimento_anual = round(random.normalvariate(60000, 30000), 2)
    rendimento_anual = max(10000, rendimento_anual)  # Evitar valores negativos
    numero_polices = random.randint(1, 6)
    valor_total_seguro = round(random.uniform(10000, 600000), 2)
    score_satisfacao = random.randint(30, 100)
    tipo_cliente = gerar_tipo_cliente(rendimento_anual, valor_total_seguro, score_satisfacao)

    dados.append([
        i, idade, genero, estado_civil, rendimento_anual,
        numero_polices, valor_total_seguro, score_satisfacao, tipo_cliente
    ])

# Criar DataFrame
colunas = [
    "ID", "Idade", "Genero", "Estado_Civil", "Rendimento_Anual",
    "Numero_Polices", "Valor_Total_Seguro", "Score_Satisfacao", "Tipo_Cliente"
]
df = pd.DataFrame(dados, columns=colunas)

# Salvar como CSV
df.to_csv("clientes_seguradora.csv", index=False, encoding='utf-8')

print("Arquivo 'clientes_seguradora.csv' criado com sucesso!")

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:30:08 2025

@author: mathe
"""
# CARREGAR BIBLIOTECAS

import statistics
import math
from scipy.stats import skew
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

# LER DADOS DO ARQUIVO CSV
dados=[]
dd=[]
print("**************************************************************")
print("EFETUANDO LEITURA DE DADOS PARA ANALISE")
path = "lebron_stats.csv"
with open (path, 'r', newline='') as ARQUIVO:
    d = csv.reader(ARQUIVO) 
    dd=list(d)
    
df=[]
df = pd.DataFrame(dd, columns=["G","Date","Age","Tm","Unnamed: 5","Opp","Unnamed: 7","GS","MP","FG","FGA","FG%","3P","3PA","3P%","FT","FTA","FT%","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PTS","GmSc","+/-"]);

# REMOVER COLUNAS
colunas_remover = ["Unnamed: 5", "Unnamed: 7", "G", "GS", "+/-", "Age", "Tm", "Opp", "GmSc"]
df = df.drop(columns=colunas_remover)

# EXCLUIR PRIMEIRA LINHA
df = df.drop([0], axis=0)

# CONVERTER COLUNA "DATE" PARA FORMATO DE DATA E EXTRAIR O ANO
df["Date"] = pd.to_datetime(df["Date"], errors='coerce').dt.year

# CONVERTER 'MP' (MINUTOS JOGADOS) PARA MINUTOS TOTAIS
df["MP"] = df["MP"].apply(lambda x: sum(int(t) * 60**i for i, t in enumerate(reversed(x.split(":")))) if isinstance(x, str) else x)

# CONVERTER TODAS AS COLUNAS NUMERICAS PARA O TIPO FLOAT
colunas_numericas = df.columns.difference(["Date"])
df[colunas_numericas] = df[colunas_numericas].apply(pd.to_numeric, errors='coerce')

# CONFIGURAR PANDAS, TODAS AS COLUNAS SEM TRUNCAMENTO
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)

# EXIBIR ESTATÍSTICAS BÁSICAS
stats = df.describe().T
print("Estatísticas Básicas:")
print(stats)

# FUNÇÃO PARA CALCULAR MEDIDAS DESCRITIVAS
def calcular_medidas_descritivas(coluna):
    media = np.mean(coluna)
    moda = coluna.mode()
    if not moda.empty:
        moda = moda.iloc[0]  # Pega o primeiro valor se houver múltiplas modas
    else:
        moda = np.nan  # Caso não exista moda, define como NaN
    mediana = np.median(coluna)
    desvio_padrao = np.std(coluna)
    variancia = np.var(coluna)
    return {
        "Média": media,
        "Moda": moda,
        "Mediana": mediana,
        "Desvio Padrão": desvio_padrao,
        "Variância": variancia
    }

# CALCULAR MEDIDAS DESCRITIVAS PARA A COLUNA "PTS" (PONTOS)
medidas_pts = calcular_medidas_descritivas(df["PTS"])
print("\nMedidas Descritivas para PTS (Pontos):")
for medida, valor in medidas_pts.items():
    print(f"{medida}: {valor:.2f}")
    
# GERAR HISTOGRAMA PARA "PTS" (PONTOS)
plt.figure(figsize=(10, 6))
plt.hist(df["PTS"], bins=10, edgecolor='black', alpha=0.7)
plt.xlabel("Pontos por Jogo")
plt.ylabel("Frequência")
plt.title("Histograma da Distribuição de Pontos por Jogo de LeBron")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# ANÁLISE DE ASSIMETRIA
df["PTS"] = pd.to_numeric(df["PTS"], errors='coerce')
df = df.dropna(subset=["PTS"])
skewness = skew(df["PTS"].dropna())

# DETERMINAR TIPO DE ASSIMETRIA
if skewness > 0:
    tipo_assimetria = "Assimétrica à direita (positiva)"
elif skewness < 0:
    tipo_assimetria = "Assimétrica à esquerda (negativa)"
else:
    tipo_assimetria = "Simétrica"

print(f"\nCoeficiente de Assimetria (Skewness) para PTS: {skewness:.2f}")
print(f"Tipo de Assimetria: {tipo_assimetria}")

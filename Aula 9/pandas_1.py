import pandas as pd

df = {
    'cargos': ["assistente", "auxiliar", "gerente"],
    'salários': [2500, 1800, 7500],
}

dados_bi = pd.DataFrame(df)
print(dados_bi.head(2))
print(dados_bi.tail(1))
print(dados_bi.shape)
print(dados_bi.info())
print(dados_bi.describe())
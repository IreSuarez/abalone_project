import pandas as pd

df = pd.read_csv("data/raw/abalone_raw.csv")
target = pd.read_csv("data/raw/abalone_target_raw.csv")

df["Rings"] = target.iloc[:, 0]
#Nueva columna
df['Age'] = df['Rings'] + 1.5

#Codificación de variable categórica
df = pd.get_dummies(df, columns=['Sex'], dtype=int)

# Criterio de IQR
columnas = df.select_dtypes(include="number").columns

for col in columnas:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 *IQR
    df = df[(df[col] >= lim_inf) & (df[col] <= lim_sup)]

df.to_csv("data/processed/abalone_clean.csv", index=False)
print("Dataset procesado correctamente y guardado")

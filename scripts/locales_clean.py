import pandas as pd

path = "../data/raw/locales-en-venta-2020.csv"

df = pd.read_csv(path)

def descartar_columnas(df):
    df = df.drop(columns=["PESOSM2", "PROPIEDADS"])
    return df

def corregir_galeria(df):
    df["EN_GALERIA"] = df["EN_GALERIA"].replace("S1", "SI")
    df["EN_GALERIA"] = df["EN_GALERIA"].fillna("NO")
    return df

def descartar_direccion_nula(df):
    df = df.dropna(subset=["DIRECCION"])
    return df

df = descartar_columnas(df)
df = corregir_galeria(df)
df = descartar_direccion_nula(df)

df.to_csv("../data/processed/locales_clean.csv", index=False)
print(df.head())
print(df.shape)
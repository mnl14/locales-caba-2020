import pandas as pd

path_in = "../data/processed/locales_clean.csv"
path_out = "../data/processed/precio_m2_vs_tiempo.csv"

df = pd.read_csv(path_in)

orden_trimestres = ["PRIMER", "SEGUNDO", "TERCER", "CUARTO"]
df["TRIMESTRE_"] = pd.Categorical(df["TRIMESTRE_"], categories=orden_trimestres, ordered=True)

def avg_precio_m2_trimestre(df):
    resultado = df.groupby("TRIMESTRE_")["USDM2"].mean()
    return resultado

resultado = avg_precio_m2_trimestre(df)
print(resultado)

resultado.to_csv(path_out)

path_out = "../data/processed/volumen_ofertas_vs_tiempo.csv"

def volumen_ofertas_trimestre(df):
    resultado = df.groupby("TRIMESTRE_").size()
    return resultado

resultado = volumen_ofertas_trimestre(df)
resultado.to_csv(path_out)

path_out = "../data/processed/distribucion_antiguedad.csv"

def distribucion_antiguedad(df):
    bins = [-1, 0, 10, 25, 50, 100, 999]
    labels = ["0", "1-10", "11-25", "26-50", "51-100", "100+"]
    
    df["RANGO_ANTIG"] = pd.cut(df["ANTIG"], bins=bins, labels=labels)
    resultado = df.groupby("RANGO_ANTIG").size()
    return resultado

resultado = distribucion_antiguedad(df)
resultado.to_csv(path_out)

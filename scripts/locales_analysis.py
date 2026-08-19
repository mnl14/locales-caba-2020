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
#print(resultado)

resultado.to_csv(path_out)

path_out = "../data/processed/volumen_ofertas_vs_tiempo.csv"

def volumen_ofertas_trimestre(df):
    resultado = df.groupby("TRIMESTRE_").size()
    resultado = resultado.rename("Ofertas")
    return resultado

resultado = volumen_ofertas_trimestre(df)
resultado.to_csv(path_out)

path_out = "../data/processed/distribucion_antiguedad.csv"

def distribucion_antiguedad(df):
    bins = [-1, 0, 10, 25, 50, 100, 999]
    labels = ["0", "1-10", "11-25", "26-50", "51-100", "100+"]
    
    df["RANGO_ANTIG"] = pd.cut(df["ANTIG"], bins=bins, labels=labels)
    resultado = df.groupby("RANGO_ANTIG").size()
    resultado = resultado.rename("CANTIDAD")
    return resultado

resultado = distribucion_antiguedad(df)
resultado.to_csv(path_out)

def resumen_por_comuna(df):
    resultado = df.groupby("COMUNA_").agg(
        precio_m2_avg=("USDM2", "mean"),
        volumen=("USDM2", "size")
    )
    return resultado

path_out = "../data/processed/resumen_comuna.csv"
resultado = resumen_por_comuna(df)
resultado.to_csv(path_out)

def exportar_dataset_dashboard(df):
    columnas = ["TRIMESTRE_", "EN_GALERIA", "USDM2", "COMUNA_", "ANTIG"]
    df_reducido = df[columnas]
    df_reducido.to_json("../dashboard/data.json", orient="records")

exportar_dataset_dashboard(df)
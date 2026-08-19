import json
import pandas as pd
import plotly.express as px

# Primer grafico
path_in = "../data/processed/precio_m2_vs_tiempo.csv"
df = pd.read_csv(path_in)
path_out = "../dashboard/precio_m2_vs_tiempo.html"

orden_trimestres = ["PRIMER", "SEGUNDO", "TERCER", "CUARTO"]

fig = px.line(
    df,
    x="TRIMESTRE_",
    y="USDM2",
    title="Precio USD/m² por trimestre - CABA 2020",
    category_orders={"TRIMESTRE_": orden_trimestres}
)
fig.write_html(path_out)

# Segundo grafico
path_in = "../data/processed/volumen_ofertas_vs_tiempo.csv"
df = pd.read_csv(path_in)
path_out = "../dashboard/volumen_ofertas_vs_tiempo.html"

orden_trimestres = ["PRIMER", "SEGUNDO", "TERCER", "CUARTO"]

fig = px.line(
    df,
    x="TRIMESTRE_",
    y="Ofertas",
    title="Volumen de ofertas por trimestre",
    category_orders={"TRIMESTRE_": orden_trimestres}
)
fig.write_html(path_out)

# Tercer grafico
path_in = "../data/processed/distribucion_antiguedad.csv"
df = pd.read_csv(path_in)
path_out = "../dashboard/distribucion_antiguedad.html"

orden_antig = ["0", "1-10", "11-25", "26-50", "51-100", "100+"]

fig = px.bar(
    df,
    x="RANGO_ANTIG",
    y="CANTIDAD",
    title="Distribución de ofertas por antigüedad",
    category_orders={"RANGO_ANTIG": orden_antig}
)
fig.write_html(path_out)

# Grafico de mapa
import json

with open("../data/raw/comunas.geojson", "r", encoding="utf-8") as f:
    geojson_comunas = json.load(f)

path_in = "../data/processed/resumen_comuna.csv"
df = pd.read_csv(path_in)

fig = px.choropleth(
    df,
    geojson=geojson_comunas,
    locations="COMUNA_",
    featureidkey="properties.comuna",
    color="precio_m2_avg",
    projection="mercator"
)
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(
                    label="Precio USD/m²",
                    method="restyle",
                    args=[{"z": [df["precio_m2_avg"]]}]
                ),
                dict(
                    label="Volumen de ofertas",
                    method="restyle",
                    args=[{"z": [df["volumen"]]}]
                ),
            ],
            direction="down",
            showactive=True,
        )
    ]
)
fig.write_html("../dashboard/mapa_comunas.html")
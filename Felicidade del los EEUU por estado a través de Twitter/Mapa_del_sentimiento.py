import folium
import pandas

estados_centro = [["AL", "Alabama", 32.7794, -86.8287], ["AK", "Alaska", 64.0685, -152.2782],
                  ["AZ", "Arizona", 34.2744, -111.6602], ["AR", "Arkansas", 34.8938, -92.4426],
                  ["CA", "California", 37.1841, -119.4696], ["CO", "Colorado", 38.9972, -105.5478],
                  ["CT", "Connecticut", 41.6219, -72.7273], ["DE", "Delaware", 38.9896, -75.5050],
                  ["FL", "Florida", 28.6305, -82.4497], ["GA", "Georgia", 32.6415, -83.4426],
                  ["HI", "Hawaii", 20.2927, -156.3737], ["ID", "Idaho", 44.3509, -114.6130],
                  ["IL", "Illinois", 40.0417,- 89.1965], ["IN", "Indiana", 39.8942, -86.2816],
                  ["IA", "Iowa", 42.0751, -93.4960], ["KS", "Kansas", 38.4937, -98.3804],
                  ["KY", "Kentucky", 37.5347, -85.3021], ["LA", "Louisiana", 31.0689, -91.9968],
                  ["ME", "Maine", 45.3695, -69.2428], ["MD", "Maryland", 39.0550, -76.7909],
                  ["MA", "Massachusetts", 42.2596, -71.8083], ["MI", "Michigan", 44.3467, -85.4102],
                  ["MN", "Minnesota", 46.2807, -94.3053], ["MS", "Mississippi", 32.7364, -89.6678],
                  ["MO", "Missouri", 38.3566, -92.4580], ["MT", "Montana", 47.0527, -109.6333],
                  ["NE", "Nebraska", 41.5378, -99.7951], ["NV", "Nevada", 39.3289, -116.6312],
                  ["NH", "New Hampshire", 43.6805, -71.5811], ["NJ", "New Jersey", 40.1907, -74.6728],
                  ["NM", "New Mexico", 34.4071, -106.1126], ["NY", "New York", 42.9538, -75.5268],
                  ["NC", "North Carolina", 35.5557, -79.3877], ["ND", "North Dakota", 47.4501, -100.4659],
                  ["OH", "Ohio", 40.2862, -82.7937], ["OK", "Oklahoma", 35.5889, -97.4943],
                  ["OR", "Oregon", 43.9336, -120.5583], ["PA", "Pennsylvania", 40.8781, -77.7996],
                  ["RI", "Rhode Island", 41.6762, -71.5562], ["SC", "South Carolina", 33.9169, -80.8964],
                  ["SD", "South Dakota", 44.4443, -100.2263], ["TN", "Tennessee", 35.8580, -86.3505],
                  ["TX", "Texas", 31.4757, -99.3312], ["UT", "Utah", 39.3055, -111.6703],
                  ["VT", "Vermont", 44.0687, -72.6658], ["VA", "Virginia", 37.5215, -78.8537],
                  ["WA", "Washington", 47.3826, -120.4472], ["WV", "West Virginia", 38.6409, -80.6227],
                  ["WI", "Wisconsin", 44.6243, -89.9941], ["WY", "Wyoming", 42.9957, -107.5512]]


def mapa_sentimiento():
    estados_geo = "us-states.json"
    sentimientos = "Sentimientos_por_estado.csv"
    sentimientos_datos = pandas.read_csv(sentimientos)

    mapa = folium.Map(location=[48, -102], zoom_start=3)

    mapa.choropleth(
        geo_data=estados_geo,
        name="Sentimientos",
        data=sentimientos_datos,
        columns=["Estado", "Punctuacion"],
        key_on="feature.id",
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Felicidad por Estado"
    )

    for estado in estados_centro:
        nombre_curto = estado[0]
        nombre = estado[1]
        lat = float(estado[2])
        lon = float(estado[3])
        leyenda = ""
        tooltip = "Click para ver detalles"
        for e in sentimientos_datos.get_values():
            if e[0] == nombre_curto:
                leyenda = e[1]
        folium.Marker([lat, lon], popup="<i>En %s la puntuacion de felicidad es %s</i>" %(nombre, leyenda), tooltip=tooltip).add_to(mapa)

    folium.LayerControl().add_to(mapa)

    mapa.save("Mapa_del_sentimiento.html")


mapa_sentimiento()
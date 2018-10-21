import folium
import pandas

def mapa_sentimiento():

    estados_geo = "us-states.json"

    sentimientos = "Sentimientos_por_estado.csv"
    sentimientos_datos = pandas.read_csv(sentimientos)

    mapa = folium.Map(location=[48, -102], zoom_start=3)

    estados_centro = [ ["Alabama","32.7794", "86.8287"],  ["Alaska","64.0685", "152.2782"],  ["Arizona","34.2744", "111.6602"],  ["Arkansas","34.8938", "92.4426"],  ["California","37.1841", "119.4696"],  ["Colorado","38.9972", "105.5478"],  ["Connecticut","41.6219", "72.7273"],  ["Delaware","38.9896", "75.5050"],  ["Florida","28.6305", "82.4497"],  ["Georgia","32.6415", "83.4426"],  ["Hawaii","20.2927", "156.3737"],  ["Idaho","44.3509", "114.6130"],  ["Illinois","40.0417", "89.1965"],  ["Indiana","39.8942", "86.2816"],  ["Iowa","42.0751", "93.4960"],  ["Kansas","38.4937", "98.3804"],  ["Kentucky","37.5347", "85.3021"],  ["Louisiana","31.0689", "91.9968"],  ["Maine","45.3695", "69.2428"],  ["Maryland","39.0550", "76.7909"],  ["Massachusetts","42.2596", "71.8083"],  ["Michigan","44.3467", "85.4102"],  ["Minnesota","46.2807", "94.3053"],  ["Mississippi","32.7364", "89.6678"],  ["Missouri","38.3566", "92.4580"],  ["Montana","47.0527", "109.6333"],  ["Nebraska","41.5378", "99.7951"],  ["Nevada","39.3289", "116.6312"],  ["New Hampshire","43.6805", "71.5811"],  ["New Jersey","40.1907", "74.6728"],  ["New Mexico","34.4071", "106.1126"],  ["New York","42.9538", "75.5268"],  ["North Carolina","35.5557", "79.3877"],  ["North Dakota","47.4501", "100.4659"],  ["Ohio","40.2862", "82.7937"],  ["Oklahoma","35.5889", "97.4943"],  ["Oregon","43.9336", "120.5583"],  ["Pennsylvania","40.8781", "77.7996"],  ["Rhode Island","41.6762", "71.5562"],  ["South Carolina","33.9169", "80.8964"],  ["South Dakota","44.4443", "100.2263"],  ["Tennessee","35.8580", "86.3505"],  ["Texas","31.4757", "99.3312"],  ["Utah","39.3055", "111.6703"],  ["Vermont","44.0687", "72.6658"],  ["Virginia","37.5215", "78.8537"],  ["Washington","47.3826", "120.4472"],  ["West Virginia","38.6409", "80.6227"],  ["Wisconsin","44.6243", "89.9941"],  ["Wyoming","42.9957", "107.5512"]]
    mapa.choropleth(
        geo_data=estados_geo,
        name='senti',
        data=sentimientos_datos,
        columns=['Estado', 'Punctuacion'],
        key_on='feature.id',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Felicidad por Estado'
    )

    folium.Marker([32.7794, 86.8287], popup="<i>Alabama</i>", tooltip='temp').add_to(mapa)
    for estado in estados_centro:
        lat = float(estado[1])
        long = float(estado[2])
        nombre = estado[0]
        folium.Marker([lat, long], popup="<i>{}</i>".format(nombre), tooltip='temp').add_to(mapa)


    folium.LayerControl().add_to(mapa)

    mapa.save('mapa.html')


mapa_sentimiento()
# coding=utf-8
# Encontrar los 5 estados más felices de USA de acuerdo al análisis de sentimiento con AFFINN e criar mapa interativo.

import json
import re

states = ["ak","al","ar","az","ca","co","ct","de","fl","ga","hi","ia","id","il",
          "in","ks","ky","la","ma","md","me","mi","mn","mo","ms","mt","nc","nd","ne","nh",
          "nj","nm","nv","ny","oh","ok","or","pa","ri","sc","sd","tn","tx","ut","va","vt",
          "wa","wi","wv","wy"]

states_names = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado',
'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois',
'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana',
'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 'NC':'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island',
'SC': 'South Carolina', 'SD': 'South Dakota', 'TN':'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia',
'WA': 'Washington','WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'}


def get_state(data):
    if data["place"] is not None and data["place"]["country_code"] == "US":
        state = str(data["place"]["full_name"]).lower().split(", ")
        if len(state) > 1:
            return state[1]


def is_state(state):
    if state in states:
        return True
    return False


def read_tweets():
    file = "output.txt"

    array = []
    with open(file, "r") as ins:

        for line in ins:
            if (len(line) > 1):
                data = json.loads(line)
                if "created_at" in data:
                    state = get_state(data)
                    if is_state(state):
                        if "text" in data:
                            tweet = data["text"].lower().encode("utf-8")
                            tweet = re.sub("[^-A-Za-z+ ]"," ", tweet)
                            array.append([tweet, state])
        return array


def dic_sent():
    sent_dic = {}
    with open("AFINN-111.txt", "r") as sentimiento:
        for a in sentimiento.readlines():
            a = a.split("\t")
            sent_dic[a[0]] = int(a[1])
    return sent_dic

def punctuacion_tweets():
    diccionario = dic_sent()
    sentimientos = diccionario.keys()
    tweets = read_tweets()
    score_tweet = 0
    n_t = 0

    while n_t < len(tweets):
        for sentimiento in sentimientos:
            if sentimiento in tweets[n_t][0]:
                score_tweet += diccionario[sentimiento]
        tweets[n_t].append(score_tweet)
        score_tweet = 0
        n_t += 1
    return tweets


def punctuacion_estado():
    global states
    tweets = punctuacion_tweets()
    punctuacion_estados = {}

    for estado in states:
        punctuacion_estados[estado] = 0

    for tweet in tweets:
        punctuacion_estados[tweet[1]] += tweet[2]

    return punctuacion_estados


def salvar_archivo():
    diccionario_estados = punctuacion_estado()
    archivo = open("Sentimientos_por_estado.csv", "w")
    csv = "Estado,Punctuacion\n"
    for estado, punctuacion in diccionario_estados.items():
        line = "%s, %d\n" %(estado.upper(), punctuacion)
        csv += line

    archivo.write(csv)

salvar_archivo()
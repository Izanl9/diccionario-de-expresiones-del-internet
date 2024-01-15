memedict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'ROFL':'una respuesta a una broma',
            'SHEESH':'ligera desaprobación',
            'CREEPY':'aterrador, siniestro',
            'AGGRO':'ponerse agresivo/enojado',
            'FURRY':'persona que se identifica como un animal humanoide'
            }
for i in range (5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in memedict.keys():
        print(memedict[word])
    else:
        print('no reconocible')

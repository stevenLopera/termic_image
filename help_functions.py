################# DICTIONARY #################################################
## KEYS ORDENADAS POR VALOR
def keysSortedBy(dict, value):
    key = sorted(dict.__iter__(), key=lambda x: (dict[x][value]))
    return key


## print dict
def printDict(dict):
    import pprint
    pprint.pprint(dict)


##################### DATAFRAME PANDA #########################################
# panda=pd.DataFrame.from_dict(pixeles)
# panda= panda.transpose()
## dict to panda
# def dictToPanda(dict):
#   import pandas as pd
#  panda = pd.DataFrame.from_dict(dict)

## Transponer data#panda=pd.DataFrame.from_dict(pixeles)
# panda= panda.transpose()frame panda y ordenarlo por una columna
# panda = panda.transpose()
# panda.sort_values("value")


## FUNCION PARA CAMBIAR KEYS
def adaptDictToJoin(dict, tag):
    for x in dict.keys():
        v = list(dict.get(x).keys())
        aux = {}
        aux[tag] = v
        dict[x] = aux


##  AÑADIR DICT DE PADRES AL DE PIXELES
def joinInDict1(dict1, dict2):
    for x in dict2.keys():
        a = dict1.get(x)
        b = dict2.get(x)
        dict1[x] = {**a, **b}


## FUNCION PARA CAMBIAR LOS INDICES DE PADRES E HIJOS EN LOS VALUES
def changeIndexFatherAndSons(dict, changeDict, tag):
    for x in dict.keys():
        elem = dict.get(x).get(tag)
        position = 0
        for i in elem:
            # aux=dict.get(x).get('hijos')[position]
            dict.get(x).get(tag)[position] = changeDict.get(i)
            position = position + 1


## FUINCION CREAR EL DIRECTORIO CON LOS INDICES MAPEADOS
def createCombi(df):
    import pandas as pd
    serie_pixeles = df.loc[:, 'index']  ##SE CONSTRUYE DICTIONARY CON LOS NUEVOS INDICES PARA PADRES E HIJOS
    combi = pd.Series.to_dict(serie_pixeles)
    combi = exchangeKeyAndValues(combi)
    return combi


## FUNCION PARA CAMBIAR KEYS POR VALUES EN UN DICT
def exchangeKeyAndValues(dict):
    out = {}
    for x in dict.keys():
        v = dict.get(x)
        out[v] = x
    return out


## LISTA DONDE NO HAY TAG
def noTagInDict(dict,tag):
    listNotTag = []
    for x in dict.keys():
        if tag not in dict.get(x):
            listNotTag.append(x)
    return listNotTag


## FUNCION AREA
def dictDeep(dict):
    faltan = noTagInDict(dict,'Flag')
    maximos=[]
    deeps=[]
    acomulado=0
    while len(faltan) > 0:  ## Mientras queden nodos sin TAG
        aux = faltan[0]  ## Primero que falta
        ultimo = False
        maximos.append(aux)

        while not ultimo:  ## Mientras tenga padre //dict.get(aux).get('padre').__len__()>0  or
            acomulado += 1
            if dict.get(aux).get('padre').__len__() == 0:  ## Se comprueba si es el ultimo
                ultimo = True


            if 'Flag' not in dict.get(aux): ##  Si no existe el campo 'TAG' en el nodo
                dict.get(aux)['Flag'] = 'hecho'

            if dict.get(aux).get('padre').__len__() > 0: ## Si tiene padre se cambia de nodo
                aux = dict.get(aux).get('padre')[0]
            faltan = noTagInDict(dict,'Flag')
        deeps.append(acomulado)
        acomulado = 0
    return maximos,deeps

def changeIndexInKeys(dict,changeDict):
    aux={}
    for x in dict.keys():
        k=changeDict.get(x)
        aux2 = {}
        aux2['Area']=dict.get(x).split(',').__len__()
        aux[k]=aux2
    return aux
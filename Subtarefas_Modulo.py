import re
from geopy.geocoders import Nominatim

# Função que faz a busca de uma palavra dentro de uma string
def kmp(t, p):
    next = [0]
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[j] != p[i]:
            j = next[j - 1]
        if p[j] == p[i]:
            j += 1
        next.append(j)
    ans = []
    j = 0
    for i in range(len(t)):
        while j > 0 and t[i] != p[j]:
            j = next[j - 1]
        if t[i] == p[j]:
            j += 1
        if j == len(p):
            ans.append(i - (j - 1))
            j = next[j - 1]
    return ans

# Função que a partir dos dados de longitude e latitude busca a localização do post caso esteja disponivel
def localiza(lat, long):
	geolocator = Nominatim(user_agent="CDA UFMG")
	loc = str(lat)+", "+str(long)
	location = geolocator.reverse(loc)
	dados = []
	if "state" in location.raw["address"].keys():
		dados.append(location.raw["address"]["state"])
	else:
		dados.append("None")
	if "city" in location.raw["address"].keys():
		cidade = str(location.raw["address"]["city"])
		dados.append(cidade)
		cidade = cidade.replace(" ", "").replace("á", "a").replace("ã", "a").replace("â", "a").replace("é", "e").replace("ê", "e").replace("î", "i").replace("í", "i").replace("õ", "o").replace("ô", "o").replace("ó", "o")
		f = open("cidades.txt", "r")
		if kmp(f.readline(),cidade.lower()) != []:
			dados.append(True)
		else:
			dados.append(False)
	else:
		dados.append("None")
		dados.append("None")
	if "region" in location.raw["address"].keys():
		dados.append(location.raw["address"]["region"])
	else:
		dados.append("None")
	return dados




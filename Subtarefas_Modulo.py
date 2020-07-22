import re
from geopy.geocoders import Nominatim

def kmp(t, p):
    """return all matching positions of p in t"""
    next = [0]
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[j] != p[i]:
            j = next[j - 1]
        if p[j] == p[i]:
            j += 1
        next.append(j)
	# the search part and build part is almost identical.
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
        dados.append(location.raw["address"]["city"])
    else:
        dados.append("None")
    if "region" in location.raw["address"].keys():
        dados.append(location.raw["address"]["region"])
    else:
        dados.append("None")
    return dados




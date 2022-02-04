# %% [markdown]
# # Dictionaries
# Dictionaries, eller også populært kalt Map siden det dreier seg om å mapping fra en nøkkel (key) til en verdi (value), er den siste "collection" typen vi skal snakke om.
# 
# Strukturen ser slik ut:
# {
#     nøkkel_1 : verdi_1
#     nøkkel_2 : verdi_2
#     .
#     .
#     .
#     nøkkel_N : verdi_N
# }
# 
# ![DICTIONARY](dictionary.png)
# 
# 
# Nøklene må selvfølgelig være unike, derfor har denne typen et visst slektskap med set. Verdiene derimot trenger ikke å være det.
# 
# Nøklene må være unmutable (uforanderlig, dvs. ikke ting som set eller lister), mens verdiene kan være hva som helst

# %%

d1 = dict()  # Tomt dictionary, kan også skrive d1 = {}
d2 = {1: "Hei", 3: "Hallo", "fint" : "flott", 1.2 : (1,2)}

# Fra python doc:
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)

a == b == c == d == e == f  # Returnerer true siden det er samme innhold, men initialisert på forskjellige måter.

# Referering til verdi
d2["fint"] # Refererer til "flott", tar altså ut innholdet som strengen "fint" peker på, og henter ut strengen "flott"

# Kan være nye dictionaries (eller andre )
d3 = {"Nøkkel til en dict": d2, "En annen nøkkel" : "En annen verdi"}

print (d3["Nøkkel til en dict"])
try :
    d4 = {d2: "Hmm, sært"}  # Funker ikke siden d2 er av en mutable type. 
except TypeError as ex :
    print(ex.args[0])

# Legge til items
a['four'] = 4

# Sletting av items:
del d2[1]  # nøkkel er 1
d2.pop("fint")  # nøkkel er "fint"

# Vi kan få tak i items, keys og values separat, og bruke disse til å iterere over.
print(d2.items())
print(d2.keys())
# Loops
for key in d2.keys():
    print(d2[key])

# Ekvivalent kode:
for key in d2 :
    print(d2[key])

# Og man vil kunne hente ut alle verdiene direkte 
for value in d2.values() :
    print(value)

# Andre nyttige metoder
existence = 1 in d2 # Tester om 1 er en nøkkel i d2
d2.popitem() # Sletter siste item lagt inn
c.clear()  # Sletter alle items



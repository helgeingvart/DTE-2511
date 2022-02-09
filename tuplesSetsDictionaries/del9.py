# %% [markdown]
# # Litt om kopiering
# 
# I en programmeringsverden ønsker man ofte å gjøre en kopi fra en "instans" av en klasse/liste/dictionary/etc til noe annet, og derfra kanskje endre på denne kopien. Da er det viktig å legge merke til forskjellen mellom assignment, shallow copy og deep copy. Nedenfor vises et bilde som illustrerer dette:
# 
# <img src="../resources/img/deep_vs_shallow_copy.png" width=500 />
# 
# Her ser vi en liste som inneholder nøstede elementer (en streng og et tall). Vi ser at assignment peker på samme objekt, en shallow copy 
# tar en unik kopi på første nivå (altså elementene i lista får NYE addresser) men ikke på nøstede nivåer (elementenes innhold i kopi peker på samme 
# streng/tall som orginalen). I en deep copy endres imidlertid alle referanser og gis nye plasser i minnet.

# %%
# Først se på helt enkel assignment

orig = 3
cpy = orig  # Egentlig ikke en kopi, samme primitiv!
print("Same ref? ", id(cpy) == id(orig)) # Referansen er den samme...

# Ikke problem for unmutable stuff, siden en ny assignment vil lage en referanse
cpy = 5
print("Same ref? ", id(cpy) == id(orig)) # Referansen er ikke lengre den samme :-)
print(orig, cpy)

# Hva nå med en liste?
orig = [1, 2, 3, 4]
cpy = orig
cpy[1] = 100
print(orig)
print(cpy)   # Begge fikk tallet 100 i pos 1 siden...
print("Same ref on top level?", id(cpy) == id(orig))

# Vi kan gjøre en shallow cpy på forskjellige måter
import copy
cpy = copy.copy(orig)
cpy = orig.copy()
cpy = list(orig)
cpy[:] = orig[:]
print("Same ref on top level?", id(cpy) == id(orig))  # Ikke samme ID lengre
orig[1] = 2  # Setter orginalen tilbake
print(orig)
print(cpy)

# Hva med elementene etter shallow cpy?
print("Same ref on element level?", id(cpy[1]) == id(orig[1]))  # Nei, iallefall ikke når elementet er endret.

# Så ser vi på en nøstet struktur
orig = [[1,2],
        [3,4]]

cpy = orig.copy()
cpy[0] = [5,6]
print(orig)
print(cpy)  # Går bra å endre på ting på nivå 1

cpy = orig.copy()
cpy[0][0] = 100  # Endring på nøstet nivå
print(orig)
print(cpy)  # Men der skjærer det seg! Kliss like!

# For å fikse må vi kjøre deep copy!
cpy = copy.deepcopy(orig)
cpy[0][0] = 200  # Endring på nøstet nivå
print(orig)
print(cpy)  # YESS! Orig forskjellig fra cpy!

# %% [markdown]
# # Noen klasser fra collections i python som kan være nyttig å kjenne til
# 
# Python tilbyr en collection modul som har en del nyttige klasser som utvider funksjonaliteten til de vanlige "kontainer"-klassene som vi har sett på (dict/set/tuple/list)
# 
# Vi skal se på disse tre: Counter, namedtuple og defaultdict
# 

# %% [markdown]
# ## Counter:
# Dict subklasse som teller "hashable" nøkler i input. På den måten en slags blending med set.

# %%
from collections import Counter

s = "aabbbbccccccccddddd"
counter = Counter(s)
print(counter.items())
counter.most_common()  # Sortert liste over (key,value) pairs
print(list(counter.elements()))   # Alle elementene som Counter ble initialisert med

# Kan også initaliseres fra en liste
c = Counter(['eggs', 'ham', 'eggs'])
c['bacon']
print(c)


# %% [markdown]
# ## namedtuple
# En mulighet for å kreere klasser basert på tupler i argumentet, og samtidig gi mening til hver posisjon

# %%
from collections import namedtuple

Point = namedtuple('Point', 'x,y,z')
Employee = namedtuple('Employee','name,age,personal_num,address')
employee = Employee("Helge Fredriksen", 52, 110969,"Hyttebakken 31")
pt = Point(1,1,1)
print (pt)

# %% [markdown]
# ## defaultdict 
# Subklasse av dict som gir deg en default-verdi ut om du spør på nøkler som ikke finnes

# %%
from collections import defaultdict

# Initialiser defaultdict med en type
d = defaultdict(int)
d['blue'] = 1
d['yellow'] = 2
print(d['green'])  # Returnerer 0 som er defaultverdi til til en int. Vi slipper at det blir en exception

# Her er en smart måte å gruppere en sekvens av (key,value) par til en dictionary der forekomsten av like nøkler 
# i sekvensen blir håndtert ved å legge til verdiene i en liste for hver unike nøkkel (fra python doc)
d = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
for key, value in s :
    d[key].append(value)

print(d)

# %% [markdown]
# ## Oppgave
# Finn forekomsten av forskjellige bokstaver i en fil ved å bruke Counter klassen. Eventuelt finn antallet av forskjellige nøkkelord i en python fil.

# %%




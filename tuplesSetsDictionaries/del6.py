# %% [markdown]
# # Tuples and sets
# Typen `tuple` ligner på `list` typen, men er uforanderlig. Dvs. har du først laget en `tuple`, så kan du ikke legge til/fjerne elementer. Innholdet i en tuple deklareres gjerne mellom to vanlige paranteser (), eventuelt uten noe som helst, bare ',' i mellom elementene.

# %%
t1 = tuple([1, 2, 3, 4])
t5 = tuple("aldkøadøfa")
t2 = ("Yalla", "jolle", (1,2,3))
t3 = (1,2,3), 'i', '123'
# t1.append(3)  # Kan ikke legge til

# Indexering og slicing fungerer akkurat som tidligere
forsteElement = t3[0]
resten = t3[1:] 

#Iterering over en tuple fungerer akkurat som før
for bokstav in t5 :
    print(bokstav, end=' ')


# %% [markdown]
# Hvorfor bruker vi ikke bare lister da?
# 1. Beskyttelse mot endring der vi ikke ønsker den muligheten
# 2. Det går opp mot 1000 ganger raksere å operere på tupler enn lister.
# 3. Veldig mye brukt type i python
# 
# # Sets
# Sets er en tredje "collection" i python som kun inneholder unike elementer. Man kan f.eks ikke ha bokstaven s med mer enn en gang i et set. 
# 
# **NB: Elementene vil nødvendigvis ikke ligge i den rekkefølgen som de ble puttet inn i settet med når du aksesserer det...**

# %%
s1 = set('foo')  # Her initialiseres set med elementene 'f' 'o' og så blir den andre 'o' ignorert...
s2 = set([1,2,3,4,1,2])  # Tallene 1 og 2 ignoreres ved siste "occurance"

s1.add('bar') # Her betraktes 'bar' som et helt element, splittes ikke opp i karakterer
# s2.remove(5) # Går ikke, siden 5 ikke er i settet
s2.discard(5) # Går videre uten exception

# s3 = {1, [1,2,3], ('foo', 'bar')}  # Hva skjedde her? Jo, et set kan ikke ha elementer som er "mutable". Den midterste listen er det...

s3 = {1, ('foo', 'bar')} # En tuple er som kjent ikke mulig å endre (unmutable), så den lar seg inkludere.

1 in s3  # Jupp
'foo' in s3 # Nope, siden 'foo' må være pakket inn i en tuple
# Vi kan også bruke metoder som len(), max(), min() og sum() på set slik som for lister og tupler

max(s2)

# %% [markdown]
# ## Metoder for å se på forskjeller mellom set, og ekstrahere ut forskjellige subset basert på ulikhetene mellom disse
# 
# Man metoder for å finne snitt/union/forskjell mellom to sett på samme måte som for matematiske mengder. Illustrasjon på tavla følger..
# 
# La oss lage noen eksempler, og gå gjennom alle variantene
# 
# ## Union
# En union kombinerer alt som er i begge settene

# %%
s1 = {1,2,3}
s2 = {3,4,5}
s1 | s2 
s1.union(s2) # Dette vil bli {1,2,3,4,5}


# %% [markdown]
# ## Snitt
# Et snitt inneholder de elementene som er felles mellom de to settene

# %%
s1 & s2
s1.intersection(s2)   # Dette vil bli {3}

# %% [markdown]
# # Subsett
# Operatorene < > <= >= kan også brukes i tillegg til == selvfølgelig. 
# Om man ikke vil bruke operatorene, kan metodene issuperset() issubset()

# %%
s1 = {1,2,3}
s2 = {1,2,3}

print(s1 == s2) # Ok selvfølgelig
print(s1 <= s2) # OK siden s1 == s2
print(s1 < s2)  # Ikke OK Alle elementene i s1 må være i s2 og det må være minst ett mer i s2 (proper subset)

s2 = {1,2}
print(s2.issubset(s1)) # samme som <=

# %% [markdown]
# # Differanse 
# s1 - s2 vil gi deg de elementene som er i s1 men som ikke er med i s2.
# s1 + s2 vil bli som union av s1 og s2 (siden snittet uansett bare vil bli med en gang pga. unikhets-regelen)

# %%
s1 = {"Hei", "Hå", "Blå", "Rød"}
s2 = {"Blå", "Rød", "Grønn"}

s1 - s2  # Vil inneholde {"Hei", "Hå"}
s2 - s1  # Vil inneholde {"Grønn"}

# %% [markdown]
# # Symmetrisk differanse, eller "XOR", exclusive or.
# Bruker ^ operatoren eller symmetric_difference() metoden for dette. Gir deg unionen mellom to sett s1 og s2, men tar vekk de elementene som er i begge. Kan dere uttrykke dette med de operatorene vi allerede har lært?

# %%
print(s1 ^ s2)
s1.symmetric_difference(s2)
sUnion = s1 | s2
print(sUnion)
sSnitt = s1 & s2
print(sSnitt)
print(sUnion - sSnitt)  # Vi tar vekk snittet fra unionen med andre ord, det vil bli det samme ;-)

# Men kunne vi ikke bare ha skrevet det slik?
s1 | s2 - s1 & s2   # NEI, siden vi har noe som kalles operator-presedens. - utføres først, deretter & og så |.
(s1 | s2) - (s1 & s2) # Paranteser rundt det vi vil ha utført først vil fikse problemet ;-)


# %% [markdown]
# # Eksempel på anvendelse
# Finne forekomsten av en viss type ord i en fil. La oss si at jeg ønsket å finne forekomsten av grafikk-relaterte tagger i en  web-addresse, slik som "canvas", "button", "dialog" etc.
# 
# PS: Siden jeg ikke er så befaren i web-prog, så ble nok dette et litt oppkonstruert eksempel :-/

# %%
import urllib

graphicsObjects = {"cavnas", "button", "dialog"} 

# url = "https://uit.no"
url = input("give me your url")
input = urllib.request.urlopen(url)
text = input.read().decode()
words = text.split(' ')
count = 0
for w in words :
    if w in graphicsObjects :
        count += 1

input.close()



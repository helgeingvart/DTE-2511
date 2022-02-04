# %% [markdown]
# # JSON
# 
# JSON står for Javascript Object Notation, og er et tekst-basert lagringsformat som er lett å lese/tolke både for mennesker og datamaskiner, uavhengig av språk eller platform.
# 
# Brukes nå av veldig mange selskaper/organisasjoner for å utveksle data, så det er essensielt (men også enkelt) å lære seg.
# 
# Elementene i en json-struktur kan være dictionaries eller lister på ytterste nivå. Inne i disse listene/dictionaries kan det så være lagret primitiver som tall, strenger og booleans, og/eller nye lister/dictionaries. Nøsting er således støttet på samme måte som i python selv.
# 
# Det er enklest å forstå strukturen ved å se på et eksempel, her eksempel.json
# 
# ## Eksempel på parsing av en json fil

# %%
import json

with open("eksempel.json") as file:
    eksempelData = json.load(file)

# Vi vet at det som kommer er en dictionary (men burde kanskje hatt en sjekk?)
fornavn = eksempelData["fornavn"]
etternavn = eksempelData["etternavn"]
addresse = eksempelData["adresse"] # Addresse feltet er et nytt dictionary...
gate = addresse["gateadresse"]
postnummer = addresse["postnummer"]
telefoner = eksempelData["telefonnumre"] # Dette vil være en liste, der hvert item er en dict
for telefon in telefoner :
    print(f"Fant telefon av typen: {telefon['type']} med nummer {telefon['nummer']}")

# Eksempelkode på parsing av fila:
# if (isinstance(eksempelData, dict)) :
#     for key in eksempelData:   # Nøkkel bør være en unmutable (streng eller tall)
#         value = eksempelData[key]
#         print (f"I {key} ligger noe av type: {type(value)}")

# elif (isinstance(eksempelData, list)) :
#     for item in eksempelData:
#         print(f"Dette liste-elementet er av type {type(item)}")


# %% [markdown]
# # Eksempel på skriving til json
# 
# Skriving til en json fil kan foregå som dette. Her har vi et eksempel på dumping av en liste som inneholder en dictionary.

# %%
myDict = {1: "one", 2: "two"}
myList = [1, 2, 3, myDict]
with open("jsonoutput.json", "w") as file:
    json.dump(myList, file)


# %% [markdown]
# # Objekt skriving/lesing
# 
# Objekter, eller instanser av klasser, som vi omgir oss med har sine interne datastrukturer. Disse kan vi ønske å serialisere/deserialisere for å sende over nett f.eks via json.
# 
# Dette må gjøres via egne encoder/decoder klasser i python
# 
# Ref: https://oxylabs.io/blog/python-parse-json
# 
# Det finnes også en mulighet for å gjøre dette automagisk vha. en modul som heter jsonpickle, som gjør livet like enkelt som med bruk av pickle. MEN: Da får man samme sikkerhets-risiko som med pickle ved at utilsiktet kode kan bli kjørt.
# 

# %%
class Country:
    def __init__(self, name, population, languages):
        self.name = name    
        self.population = population
        self.languages = languages

    
canada = Country("Canada", 37742154, ["English", "French"])

# print(json.dumps(canada)) Går ikke siden Country klassen ikke er "json serialiserbar"

# Må definere en klasse som arver fra JSONEncoder klassen for å håndtere dette eksplisitt
class CountryEncoder(json.JSONEncoder):
    def default(self, o): 
        if isinstance(o, Country):
           # JSON object would be a dictionary.
            return {
                "name" : o.name,
                "population": o.population,
                "languages": o.languages
                } 
        else:
            # Base class will raise the TypeError.
            return super().default(o)

jsonString = json.dumps(canada, cls=CountryEncoder)

# På samme måte må vi definere en decoder klasse om man ønsker å lese tilbake objektet:

class CountryDecoder(json.JSONDecoder) :
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, o):
        decoded_country =  Country(
            o.get('name'), 
            o.get('population'), 
            o.get('languages'),
        )
        return decoded_country

country_object = json.loads(jsonString, cls=CountryDecoder)
print(type(country_object))

country_object == canada  # Hmm, hvorfor ikke???



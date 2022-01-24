# %% [markdown]
# # Repetisjon 
# Kommer til å gå gjennom en del av de grunnleggende tingene fra "Grunnleggende programmering", kanskje ispedd noen oppgaver underveis for å komme igang litt igjen.
# 
# ## Struktur
# 1. Jeg viser litt om forskjellige konsepter i en jupyter code celle som jeg enten har lagt på forhånd, eller som jeg koder underveis
# 2. Jeg gir dere i oppgave å løse en oppgave, og deretter tilordner jeg dere til ulike "breakout" rooms i discord
# 3. Dere løser oppgaven i grupper, kanskje vha. peer programming? Dere finner en måte å gjøre dette på. Jeg beveger meg mellom rommene og kommenterer, ser på hva dere holder på med, gir hint hvis mulig.
# 4. Vi samles etter en angitt tid igjen i plenum og gruppene presenterer det de har gjort på en kortfattet måte til de andre i klassen
# 5. Jeg går videre til neste konsept og gjør en ny iterasjon i denne loopen

# %% [markdown]
# # Typer i python
# 
# Typene i python deles inn i primitiver, sett, sekvenser og ordlister. Selv om strenger er regnet for å være en primitiv, er den også en liste av karakterer som man kan iterere over, så denne er litt dualistisk i natur...

# %%
# Hjelpe-funksjoner
def printSekvens(sekvens):
    for s in sekvens:
        print(s)

def booleanFunksjon ( test: int ) :
    print(test)

# Primitiver
myStr: str = "Sånn passe flink lærer"
myInt: int = 123
myFloat: float = 123.12e10
myBool: bool = False

# Set
mySet: set = {1, "Flaske", 1.23, "Flaske"} # Kun unike innslag

# printSekvens(mySet)

# Sekvenser
myRange: range = range(11, 0, -2)
myList = [1, 2, 3]
myTuple = (1, [1,2,3], (1,2), "Hello") # Oppfører seg som statisk liste

# Ordbok
myDictionary: dict = {"Jenny" : 3, "Per" : 2, "Gunnar" : 5}
# printSekvens(myDictionary)

#Endring
myList.append("Nissen i berget")
myList.insert(2, "Tjo og hei")

# printSekvens(myList)

booleanFunksjon(myStr)



# %% [markdown]
# ## Kontrollflyt
# 
# Kontroll-flyt er en fellesbetegnelse for bruk av boolske uttrykk og if/else/elif for å kontrollere hvilken kode som kjører under gitte betingelser

# %%
# relasjonelle operatorer: <, >, ==, <=, >=, !=

# Initiering
b1 = bool(0)
b2 = bool(1)

# if/elif
x = 15
if x > 15 or x < 10 :
    y = 1
elif x > 5 :
    y = 2

# Conditional expressions
v = 1 if x > 0 else 2
number = 6
print("number is even" if number % 2 == 0 else "numer is odd" )


# %% [markdown]
# # Funksjoner og løkker. 
# 
# Her viser vi et eksempel på de to løkketypene "for" og "while". 
# 
# Funksjonen isPrime har vi laget for å gjøre koden mer lesbar i dette tilfellet.
# 
# Selve hovedkoden går gjennom alle tallene under en viss Range og sjekker for primtall. Prøv gjerne å sett denne høyere og sjekk hva som skjer ;-)

# %%
def isPrime( n ) :
    i = 2
    while ( i < n ) :
        if ( n % i == 0 ):
            return False
        i += 1
    return True

# Loops: Find all prime below Range
Range = 100
for i in range(1,Range+1) :
    if isPrime(i) :
        print("Found a prime. It was: " + str(i))





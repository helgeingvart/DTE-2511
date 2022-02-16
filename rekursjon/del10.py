# %% [markdown]
# # Rekursjon: Funksjoner som kaller på seg selv
# 
# Rekursive funksjoner ligner litt på loops, men der får fram den iterative prosessen ved å la funksjonen kalle på seg selv.
# Vi kan tenke på mange problemstillinger fra dagliglivet som kan formulerers rekursivt. F.eks. gange:
# 
# ```
# def gå_et_skritt:
#     hvis ikke framme:
#         gå_et_skritt()
#     ellers
#         return
# ```
# 
# Det enkleste for å illustrere konseptet programmeringsmessig er å begynne med et eksempel: En funksjon som skriver ut en stadig økende liste av påfølgende tall.

# %%
biggest_number = 10

def print_number(number) :
    if (number <= biggest_number) :
        print(number,end=" ")   # Vi skriver ut
        print_number(number+1)  # Vi kaller på oss selv med tallet, bare økt med 1
    else :
        return
    
print_number(1)

# %% [markdown]
# Vi kan se på et annet mer matnyttig eksempel: Regne ut n! som dere kjenner fra matematikken.
# 
# Dere vet også at $n! = n*(n-1)*(n-2)*....*2*1$
# 
# Dette kan enkelt løses med en for loop i python

# %%
n = input("Gi meg et positivt heltall")
produkt = 1
for i in range(int(n)) :
    produkt = produkt*i

print ("Svaret er ", produkt)


# %% [markdown]
# MEN: Dette kan også løses på en annen måte, vha. rekursjon. La oss benytte oss av at vi kan omskrive fakultet som
# 
# 1. $n! = n*(n-1)!$
# 2. $(n-1)! = (n-1)*(n-2)!$
# 3. $(n-2)! = (n-2)*(n-3)!$
# osv.
# 
# Vi ser at vi har en rekursiv regel her, der beregning i øverste steg avhenger av samme beregningen i neste steg, som igjen avhenger av samme beregning i neste steg osv... Helt til man kommer ned til tallet 1 som er slutt-betingelsen. Hvordan kan vi implementere dette vha. rekursjon?

# %%
# Rekursjon starter med største tallet i produktet
def factorial(n) : 
    if (n > 0) :
        return n*factorial(n-1)
    else :
        return 1   

factorial(10)

# %% [markdown]
# Vi ser at vi MÅ ha en grein i kontrollflyten som stopper rekursjonen.
# * Kalles basis-operasjonen
#     * Grunnen til dette er at det er den enkleste varianten som kan bli spurt etter i kallet til den rekursive funksjonen
#     * Kalles også stopp-betingelsen eller "stopping condition"
# 
# Den andre greina tar seg av **sub-problemet**, der gjerne det rekursive kallet skjer.
# 
# ### Oppgaver til dere: 
# 1. Lag en rekursiv funksjon for å regne ut $2^n$ 
# 2. Lag en rekursiv funksjon for å regne ut summen av alle tallene fra 1 til n.

# %% [markdown]
# ## Case: Fibonacci tall
# Fibonacci sekvensen er en enkel rekursiv formel, eller differens-ligning, som har inspirert fagområder som arkitektur, biologi, geometri etc..
# Den kan enkelt defineres som $f_{n} = f_{n-1} + f_{n-2}$, der $f_1 = f_2 = 1$. Vi skal nå se på rekursjon for å regne ut disse tallene:
# 

# %%
def fib(n) : 
    if (n > 2) :
        return fib(n-1) + fib(n-2)
    elif (n == 2 or n == 1) :
        return 1

fib(4)

# %% [markdown]
# Selv om algoritmen blir svært elegant og lesbar er det som skjer bak kulissene nokså komplisert:
# 
# <img src="..\resources\img\fibonacci.png">
# 
# F.eks vil fib(10) kreve 177 rekursive kall, og fib(30) 2692537.... 
# * Betyr at det kan være kostbart ressursmessig å bruke rekursjon (minne/CPU-tid)
# * Kan være vanskelig å debugge
# Rekursjon må derfor brukes med varsomhet.
# 
# Sidenote: Credit til Christopher kjente til en mekanisme kalt funksjons-caching som kan brukes for å redusere antall like funksjonskall i en programkjøring vha. caching. Dette er spesielt nyttig i rekursiv sammenheng, og da spesielt når du har nøstede rekursjons-trær slik som vist i figur. Instrumentert kode for dette kan være som under:

# %%
from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n) : 
    if (n > 2) :
        return fib(n-1) + fib(n-2)
    elif (n == 2 or n == 1) :
        return 1

fib(100) 

# %% [markdown]
# Igjen en liten oppgave til dere. Oppgave 15.2.1 i boka (den nederste varianten). Hva er output av følgende rutine (gjøres uten å implementere)
# 
# ```
# def m(r) :
#     return r * m(r-1) if r > 2 else r
# 
# print (m(4))
# ```
# ## Case: Palindrom deteksjon
# Et palindrome er en tekst-streng som er symmetrisk, f.eks. "agnes i senga". Vi ønsker å lage en algoritme for å bestemme om teksten er et palindrom. Her kan vi benytte fleksibiliteten i python med å ta ut sub-strenger og behandle disse separat.
# 

# %%
def is_palindrome(streng) :
    if (len(streng) <= 1) :   # Basis tilfelle 1: Stopper dersom strengen er redusert til kun midterste karakter (odde antall) eller ingenting (partall)
        return True
    elif (streng[0] != streng[len(streng) - 1]) :  # Basis tilfelle: Asymmetri detektert. Stopper og returnerer.
        return False
    else:
        returnVal = is_palindrome(streng[1:len(streng)-1])
        return returnVal

print(is_palindrome("agnes i senga"))
print(is_palindrome("anna"))

# %% [markdown]
# ## Såkalte hjelpe-funksjoner i rekursive kall
# 
# Denne koden, selv om den er svært enkel i sin form, og derfor lett å forstå seg på, er ikke veldig effektiv pga. at den lager nye strenger
# for hvert kall som krever ny minne-allokering for hvert rekursive kall.
# Vi kan effekstivisere dette ved å legg inn posisjons-angivelser i strengen 

# %%
def is_palindrome_helper(streng, low, high) :
    if (high <= low) :
        return True
    elif streng[low] != streng[high] :
        return False
    else :
        return is_palindrome_helper(streng, low+1, high-1)

def is_palidrome_v2(streng) :
    returnVal = is_palindrome_helper(streng, 0, len(streng)-1)  # Angi laveste og høyeste posisjon.
    return returnVal

print(is_palidrome_v2("anna"))

# %% [markdown]
# # Case: Towers of Hanoi
# 
# La oss prøve å formulere dette som en algoritme.

# %%
def move_it(n, fra, til, hjelp) :
    if n == 1:
        print("Flytter skive 1 fra", fra, "til", til)
    else :
        move_it(n-1, fra, hjelp, til) 
        print("Flytter skive", n, "fra", fra, "til", til)
        move_it(n-1, hjelp, til, fra)

move_it(3, 'A', 'C', 'B')

# %% [markdown]
# ## Binært søk
# 
# Nytt case, søking i ordnet liste etter posisjon til et element. Vi opererer med variable posisjoner i lista, som angir søke-området. Søke-området innsnevres til høyre eller venstre for midterste posisjon til søke-området, avhengig av størrelsen på verdien det søkes etter.

# %%
def recursiveSearch(lst, value) :
    return recursiveSearchHelper(lst, value, 0, len(lst)-1)

def recursiveSearchHelper(liste, value, low, high) :
    
    if (high < low or low < 0 or high < 0 or low > len(liste) - 1 or high > len(liste) - 1) : # Sanity check: Vindus-pekere utenfor range på mulige liste-indexer
        return -1  # Algoritmen feilet, betyr at vi ikke fant verdien.
    elif liste[low] == value :
        return low # Fant verdi på laveste del av søke-vindu
    elif liste[high] == value :
        return high  # Fant verdi på høyeste del av søke-vindu
    
    mid = (low + high) // 2  # Midt posisjon, men rundet nedover.
    if (liste[mid] == value) :
        return mid    # Fant verdi på ny midt-posisjon.
    if (value < liste[mid]) :
        high = mid-1 # Jeg kan steppe meg et hakk lengre ned, siden jeg allerede har testet at verdien ikke ligger akkurat på midten
    elif (value > liste[mid]) :
        low = mid+1  # Samme her, jeg stepper meg ett hakker lengre opp, mid trengs ikke å tas med i søkevindu.
    val = recursiveSearchHelper(liste, value, low, high)
    return val

val = recursiveSearch([1,2,3,6,7,19,34], 6)
print (val)




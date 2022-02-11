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
    if (len(streng) <= 1) :
        print(streng)
        return True
    elif (streng[0] != streng[len(streng) - 1]) :
        return False
    else:
        is_palindrome(streng[1:len(streng)-1])

print(type(is_palindrome("agnes i senga")))



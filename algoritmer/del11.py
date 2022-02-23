# %% [markdown]
# # Effektivisering av algoritmer
# 
# Vi har sett på en rekursiv håndtering av binært søk. Kunne dette blitt gjort ved hjelp av en ren løkke for å spare "overhead" ved rekursjon? Svaret er ja

# %%
def binarySearch(liste, value):

    index = -1
    low = 0
    high = len(liste) - 1
    while (low <= high) :
        mid = (low + high) // 2  # Midt posisjon, men rundet nedover.
        if (liste[mid] == value) :
            index = mid # Fant verdi på ny midt-posisjon.
            break
        if (value < liste[mid]) :
            high = mid-1 # Jeg kan steppe meg et hakk lengre ned, siden jeg allerede har testet at verdien ikke ligger akkurat på midten
        elif (value > liste[mid]) :
            low = mid+1  # Samme her, jeg stepper meg ett hakker lengre opp, mid trengs ikke å tas med i søkevindu.
    
    return index

print( binarySearch([1,2,3,6,7,10,19,34], 34) )

# %% [markdown]
# Dette eksemplet viser at det er mange måter å løse en programmerings-oppgave på. En enda enklere måte å finne tallet i lista på ville være å gjøre det med et lineært søk slik som dette:

# %%
def linearSearch(liste, value) :
    index = -1
    for i in range(len(liste)) :
        if liste[i] == value:
            index = i
    return index

print (linearSearch([1,2,3,6,7,10,19,34], 6))

# %% [markdown]
# Veldig enkel kode, som til og med støtter ikke-ordnede lister. Så hvorfor ikke bare bruke en slik algoritme?
# 
# Dette skyldes antall operasjoner vi kan risikere å måtte utføre for å finne indeksen. Hvis tallet var plassert på slutten av lista, og lista var n lang, ville vi måtte utføre n sammenligninger.
# 
# Et binært søk vil utføre langt færre, faktisk log(n). Dette forstås gjennom å forestille oss at lista er n = 2^m lang. Vi halverer søkevindu hver gang, som betyr at vi kun utfører m operasjoner. Tar vi log på begge sider av ligninga over får vi m = 2 log (n).
# 
# En slik analyse av algoritmens tidsforbruk (som oftest måles i antall operasjoner), kan gjøres ved å se på orden. Da ser vi bort fra konstante faktorer i uttrykket, og ser bare på uttryket for n. I eksemplet over blir det $O(\log(n))$, mens for linært søk blir det $O(n)$.
# 
# La oss se på noen flere enkle eksempler

# %%
def linear(n) :
    sum = 0
    for i in range(n) :
        sum = sum + n 
    return sum

def quadratic(n) :
    sum = 0
    for i in range(n):
        for j in range(n) :
            sum = sum + i + j
    return sum

import time
def time_it(func, n) :
    start_time = time.time()
    func(n)
    end_time = time.time()
    print("It took",end_time - start_time,"with",n,"iterations on",func)

time_it(linear, 100000)
time_it(linear, 1000000)

time_it(quadratic, 1000)
time_it(quadratic, 10000)

# %% [markdown]
# Naturlig nok vil altså en indre løkke som gjøres n ganger for hver iterasjon som den ytre løkken gjør n ganger være av orden $O(n^2)$. Men hva om vi terminerer den indre løkken etter 20 iterasjoner? Anta tiden det tar for en operasjon er $T(1) = c$. Da kan vi lage regnskapet $T(n) = 20\cdot c\cdot n = O(n)$. Siden 20c bare er en skaleringsfaktor, sider vi at vi fortsatt har $O(n)$ operasjoner. Hva med følgende kode:

# %%
# Tilfelle 1
# n=100

for i in range(n) :
    k = k + 4

for i in range(n) :
    for j in range(20) :
        k = k + i + j

# Tilfelle 2
e = 10
liste = range(n)
if e in liste:
    # gjør noe
    pass
else:
    for e in liste:
        # Gjør noe annet
        pass

# %% [markdown]
# ### Diskusjon....

# %% [markdown]
# ## Analyse av rekursive algoriter: Case Towers of Hanoi
# 
# Denne var som følger
# 1. Flytt de første n-1 skivene fra A til C via B
# 2. Flytt skive n fra A til B
# 3. Flytt de andre n-1 skivene fra C til B via A
# 
# La oss anta at $T(n)$ angir tida det tar å flytte n skiver, og at T(1)=1
# 
# Da kan vi nøste oss fram til orden på følgende måte via n skiver: $T(n-1) + 1 + T(n-1) = 2T(n-1) + 1$. Vi vet også at $T(n-1) = 2T(n-2) + 1$. Ergo
# $T(n) = 2(2T(n-2) + 1) + 1 = 2(2(T(n-3) + 1) + 1) + 1 = ... = 2^{n-1}T(1) + 2^{n-2} + ... + 2 + 1 = (2^n -1) = O(2^n)$. Sistnevnte overgang kan vises vha. summeformelen av de n første leddene i en geometrisk rekke, her er k=1/2...
# 
# Samme type analyse kan gjøres for Fibonacci tall. 
# 
# ## Oppgave til forsamlingen: Forbedring av ytelse på fibonacci tall
# 
# Husk tilbake til rekursiv rutine for å finne fibonacci tall (NB: Her ser jeg bort fra f_0 = 0)

# %%
def fib(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fib(n-1) + fib(n-2)

fib(8)

# %% [markdown]
# Oppgave: Kan denne gjøres mer effektiv ved en loop?
# 

# %%
def fib_loop(n) :
    
    if (n == 0): return 0
    if (n == 1): return 1

    i = 1
    fn = 1
    fn_minus_1 = 0
    fn_minus_2 = 1
    while i <= n :
        fn = fn_minus_1 + fn_minus_2
        fn_minus_2 = fn_minus_1
        fn_minus_1 = fn
        i+=1

    return fn

fib_loop(6)

# %% [markdown]
# Og hva er orden av denne? Ser da vitterlig ut som $O(n)$ :-)
# 
# ## Selection sort
# 
# For å se på hvordan denne fungerer, se boka under kapittel 16.4.2. Algoritmen er laget på den måten at for hvert element i lista, så sammenlignes alle elementene framover i lista. Man ser etter det minste elementet blant de elementene som gjenstår i lista, og bytter dette elementet med dette. Om man ikke finner noe, så hopper man bare videre til neste.

# %%
def selectionSort(liste) :
    for i in range(len(liste)-1) :
        element = liste[i]
        minimumValue = min(liste[i+1:])
        minimumIndex = liste[i+1:].index(minimumValue) + i+1
        minimumElement = liste[minimumIndex]
        if minimumElement < element :
            liste[i] = minimumElement
            liste[minimumIndex] = element

liste = [-2, 4, 5, -1, 3, 5]
selectionSort(liste)
print(liste)

# %% [markdown]
# Hva er orden her? Lista er n lang. For hvert element i lista gjør man et søk som potensielt er n-1 langt. Antall sammenligninger kan røfli summeres til noe slikt som
# $ (n-1) + (n-2) + (n-3) + ... + 1$. Vi har en summeformel for dette. Dette er $\frac{n(n+1)}{2} - n = n^2/2 - n/2$. (-n på slutten der fordi vi startet i (n-1)). Altså $O(n^2)$
# 
# # Case study: Finne prim-tall. 
# Motivasjon: Det finnes en $150.000 pris for den som greier å finne et primtall som inneholder minst 100.000.000 siffer. (https://www.eff.org/awards/coop)
# Hvordan kan vi finne en raskest mulig algoritme for dette? 
# * Enkleste versjon: Gå gjennom alle tall opp til n og sjekk at de ikke er delelig med alle tall som er under n. Vi ser at dette er en $O(n^2)$ algoritme. Ikke særlig effektiv.
# * Andre versjon: Vi sjekker bare delelighet med odde-tall, siden alle par-tall er delelig med 2. Dessverre fortsatt $O(n^2)$.
# * Tredje versjon: Det kan vises at vi kun trenger å sjekke delelighet med tallene under $\sqrt{n}$. Dette minker kompleksiteten til $O(n\sqrt{n})$
# 
# 

# %%
from math import sqrt
def findPrimes(n) :
    primtall = []

    candidate = 2
    
    while (candidate < n) :

        isPrime = True    
        root = int(sqrt(candidate)) + 1  # Det at vi plusser på en er en avrunding oppover.

        for divisor in range(2, root):  # Sjekker i forhold til divisor på alle tall under rota av kandidaten
            if candidate % divisor == 0 :
                isPrime = False
                break
        if (isPrime) :
            primtall.append(candidate)

        candidate += 1
    
    return primtall

findPrimes(50)

# %% [markdown]
# Algoritmen er ikke så effektiv, siden vi må kvadratrota må regnes ut for hver kandidat. Legg merke til at ``int(sqrt(candidate))`` økes med 1 kun mellom kandidat-tall som er kvadratisk. Ellers er det samme heltallsverdi hele tiden. Dersom vi gjør det slik at denne økes kun når ``root*root >= candidate`` så sparer vi mye kvadratrot beregning.
# 
# I tillegg er det slik at vi egentlig kun trenger å sjekke på primtall når det gjelder mulige divisorer. Dette siden andre tall er sammensatt (er multiplisert sammen) av andre primtall som er mindre, og derfor allerede blir sjekket når man sjekker selve primtallene.
# 
# F.eks. vi trenger ikke sjekke om 13 er delelig med 6, siden vi allerede har sjekket om det er delelig med 3 og 2.
# 
# Ny forbedret algoritme ser vi under
# 

# %%
def findPrimes(n) :
    primtall = []

    candidate = 2
    root = 1
    while (candidate < n) :

        isPrime = True    
        if (candidate > root*root) :
            root += 1

        for divisor in primtall :
            if divisor <= root and candidate % divisor == 0:
                isPrime = False
                break   # Vi ser ikke på mulige divisorer større en rota
        if (isPrime) :
            primtall.append(candidate)

        candidate += 1
    
    return primtall

findPrimes(50)

# %% [markdown]
# Hvilken orden har denne rutina nå når vi bare sjekker mot tidligere detekterte primtall? Vel, da må vi anslå hvor mange primtall som er under et visst tall n. Det er mulig å vise via tallteori at dette vil være i størrelsesorden $n/log(n)$
# 
# Dette fører til at siden vi nå bare sjekker divisorer som bare er primtall + at vi begrenser oss oppad til $\sqrt{n}$, så vil det totalt sett være $O(n\sqrt{n}/log(n))$



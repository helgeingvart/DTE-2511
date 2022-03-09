# %% [markdown]
# # Sortering
# 
# Vi vil gå gjennom 5 forskjellige algoritmer for sortering (det eksisterer mange flere)
# * Insertion sort
# * Bubble sort
# * Merge sort
# * Quick sort
# * Heap sort
# 
# Det vil kun være tall som behandles, og disse vil være lagret i lister. Husk at vi allerede har vært gjennom en algoritme for sortering, selection sort. Denne fungerte ved at man for hvert element i lista lette etter et element i den gjenstående delen av lista som var mindre. Dersom så, ble disse byttet. Dette er den enkleste formen for sortering, men har $O(n^2)$ operasjoner, noe som gjør den nokså ineffektiv for store lister iallefall. La oss først se på insertion sort
# 
# ## Insertion sort
# Denne fungerer litt slik som selection sort, ved at man går gjennom hvert element suksessivt framover i lista. Når man møter på et element som ikke er større enn foregående element, sørger man for å flytte dette elementet til det stedet i lista der det "hører hjemme". For å gjøre dette trenger man en indre løkke som spinner seg bakover til man finner dette stedet, og suksessivt flytter om på de foregående elementene mens man leter seg igjennom.

# %%
def insertionSort(liste) :

    for i in range(1, len(liste)) :
        currentElement = liste[i]
            # Need to search and replace backwards in list
        k = i-1
        while k >= 0 and liste[k] > currentElement:
            liste[k+1] = liste[k]
            k -= 1
            
        liste[k+1] = currentElement

    return liste

liste = [1,2, 6, 9, 3, 2, 9,-1]
insertionSort(liste)

# %% [markdown]
# I verste fall vil denne også være av orden $O(n^2)$, siden man for hvert element kan risikere å måtte flytte currentElement helt bakerst.
# 
# ## Boble sortering
# Boble-sortering fungerer på litt samme måte som insertionsort, ved at man sammenligner to nabo-elementer og finner ut om rekkefølgen er riktig. MEN, i motsetning til insertionsort, flytter man bare element et hakk ved hjelp av bytting. Så gjør man suksessive nye scan gjennom lista helt til alle elementene er i riktig rekkefølge. Neste scan kan minskes til ett hakk mindre opp i lista, siden siste element vi "flyte" opp til rett plass i foregående scan.

# %%
def bubbleSort(liste) :
    
    k = len(liste)
    while k > 0 :
        for i in range(k-1) :
            if liste[i] > liste[i+1] :
            # Do the swapping
                liste[i], liste[i+1] = liste[i+1], liste[i]

        k-= 1

    return liste

liste = [1,2, 6, 9, 3, 2, 9]
bubbleSort(liste)


# %% [markdown]
# Observer at vi egentlig ikke trenger å kjøre neste scan dersom vi ikke har gjort noen bytte i forrige runde, da er jo lista allerede ferdig sortert. Vi tar vare på om dette er tilfelle i et `needNewScan` flag

# %%
def bubbleSort(liste) :
    
    k = len(liste)
    needNewScan = True
    while k > 0 and needNewScan:
        needNewScan = False
        for i in range(k-1) :
            if liste[i] > liste[i+1] :
                # Do the swapping
                liste[i], liste[i+1] = liste[i+1], liste[i]
                needNewScan = True
        k-= 1

    return liste

liste = [1,2, 6, 9, 3, 2, 9]
bubbleSort(liste)

# %% [markdown]
# ## Mergesort
# 
# Mergesort er en rekursiv sorteringsalgoritme. Den splitter opp listen som skal sorteres i to halvdeler, splitter hver av disse i to halvdeler, osv, helt til det bare er ett element igjen i hver subliste. Deretter flettes disse sammen suksessivt mens man sammenligner elementer i hver av listene og sørger for at de kommer på rett plass slik det vises i figuren under hentet fra Liang:
# 
# ![](../resources/img/merge-sort.png)
# 
# (Ta også en titt på figur/animasjon 17.5 i Liang)

# %%
def merge_sort(liste) :
    if len(liste) > 1 :
        # Split list in two
        first_half = liste[:len(liste)//2]
        second_half = liste[len(liste)//2:]
        
        merge_sort(first_half)
        merge_sort(second_half)

        merge(first_half, second_half, liste)

    return liste

def merge(first, second, target) :

    current1 = 0
    current2 = 0
    current3 = 0
    while current3 < len(target) :

        if first[current1] < second[current2] :
            target[current3] = first[current1]
            current1 += 1
        else :
            target[current3] = second[current2]
            current2 += 1
        current3 += 1

        # No more items in one of the halves to compare with, need to break out of this logic
        if current2 == len(second) or current1 == len(first) :
            break

    # If there are items left in first, that means second is empty. Flush the rest of first into target
    while current1 < len(first) :
        target[current3] = first[current1]
        current3 += 1
        current1 += 1

    # OR: If there are items left in second, that means first is empty. Flush the rest of second into target
    while current2 < len(second) :
        target[current3] = second[current2]
        current3 += 1
        current2 += 1

    return target


liste = [1,-1,4,5,-2,3,9,1,-7,4,8,-2]
merge_sort(liste)

# %% [markdown]
# Denne rutina vil bruke i orden $O(n\log{n})$ operasjoner, og er derfor mer effektiv enn de vi har vært gjennom til nå.
# 
# ## Quicksort
# 
# Quicksort er vel regnet for å være state-of-the-art når det gjelder effektivitet. Den fungerer også rekursivt, men isteden for å dele opp i halvdeler, så deler den array opp rundt et "pivot" point. Pivot betyr vippe-punkt, og brukes til å avgjøre hva som er mindre enn og større enn i en sorterings-sammenheng.
# 
# Vis 

# %%
def quicksort(liste) :
    return quicksort_helper(liste, 0, len(liste)-1)

def quicksort_helper(liste, left, right) :

    if left >= right :
        return liste

    pivotValue = liste[(right + left)//2]
    partitionIndex = partition(liste, left, right, pivotValue)
    quicksort_helper(liste, left, partitionIndex-1)
    quicksort_helper(liste, partitionIndex, right)

    return liste

def partition(liste, left, right, pivot) :

    while right >= left :
        # Find first postion in list from the left that has a element higher than pivot
        while liste[left] < pivot:
            left += 1

        # Find first postion in list from the right that has a element lower than pivot
        while liste[right] > pivot:
            right -= 1

        if right >= left :  # swap elements
            liste[left], liste[right] = liste[right], liste[left]
            left += 1
            right -= 1

    return left

liste = [1,-1,4,5,-2,3,9,1,-7,4,8,-2]
quicksort(liste)








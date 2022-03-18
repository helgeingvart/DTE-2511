# %% [markdown]
# # Heap: Et binært tre
# 
# Se egen presentasjon. 
# 
# La oss nå se på en klasse som lagrer heap-elementene i en liste (kunne valgt en annen struktur også...) 

# %%
class Heap :

    def __init__(self) :
        self.__liste = []

    def add(self, element) :
        self.__liste.append(element)
        current = len(self.__liste) - 1
        parent = (current-1)//2
        if (len(self.__liste) == 1): return
        while self.__liste[current] > self.__liste[parent] :
            self.__liste[current], self.__liste[parent] = self.__liste[parent], self.__liste[current] # Swap
            current = parent
            parent = (current-1)//2
            if parent < 0 : break

    def remove_root(self) :
        if (len(self.__liste) == 0):  return None  # Nothing to remove

        removedItem = self.__liste[0]  # Remove the last in the list
        lastItem = self.__liste.pop()  # Last item will be the new root
        if len(self.__liste) == 0 : return lastItem   # After popping, the list became empty, so we just return that one.
        self.__liste[0] = lastItem
        current = 0

        while (current < len(self.__liste)) : 
            leftChild = 2*current + 1
            rightChild = 2*current + 2
            if leftChild >= len(self.__liste) : # There is no children
                break  # We are done
            
            leftWillSwap = False
            willSwap = False
            if rightChild == len(self.__liste) : # There is only the left child, since the rightChild is out of bounds
                if self.__liste[current] < self.__liste[leftChild] :
                    leftWillSwap = True
                    willSwap = True
            else :
                if self.__liste[leftChild] > self.__liste[current] :
                    leftWillSwap = True
                    willSwap = True
                    if self.__liste[rightChild] > self.__liste[leftChild] :
                        leftWillSwap = False
            
            if willSwap :
                index = leftChild if leftWillSwap else rightChild
                self.__liste[current], self.__liste[index] = self.__liste[index], self.__liste[current] # Swap
                current = index
            else :
                break

        return removedItem

    def getSize(self) :
        return len(self.__liste)

    def print(self) :
        print(self.__liste)


# %% [markdown]
# Nå har vi klassen klar for å manipulere heap etter oppskriften vår. Denne kan nå brukes for å sortere på en veldig enkel måte. Listen vi har kan første legges inn i heap, og deretter plukkes ut av heap igjen. Den vil da automatisk bli sortert i riktig rekkefølge.

# %%
def heapsort(liste) :
    heap = Heap()
    for item in liste :
        heap.add(item)

    heap.print()

    for i in range(len(liste)-1,-1,-1) :
        liste[i] = heap.remove_root()
    
    return liste
    
liste = [0,5,2,4,9]
heapsort(liste)



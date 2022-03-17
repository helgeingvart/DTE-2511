# %% [markdown]
# # Lister
# 
# En liste er en datastruktur for å lagre objekter i en sekvens, og vi har til nå sett på den innebygde container-typen `list` i python. 
# Vi skal nå lage vår egen versjon av en liste, der et element i listen er en node som linker til neste node i sekvensen, fra "Head" til "Tail". Operasjoner som skal støttes er
# * Legge inn nytt element
# * Ta vekk element
# * Hente ut verdien i et element vha. indeks
# * Finne størrelsen til lista, inkludert om den er tom
# * Finne ut om et element er i lista
# 
# Vi implementerer en node på følgende måte:

# %%
class Node :
    def __init__(self, e) :
        self.element = e
        self.next = None


# %% [markdown]
# En liste av disse nodene vil da enkelt og greit henge sammen på denne måten:
# 
# ![](../resources/img/LinkedList.png)

# %%
class Linked_list :
    def __init__(self) :   # Empty list
        self.__head = None
        self.__tail = None
        self.__length = 0

    def add_first(self, element) :
        node = Node(element)
        if self.__head == None :   # If this is the first node
            self.__head = self.__tail = node
        else :
            current = self.__head
            node.next = current
            self.__head = node
        self.__length += 1

    def add_last(self, element) :
        node = Node(element)
        if self.__head == None :   # If this is the first node
            self.__head = self.__tail = node
        else :
            current = self.__tail
            current.next = node
            self.__tail = node
        self.__length += 1

    def insert(self, index, element) :
        
        if index > self.__length or index < 0:
            raise RuntimeError("Out of bounds, current length is", self.__length, ", tried to insert at index", index)

        # Check if the list is empty:
        if self.__length == 0 or index == 0 :
            self.add_first(element)
        elif (index == self.__length) :
            self.add_last(element)
        else :
            new_node = Node(element)
            current = self.__head
            for i in range(index-1) :
                current = current.next
            
            # Now, insert the node after current
            next = current.next # Temporary store the next element that will come after new_node
            current.next = new_node
            new_node.next = next # Continue chain

        self.__length += 1

    def remove_first(self) :
        if self.__length == 0 :
            return None
        current = self.__head
        self.__head = self.__head.next
        if  self.__head == None : # We have now an empty list   
            self.__tail = None  # Need to set tail to None too

        self.__length -= 1
        current.next = None  # IMPORTANT: Reset the pointer to next, or we will get a memory leak!
        return current.element

    def remove_last(self) :
        if self.__length == 0 :
            return None
        elif self.__length == 1 :
            toRemove = self.__tail
            self.__tail = self.__head = None
            self.__length -= 1
            return toRemove.element
        
        toRemove = self.__tail
        current = self.__head
        for i in range(self.__length - 2) : # Take node second to last and assign as new tail
            current = current.next
        self.__tail = current

        self.__length -= 1
        toRemove.next = None
        return toRemove.element

    def clear(self) :
        self.__head = self.__tail = None
        self.__length = 0
    
    def remove_at(self, index) :
        if index >= self.__length or index < 0:
            raise RuntimeError("Out of bounds, current length is", self.__length, ", tried to insert at index", index)

        if index == 0 :
            return self.remove_first()
        elif index == self.__length-1 :
            return self.remove_last()
        else :
            previous = self.__head
            for i in range(index-1) :
                previous = previous.next
        
        current = previous.next   # Temporary store the next element
        if current == None : # We are at the end...
            self.__tail = previous
            previous.next = None
        else :
            previous.next = current.next   # This will release current.

        self.__length -= 1
        current.next = None # Important: Reset pointer to next so current can be garbage collected. If there is a dangeling reference here it will not happen.


    def __str__(self) :
        streng = "["
        current = self.__head
        while current != None :
            streng += current.element
            current = current.next
            if current != None :
                streng += ", "
            else :
                streng += "]"
            
        return streng
    
    @property
    def size(self) :
        return self.__length

liste = Linked_list()
liste.add_last("Helge")
liste.add_last("Fred")
liste.add_first("Risvoll")
liste.add_first("Hilde")
liste.insert(0, "Jumbo")
liste.remove_at(4)
print(liste)



# %% [markdown]
# ## Variasjoner over lenket liste
# 
# ![](../resources/img/variasjoner%20lenket%20liste.png)

# %% [markdown]
# 
# ## Arrays vs. lists
# 
# En liten merknad når det gjelder allokering: Kanskje tror man at den interne datatypen `list` er representert av en kontinuerlig sekvens i minnet på datamaskinen, men dette er ikke tilfellet (i likhet med Linked_list som vi nettopp implementerte)
# 
# ![](../resources/img/List_memory.png).
# 
# Dette vil medføre at selv om fleksibiliteten er veldig god, så vil det være mye overhead forbundet med å allokere/deallokere temporært minne når nye elementer legges til/fjernes siden minnet er så fragmentert.
# 
# Det finnes andre måter å lagre data i en sekvens i python som er mer effektive mhp. minne. Har man store data-mengder man vil lagre i en liste, der data-typen ikke er forskjellig over elementene, kan det lønne seg å se på typen `array` fra pakken `array`. For numeriske beregninger (som f.eks. i maskinlæring) brukes en annen versjon som heter `ndarray` i pakken `numpy` som ligner noe på array, men som er mer fleksibel mhp. operasjoner som kan gjøres globalt på alt innhold i arrayen i et statement. Under demonstreres litt angående tidsbruken når det gjelder numeriske operasjoner på de to liste typene:

# %%
# How to initialize the array type

from array import array
arr = array('i',[3, 6, 9, 12])

import time
import numpy as np

list_array1 = [i for i in range(1000000)]
list_array2 = [i for i in range(1000000)]

start_time = time.time()
list_multiply = [list_array1[i] * list_array2[i] for i in range(1000000)]
final_time = time.time()

print("Time taken by Lists to perform multiplication: ",
      (round((final_time - start_time), 2)), "millisecond")

arr1 = array('i', list_array1)
arr2 = array('i', list_array2)

start_time = time.time()
arr_multiply = [arr1[i] * arr2[i] for i in range(1000000)]
final_time = time.time()
print("Time taken by array to perform multiplication: ",
      (round((final_time - start_time), 2)), "millisecond")


numpy_array1 = np.arange(1000000)
numpy_array2 = np.arange(1000000)

start_time = time.time()
numpy_multiply = numpy_array1 * numpy_array2
final_time = time.time()

print("Time taken by Lists to perform multiplication: ",
      (round((final_time - start_time), 5)), "millisecond")


# %% [markdown]
# Vi ser at tiden de tar for en numpy liste multiplikasjon er i størrelsesorden 100 ganger kjappere enn for vanlige lister.



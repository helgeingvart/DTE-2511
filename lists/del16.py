# %% [markdown]
# # Forskjellige anvendelser av lister
# 
# Vi ser først på hvordan en Heap kan anvendes til å lage en prioritets-kø (Heap klassen fra del14 er tatt med igjen for info/import).

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


# %%
class Stack :
    def __init__(self) :
        self.__liste = []

    def push(self, element) :
        self.__liste.append(element)

    def pop(self) :
        return self.__liste.pop()

    def peek(self) :
        return self.__liste[-1]

    def size(self) :
        return len(self.__liste)

class PriorityQueue :
    def __init__(self) :
        self.__heap = Heap()

    def enqueue(self, element) :
        self.__heap.add(element)

    def dequeue(self) :
        if self.__heap.getSize() == 0 :
            return None
        return self.__heap.remove_root()

    def get_size(self) :
        return self.__heap.getSize()

# Eksempel med prioritert rekkefølge på pasienter (ja, tallet først i hvert liste-item er det som faktisk blir brukt av Heap for sortering)

patient1 = [2, "Ashley"]
patient2 = [1, "Emilia"]
patient3 = [5, "Bakary"]
patient4 = [7, "Abbi"]

priorityQueue = PriorityQueue() # Create a PriorityQueue
priorityQueue.enqueue(patient1)
priorityQueue.enqueue(patient2)
priorityQueue.enqueue(patient3)
priorityQueue.enqueue(patient4)
    
while priorityQueue.get_size() > 0:
    print(priorityQueue.dequeue(), end = " ")

# %% [markdown]
# Under har vi en helt enkel implementasjon av post-fix evaluering av aritmetiske uttrykk. For å gjøre det enkelt har vi bare gjort det slik at for å stoppe eksekveringen, så er det bare å gi en feil input-streng.

# %%
stack = Stack()

while True :
    num = input("Operand please: [1-9]")
    try :
        a = int(num)
    except:
        print("Not a valid input: ", num, ", should be a number")
        break

    stack.push(a)
    if stack.size() == 1 : # Should happen only in the beginning
        num = int(input("Operand please: [1-9]"))
        try :
            b = int(num)
        except:
            print("Not a valid input: ", num, ", should be a number")
            break
        stack.push(b)
    oper = input("Operator [+, -, * or /]: ")
    if (oper == '+') :
        result = stack.pop() + stack.pop()
        print(result, flush=True)
        stack.push(result)
    elif (oper == '-') :
        num2 = stack.pop()  # They will appear in reverse order compared to what order the operation is wanted
        num1 = stack.pop()
        result = num2 - num1
        print(result, flush=True)
        stack.push(result)
    elif (oper == '*') :
        result = stack.pop() * stack.pop()
        print(result, flush=True)
        stack.push(result)
    elif (oper == '/') :
        num2 = stack.pop()  # They will appear in reverse order compared to what order the operation is wanted
        num1 = stack.pop()
        result = num1 / num2
        print(result, flush=True)
        stack.push(result)
    else :
        print("Wrong operand", oper)
        break




# %% [markdown]
# # Exception handling
# 
# Handler om å håndtere feilsituasjoner på en strukturert måte. Det kan kastes exception og fanges exception. Når noe eksepsjonelt skjer, så må man i egen kode avbryte eksekveringen i det scopet der man er, og hoppe ut i et annet scope.

# %%
import urllib.request
from urllib.error import *

try:
    url = "https://uit.no"
    input = urllib.request.urlopen(url)
    text = input.read().decode()
    lines = text.split('\n')
    for line in lines :
        f = float(line)


except URLError as ex:
    print("Caught exception: " + ex.reason)

except BaseException as ex:
    print("Caught unknown exception: " + str(ex.args[0]))

except:
    pass

else:
    print("No exception happened!")
    
finally:
    print("Dette kjører alltid!")
    input.close()

    

# %% [markdown]
# # Eksempel på klasse med 'exception' håndering
# 
# Vi skal her skrive en klasse som representer et andregradspolynom og der vi kan finne røttene til dette.
# I tillegg ønsker vi å lage en egen exception klasse som "enkapsulerer" alt av feil som kan oppstå i denne klassen

# %%
class PolynomialSolverException(Exception) :
    def __init__(self, message) :
        super().__init__()
        self.message = message

from math import sqrt

class SecondOrderPolynomal :
    def __init__(self, *args) :
        for arg in args :
            if not isinstance(arg,(int, float)) :
                raise PolynomialSolverException("You tried to construct a polynomial with non-numeric coeffisients")
        self.__a, self.__b, self.__c = args[0], args[1], args[2]

    def findRoots(self) :
        try:
            root1 = (-self.__b + sqrt(self.__b**2 - 4*self.__a*self.__c))/(2*self.__a)
            root2 = (-self.__b - sqrt(self.__b**2 - 4*self.__a*self.__c))/(2*self.__a)
            return root1, root2
        except ValueError as ex:
            raise PolynomialSolverException("Negative discriminant")


try:
    polynom = SecondOrderPolynomal('a',1,-1)
    root1, root2 = polynom.findRoots()
except PolynomialSolverException as ex:
    print("Got exception: " + ex.message)
else:
    print(f"Found root1 as {root1} and root2 as {root2}")






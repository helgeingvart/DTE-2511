# %% [markdown]
# # Klasser 
# 
# En klasse er egentlig bare en samling av funkjoner og variable som hører naturlig sammen i en entitet. Funksjoner kalles her metoder og variablene kalles attributter. Metoder og attributter kan enten gjøres privat eller offentlig (public). Når de er private er de ment å kun aksesseres internt i klassen, mens de som er public aksesseres eksternt.
# 
# Under viser vi et eksempel på en klasse "vektor".

# %%
from math import sin, cos, pi

class Vector : 

    # Contructor
    def __init__(self, x=0, y=0, polar=False) : # if given in polar coordinates, interpret x as length, and y as angle
        if ( polar ) :
            self.__x = x*cos(y)
            self.__y = x*sin(y)
        else :
            self.__x = x
            self.__y = y
        self.filename = str(id(self)) + ".txt"

    @property
    def x(self) :
        return self.__x

    @property
    def y(self) :
        return self.__y

    @x.setter
    def x(self, x) :
        self.__x = x

    @y.setter
    def y(self, y) :
        self.__y = y

    def __str__(self) :
        return f"Vector: ({self.__x}, {self.__y})"

    def __add__(self, other) :
        return Vector(self.__x + other.__x, self.__y + other.__y)

    def __mul__(self, other) :
        return self.__x*other.__x + self.__y*other.__y

    def save(self) :
        with open(self.filename, "w") as file : 
            file.write(f"{self.__x}, {self.__y}")
            # file.write(self)
    
    def load(self) :
        with open(self.filename, "r") as file :
            coords = file.readline()  # Format is "x, y"

        xAndy = coords.split(",")
        self.__x = float(xAndy[0])
        self.__y = float(xAndy[1])

u = Vector(2,1)
v = Vector(1,pi, True)

# print(u)
# print(v)

w = u + v
w.filename = "w.txt"
w.save()

w.x = 120
w.y = 340

w.load()

print(w)

# print(u*v)






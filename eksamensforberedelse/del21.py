# %%
# inherits, extend, override
class Employee :

    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def work(self) :
        print(self.name,"is working...")

class SwEngineer(Employee) :
    
    def __init__(self, name, age, level) :
        super().__init__(name, age)
        self.level = level

    def debug(self) :
        print(self.name, "is debugging...")

    def work(self) :
        print(self.name, "is coding...")

class Designer(Employee) :
    
    def draw(self) :
        print(self.name, "is drawing...")

    def work(self) :
        print(self.name, "is designing...")

se = SwEngineer("Helge", 25, "junior")
# se.work()
de = Designer("Anders", 18)
# de.work()

# Polymorphism
def motivate_employees(employees) :
    for employee in employees :
        employee.work()

employees = [SwEngineer("Helge", 25, "junior"), SwEngineer("Konrad", 16, "senior"), Designer("Anders", 18)]

motivate_employees(employees)








# criação de classe

class MyClass:
  x = 5


# Create Object
p1 = MyClass()
'''print(p1.x)'''


# The __init__() Function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

'''
print(p1.name)
print(p1.age)
'''



# The __str__() Function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

'''print(p1)'''



# Object Methods

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
'''p1.myfunc()'''



# The self Parameter

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
'''p1.myfunc()'''



# Modify Object Properties
p1.age = 40



# Delete Object Properties

del p1.age

del p1


# testando código



class Veiculo:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Veiculo):
    def move(self):
       print(f"{self.brand} {self.model} - Dirigir carro")

class Moto(Veiculo):
    def move(self):
       print(f"{self.brand} {self.model} - Dirigir moto")

class Caminhao(Veiculo):
    def move(self):
       print(f"{self.brand} {self.model} - Dirigir caminhão")




car1 = Car("Ford", "Mustang")
moto1 = Moto("Yahamaha", "Fazer 250")
caminhao1 = Caminhao("Volkswagen", "Meteor")


for x in (car1, moto1, caminhao1):
    x.move()




class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)  # Inicializa atributos herdados


# Instanciar um objeto da classe Carro
carro1 = Carro("Ford", "Mustang", 2022)
print(carro1.marca, carro1.modelo, carro1.ano)

 















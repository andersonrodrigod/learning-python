# Criando uma lista ----------------------------------------------------

# Exemplo de lista de números
numeros = [1, 2, 3, 4, 5]

# Exemplo de lista de strings
frutas = ["maçã", "banana", "laranja"]

# Lista com diferentes tipos de elementos
misturado = [1, "olá", 3.14]



# Acessando elementos da lista -----------------------------------------

# Acessando o primeiro elemento
print(frutas[0])  # saída: maçã

# Acessando o terceiro elemento
print(frutas[2])  # saída: laranja




# Alterando elementos da lista ------------------------------------------

# Alterando o segundo elemento
frutas[1] = "morango"
print(frutas) # saída: ['maçã', 'morango', 'laranja']




# Adicionando elementos à lista ------------------------------------------

# Usando append()
frutas.append("uva")
print(frutas)  # saída: ['maçã', 'morango', 'laranja', 'uva']

# Usando insert()
frutas.insert(1, "abacaxi")
print(frutas)  # saída: ['maçã', 'abacaxi', 'morango', 'laranja', 'uva']

# Usando extend()
frutas.extend(["kiwi", "manga"])
print(frutas)  # saída: ['maçã', 'abacaxi', 'morango', 'laranja', 'uva', 'kiwi', 'manga']




# Removendo elementos da lista --------------------------------------------

# Usando remove()
frutas.remove("morango")
print(frutas)  # saída: ['maçã', 'abacaxi', 'laranja', 'uva', 'kiwi', 'manga']

# Usando pop()
fruta_removida = frutas.pop(2)
print(fruta_removida)  # saída: laranja
print(frutas)  # saída: ['maçã', 'abacaxi', 'uva', 'kiwi', 'manga']

# Usando clear()
frutas.clear()
print(frutas)  # saída: []




# Tamanho da lista -----------------------------------------------------------

numeros = [1, 2, 3, 4, 5]
print(len(numeros))  # saída: 5




# Iterando sobre uma lista ---------------------------------------------------

frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
# saída:
# maçã
# banana
# laranja




# Verificando a existência de um elemento -------------------------------------

frutas = ["maçã", "banana", "laranja"]
print("banana" in frutas)  # saída: True
print("morango" in frutas)  # saída: False














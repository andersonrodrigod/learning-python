pessoa = {
  "nome": "Rodrigo",
  "idade": 27,
  "peso": 70.2
 }

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["peso"])


# In ormacoes o Joga or
player = {
    "nome": "Guilherme",
    "level": 1,
    "hp": 10,
    "dano": 5,
}
# lista de inimigos
npcs = [
    {"nome": "Monstrinho", "dano": 2, "hp": 50, "exp": 5 },
    {"nome": "Monstro", "dano": 5, "hp": 100, "exp": 10 },
    {"nome": "Monstrão", "dano": 10, "hp": 150, "exp": 15 },
    {"nome": "Chefão", "dano": 25, "hp": 200, "exp": 20 }
]

nome_e_dano = []

for npc in npcs:
    nome_e_dano.append((npc["nome"], npc["dano"]))

print(nome_e_dano)



"""
nome_dano = []
index = 0
while index < len(npcs):
    nome_dano.append((npcs[index]["nome"], npcs[index]["dano"]))
    index += 1

print(nome_dano)
"""
    

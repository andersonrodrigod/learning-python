# idade = int(input("imfome a sua idade: "))

"""
if idade >= 18:
    print("PERMITIDO")
else:
    print("BLOQUEADO")

"""


salario = float(input("Informe o salário: "))


if salario <= 3000:
    print("programador junior")
elif salario > 3000 and salario <= 6000:
    print("programador pleno")
elif salario > 6000 and salario <= 1500:
    print("Programador senior")
else:
    print("gerente de projetos")
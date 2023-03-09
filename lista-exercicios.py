categoria = input("Digite sua categoria: Gerente ou Operário \n")
periodo = input("Digite seu turno: matutino, vespertino ou noturno \n")
g="Gerente"
o="Operário"
m="matutino"
v="vespertino"
n="noturno"
sm = 1300

categoria=[g, o]
turno=[m, v, n]

if categoria == "g" and periodo == "n":
    print("Sua hora trabalhada é", + sm * 0.10)

else categoria == "g" and periodo == "m" or periodo == "v":
    print("Sua hora trabalhada é", + sm * 0.15)

else categoria == "o" and periodo == "n":
    print("Sua hora trabalhada é", + sm * 0.09)

else categoria == "o" and periodo == "m" or periodo == "v":
    print("Sua hora trabalhada é", + sm * 0.14)
else:
    print("Categoria ou turno inválido") 
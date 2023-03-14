TURNO = ["Matutino", "Vespertino", "Noturno"]
CATEROGIAS = ["Gerente", "Operacional"]
SM = 1320

PORCENTAGENS = {"Gerente": {"Noturno": 0.1, "Matutino": 0.15, "Vespertino": 0.15}, "Operacional": {"Noturno": 0.9, "Matutino": 0.14, "Vespertino": 0.14}}

nome = input("Digite seu nome: ")
horasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês: "))
turno = input(f"Turno {TURNO}: ")
categoria = input(f"Categoria {CATEROGIAS}: ")

try:
    assert turno in TURNO and categoria in CATEROGIAS
    assert len(nome) > 0 and horasTrabalhadas > 0
except AssertionError:
    print("Dados inválidos, finalizando programa")
    exit()

valorHoraTrabalhada = PORCENTAGENS[categoria][turno]

remuneracao = (valorHoraTrabalhada * SM) * horasTrabalhadas

print(f"{nome}, O seu salário é de R${remuneracao}")
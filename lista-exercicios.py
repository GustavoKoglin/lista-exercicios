#Constantes definindo as arrays de opções dos turnos e categorias, defininfo o valor do salário mínimo e as porcentagens de cada categoria em cada turno.

TURNO = ["Matutino", "Vespertino", "Noturno"]
CATEROGIAS = ["Gerente", "Operacional"]
SM = 1320

PORCENTAGENS = {"Gerente": {"Noturno": 0.1, "Matutino": 0.15, "Vespertino": 0.15}, "Operacional": {"Noturno": 0.09, "Matutino": 0.14, "Vespertino": 0.14}}


#Variáveis que irão receber os dados do usuário.
nome = input("Digite seu nome: ")
horasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês: "))
turno = input(f"Turno {TURNO}: ")
categoria = input(f"Categoria {CATEROGIAS}: ")


#Verificação de dados inválidos com try, assert e exept para veirificar possíveis erros no código, verificando se foram inseridos dados incorretos para emitir mensagem de erro.
try:
    assert turno in TURNO and categoria in CATEROGIAS
    assert len(nome) > 0 and horasTrabalhadas > 0
except AssertionError:
    print("Dados inválidos, finalizando programa")
    exit()

#Cálculo da remuneração do usuário para a hora trabalhada.
valorHoraTrabalhada = PORCENTAGENS[categoria][turno]

#Definindo a remuneração do usuário.
remuneracao = (valorHoraTrabalhada * SM) * horasTrabalhadas

#Imprimindo os dados do usuário, com a função e a string.
print(f"{nome}, O seu salário é de R${remuneracao}")
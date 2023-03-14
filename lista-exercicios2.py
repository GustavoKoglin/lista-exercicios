#Definindo os elevadores ativos e os períodos de uso, e criando um dicionário para armazenar os dados.
ELEVADORES = ["A", "B", "C"]
PERIODOS = ["Matutino", "Vespertino", "Noturno"]

#Armazenando os dados em um dicionário.
dados = {"A": {"Matutino": 0, "Vespertino": 0, "Noturno": 0}, "B": {"Matutino": 0, "Vespertino": 0, "Noturno": 0}, "C": {"Matutino": 0, "Vespertino": 0, "Noturno": 0}}

#Enquando a resposta do usuário for sim, o programa irá continuar a rodar.
while True:
    elevador = input(f"Qual elevador você utiliza com mais frequência {ELEVADORES}: ")
    periodo = input(f"Em qual periodo você mais utiliza o elevador {PERIODOS}: ")

    try:
        assert elevador in ELEVADORES and periodo in PERIODOS
        dados[elevador][periodo] += 1
    except AssertionError:
        print("Valores inválidos, pulando")

    if input("Deseja continuar [sim] ") != "sim":
        break

#Somando os valores de cada elevador e período para descobrir o mais usado.
elevadores_total = [sum(list(list(dados.values())[0].values())), sum(list(list(dados.values())[1].values())), sum(list(list(dados.values())[2].values()))]
periodos_total = [sum([dados["A"]["Matutino"], dados["B"]["Matutino"], dados["C"]["Matutino"]]), sum([dados["A"]["Vespertino"], dados["B"]["Vespertino"], dados["C"]["Vespertino"]]), sum([dados["A"]["Noturno"], dados["B"]["Noturno"], dados["C"]["Noturno"]])]

#Imprimindo os resultados.
print("="*30)

#Imprimindo o elevador mais usado.
print("Elevador mais usado:", end=" ")

#Imprimindo o total de elevadores usados.
print(ELEVADORES[elevadores_total.index(max(elevadores_total))])

#Imprimindo o período mais usado.
print("Periodo mais usado:", end=" ")

#Imprimindo o total de períodos usados.
print(PERIODOS[periodos_total.index(max(periodos_total))])

#Imprimindo a diferença de percentual entre o período mais usado e menos usado.
print("Diferença de percentual entre o período mais usado e menos usado:", end=" ")
print(f"{round(1-(min(periodos_total)/max(periodos_total)), 2)*100}%")
ELEVADORES = ["A", "B", "C"]
PERIODOS = ["Matutino", "Vespertino", "Noturno"]

dados = {"A": {"Matutino": 0, "Vespertino": 0, "Noturno": 0}, "B": {"Matutino": 0, "Vespertino": 0, "Noturno": 0}, "C": {"Matutino": 0, "Vespertino": 0, "Noturno": 0}}

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

elevadores_total = [sum(list(list(dados.values())[0].values())), sum(list(list(dados.values())[1].values())), sum(list(list(dados.values())[2].values()))]
periodos_total = [sum([dados["A"]["Matutino"], dados["B"]["Matutino"], dados["C"]["Matutino"]]), sum([dados["A"]["Vespertino"], dados["B"]["Vespertino"], dados["C"]["Vespertino"]]), sum([dados["A"]["Noturno"], dados["B"]["Noturno"], dados["C"]["Noturno"]])]

print("="*30)
print("Elevador mais usado:", end=" ")
print(ELEVADORES[elevadores_total.index(max(elevadores_total))])
print("Periodo mais usado:", end=" ")
print(PERIODOS[periodos_total.index(max(periodos_total))])
print("Diferença de percentual entre o período mais usado e menos usado:", end=" ")
print(f"{round(1-(min(periodos_total)/max(periodos_total)), 2)*100}%")
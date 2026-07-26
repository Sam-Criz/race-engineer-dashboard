print("---------------------------------------")
print("- SIMULADOR DASH BOARD RACE ENGINEER -")
print("---------------------------------------")

Elementos = {
    "Velocidade Média": 0,
    "Marcha": 0,
    "RPM": 0,
    "Temperatura Média": 0,
    "Combustível": 0,
    "Desgaste dos Pneus": 0,
    "Tempo de Volta": 0,
    "GapLíder": 0,
    "GapAtrás": 0,
    "DRS": "Desativado",
    "ERS": "Ativado",
    "PrevisãoPit": "parada",
}
VelocidadeMédia =int(input("Informe a Velocidade Média do Carro:"))
Elementos["Velocidade Média"] = str(VelocidadeMédia) + " Km/h"
Marcha = 0
if VelocidadeMédia <= 50:
    Marcha = 1
elif VelocidadeMédia >= 50 and VelocidadeMédia <= 100:
    Marcha = 2
elif VelocidadeMédia >= 100 and VelocidadeMédia <= 150:
    Marcha = 3
elif VelocidadeMédia >= 150 and VelocidadeMédia <= 200:
    Marcha = 4
elif VelocidadeMédia >= 200 and VelocidadeMédia <= 250:
    Marcha = 5
elif VelocidadeMédia >= 250 and VelocidadeMédia <= 300:
    Marcha = 6
else:  
    Marcha = 7
Elementos["Marcha"] = Marcha
RPM = str(VelocidadeMédia * 100) + "RPM"
Elementos["RPM"] = RPM
TemperaturaMédia = float(input("Informe a Temperatura Média do Carro: "))
Elementos["Temperatura Média"] = str(TemperaturaMédia) + "°C"
Combustível = float(input("Informe o Combustível Restante do Carro: "))
Elementos["Combustível"] = str(Combustível) + "L"
DesgastePneus = float(input("Informe o Desgaste dos Pneus do Carro: "))
Elementos["Desgaste dos Pneus"] = str(DesgastePneus) + "%"
TempoVolta = float(input("Informe o Tempo de Volta do Carro: "))
Elementos["Tempo de Volta"] = str(TempoVolta) + "s"
TempoLíder = float(input("Informe o Tempo do Líder: "))
GapLíder = TempoVolta - TempoLíder
Elementos["GapLíder"] = str(GapLíder) + "s"
TempoAtrás = float(input("Informe o Tempo do Carro Atrás: "))
GapAtrás = TempoVolta - TempoAtrás
Elementos["GapAtrás"] = str(GapAtrás) + "s"
DRS = int(input("Informe se o DRS está Ativado (1) ou Desativado (0): "))
if DRS == 1:
    Elementos["DRS"] = "Ativado"
else:
    Elementos["DRS"] = "Desativado"
ERS = int(input("Informe se o ERS está Ativado (1) ou Desativado (0): "))
if ERS == 1:
    Elementos["ERS"] = "Ativado"
else:
    Elementos["ERS"] = "Desativado"
# Previsão de parada: se combustível baixo ou desgaste dos pneus alto
if Combustível <= 10 or DesgastePneus >= 80:
    Elementos["PrevisãoPit"] = "BOX BOX"
else:
    Elementos["PrevisãoPit"] = "Sem previsão de parada"
print("\n========== DASHBOARD ==========\n")

for chave, valor in Elementos.items():
    print(f"{chave}: {valor}")
def calcular_marcha(VelocidadeMédia):
    if VelocidadeMédia <= 50:
        return 1
    elif VelocidadeMédia <= 100:
        return 2
    elif VelocidadeMédia <= 150:
        return 3
    elif VelocidadeMédia <= 200:
        return 4
    elif VelocidadeMédia <= 250:
        return 5
    elif VelocidadeMédia <= 300:
        return 6
    else:
        return 7
    
def mostrar_titulo():
    print("---------------------------------------")
    print("- SIMULADOR DASH BOARD RACE ENGINEER -")
    print("---------------------------------------")
mostrar_titulo()

telemetria = {
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
def ler_dados():
    VelocidadeMédia =int(input("Informe a Velocidade Média do Carro:"))
    telemetria["Velocidade Média"] = (VelocidadeMédia)
    telemetria["Marcha"] = calcular_marcha(VelocidadeMédia)
    RPM = (VelocidadeMédia * 100)
    telemetria["RPM"] = RPM
    TemperaturaMédia = float(input("Informe a Temperatura Média do Carro: "))
    telemetria["Temperatura Média"] = (TemperaturaMédia)
    Combustível = float(input("Informe o Combustível Restante do Carro: "))
    telemetria["Combustível"] = (Combustível)
    DesgastePneus = float(input("Informe o Desgaste dos Pneus do Carro: "))
    telemetria["Desgaste dos Pneus"] = (DesgastePneus)
    TempoVolta = float(input("Informe o Tempo de Volta do Carro: "))
    telemetria["Tempo de Volta"] = (TempoVolta)
    TempoLíder = float(input("Informe o Tempo do Líder: "))
    GapLíder = TempoVolta - TempoLíder
    telemetria["GapLíder"] = (GapLíder)
    TempoAtrás = float(input("Informe o Tempo do Carro Atrás: "))
    GapAtrás = TempoVolta - TempoAtrás
    telemetria["GapAtrás"] = (GapAtrás)

def estado_sistema(valor):
    if valor == 1:
        return "Ativado 🟢"
    return "Desativado 🔴"

DRS = int(input("Informe se o DRS está Ativado (1) ou Desativado (0): "))
ERS = int(input("Informe se o ERS está Ativado (1) ou Desativado (0): "))
telemetria["DRS"] = estado_sistema(DRS)
telemetria["ERS"] = estado_sistema(ERS)

# Previsão de parada: se combustível baixo ou desgaste dos pneus alto
def prever_pit(combustivel, desgaste):
        if combustivel <= 10 or desgaste >= 80:
            return "BOX BOX"
        return "Sem previsão de parada"
telemetria["PrevisãoPit"] = prever_pit(telemetria["Combustível"], telemetria["Desgaste dos Pneus"])

def criar_barra(valor, maximo):
    tamanho_total = 20
    preenchido = int((valor / maximo) * tamanho_total)
    vazio = tamanho_total - preenchido

    return "█" * preenchido + "░" * vazio

def barras(elementos):

    barra_combustivel = criar_barra(
        elementos["Combustível"],
        100
    )

    barra_pneus = criar_barra(
        elementos["Desgaste dos Pneus"],
        100
    )
    return barra_combustivel, barra_pneus

def mensagem_engenheiro(elementos):
    if elementos["Desgaste dos Pneus"] >= 80:
        return "📡 Engineer: BOX THIS LAP"

    elif elementos["Combustível"] <= 15:
        return "📡 Engineer: FUEL SAVING"

    return "📡 Engineer: KEEP PUSHING"


def mostrar_dashboard(elementos):
    print("\n========== DASHBOARD ==========\n")

    barra_combustivel, barra_pneus = barras(telemetria)

    print()
    print("📈 PERFORMANCE")
    print("Velocidade", "......",(telemetria["Velocidade Média"]), "km/h")
    print(f"{'Marcha':<20}{elementos['Marcha']}ª")
    print(f"RPM:...........{elementos['RPM']:,}")
    print()
    print("🌡 MOTOR")
    print("Temperatura...........", (telemetria["Temperatura Média"]), "°C")
    print()
    print("⛽ COMBUSTÍVEL")
    print(f"⛽ {barra_combustivel} {elementos['Combustível']}%")
    print()
    print("PNEUS")
    print(f"🛞 {barra_pneus} {elementos['Desgaste dos Pneus']}%")
    print()
    print("📡 SISTEMAS")
    print("DRS...........", elementos["DRS"])
    print("ERS...........", elementos["ERS"])
    print()
    print("🏁 CORRIDA")
    print(f"Tempo de Volta:...........{elementos['Tempo de Volta']:.3f}s")
    print(f"GapLíder:........... +{elementos['GapLíder']:.3f}s")
    print(f"GapAtrás:...........{elementos['GapAtrás']:.3f}s")
    print()
    print("📢 ESTRATÉGIA")
    print("Mensagem do Engenheiro:....", mensagem_engenheiro(telemetria))

ler_dados()
print()
mostrar_dashboard(telemetria)
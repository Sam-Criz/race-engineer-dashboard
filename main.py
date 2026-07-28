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
    "Voltas Feitas": 0,
    "Voltas Totais": 0
}
def ler_dados():
    VelocidadeMédia =int(input("Informe a Velocidade Média do Carro:"))
    telemetria["Velocidade Média"] = (VelocidadeMédia)
    telemetria["Marcha"] = calcular_marcha(VelocidadeMédia)
    RPM = min(int(4000 + VelocidadeMédia * 35), 15000)
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
    DRS = float(input("Qual a distância do carro a frente? "))
    ERS = int(input("Ainda resta quantos % de bateria? "))
    telemetria["DRS"] = estado_drs(DRS)
    telemetria["ERS"] = estado_ers(ERS)
    voltas_feitas = int(input("Informe o número de voltas já feitas: "))
    telemetria["Voltas Feitas"] = voltas_feitas
    voltas_totais = int(input("Informe o número total de voltas da corrida: "))
    telemetria["Voltas Totais"] = voltas_totais

def estado_drs(DRS):
    if DRS < 1.01:
        return "AVAILABLE 🟢"
    return "UNAVAILABLE 🔴"

def estado_ers(ERS):
    if ERS > 20:
        return "AVAILABLE 🟢"
    return "UNAVAILABLE 🔴"

# Previsão de parada: se combustível baixo ou desgaste dos pneus alto
def prever_pit(combustivel, desgaste, voltas_restantes):
        if desgaste >= 75:
            return "BOX THIS LAP"

        elif combustivel <= 8:
            return "BOX THIS LAP"

        elif desgaste >=60 and voltas_restantes<5:
            return "STAY OUT"

        else:
            return "CONTINUE"

def criar_barra(valor, maximo):
    tamanho_total = 20

    valor = max(0, min(valor, maximo))

    preenchido = int((valor / maximo) * tamanho_total)
    vazio = tamanho_total - preenchido

    return "█" * preenchido + "░" * vazio

def barras(elementos):

    barra_combustivel = criar_barra(
        elementos["Combustível"],
        100
    )

    barra_pneus = criar_barra(
    100 - elementos["Desgaste dos Pneus"],
    100
    )
    return barra_combustivel, barra_pneus

def mensagem_engenheiro(elementos):
    if elementos["Desgaste dos Pneus"] >= 80:
        return "📡 Engineer: 🔴 BOX THIS LAP"

    elif elementos["Combustível"] <= 15:
        return "📡 Engineer: 🟡 FUEL SAVING"

    return "📡 Engineer: 🟢 KEEP PUSHING"

def alerta_temperatura(valor):
    if valor < 80:
        return "NORMAL"

    elif 80 <= valor < 95:
        return "WARNING"

    return "CRITICAL"

def alerta_combustivel(valor):
    if valor <= 10:
        return f"⚠️ {valor} 🔴 LOW FUEL!"
    return f"✅ {valor} 🟢 FUEL OK"

def alerta_pneus(valor):
    if valor >= 55:
        return f"⚠️ {valor} 🔴 TIRES WORN!"
    return f"✅ {valor} 🟢 TIRES OK"

def relatorio_combustivel(valores):
    if valores <=10:
        return "LOW"
    elif valores <= 20:
        return "NORMAL"
    elif valores <= 35:
        return "OK"
    elif valores <= 50:
        return "GOOD"
    return "EXCELLENT"

def relatorio_temperatura(valor):
    if valor < 70:
        return "COLD"

    elif valor <= 95:
        return "OPTIMAL"

    elif valor <= 105:
        return "WARNING"

    return "CRITICAL"

def relatorio_pneus(desgaste):
    if desgaste <=10:
        return "EXCELLENT"
    elif desgaste <=20:
        return "GOOD"
    elif desgaste <=35:
        return "NORMAL"
    elif desgaste <=50:
        return "WARNING"
    return "CRITICAL"

def voltas_restantes(voltas_feitas, voltas_totais):
    voltas_restantes = voltas_totais - voltas_feitas
    return voltas_restantes

def gap1(GapLíder):
    if GapLíder > 0:
        return f"+{GapLíder:.3f}s"
    return f"{GapLíder:.3f}s"

def gap2(GapAtrás):
    if GapAtrás > 0:
        return f"+{GapAtrás:.3f}s"
    return f"{GapAtrás:.3f}s"


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
    print(f"{alerta_temperatura(telemetria['Temperatura Média'])}")
    print()
    print("⛽ COMBUSTÍVEL")
    print(f"{barra_combustivel} {elementos['Combustível']}%")
    print(f"{alerta_combustivel(telemetria['Combustível'])}")
    print()
    print("PNEUS")
    print(f"{barra_pneus} {100-elementos['Desgaste dos Pneus']}% restante")
    print(f"{alerta_pneus(telemetria['Desgaste dos Pneus'])}")
    print()
    print("📡 SISTEMAS")
    print("DRS...........", elementos["DRS"])
    print("ERS...........", elementos["ERS"])
    print()
    print("🏁 CORRIDA")
    print(f"Tempo de Volta:...........{elementos['Tempo de Volta']:.3f}s")
    print(f"GapLíder:........... {gap1(elementos['GapLíder'])}")
    print(f"GapAtrás:...........{gap2(elementos['GapAtrás'])}")
    print()
    print("📢 ESTRATÉGIA")
    print(f"Pit Strategy: {elementos['PrevisãoPit']}")
    print(mensagem_engenheiro(telemetria))
    print(f"FUEL: {relatorio_combustivel(telemetria['Combustível'])}")
    print(f"TIRES: {relatorio_pneus(telemetria['Desgaste dos Pneus'])}")
    print(f"TEMPERATURE: {relatorio_temperatura(telemetria['Temperatura Média'])}")
    print()
    print(f"Estimated Laps Remaining: {voltas_restantes(telemetria['Voltas Feitas'], telemetria['Voltas Totais'])}")

ler_dados()

telemetria["PrevisãoPit"] = prever_pit(
    telemetria["Combustível"],
    telemetria["Desgaste dos Pneus"],
    voltas_restantes(
        telemetria["Voltas Feitas"],
        telemetria["Voltas Totais"]
    )
)

print()
mostrar_dashboard(telemetria)
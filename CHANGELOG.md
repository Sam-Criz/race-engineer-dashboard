# Changelog

Todas as mudanças importantes deste projeto serão documentadas neste arquivo.

---

# V0.1 - Dashboard em Terminal

### Adicionado
- Estrutura inicial do projeto.
- Dashboard exibido no terminal.
- Entrada manual dos dados de telemetria.
- Cálculo automático da marcha.
- Cálculo de RPM baseado na velocidade.
- Exibição de:
  - Velocidade
  - Marcha
  - RPM
  - Temperatura
  - Combustível
  - Desgaste dos pneus
  - Tempo de volta
  - Gap para líder
  - Gap para o carro atrás
  - DRS
  - ERS
- Primeira previsão simples de pit stop.

---

# V0.2 - Refatoração

### Adicionado
- Organização do código em funções.
- Separação da lógica de cálculo.
- Função para exibir o dashboard.
- Melhor organização da leitura dos dados.

### Alterado
- Código mais limpo e reutilizável.
- Melhor legibilidade.

---

# V0.3 - Dashboard Visual

### Adicionado
- Barras gráficas para combustível.
- Barras gráficas para desgaste dos pneus.
- Dashboard dividido por seções:
  - Performance
  - Motor
  - Combustível
  - Pneus
  - Sistemas
  - Corrida
  - Estratégia
- Melhor formatação das informações.
- Ícones para facilitar a leitura.

### Alterado
- Visual do terminal mais próximo de uma telemetria.

---

# V0.4 - Organização e Aprimoramento

### Adicionado
- Mensagens do engenheiro.
- Melhor separação das funções.
- Função para criação de barras.
- Melhor organização do código.

### Alterado
- Dashboard reorganizado.
- Melhor alinhamento das informações.
- Código preparado para futuras expansões.

---

# V0.5 - Intelligent Telemetry

### Adicionado
- RPM calculado de forma mais realista.
- Disponibilidade do DRS baseada na distância para o carro da frente.
- Disponibilidade do ERS baseada na bateria restante.
- Alertas de temperatura.
- Alertas de combustível.
- Alertas de desgaste dos pneus.
- Relatórios de:
  - Fuel
  - Tires
  - Temperature
- Estratégia de pit mais inteligente.
- Mensagens do engenheiro com diferentes situações.
- Cálculo de voltas restantes.
- Melhor tratamento dos gaps.
- Barras protegidas contra valores inválidos.

### Alterado
- Barra dos pneus passou a mostrar vida restante.
- Dashboard mais semelhante a um sistema de Race Engineer.
- Código mais organizado para futura modularização.

---

# Próximas versões

## V0.6
- Modularização do projeto.
- Separação em:
  - dashboard.py
  - telemetry.py
  - strategy.py
  - utils.py
- Melhor arquitetura.

## V0.7
- Simulação em tempo real.
- Atualização automática da telemetria.
- Consumo de combustível.
- Desgaste progressivo dos pneus.
- Temperatura dinâmica.
- Atualização automática do DRS e ERS.

## V1.0
- Interface gráfica.
- Dashboard semelhante aos utilizados na Fórmula 1.
- Indicadores visuais.
- Velocímetro.
- Painel profissional.

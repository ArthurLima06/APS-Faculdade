# ========================================
# CALCULADORA DE CARBONO - VERSÃO ATUALIZADA
# ========================================

# Funções para cada tipo de emissão
def emissao_energia(kwh):
    # fator médio de emissão: 0.092 kg CO2 por kWh (exemplo)
    return kwh * 0.092

def emissao_combustivel(litros):
    # fator médio: 2.31 kg CO2 por litro de gasolina (exemplo)
    return litros * 2.31

def emissao_viagem_veiculo(km, tipo):
    # fatores médios de emissão por km
    fatores = {
        "carro": 0.15,   # kg CO2 por km
        "moto": 0.10,    # kg CO2 por km
        "avião": 0.25,   # kg CO2 por km
        "barco": 0.20    # kg CO2 por km
    }
    return km * fatores.get(tipo, 0)

# Função principal de cálculo
def calcular_emissoes():
    print("=== Calculadora de Carbono ===")

    energia = float(input("Digite o consumo de energia elétrica (kWh): "))
    
    print("\n--- Tipos de veículos disponíveis ---")
    print("1 - Carro")
    print("2 - Moto")
    print("3 - Avião")
    print("4 - Barco")

    escolha = input("Escolha o tipo de veículo (1/2/3/4): ")

    veiculos = {"1": "carro", "2": "moto", "3": "avião", "4": "barco"}
    tipo_veiculo = veiculos.get(escolha, "carro") 
    adrão = carro

    km = float(input(f"Digite a distância percorrida em (km): "))
    combustivel = float(input("Digite o consumo de combustível (litros/KM): ")) #

    # Cálculos
    emissao_e = emissao_energia(energia)
    emissao_c = emissao_combustivel(combustivel)
    emissao_v = emissao_viagem_veiculo(km, tipo_veiculo)
    total = emissao_e + emissao_c + emissao_v

    # Resultados parciais
    print("\n--- RESULTADOS PARCIAIS ---")
    print(f"Emissões por energia: {emissao_e:.2f} kg CO2")
    print(f"Emissões por combustível: {emissao_c:.2f} kg CO2")
    print(f"Emissões por {tipo_veiculo}: {emissao_v:.2f} kg CO2")
    print(f"TOTAL de emissões: {total:.2f} kg CO2")

    # Resumo final (entrada + saída)
    print("\n=== RESUMO FINAL ===")
    print(f"Consumo de energia: {energia} kWh")
    print(f"Consumo de combustível: {combustivel} litros")
    print(f"Distância percorrida de {tipo_veiculo}: {km} km")
    print(f"Total de emissões: {total:.2f} kg CO2")

    return total

# Função para calcular créditos necessários
def calcular_creditos(total_emissao):
    preco_credito = 50.0  # exemplo: R$ 50 por tonelada de CO2
    toneladas = total_emissao / 1000  # converter kg para toneladas
    custo = toneladas * preco_credito

    print("\n--- COMPENSAÇÃO ---")
    print(f"Total de créditos de carbono necessários: {toneladas:.2f} tCO2")
    print(f"Custo estimado para compensação: R$ {custo:.2f}")

# Execução
if __name__ == "__main__":
    total = calcular_emissoes()
    calcular_creditos(total)

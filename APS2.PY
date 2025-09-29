# ========================================
# CALCULADORA DE CARBONO - VERSÃO ATUALIZADA COM INTERFACE GRÁFICA
# ========================================

from tkinter import *

# Funções para cada tipo de emissão
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

    # Entrada de dados   
    print("\n--- Tipos de veículos disponíveis ---")
    print("1 - Carro")
    print("2 - Moto")
    print("3 - Avião")
    print("4 - Barco")

    escolha = int(input("Escolha o tipo de veículo (1/2/3/4): "))

    if escolha == 1:
        veiculos = "carro"
    elif escolha == 2:
        veiculos = "moto"
    elif escolha == 3:
        veiculos = "avião"
    elif escolha == 4:
        veiculos = "barco"
    else:
        print("Escolha inválida.")
        return 0

    km = float(input(f"Digite a distância percorrida em (km): "))
    combustivel = float(input("Digite o consumo de combustível (litros/KM): ")) 

    # Consumo de energia personalizado para cada veículo, ou padrão para todos
    opcoes = input("você quer usar o consumo de energia padrão ou personalizado? (p/pers): ").lower()
    if opcoes == 'pers':
        if escolha == 1: 
            mediaenergia = km * 0.67
        elif escolha == 2:
            mediaenergia = km * 0.33
        elif escolha == 3:
            passageiros = int(input("Digite o número de passageiros do avião: "))
            mediaenergia = km * 0.33 * passageiros
        elif escolha == 4:
            mediaenergia = km * 4.8
    elif opcoes == 'p':
        mediaenergia = (km * combustivel) * 9.5

    # Cálculos
    emissao_c = emissao_combustivel(combustivel)
    emissao_v = emissao_viagem_veiculo(km, veiculos )
    
    emissao_e = mediaenergia * 0.233 #Consumo em KG de CO2 por kWh (média global)
    total = emissao_e + emissao_c + emissao_v

    # Resultados parciais
    print("\n--- RESULTADOS PARCIAIS ---")
    print(f"Consumo médio de energia do veículo: {mediaenergia:.2f} kWh/100km")
    if opcoes == 'p': # Se for padrão, mostrar a mensagem avisando que é media geral de todos os veículos
        print("OBS: Consumo médio baseado em dados genéricos.")
    print(f"Emissões por energia: {emissao_e:.2f} kg CO2")
    print(f"Emissões por combustível: {emissao_c:.2f} kg CO2")
    print(f"Emissões por {veiculos}: {emissao_v:.2f} kg CO2")
    print(f"TOTAL de emissões: {total:.2f} kg CO2")

    # Resumo final (entrada + saída)
    print("\n=== RESUMO FINAL ===")
    print(f"Consumo de combustível: {combustivel} litros")
    print(f"Distância percorrida: {km} km")
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

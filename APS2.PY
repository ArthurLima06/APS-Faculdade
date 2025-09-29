# ========================================
# CALCULADORA DE CARBONO - VERSÃO ATUALIZADA COM INTERFACE GRÁFICA
# ========================================

#função principal para interface gráfica "TKinter"
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# --- Funções de cálculo ---------------------------------------------------

def emissao_combustivel(litros):
    """Emissão por combustão (kg CO2) assumindo 2.31 kgCO2 por litro."""
    return litros * 2.31

def emissao_viagem_veiculo(km, tipo):
    """Emissão direta por km do veículo (kg CO2 / km * km = kg CO2)"""
    fatores = {
        "carro": 0.15,   # kg CO2 por km
        "moto": 0.10,
        "avião": 0.25,
        "barco": 0.20
    }
    return km * fatores.get(tipo, 0)

# --- Funções auxiliares ---------------------------------------------------

def calcular():
    try:
        km = float(entry_km.get())
        consumo_km_l = float(entry_consumo.get())  # km por litro
        tipo = vehicle_var.get()
        modo = modo_var.get()

        if km <= 0 or consumo_km_l <= 0:
            raise ValueError("Valores devem ser positivos.")

        # litros gastos na viagem
        litros_totais = km / consumo_km_l
        emis_combustivel = emissao_combustivel(litros_totais)
        emis_veiculo = emissao_viagem_veiculo(km, tipo)

        # Consumo de energia
        if modo == "pers":
            if tipo == "carro":
                media_energia = km * 0.67
            elif tipo == "moto":
                media_energia = km * 0.33
            elif tipo == "avião":
                passageiros = int(spin_passageiros.get())
                passageiros = max(1, passageiros)
                media_energia = km * 0.33 * passageiros
            elif tipo == "barco":
                media_energia = km * 4.8
            else:
                media_energia = 0.0
        else:
            media_energia = litros_totais * 9.5

        emis_energia = media_energia * 0.233
        total = emis_combustivel + emis_veiculo + emis_energia

        preco_credito = 50.0  # R$ por tonelada
        toneladas = total / 1000.0
        custo = toneladas * preco_credito

        # Atualiza os resultados
        lbl_result_combustivel.config(
            text=f"Emissão por combustível: {emis_combustivel:.2f} kg CO₂")
        lbl_result_veiculo.config(
            text=f"Emissão pelo veículo: {emis_veiculo:.2f} kg CO₂")
        lbl_result_energia.config(
            text=f"Emissão por energia elétrica: {emis_energia:.2f} kg CO₂")
        lbl_result_total.config(
            text=f"TOTAL: {total:.2f} kg CO₂ ({toneladas:.3f} tCO₂)")
        lbl_result_creditos.config(
            text=f"Créditos necessários: {toneladas:.3f} tCO₂ — Custo estimado: R$ {custo:.2f}")

        global resultados_atual
        resultados_atual = {
            "Distância (km)": km,
            "Consumo (km/L)": consumo_km_l,
            "Veículo": tipo,
            "Combustível (kg CO₂)": emis_combustivel,
            "Veículo (kg CO₂)": emis_veiculo,
            "Energia (kg CO₂)": emis_energia,
            "Total (kg CO₂)": total,
            "Total (tCO₂)": toneladas,
            "Custo (R$)": custo
        }

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos e positivos.")
    except Exception as e:
        messagebox.showerror("Erro inesperado", str(e))

def limpar():
    entry_km.delete(0, tk.END)
    entry_consumo.delete(0, tk.END)
    vehicle_var.set("carro")
    modo_var.set("p")
    spin_passageiros.set(1)
    lbl_result_combustivel.config(text="Emissão por combustível: -")
    lbl_result_veiculo.config(text="Emissão pelo veículo: -")
    lbl_result_energia.config(text="Emissão por energia elétrica: -")
    lbl_result_total.config(text="TOTAL: -")
    lbl_result_creditos.config(text="Créditos: -")

def exportar():
    if not resultados_atual:
        messagebox.showinfo("Aviso", "Nenhum cálculo realizado ainda.")
        return

    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Arquivo de texto", "*.txt")])
    if not filepath:
        return

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=== Relatório da Calculadora de Carbono ===\n\n")
        for chave, valor in resultados_atual.items():
            f.write(f"{chave}: {valor}\n")

    messagebox.showinfo("Exportação concluída", f"Resultados salvos em:\n{filepath}")

def atualizar_passageiros(*args):
    if vehicle_var.get() == "avião":
        lbl_passageiros.grid()
        spin_passageiros.grid()
    else:
        lbl_passageiros.grid_remove()
        spin_passageiros.grid_remove()

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)

# --- Interface gráfica ----------------------------------------------------

root = tk.Tk()
root.title("Calculadora de Carbono")
root.geometry("620x540")
root.configure(bg="#f0f8ff")  # azul claro no fundo

# Atalhos para fullscreen
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", end_fullscreen)

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(fill="both", expand=True, padx=15, pady=15)

font_label = ("Arial", 11)

# Título
tk.Label(frame, text="🌱 Calculadora de Emissões de Carbono 🌍",
         font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#006400").grid(row=0, column=0, columnspan=3, pady=(0, 15))

# Distância
tk.Label(frame, text="Distância percorrida (km):", font=font_label, bg="#f0f8ff").grid(row=1, column=0, sticky="w")
entry_km = ttk.Entry(frame)
entry_km.grid(row=1, column=1, sticky="ew", padx=6, pady=4)

# Consumo
tk.Label(frame, text="Consumo (km por litro):", font=font_label, bg="#f0f8ff").grid(row=2, column=0, sticky="w")
entry_consumo = ttk.Entry(frame)
entry_consumo.grid(row=2, column=1, sticky="ew", padx=6, pady=4)

# Tipo de veículo
tk.Label(frame, text="Tipo de veículo:", font=font_label, bg="#f0f8ff").grid(row=3, column=0, sticky="w")
vehicle_var = tk.StringVar(value="carro")
vehicle_combo = ttk.Combobox(frame, textvariable=vehicle_var, state="readonly",
                             values=["carro", "moto", "avião", "barco"])
vehicle_combo.grid(row=3, column=1, sticky="ew", padx=6, pady=4)
vehicle_var.trace_add("write", atualizar_passageiros)

# Consumo de energia
tk.Label(frame, text="Consumo de energia:", font=font_label, bg="#f0f8ff").grid(row=4, column=0, sticky="w")
modo_var = tk.StringVar(value="p")
tk.Radiobutton(frame, text="Padrão (genérico)", variable=modo_var, value="p",
               bg="#f0f8ff").grid(row=4, column=1, sticky="w")
tk.Radiobutton(frame, text="Personalizado (por veículo)", variable=modo_var, value="pers",
               bg="#f0f8ff").grid(row=5, column=1, sticky="w")

# Passageiros (avião)
lbl_passageiros = tk.Label(frame, text="Número de passageiros (avião):", font=font_label, bg="#f0f8ff")
spin_passageiros = ttk.Spinbox(frame, from_=1, to=500, width=6)
spin_passageiros.set(1)
lbl_passageiros.grid(row=6, column=0, sticky="w")
spin_passageiros.grid(row=6, column=1, sticky="w")
atualizar_passageiros()

# Botões coloridos
btn_calc = tk.Button(frame, text="Calcular", command=calcular,
                     bg="#32cd32", fg="white", font=("Arial", 11, "bold"))
btn_calc.grid(row=7, column=0, pady=10, sticky="ew")

btn_clear = tk.Button(frame, text="Limpar", command=limpar,
                      bg="#ff4500", fg="white", font=("Arial", 11, "bold"))
btn_clear.grid(row=7, column=1, pady=10, sticky="ew")

btn_export = tk.Button(frame, text="Exportar", command=exportar,
                       bg="#1e90ff", fg="white", font=("Arial", 11, "bold"))
btn_export.grid(row=7, column=2, pady=10, sticky="ew")

# Resultados
tk.Label(frame, text="Resultados:", font=("Arial", 13, "bold"),
         bg="#f0f8ff", fg="#000080").grid(row=8, column=0, columnspan=3, sticky="w", pady=(10, 5))

lbl_result_combustivel = tk.Label(frame, text="Emissão por combustível: -", font=font_label, bg="#f0f8ff")
lbl_result_combustivel.grid(row=9, column=0, columnspan=3, sticky="w")

lbl_result_veiculo = tk.Label(frame, text="Emissão pelo veículo: -", font=font_label, bg="#f0f8ff")
lbl_result_veiculo.grid(row=10, column=0, columnspan=3, sticky="w")

lbl_result_energia = tk.Label(frame, text="Emissão por energia elétrica: -", font=font_label, bg="#f0f8ff")
lbl_result_energia.grid(row=11, column=0, columnspan=3, sticky="w")

lbl_result_total = tk.Label(frame, text="TOTAL: -", font=("Arial", 12, "bold"), bg="#f0f8ff", fg="#8b0000")
lbl_result_total.grid(row=12, column=0, columnspan=3, sticky="w")

lbl_result_creditos = tk.Label(frame, text="Créditos: -", font=font_label, bg="#f0f8ff")
lbl_result_creditos.grid(row=13, column=0, columnspan=3, sticky="w")

frame.columnconfigure(1, weight=1)

# Variável global para exportar resultados
resultados_atual = {}

#função essencial para finalizar a interface gráfica
root.mainloop()

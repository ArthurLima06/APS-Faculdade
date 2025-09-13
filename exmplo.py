from tkinter import *
import funcoes as f

def soma():
    vNumero1 = int(txtNumero1.get())
    vNumero2 = int(txtNumero2.get())
    
    vResultado = f.soma(vNumero1, vNumero2)
    
    lblResultado.config(text=vResultado)

def subtracao():
    vNumero1 = int(txtNumero1.get())
    vNumero2 = int(txtNumero2.get())
    
    vResultado = f.subtracao(vNumero1, vNumero2)
    
    lblResultado.config(text=vResultado)


janela = Tk()
janela.geometry("400x400")
janela.title("Calculadora")

txtNumero1 = Entry(janela, font="Arial 20")
txtNumero1.pack()
txtNumero2 = Entry(janela, font="Arial 20")
txtNumero2.pack()

btnSoma = Button(janela, text="+", font="Arial 20", command=soma)
btnSoma.pack()

btnSubtracao = Button(janela, text="-", font="Arial 20", command=subtracao)
btnSubtracao.pack()

lblResultado = Label(janela, text="", font="Arial 20")
lblResultado.pack()

janela.mainloop()
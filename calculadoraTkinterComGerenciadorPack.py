from tkinter import *

janela = Tk()

def somar () :
    val1 = int(ed1.get())
    val2 = int(ed2.get())
    soma = val1 + val2
    print("Soma: ", soma)
    somastr = str(soma)
    lb["text"] = "O Resultado é: " + somastr

def subtrair () :
    val1 = int(ed1.get())
    val2 = int(ed2.get())
    soma = val1 - val2
    print("Resultado: ", soma)
    somastr = str(soma)
    lb["text"] = "O Resultado é: " + somastr

def multiplicar () :
    val1 = int(ed1.get())
    val2 = int(ed2.get())
    soma = val1 * val2
    print("Produto: ", soma)
    somastr = str(soma)
    lb["text"] = "O Resultado é: " + somastr

def dividir () :
    val1 = int(ed1.get())
    val2 = int(ed2.get())
    soma = val1 / val2
    print("Quociente: ", soma)
    somastr = str(soma)
    lb["text"] = "O Resultado é: " + somastr

def potenciar () :
    val1 = int(ed1.get())
    val2 = int(ed2.get())
    soma = val1 ** val2
    print("Resultado: ", soma)
    somastr = str(soma)
    lb["text"] = "O Resultado é: " + somastr

lb_main = Label(janela, text="Calculadora Tkinter", font="arial -22 bold")
lb_main.pack()

ed1 = Entry(janela)
lb_ed1 = Label(janela, text='Primeiro valor')
ed1.pack()
lb_ed1.pack()

ed2 = Entry(janela)
lb_ed2 = Label(janela, text='Segundo valor')
ed2.pack()
lb_ed2.pack()

#Botões de operação   <<<<<<<<<<<<<<<<<<<<<<<<
bt = Button(janela, text="Somar", width=20, command=somar)
bt.pack()

bt = Button(janela, text="Subtrair", width=20, command=subtrair)
bt.pack()

bt = Button(janela, text="Multiplicar", width=20, command=multiplicar)
bt.pack()

bt = Button(janela, text="Dividir", width=20, command=dividir)
bt.pack()

bt = Button(janela, text="Potenciar", width=20, command=potenciar)
bt.pack()

lb = Label(janela, text="Resultado vem aqui")
lb.pack()

janela.title("Calculadora marota em python by Lucas59356")
janela.geometry("400x300+200+200")
janela.mainloop()

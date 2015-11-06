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

lb_ed1 = Label(janela, text='Primeiro valor')
ed1 = Entry(janela)
ed1.place(x=150, y=10)
lb_ed1.place(x=50,y=10)

lb_ed2 = Label(janela, text="Segundo valor")
ed2 = Entry(janela)
ed2.place(x=150,y=40)
lb_ed2.place(x=50, y=40)

#Botões de operação   <<<<<<<<<<<<<<<<<<<<<<<<
bt = Button(janela, text="Somar", width=20, command=somar)
bt.place(x=100,y=80)

bt = Button(janela, text="Subtrair", width=20, command=subtrair)
bt.place(x=100,y=110)

bt = Button(janela, text="Multiplicar", width=20, command=multiplicar)
bt.place(x=100,y=140)

bt = Button(janela, text="Dividir", width=20, command=dividir)
bt.place(x=100,y=170)

bt = Button(janela, text="Potenciar", width=20, command=potenciar)
bt.place(x=100,y=200)

lb = Label(janela, text="Resultado vem aqui")
lb.place(x=70, y=270)

janela.title("Calculadora marota em python by Lucas59356")
janela.geometry("400x300+200+200")
janela.mainloop()

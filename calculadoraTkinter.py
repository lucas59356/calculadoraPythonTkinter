from tkinter import Tk, Label, Entry, Button
from utils import somar, subtrair, multiplicar, dividir, potenciar

janela = Tk()

lb_ed1 = Label(janela, text='Primeiro valor')
ed1 = Entry(janela)
ed1.place(x=150, y=10)
lb_ed1.place(x=50, y=10)

lb_ed2 = Label(janela, text="Segundo valor")
ed2 = Entry(janela)
ed2.place(x=150, y=40)
lb_ed2.place(x=50, y=40)

lb = Label(janela, text="Resultado vem aqui") # Label do resultado
lb.place(x=70, y=270)

#Botões de operação   <<<<<<<<<<<<<<<<<<<<<<<<
bt = Button(janela, text="Somar", width=20, command=lambda: somar(ed1, ed2, lb))
bt.place(x=100, y=80)

bt = Button(janela, text="Subtrair", width=20, command=lambda: subtrair(ed1, ed2, lb))
bt.place(x=100, y=110)

bt = Button(janela, text="Multiplicar", width=20, command=lambda: multiplicar(ed1, ed2, lb))
bt.place(x=100, y=140)

bt = Button(janela, text="Dividir", width=20, command=lambda: dividir(ed1, ed2, lb))
bt.place(x=100, y=170)

bt = Button(janela, text="Potenciar", width=20, command=lambda: potenciar(ed1, ed2, lb))
bt.place(x=100, y=200)

janela.title("Calculadora marota em python by Lucas59356")
janela.geometry("400x300+200+200")
janela.mainloop()

from tkinter import Entry, Label, Tk, Button
from utils import somar, subtrair, multiplicar, dividir, potenciar

janela = Tk()

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
bt = Button(janela, text="Somar", width=20, command=lambda: somar(ed1, ed2, lb))
bt.pack()

bt = Button(janela, text="Subtrair", width=20, command=lambda: subtrair(ed1, ed2, lb))
bt.pack()

bt = Button(janela, text="Multiplicar", width=20, command=lambda: multiplicar(ed1, ed2, lb))
bt.pack()

bt = Button(janela, text="Dividir", width=20, command=lambda: dividir(ed1, ed2, lb))
bt.pack()

bt = Button(janela, text="Potenciar", width=20, command=lambda: potenciar(ed1, ed2, lb))
bt.pack()

lb = Label(janela, text="Resultado vem aqui")
lb.pack()

janela.title("Calculadora marota em python by Lucas59356")
janela.geometry("400x300+200+200")
janela.mainloop()

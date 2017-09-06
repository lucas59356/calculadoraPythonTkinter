def somar(ed1, ed2, lb):
    val1 = int(ed1.get())
    val2 = int(ed2.get())
    soma = val1 + val2
    print("Soma: ", soma)
    somastr = str(soma)
    lb["text"] = "O Resultado é: " + somastr

def subtrair(ed1, ed2, lb):
    val1 = int(ed1.get())
    val2 = int(ed2.get())
    soma = val1 - val2
    print("Subtração: ", soma)
    somastr = str(soma)
    lb["text"] = "O Resultado é: " + somastr

def multiplicar(ed1, ed2, lb):
    val1 = int(ed1.get())
    val2 = int(ed2.get())
    soma = val1 * val2
    print("Produto: ", soma)
    somastr = str(soma)
    lb["text"] = "O Resultado é: " + somastr

def dividir(ed1, ed2, lb):
    val1 = int(ed1.get())
    val2 = int(ed2.get())
    soma = val1 / val2
    print("Quociente: ", soma)
    somastr = str(soma)
    lb["text"] = "O Resultado é: " + somastr

def potenciar(ed1, ed2, lb):
    val1 = int(ed1.get())
    val2 = int(ed2.get())
    soma = val1 ** val2
    print("Potencia: ", soma)
    somastr = str(soma)
    lb["text"] = "O Resultado é: " + somastr

from tkinter import *



# Criando a janela
janela = Tk()
janela.title("Operações Básicas")
numero1 = Label(janela, text='Digite um número: ')
numero1.grid(row=0, column=0)
numero2 = Label(janela, text="Digite outro número: ")
numero2.grid(row=1, column=0)
numero1_entrada = Entry(janela)
numero1_entrada.grid(row=0, column=1)
numero2_entrada = Entry(janela)
numero2_entrada.grid(row=1, column=1)
resultado_label = Label(janela, text="Resultado: ")
resultado_label.grid(row=2, column=0)
resultado = Label(janela, text="0")
resultado.grid(row=2, column=1)

# Criando botões
botao_somar = Button(janela, text="Somar", command=lambda: somar(numero1_entrada.get(), numero2_entrada.get()))
botao_somar.grid(row=3, column=0)
botao_subtrair = Button(janela, text="Subtrair", command=lambda: subtrair(numero1_entrada.get(), numero2_entrada.get()))
botao_subtrair.grid(row=3, column=1)
botao_multiplicar = Button(janela, text="Multiplicar", command=lambda: multiplicar(numero1_entrada.get(), numero2_entrada.get()))
botao_multiplicar.grid(row=4, column=0)
botao_dividir = Button(janela, text="Dividir", command=lambda: dividir(numero1_entrada.get(), numero2_entrada.get()))
botao_dividir.grid(row=4, column=1)
botao_limpar = Button(janela, text="Limpar", command= lambda: limpar())
botao_limpar.grid(row=5, column=0)
botao_sair = Button(janela, text="Sair", command=janela.destroy)
botao_sair.grid(row=5, column=1)


# Criando funções
def somar(num1, num2):
    resultado.config(text=int(num1) + int(num2))

def subtrair(num1, num2):
    resultado.config(text=int(num1) - int(num2))

def multiplicar(num1, num2):
    resultado.config(text=int(num1) * int(num2))

def dividir(num1, num2):
    resultado.config(text=int(num1) / int(num2))

def limpar():
    numero1_entrada.delete(0, END)
    numero2_entrada.delete(0, END)
    resultado.config(text= "")

def sair():
    janela.destroy()


janela.mainloop()


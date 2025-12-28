# Identificador-de-numeros-pares-impares
import tkinter as tk

window = tk.Tk()
window.title("É par ou impar?")
window.geometry("200x200")

text = tk.Label(window, text=f"Digite o número:")
text.pack()

entrada_text = tk.Entry(window)
entrada_text.pack()

par = []
impar = []

status_label = tk.Label(window, text=f"...")
status_label.pack()

def calcular():
    # for i in range(1): 
        numero = int(entrada_text.get())
        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)
        status_label['text'] = f"Último número adicionado: {numero}"


tk.Button(window, text="Adicionar", command=calcular).pack()

def imprimir():
    #print('\nOs numeros pares são:')
    for numero in par:
        print(f' - {numero}')
    tk.Label(window, text=f"Números pares:\n {par}").pack()
    #print('\nOs numeros impares são:')
    for numero in impar:
        print(f' - {numero}')
    tk.Label(window, text=f"Números impares:\n {impar}").pack()


tk.Button(window, text="Imprimir", command=imprimir).pack()

window.mainloop()
    

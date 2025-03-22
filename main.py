#importando tkinter
from tkinter import*
from tkinter import ttk

# cores 

cor1 = "#1e1f1e" #black/preta
cor2 = "feffff"  #white/branca
cor3 = "38576b"  #Azul carregado
cor4 = ""
Janela =Tk()
Janela.title("Calculadora do Gabriel")
Janela.geometry("235x318")
Janela.config(bg=cor1)


Frame_tela = Frame(Janela,width=235, height=50)
Frame_tela.grid(row=0, column=0)
 
Janela.mainloop()

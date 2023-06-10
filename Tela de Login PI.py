
from tkinter import *
import tkinter.messagebox as MessageBox
from PIL import Image, ImageTk, ImageFont, ImageDraw

def tela2():
    Tela2.place_forget()
    Tela2.place(width=370, height=620)
    Botao.place_forget()

def cadastro():
    print(CampoUsuario.get().strip())
    print(CampoSenha.get().strip())
    CampoUsuario.delete(0, 'end')
    CampoSenha.delete(0, 'end')

def set_transparent_entry_style(entry):
    entry.configure(background=entry.cget("bg"))
    entry.configure(highlightbackground="white", highlightcolor="white", highlightthickness=1)

# Criação Da Tela 
Tela = Tk()
Tela.geometry("370x620")
Tela.title("SoUn EasyGym")

# Incluindo Imagem de Fundo + Incluindo Tela secundaria(Quadrado Transparente)
Fundo = Image.open("C:\\Users\\evell\\OneDrive\\Documentos\\CURSO DS (ETE)\\Visual Code Projetos\\PyThon\\Projeto PI\\Imagens\\SoUn Principal.png")
Fundo = Fundo.resize((370, 620), Image.ANTIALIAS)
FundoTk = ImageTk.PhotoImage(Fundo)
label_f = Label(Tela, image=FundoTk)

# Dimensões da Tela
LarguraTela = 370
AlturaTela = 620

# Calcula as coordenadas x e y do rótulo para centralizá-la na Tela
x = (LarguraTela - Fundo.width) // 2
y = (AlturaTela - Fundo.height) // 2

# Rótulo com a imagem de fundo
label_fundo = Label(Tela, image=FundoTk)
label_fundo.place(x=x, y=y)

# Criação Da Tela2
Tela2 = Frame(Tela)
Fundo2 = Image.open("C:\\Users\\evell\\OneDrive\\Documentos\\CURSO DS (ETE)\\Visual Code Projetos\\PyThon\\Projeto PI\\Imagens\\SoUn Cadastro.png")
Fundo2 = Fundo2.resize((370, 620))
Fundo2Tk = ImageTk.PhotoImage(Fundo2)
label_fundo = Label(Tela2, image=Fundo2Tk)

LarguraTela2 = 370
AlturaTela2 = 620

x = (LarguraTela2 - Fundo2.width) // 2
y = (AlturaTela2 - Fundo2.height) // 2

label_fundo = Label(Tela2, image=Fundo2Tk)
label_fundo.place(x=x, y=y)

#Botão Tela 1 Inicial
Botao = Button(text="  Iniciar  ", bg="#d7d6ea", fg="#57d543", font=("Arial Black", 11), command= tela2)
Botao.place(x=150, y=430)

# Campo do Usuário
CampoUsuario = Entry(Tela2, text="", font=(17), width=20)
set_transparent_entry_style(CampoUsuario)
CampoUsuario.place(x=125, y=215)

# Campo da Senha
CampoSenha = Entry(Tela2, text="", font=(17), width=20, show="*")
set_transparent_entry_style(CampoSenha)
CampoSenha.place(x=125, y=300)

BotaoCadastro = Button(Tela2, text="  Cadastrar ", bg="#d7d6ea", fg="#57d543", font=("Arial Black", 11), command= cadastro)
BotaoCadastro.place(x=130, y=400)

Tela.mainloop()
import tkinter as tk
from tkinter import  ttk, font, messagebox
from tkinter import PhotoImage

# janela
janela = tk.Tk();
janela.title("App de Tarefas");
janela.configure(bg="#F0F0F0");
janela.geometry("500x600");

frameEmEdicao = None;
# funcoes
def adcionarTarefa():
    global frameEmEdicao

    tarefa = entradaTarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui:":
        if frameEmEdicao is not None:
            atualizarTarefa(tarefa)
            frameEmEdicao = None
        else:
            adcionarItemTarefa(tarefa)
            entradaTarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, insira uma tarefa")

def adcionarItemTarefa(tarefa):
    frameTarefa = tk.Frame(canvasInterior, bg="white", bd=1, relief=tk.SOLID)

    labelTarefa = tk.Label(frameTarefa, text=tarefa, font=("Garamond", 16), bg="white", width=25, height=2, anchor="w")
    labelTarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    botaoEditar = tk.Button(frameTarefa, image=iconEditar, command=lambda f=frameTarefa, l=labelTarefa: preparaEdicao(f, l), bg="white", relief=tk.FLAT)
    botaoEditar.pack(side=tk.RIGHT, padx=5)

    botaoDeletar = tk.Button(frameTarefa, image=iconDeletar,command=lambda f=frameTarefa: deletarTarefa(f), bg="white", relief=tk.FLAT)
    botaoDeletar.pack(side=tk.RIGHT, padx=5)

    frameTarefa.pack(fill=tk.X, padx=5, pady=5)

    checkButton = ttk.Checkbutton(frameTarefa, command=lambda label=labelTarefa: alterarSublinhado(label))
    checkButton.pack(side=tk.RIGHT, padx=5)

    canvasInterior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def preparaEdicao(frameTarefa, labelTarefa):
    global frameEmEdicao
    frameEmEdicao = frameTarefa
    entradaTarefa.delete(0, tk.END)
    entradaTarefa.insert(0, labelTarefa.cget("text"))

def atualizarTarefa(novaTarefa):
    global frameEmEdicao
    for widget in frameEmEdicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text= novaTarefa)

def deletarTarefa(frameTarefa):
    frameTarefa.destroy()
    canvasInterior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def alterarSublinhado(label):
    fonteAtual = label.cget("font")
    if " overstrike" in fonteAtual:
        novaFonte = fonteAtual.replace(" overstrike", "")
    else:
        novaFonte = fonteAtual + " overstrike"

    label.config(font=novaFonte)

iconEditar = PhotoImage(file="editar.png").subsample(40,40)
iconDeletar = PhotoImage(file="lixeira.png").subsample(50,50)

fonteCabecalho = font.Font(family="Garamond", size=24, weight="bold");
rotuloCabecalho = tk.Label(janela, text="App de Tarefas",font=fonteCabecalho, bg= "#F0F0F0", fg= "#333").pack(pady=20);

frame = tk.Frame(janela, bg="#F0F0F0")
frame.pack(pady=10);

# funcionalidades
entradaTarefa = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30);
entradaTarefa.pack(side=tk.LEFT, padx=10);

botaoAdicionar = tk.Button(frame, command=adcionarTarefa, text="Adicionar Tarefa", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief= tk.FLAT);
botaoAdicionar.pack(side=tk.LEFT, padx=10);

# lista de tarefas
frameListaTarefas = tk.Frame(janela, bg="white");
frameListaTarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10);

canvas = tk.Canvas(frameListaTarefas, bg="white");
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True);

scrollbar = ttk.Scrollbar(frameListaTarefas, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y);

canvas.configure(yscrollcommand=scrollbar.set);

canvasInterior = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=canvasInterior, anchor="nw")
canvasInterior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")));

janela.mainloop();
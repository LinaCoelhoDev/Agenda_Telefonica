from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#storage in memory
agenda = []
index = 0

def adicionarContato() -> None:
    #pegando o valor digitado em txt nome
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    categoria = cb_categorias.get()
    contato = {
        "nome": nome,
        "telefone": telefone,
        "categoria": categoria
    }
    
    agenda.append(contato)
    limparCampos()
    atualizarTabela()
    messagebox.showinfo("Sucesso!", "Contato adicionado com sucesso!")

def limparCampos() -> None:
    #Limpando os campos    
    txt_nome.delete(0, END)
    txt_telefone.delete(0, END)
    cb_categorias.set("")
    

def editarContato() -> None:
    agenda[index] = {
        "nome": txt_nome.get(),
        "telefone": txt_telefone.get(),
        "categoria": cb_categorias.get()
    }
    messagebox.showinfo("Editado!", "Contato atualizado com sucesso!")
    atualizarTabela()
    limparCampos()

def deletarContato() -> None:
    agenda.remove(agenda[index])
    messagebox.showinfo("Deletado!", "Contato apagado com sucesso!")
    limparCampos()
    atualizarTabela()
    
def atualizarTabela() -> None:
    #limpando a tabela 
    for linha in tabela.get_children():
        tabela.delete(linha)

    for contato in agenda:
        tabela.insert("", END, values=(contato["nome"], contato["telefone"], contato["categoria"]))

def tabelaClique(event) -> None:
    # Obtendo a linha clicada
    linha_selecionada = tabela.selection()
    global index
    index = tabela.index(linha_selecionada[0])
    contato = agenda[index]
    limparCampos()
    txt_nome.insert(0, contato['nome'])
    txt_telefone.insert(0, contato['telefone'])
    cb_categorias.set(contato['categoria'])

janela = Tk()
janela.title("Agenda Telefônica")

#Entry
label_nome = Label(janela, text="Nome: ", fg="blue", font="Tahoma 14 bold")
label_nome.grid(row=0, column=0)

txt_nome = Entry(janela, font="Tahoma 14", width=27)
txt_nome.grid(row=0, column=1)

#Entry
label_telefone = Label(janela, text="Telefone: ", fg="blue", font="Tahoma 14 bold")
label_telefone.grid(row=1, column=0)

txt_telefone = Entry(janela, font="Tahoma 14", width=27)
txt_telefone.grid(row=1, column=1)

#Combobox

label_categorias = Label(janela, text="categoria: ", fg="blue", font="Tahoma 14 bold")
label_categorias.grid(row=2, column=0)

categorias = ["Amigos","Família", "Trabalho"]
cb_categorias = ttk.Combobox(janela, values=categorias, width=25, font="Tahoma 14")
cb_categorias.grid(row=2, column=1)

#Botão
btn_adicionar = Button(janela, text="Adicionar", fg="blue", font="Tahoma 12 bold", width=8, command=adicionarContato)
btn_adicionar.grid(row=3, column=0)

btn_editar = Button(janela, text="Editar", fg="blue", font="Tahoma 12 bold", width=8, command=editarContato)
btn_editar.grid(row=3, column=1)

btn_deletar = Button(janela, text="Deletar", fg="blue", font="Tahoma 12 bold", width=8, command=deletarContato)
btn_deletar.grid(row=3, column=2)

#COMPONENTE QUE CRIA A LISTA DE CONTATOS JÁ SALVOS NA AGENDA - SE CHAMA TREEVIEW - A TABELA É A SEGUINTE:
colunas = ["Nome", "Telefone", "Categoria"]
tabela = ttk.Treeview(janela, columns=colunas, show="headings")
for coluna in colunas:
    tabela.heading(coluna, text=coluna)

tabela.grid(row=4, columnspan=3)

#CRIANDO UMA BIND
tabela.bind("<ButtonRelease-1>", tabelaClique)

#Executando a Janela
janela.mainloop()
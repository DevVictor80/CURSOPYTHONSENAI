#sistema cadastro pet

import tkinter as tk #importa ferramentas basica na biblioteca
from tkinter import ttk, messagebox #importa ferramentas especificas do tkinter

#dados em memoria
pets = []#cria a lista de pets
next_pet_id = 1#contador

# configuração da janela principal
root = tk.Tk()#cria a janela
root.title ('sistema de cadastro pets')#nome da janela
root.geometry('800x500')#tamanho da janela 
#frame do formulario
frame_form = ttk.LabelFrame(root,text='Formulario de Pet')
frame_form.pack(padx=10, pady=5, fill='x')

#campos do formulario
ttk.Label(frame_form, text='Tutor:').grid(row=0,column=0,padx=5,pady=5,sticky='e')
entry_tutor =ttk.Entry(frame_form,width=40)
entry_tutor.grid(row=0, column=1,padx=5, pady=5)

ttk.Label(frame_form, text='Nome pet:').grid(row=1,column=0,padx=5,pady=5,sticky='e') #row linha, #column coluna, padx e pady eixo x- y'
entry_nome =ttk.Entry(frame_form,width=40)
entry_nome.grid(row=1, column=1,padx=5, pady=5)

ttk.Label(frame_form, text='Especie:').grid(row=2,column=0,padx=5,pady=5,sticky='e')
entry_especie =ttk.Entry(frame_form,width=40)
entry_especie.grid(row=2, column=1,padx=5, pady=5)

ttk.Label(frame_form, text='Raça:').grid(row=3,column=0,padx=5,pady=5,sticky='e')
entry_raça =ttk.Entry(frame_form,width=40)
entry_raça.grid(row=3, column=1,padx=5, pady=5)

ttk.Label(frame_form, text='Idade:').grid(row=4,column=0,padx=5,pady=5,sticky='e')#sticky alinha o quadro na tela conforme aumenta ou diminui
entry_idade =ttk.Entry(frame_form,width=40)
entry_idade.grid(row=4, column=1,padx=5, pady=5)

#frame de button
frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=5)

btn_adicionar = ttk.Button(frame_botoes,text='Adicionar',command=None) #cria botao
btn_adicionar.grid(row=0, column=0, padx=5)

btn_editar = ttk.Button(frame_botoes,text='Editar',command=None) #cria botao
btn_editar.grid(row=0, column=1, padx=5)

btn_remover = ttk.Button(frame_botoes,text='Remover',command=None) #cria botao
btn_remover.grid(row=0, column=2, padx=5)

btn_limpar = ttk.Button(frame_botoes,text='Limpar',command=None) #cria botao
btn_limpar.grid(row=0, column=3, padx=5)

#tabela de pets
frame_tabela = ttk.Frame(root)
frame_tabela. pack(padx=10, pady=5, fill='both', expand=True)

tree = ttk.Treeview(frame_tabela,columns=('ID','Tutor','Nome pet','Especie','Raça','Idade'),show='headings')
tree.heading('ID', text='ID')
tree.heading('Tutor', text='Tutor')
tree.heading('Nome pet', text='Nome pet')
tree.heading('Especie', text='Especie')
tree.heading('Raça', text='Raça')
tree.heading('Idade', text='Idade')



root.mainloop() #loop para continuar programa, ultimo cod
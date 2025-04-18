import tkinter as tk
from tkinter import ttk, messagebox

def carregar_pets():
    for item in tree.get_children():
        tree.delete(item)
    for pet in pets:
        tree.insert('', 'end', values=(pet['Id'], pet['Tutor'], pet['Nomepet'], pet['Espécie'], pet['Raça'], pet['Idade']))

def adicionar_pet():
    global next_pet_id
    tutor = entry_tutor.get()
    nome = entry_nome.get()
    espécie = entry_espécie.get()
    raça = entry_raça.get()
    idade = entry_idade.get()
    
    if not tutor or not nome:
        messagebox.showerror('Erro', 'Tutor e nome do pet são obrigatórios!')
        return
    
    try:
        idade_int = int(idade) if idade else 0
    except ValueError:
        messagebox.showerror('Erro', 'Idade deve ser um número inteiro!')
        return
    
    novo_pet = {
        'Id': next_pet_id,
        'Tutor': tutor,
        'Nomepet': nome,
        'Espécie': espécie,
        'Raça': raça,
        'Idade': idade_int
    }

    pets.append(novo_pet)
    next_pet_id += 1

    messagebox.showinfo('Sucesso', '🐾 Pet cadastrado com sucesso!')
    limpar_campos()
    carregar_pets()

def selecionar_pet(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    
    values = tree.item(selected_item)['values']
    limpar_campos()

    entry_tutor.insert(0, values[1])
    entry_nome.insert(0, values[2])
    entry_espécie.insert(0, values[3])
    entry_raça.insert(0, values[4])
    entry_idade.insert(0, str(values[5]))

def limpar_campos():
    entry_tutor.delete(0, 'end')
    entry_nome.delete(0, 'end')
    entry_espécie.delete(0, 'end')
    entry_raça.delete(0, 'end')
    entry_idade.delete(0, 'end')

def editar_pet():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um pet para editar!')
        return

    pet_id = tree.item(selected_item)['values'][0]
    tutor = entry_tutor.get()
    nome = entry_nome.get()
    espécie = entry_espécie.get()
    raça = entry_raça.get()
    idade = entry_idade.get()

    if not tutor or not nome:
        messagebox.showerror('Erro', 'Tutor e nome do pet são obrigatórios!')
        return

    try:
        idade_int = int(idade) if idade else 0
    except ValueError:
        messagebox.showerror('Erro', 'Idade deve ser um número inteiro!')
        return

    for pet in pets:
        if pet['Id'] == pet_id:
            pet.update({
                'Tutor': tutor,
                'Nomepet': nome,
                'Espécie': espécie,
                'Raça': raça,
                'Idade': idade_int
            })
            break

    messagebox.showinfo('Sucesso', '🐶 Pet atualizado com sucesso!')
    carregar_pets()

def remover_pet():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um pet para remover!')
        return

    pet_id = tree.item(selected_item)['values'][0]

    if messagebox.askyesno('Confirmação', 'Tem certeza que deseja remover este pet?'):
        global pets
        pets = [pet for pet in pets if pet['Id'] != pet_id]
        messagebox.showinfo('Sucesso', '🐾 Pet removido com sucesso!')
        limpar_campos()
        carregar_pets()

# ------------------------ DADOS EM MEMÓRIA ------------------------
pets = []
next_pet_id = 1

# ------------------------ JANELA PRINCIPAL ------------------------
root = tk.Tk()
root.title('🐾 Sistema de Cadastro de Pets 🐶🐱')
root.geometry('850x550')
root.configure(bg='#f2f2f2')

# ------------------------ FORMULÁRIO ------------------------
frame_form = ttk.LabelFrame(root, text='📋 Formulário do Pet')
frame_form.pack(padx=15, pady=10, fill='x')

ttk.Label(frame_form, text='Tutor:').grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_tutor = ttk.Entry(frame_form, width=40)
entry_tutor.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Nome do Pet:').grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_nome = ttk.Entry(frame_form, width=40)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Espécie:').grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_espécie = ttk.Entry(frame_form, width=40)
entry_espécie.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Raça:').grid(row=3, column=0, padx=5, pady=5, sticky='e')
entry_raça = ttk.Entry(frame_form, width=40)
entry_raça.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Idade:').grid(row=4, column=0, padx=5, pady=5, sticky='e')
entry_idade = ttk.Entry(frame_form, width=40)
entry_idade.grid(row=4, column=1, padx=5, pady=5)

# ------------------------ BOTÕES ------------------------
frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=10)

btn_adicionar = ttk.Button(frame_botoes, text='➕ Adicionar', command=adicionar_pet)
btn_adicionar.grid(row=0, column=0, padx=10)

btn_editar = ttk.Button(frame_botoes, text='✏️ Editar', command=editar_pet)
btn_editar.grid(row=0, column=1, padx=10)

btn_remover = ttk.Button(frame_botoes, text='🗑️ Remover', command=remover_pet)
btn_remover.grid(row=0, column=2, padx=10)

btn_limpar = ttk.Button(frame_botoes, text='🧹 Limpar', command=limpar_campos)
btn_limpar.grid(row=0, column=3, padx=10)

# ------------------------ TABELA ------------------------
frame_tabela = ttk.Frame(root)
frame_tabela.pack(padx=15, pady=10, fill='both', expand=True)

tree = ttk.Treeview(frame_tabela, columns=('ID', 'Tutor', 'Nomepet', 'Espécie', 'Raça', 'Idade'), show='headings')

tree.heading('ID', text='ID')
tree.heading('Tutor', text='Tutor')
tree.heading('Nomepet', text='Nome do Pet')
tree.heading('Espécie', text='Espécie')
tree.heading('Raça', text='Raça')
tree.heading('Idade', text='Idade')

tree.column('ID', width=50)
tree.column('Tutor', width=150)
tree.column('Nomepet', width=120)
tree.column('Espécie', width=100)
tree.column('Raça', width=100)
tree.column('Idade', width=50)

scrollbar = ttk.Scrollbar(frame_tabela, orient='vertical')
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=tree.yview)

tree.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

tree.bind('<<TreeviewSelect>>', selecionar_pet)

# ------------------------ EXECUTA O APP ------------------------
root.mainloop()

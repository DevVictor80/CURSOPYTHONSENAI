import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json

def carregar_de_json():
    global pacientes, next_paciente_id

    arquivo = filedialog.askopenfilename(filetypes=[('Arquivos JSON', '.json')], title='Selecionar arquivos JSON para carregar')

    if not arquivo:
        return

    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            pacientes_carregados = json.load(f)

        pacientes = pacientes_carregados
        if pacientes:
            next_paciente_id = max(paciente['id'] for paciente in pacientes) + 1
        else:
            next_paciente_id = 1
        carregar_pacientes()
        messagebox.showinfo('Sucesso', f'Dados carregados com sucesso de:\n{arquivo}')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao carregar:\n{str(e)}')

def salvar_para_json():
    if not pacientes:
        messagebox.showwarning('Aviso', 'Não há pacientes!')
        return

    arquivo = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[('Arquivo JSON', '*.json')],
                                           title='Salvar lista de pacientes como json')

    if not arquivo:
        return
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(pacientes, f, ensure_ascii=False, indent=4)
        messagebox.showinfo('Sucesso', f'Dados salvos com sucesso em: \n{arquivo}')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao salvar:\n{str(e)}')

def carregar_pacientes(pacientes_list=None):
    for item in tree.get_children():
        tree.delete(item)
    pacientes_to_load = pacientes_list if pacientes_list is not None else pacientes

    for paciente in pacientes_to_load:
        tree.insert('', 'end', values=(paciente['nome'], paciente['data de nascimento'], paciente['genero'],
                                      paciente['estado civil'], paciente['profissao'], paciente['telefone']))

def adicionar_paciente():
    global next_paciente_id
    nome = entry_nome.get()
    data_de_nascimento = entry_datadenascimento.get()
    genero = entry_genero.get()
    estado_civil = entry_estadocivil.get()
    profissao = entry_profissao.get()
    telefone = entry_telefone.get()

    if not nome or not data_de_nascimento:
        messagebox.showerror('Erro', 'Nome e data de nascimento são obrigatórios!')
        return

    novo_paciente = {
        'id': next_paciente_id,
        'nome': nome,
        'data de nascimento': data_de_nascimento,
        'genero': genero,
        'estado civil': estado_civil,
        'profissao': profissao,
        'telefone': telefone
    }

    pacientes.append(novo_paciente)
    next_paciente_id += 1

    messagebox.showinfo('Sucesso', 'Paciente cadastrado com sucesso!')
    limpar_campos()
    carregar_pacientes()

def selecionar_paciente(event):
    selected_item = tree.selection()
    if not selected_item:
        return

    values = tree.item(selected_item)['values']
    limpar_campos()

    entry_nome.insert(0, values[0])
    entry_datadenascimento.insert(0, values[1])
    entry_genero.insert(0, values[2])
    entry_estadocivil.insert(0, values[3])
    entry_profissao.insert(0, values[4])
    entry_telefone.insert(0, str(values[5]))

def limpar_campos():
    entry_nome.delete(0, 'end')
    entry_datadenascimento.delete(0, 'end')
    entry_genero.delete(0, 'end')
    entry_estadocivil.delete(0, 'end')
    entry_profissao.delete(0, 'end')
    entry_telefone.delete(0, 'end')

def editar_paciente():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um paciente para editar!')
        return

    paciente_id = tree.item(selected_item)['values'][0]
    nome = entry_nome.get()
    data_de_nascimento = entry_datadenascimento.get()
    genero = entry_genero.get()
    estado_civil = entry_estadocivil.get()
    profissao = entry_profissao.get()
    telefone = entry_telefone.get()

    if not nome or not data_de_nascimento:
        messagebox.showerror('Erro', 'Nome e data de nascimento são obrigatórios!')
        return

    for paciente in pacientes:
        if paciente['id'] == paciente_id:
            paciente.update({
                'nome': nome,
                'data de nascimento': data_de_nascimento,
                'genero': genero,
                'estado civil': estado_civil,
                'profissao': profissao,
                'telefone': telefone
            })
            break

    messagebox.showinfo('Sucesso', 'Paciente atualizado com sucesso!')
    carregar_pacientes()

def remover_paciente():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um paciente para remover!')
        return

    paciente_id = tree.item(selected_item)['values'][0]

    if messagebox.askyesno('Confirmação', 'Tem certeza que deseja remover este paciente?'):
        global pacientes
        pacientes = [paciente for paciente in pacientes if paciente['id'] != paciente_id]
        messagebox.showinfo('Sucesso', 'Paciente removido com sucesso!')
        limpar_campos()
        carregar_pacientes()

def pesquisa_por_paciente():
    termo_pesquisa = entry_nome.get().lower()

    if not termo_pesquisa:
        carregar_pacientes()
        return

    pacientes_encontrados = [paciente for paciente in pacientes if termo_pesquisa in paciente['nome'].lower()]

    if not pacientes_encontrados:
        messagebox.showinfo('Pesquisa', 'Nenhum paciente encontrado!')
        carregar_pacientes()
    else:
        carregar_pacientes(pacientes_encontrados)

# dados em memória
pacientes = []
next_paciente_id = 1

# configuração da janela principal
root = tk.Tk()
root.title('Sistema de Cadastro de Pacientes')
root.geometry('800x500')

# frame do formulário
frame_form = ttk.LabelFrame(root, text='Formulário de Paciente')
frame_form.pack(padx=10, pady=5, fill='x')

# campos do formulário
ttk.Label(frame_form, text='Nome:').grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_nome = ttk.Entry(frame_form, width=40)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Data de nascimento:').grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_datadenascimento = ttk.Entry(frame_form, width=40)
entry_datadenascimento.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Gênero:').grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_genero = ttk.Entry(frame_form, width=40)
entry_genero.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Estado civil:').grid(row=3, column=0, padx=5, pady=5, sticky='e')
entry_estadocivil = ttk.Entry(frame_form, width=40)
entry_estadocivil.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Profissão:').grid(row=4, column=0, padx=5, pady=5, sticky='e')
entry_profissao = ttk.Entry(frame_form, width=40)
entry_profissao.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Telefone:').grid(row=5, column=0, padx=5, pady=5, sticky='e')
entry_telefone = ttk.Entry(frame_form, width=40)
entry_telefone.grid(row=5, column=1, padx=5, pady=5)

# frame de botões
frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=5)

btn_adicionar = ttk.Button(frame_botoes, text='Adicionar', command=adicionar_paciente)
btn_adicionar.grid(row=0, column=0, padx=5)

btn_editar = ttk.Button(frame_botoes, text='Editar', command=editar_paciente)
btn_editar.grid(row=0, column=1, padx=5)

btn_remover = ttk.Button(frame_botoes, text='Remover', command=remover_paciente)
btn_remover.grid(row=0, column=2, padx=5)

btn_salvar = ttk.Button(frame_botoes, text='Salvar', command=salvar_para_json)
btn_salvar.grid(row=0, column=3, padx=5)

btn_carregar = ttk.Button(frame_botoes, text='Carregar', command=carregar_de_json)
btn_carregar.grid(row=0, column=4, padx=5)

# treeview para mostrar pacientes
tree = ttk.Treeview(root, columns=('Nome', 'Data de nascimento', 'Gênero', 'Estado civil', 'Profissão', 'Telefone'),
                    show='headings')
tree.pack(padx=10, pady=10, fill='x')

for col in tree['columns']:
    tree.heading(col, text=col)

tree.bind('<ButtonRelease-1>', selecionar_paciente)

root.mainloop()

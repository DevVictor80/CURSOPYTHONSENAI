#sistema cadastro pet
import tkinter as tk #importa ferramentas basica na biblioteca
from tkinter import ttk, messagebox, filedialog #importa ferramentas especificas do tkinter
import json #import necessario para trabalhar com JSON
def carregar_de_json():
    global pacientes, next_paciente_id

    arquivo = filedialog.askopenfilename(filetypes=[('Arquivos JSON', '.json')], title='Selecionar arquivos JSON para carregar')

    if not arquivo: # se o usuario cancelar 
        return

    try:#todo try precisa ter um except exception
        with open (arquivo, 'r', encoding='utf-8') as f: 
            pacientes_carregados = json.load(f)

        #atualiza a lista de pets e o proximo id
        pacientes = pacientes_carregados
        if pacientes:
            next_paciente_id=max(paciente['nome']for paciente in pacientes)+1
        else :
              next_paciente_nome =1
        carregar_pacientes()
        messagebox.showinfo('Sucesso', f'Dados carregados com sucesso de:\n{arquivo}')
    except Exception as e: messagebox.showerror('Erro', f'Ocorreu um erro ao carregar:\n{str(e)}')

def salvar_para_json():
    if not pacientes:
        messagebox.showwarning('Aviso', 'Não há pacientes !')
        return
    
    #Abre a janela para selecionar onde salvar o arquivo 
    arquivo = filedialog.asksaveasfilename( defaultextension=',json', filetypes= [('Arquivo JSON','*.json')],
    title ='Salvar lista de pacientes como json' )

    if not arquivo: #se o usuario cancelar 
        return
    try: # verifica se vai dar erro try (tentar)
        with open (arquivo, 'w', encoding= 'utf-8') as f: json.dump(pets, f, ensure_ascii=False, indent=4)
        messagebox.showinfo ('Sucesso', f'Dados salvos com sucesso em: \n{arquivo}')
    except Exception as e:
        messagebox.showerror ('Erro', f'Ocorreu um erro ao salvar:\n{str(e)}')
                                            


def carregar_pacientes(pacientes_list=None):
    for item in tree.get_children():
        tree.delete(item)
    pacientes_to_load = pacientes_list if pacientes_list is not None else pacientes 

    for paciente in  pacientes_to_load: tree.insert('','end', values=(paciente['nome'], paciente['data de nascimento'], paciente['genero'], paciente['estado civil'], paciente['profissao'], paciente['telefone']))


def adicionar_paciente():
    global next_pet_id
    data_de_nascimento = entry_datadenascimento.get()
    genero = entry_genero.get()
    estado_civil = entry_estadocivil.get()
    profissao = entry_profissao.get()
    telefone = entry_telefone.get()
    
    if not tutor or not nome:
        messagebox.showerror('Erro', 'nome e data de nascimento são obrigatorios!')
        return
    
    try: 
        idade_int= int(idade) if idade else 0
    except ValueError:
        messagebox.showerror('Erro', 'data de nscimento deve ser um numero inteiro!')
        return
    
    novo_paciente = { 'nome': next_nome_id, 'data de nascimento': entry_datadenascimento, 'genero': entry_genero, 'estado civil': entry_estadocivil, 'profissao': entry_profissao, 'telefone': entry_telefone}

    pets.append(novo_pet)
    next_pet_id += 1

    messagebox.showinfo ('Sucesso', 'Pet cadastrado com sucesso!')
    limpar_campos()
    carregar_paciente()
def selecionar_paciente(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    
    values = tree.item(selected_item)['values']
    limpar_campos()

    entry_nome.insert(0, values[1])
    entry_datadenascimento.insert(0, values[2])
    entry_estadocivil.insert(0, values[3])
    entry_profissao.insert(0, values[4])
    entry_telefone.insert(0, str(values[5]))
    
def limpar_campos(): #limpa o campo 
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
    
    pet_id = tree.item(selected_item)['values'][0]
    data_de_nscimento = entry_datadenascimento.get()
    genero = entry_genero.get()
    estado_civil = entry_estado_civil.get()
    profissao= entry_profissao.get()
    telefone = entry_telefone.get()

    if not paciente or not nome:
        messagebox.showerror('Erro','nome e data de nascimento do paciente são obrigatorios!')
        return
    
    try:
        idade_int = int(idade) if idade else 0
    except ValueError:
        messagebox.showerror('Erro ', 'Idade deve ser um numero inteiro!')
        return
    for pet in pets:
        if paciente['nome'] == nome_id:
            paciente.update({ 'nome': nome, 'data de nascimento': data_de_nascimento, 'estado civil': estado_civil, 'profissao': profissao, 'telefone': telefone })
            break
    messagebox.showinfo('Sucesso', 'paciente atualizado com sucesso!')
    carregar_paciente()

def remover_paciente():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', ' selecione um paciente para remover!')
        return
    
    paciente_id = tree.item(selected_item)['values'][0]

    if messagebox.askyesno('Confirmação', 'Tem certeza que deseja remover este paciente?'):
        global pacientes
        paciente = [paciente for paciente in pacientes if paciente ['nome'] != nome_id]
        messagebox.showinfo('Sucesso', 'paciente removido com sucesso!')

        limpar_campos()
        carregar_paciente()


def pesquisa_por_paciente():
    termo_pesquisa = entry_paciente.get().lower()#lower pesquisa em letras minuscula 

    if not termo_pesquisa:
        carregar_paciente()
        return
    
    pacientes_encontrados = [paciente for paciente in pacientes if termo_pesquisa in pet['nome'].lower()]

    if not paciente_encontrados:
        messagebox.showinfo('Pesquisa','Nenhum paciente encontrado para este tutor')

        carregar_paciente()
    else:
        carregar_paciente(paciente_encontrados)


    #dados em memoria
pets = []#cria a lista de pets
next_pet_id = 1#contador

# configuração da janela principal
root = tk.Tk()#cria a janela
root.title ('sistema de cadastro paciente')#nome da janela
root.geometry('800x500')#tamanho da janela 
#frame do formulario
frame_form = ttk.LabelFrame(root,text='formulario de paciente')
frame_form.pack(padx=10, pady=5, fill='x')

#campos do formulario
ttk.Label(frame_form, text='nome:').grid(row=0,column=0,padx=5,pady=5,sticky='e')
entry_nome =ttk.Entry(frame_form,width=40)
entry_nome.grid(row=0, column=0,padx=5, pady=5)

ttk.Label(frame_form, text='data de nascimento:').grid(row=0,column=0,padx=5,pady=5,sticky='e')
entry_datadenascimento =ttk.Entry(frame_form,width=40)
entry_datadenascimento.grid(row=0, column=1,padx=5, pady=5)

ttk.Label(frame_form, text='genero:').grid(row=1,column=0,padx=5,pady=5,sticky='e') #row linha, #column coluna, padx e pady eixo x- y'
entry_genero =ttk.Entry(frame_form,width=40)
entry_genero.grid(row=1, column=1,padx=5, pady=5)

ttk.Label(frame_form, text='estado civil:').grid(row=2,column=0,padx=5,pady=5,sticky='e')
entry_estadocivil =ttk.Entry(frame_form,width=40)
entry_estadocivil.grid(row=2, column=1,padx=5, pady=5)

ttk.Label(frame_form, text='profissao:').grid(row=3,column=0,padx=5,pady=5,sticky='e')
entry_profissao =ttk.Entry(frame_form,width=40)
entry_profissao.grid(row=3, column=1,padx=5, pady=5)

ttk.Label(frame_form, text='telefone:').grid(row=4,column=0,padx=5,pady=5,sticky='e')#sticky alinha o quadro na tela conforme aumenta ou diminui
entry_telefone =ttk.Entry(frame_form,width=40)
entry_telefone.grid(row=4, column=1,padx=5, pady=5)

#frame de button
frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=5)

btn_adicionar = ttk.Button(frame_botoes,text='Adicionar',command=adicionar_paciente) #cria botao
btn_adicionar.grid(row=0, column=0, padx=5)

btn_editar = ttk.Button(frame_botoes,text='Editar',command=editar_paciente) #cria botao
btn_editar.grid(row=0, column=1, padx=5)

btn_remover = ttk.Button(frame_botoes,text='Remover',command=remover_paciente) #cria botao
btn_remover.grid(row=0, column=2, padx=5)

btn_limpar = ttk.Button(frame_botoes,text='Limpar',command=limpar_campos) #cria botao
btn_limpar.grid(row=0, column=3, padx=5)

btn_pesquisar = ttk.Button (frame_botoes,text='data de nascimento', command=pesquisa_por_data_de_nascimento)
btn_pesquisar.grid(row=0,column=4, padx=5)

btn_salvar_json = ttk.Button (frame_botoes,text='Salvar Json', command=salvar_para_json)
btn_salvar_json.grid(row=0, column=5, padx=5)
btn_carregar_json = ttk.Button (frame_botoes,text='Carregar Json', command=carregar_de_json)
btn_carregar_json.grid(row=0, column=6, padx=5)
#tabela de pets
frame_tabela = ttk.Frame(root)
frame_tabela. pack(padx=10, pady=5, fill='both', expand=True)

tree = ttk.Treeview(frame_tabela,columns=('nome','data de nascimento','genero','estado civil','profissao','telefone'),show='headings')

#cria cabeçalho
tree.heading('nome', text='nome')
tree.heading('data de nascimento', text='data de nascimento')
tree.heading('genero', text='genero')
tree.heading('estado civil', text='estado civil')
tree.heading('profissao', text='profissao')
tree.heading('telefone', text='telefone')

#cria colunas
tree.column('nome', width=50)#width e na horizontal
tree.column('data de nascimento', width=150)
tree.column('genero', width=100)
tree.column('estado civil', width=100)
tree.column('profissao', width=100)
tree.column('telefone', width=50)

#cria barra de rolagem
scrollbar = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right',fill='y')

tree.bind('<<TreeviewSelect>>', selecionar_paciente)#bind monitora os comandos utilizados


root.mainloop() #loop para continuar programa, ultimo cod
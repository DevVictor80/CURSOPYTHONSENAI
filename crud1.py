#sistema cadastro pet
import tkinter as tk #importa ferramentas basica na biblioteca
from tkinter import ttk, messagebox, filedialog #importa ferramentas especificas do tkinter
import json #import necessario para trabalhar com JSON
def carregar_de_json():
    global pets, next_pet_id

    arquivo = filedialog.askopenfilename(filetypes=[('Arquivos JSON', '.json')], title='Selecionar arquivos JSON para carregar')

    if not arquivo: # se o usuario cancelar 
        return

    try:#todo try precisa ter um except exception
        with open (arquivo, 'r', encoding='utf-8') as f: 
            pets_carregados = json.load(f)

        #atualiza a lista de pets e o proximo id
        pets = pets_carregados
        if pets:
            next_pet_id=max(pet['Id']for pet in pets)+1
        else :
              next_pet_id =1
        carregar_pets()
        messagebox.showinfo('Sucesso', f'Dados carregados com sucesso de:\n{arquivo}')
    except Exception as e: messagebox.showerror('Erro', f'Ocorreu um erro ao carregar:\n{str(e)}')

def salvar_para_json():
    if not pets:
        messagebox.showwarning('Aviso', 'Não há pets !')
        return
    
    #Abre a janela para selecionar onde salvar o arquivo 
    arquivo = filedialog.asksaveasfilename( defaultextension=',json', filetypes= [('Arquivo JSON','*.json')],
    title ='Salvar lista de pets como json' )

    if not arquivo: #se o usuario cancelar 
        return
    try: # verifica se vai dar erro try (tentar)
        with open (arquivo, 'w', encoding= 'utf-8') as f: json.dump(pets, f, ensure_ascii=False, indent=4)
        messagebox.showinfo ('Sucesso', f'Dados salvos com sucesso em: \n{arquivo}')
    except Exception as e:
        messagebox.showerror ('Erro', f'Ocorreu um erro ao salvar:\n{str(e)}')
                                            


def carregar_pets(pets_list=None):
    for item in tree.get_children():
        tree.delete(item)
    pets_to_load = pets_list if pets_list is not None else pets 

    for pet in  pets_to_load: tree.insert('','end', values=(pet['Id'], pet['Tutor'], pet['Nomepet'], pet['Espécie'], pet['Raça'], pet['Idade']))


def adicionar_pet():
    global next_pet_id
    tutor = entry_tutor.get()
    nome = entry_nome.get()
    espécie = entry_espécie.get()
    raça = entry_raça.get()
    idade = entry_idade.get()
    
    if not tutor or not nome:
        messagebox.showerror('Erro', 'Tutor e nome do pet são obrigatorios!')
        return
    
    try: 
        idade_int= int(idade) if idade else 0
    except ValueError:
        messagebox.showerror('Erro', 'idade deve ser um numero inteiro!')
        return
    
    novo_pet = { 'Id': next_pet_id, 'Tutor': tutor, 'Nomepet': nome, 'Espécie': espécie, 'Raça': raça, 'Idade': idade_int}

    pets.append(novo_pet)
    next_pet_id += 1

    messagebox.showinfo ('Sucesso', 'Pet cadastrado com sucesso!')
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
    
def limpar_campos(): #limpa o campo 
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
        messagebox.showerror('Erro','Tutor e nome do pet são obrigatorios!')
        return
    
    try:
        idade_int = int(idade) if idade else 0
    except ValueError:
        messagebox.showerror('Erro ', 'Idade deve ser um numero inteiro!')
        return
    for pet in pets:
        if pet['Id'] == pet_id:
            pet.update({ 'Tutor': tutor, 'Nome': nome, 'Espécie': espécie, 'Raça': raça, 'Idade': idade_int })
            break
    messagebox.showinfo('Sucesso', 'Pet atualizado com sucesso!')
    carregar_pets()

def remover_pet():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', ' Selecione um pet para remover!')
        return
    
    pet_id = tree.item(selected_item)['values'][0]

    if messagebox.askyesno('Confirmação', 'Tem certeza que deseja remover este pet?'):
        global pets
        pets = [pet for pet in pets if pet ['Id'] != pet_id]
        messagebox.showinfo('Sucesso', 'Pet removido com sucesso!')

        limpar_campos()
        carregar_pets()


def pesquisa_por_tutor():
    termo_pesquisa = entry_tutor.get().lower()#lower pesquisa em letras minuscula 

    if not termo_pesquisa:
        carregar_pets()
        return
    
    pets_encontrados = [pet for pet in pets if termo_pesquisa in pet['Tutor'].lower()]

    if not pets_encontrados:
        messagebox.showinfo('Pesquisa','Nenhum pet encontrado para este tutor')

        carregar_pets()
    else:
        carregar_pets(pets_encontrados)


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

ttk.Label(frame_form, text='Espécie:').grid(row=2,column=0,padx=5,pady=5,sticky='e')
entry_espécie =ttk.Entry(frame_form,width=40)
entry_espécie.grid(row=2, column=1,padx=5, pady=5)

ttk.Label(frame_form, text='Raça:').grid(row=3,column=0,padx=5,pady=5,sticky='e')
entry_raça =ttk.Entry(frame_form,width=40)
entry_raça.grid(row=3, column=1,padx=5, pady=5)

ttk.Label(frame_form, text='Idade:').grid(row=4,column=0,padx=5,pady=5,sticky='e')#sticky alinha o quadro na tela conforme aumenta ou diminui
entry_idade =ttk.Entry(frame_form,width=40)
entry_idade.grid(row=4, column=1,padx=5, pady=5)

#frame de button
frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=5)

btn_adicionar = ttk.Button(frame_botoes,text='Adicionar',command=adicionar_pet) #cria botao
btn_adicionar.grid(row=0, column=0, padx=5)

btn_editar = ttk.Button(frame_botoes,text='Editar',command=editar_pet) #cria botao
btn_editar.grid(row=0, column=1, padx=5)

btn_remover = ttk.Button(frame_botoes,text='Remover',command=remover_pet) #cria botao
btn_remover.grid(row=0, column=2, padx=5)

btn_limpar = ttk.Button(frame_botoes,text='Limpar',command=limpar_campos) #cria botao
btn_limpar.grid(row=0, column=3, padx=5)

btn_pesquisar = ttk.Button (frame_botoes,text='Pesquisar tutor', command=pesquisa_por_tutor)
btn_pesquisar.grid(row=0,column=4, padx=5)

btn_salvar_json = ttk.Button (frame_botoes,text='Salvar Json', command=salvar_para_json)
btn_salvar_json.grid(row=0, column=5, padx=5)
btn_carregar_json = ttk.Button (frame_botoes,text='Carregar Json', command=carregar_de_json)
btn_carregar_json.grid(row=0, column=6, padx=5)
#tabela de pets
frame_tabela = ttk.Frame(root)
frame_tabela. pack(padx=10, pady=5, fill='both', expand=True)

tree = ttk.Treeview(frame_tabela,columns=('ID','Tutor','Nomepet','Espécie','Raça','Idade'),show='headings')

#cria cabeçalho
tree.heading('ID', text='ID')
tree.heading('Tutor', text='Tutor')
tree.heading('Nomepet', text='Nome pet')
tree.heading('Espécie', text='Especie')
tree.heading('Raça', text='Raça')
tree.heading('Idade', text='Idade')

#cria colunas
tree.column('ID', width=50)#width e na horizontal
tree.column('Tutor', width=150)
tree.column('Nomepet', width=100)
tree.column('Espécie', width=100)
tree.column('Raça', width=100)
tree.column('Idade', width=50)

#cria barra de rolagem
scrollbar = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right',fill='y')

tree.bind('<<TreeviewSelect>>', selecionar_pet)#bind monitora os comandos utilizados


root.mainloop() #loop para continuar programa, ultimo cod
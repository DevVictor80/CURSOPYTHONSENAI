#streamlit run nomearquivo.py cria a pagina web

#primeiro comando chamar

import streamlit as st #st abreviação streamlit 
import json
import os
import datetime
ARQUIVO_DADOS= 'veiculos.json'

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS,'r', encoding="utf-8") as f:
            return json.load(f)
    return{}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def criar_veiculo(marca, modelo, combustivel, cor, renavam, placa, numero_do_chassi, data_fabricação, data_apreensão, data_para_ir_para_leilão):
    return{
        'marca': marca,
        'modelo': modelo,
        'combustivel': combustivel,
        'cor': cor,
        'renavam': renavam,
        'placa': placa,
        'numero_do_chassi': numero_do_chassi,
        'data_fabricaçao': data_fabricação,
        'data_apreensão': data_apreensão,
        'data_para_ir_para_leilão': data_para_ir_para_leilão,
    }

    pass

def cadastra_veiculo():
    st.title ('Cadastro motos leilao')
    marca = st.text_input ('Marca veiculo') #subistitui input
    modelo = st.text_input ('Modelo')
    combustivel = st.text_input('Combustivel')
    cor = st.text_input('Cor')
    renavan = st.text_input('RENAVAM')
    placa = st.text_input('Placa')
    numeroch = st.text_input('Numero do CHASSI')
    Dtfabricacao = st.date_input('Data Fabricação', format="DD/MM/YYYY",min_value=data_minima, max_value=data_maxima)
    Dtapreensão = st.date_input('Data apreensão', format="DD/MM/YYYY",min_value=data_minima, max_value=data_maxima)
    data_para_ir_para_leilão = st.date_input('Data para ir para leilão', format="DD/MM/YYYY",min_value=data_minima, max_value=data_maxima)

    st.write('Defeitos apresentados')
    bio = st.text_area('descreva os defeitos')# st.text_area('') abre um escritor de texto 

def listar_veiculo():
    pass
def editar_veiculo():
    pass
def excluir_veiculo():
    pass

st.sidebar.title('Menu')
opcao= st.sidebar.radio('Selecione uma opcao:',('Cadastra Veiculo','Listar Veiculo','Editar Veiculo','Excluir Veiculo'))
#st.write('Indentificação do veiculo!') #st.write subistitui print

#navegação entre paginas 
if opcao == "Cadastra Veiculo":
    cadastra_veiculo()
elif opcao == "Listar Veiculo":
    listar_veiculo()
elif opcao == "Editar Veiculo":
    editar_veiculo()
elif opcao == "Excluir Veiculo":
    excluir_veiculo()

#rodape
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvimento por victor")
st.sidebar.markdown(f"Total de Veiculos")


data_minima = datetime.date(2000,1,1)
data_maxima = datetime.date(2030,12,31)




#(write) subistitui print



#st.sidebar.title ('Cadastro motos leilao')
#opcao= st.sidebar.radio('Selecione uma opcao:',('Cadastra Veiculo','Listar Veciculo','Editar Veiculo','Excluir Veiculo'))
#st.write('Indentificação do veiculo!') #st.write subistitui print

#navegação entre paginas 
#if opcao =='Cadastro Veiculo':
 #   cadastro_veiculo()
#elif opcao == 'Listar Veiculo':
#    listar_veiculo()
#elif opcao == 'Editar Veiculo':
#     editar_veiculo()
#elif opcao == 'Excluir Veiculo':
 #    excluir_veiculo()

#rodape
#st.sidebar.markdown("---")
#st.sidebar.markdown("Desenvolvimento por victor")
#st.sidebar.markdow('Total de Veiculos')


#data_minima = datetime.date(1900,1,1)
#data_maxima = datetime.date(2100,12,31)


#nome = st.text_input ('Marca veiculo') #subistitui input
#nome = st.text_input ('Modelo')
#nome = st.text_input('Combustivel')
#nome = st.text_input('Cor')
#nome = st.text_input('RENAVAM')
#nome = st.text_input('Placa')
#nome = st.text_input('Numero do CHASSI')
#Dtnasc = st.date_input('Data de Fabricação', format="DD/MM/YYYY",min_value=data_minima, max_value=data_maxima)
#dataapreensão = st.date_input('Data de apreensão', format="DD/MM/YYYY",min_value=data_minima, max_value=data_maxima)
#dataparairparaleilão = st.date_input('Data para ir para leilão', format="DD/MM/YYYY",min_value=data_minima, max_value=data_maxima)



#st.write('Defeitos apresentados')#(write) subistitui print
#bio = st.text_area('descreva os defeitos')# st.text_area('') abre um escritor de texto 



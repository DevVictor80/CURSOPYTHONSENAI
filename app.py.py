import streamlit as st
import json
import os
import datetime
import base64

ARQUIVO_DADOS = 'veiculos.json'

# Função para adicionar imagem de fundo
def adicionar_fundo(imagem):
    if os.path.exists(imagem):
        with open(imagem, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Imagem de fundo não encontrada. Verifique o nome e se está na mesma pasta.")

# Função para aplicar estilo ao texto
def destacar_texto():
    st.markdown("""
        <style>
        .stApp {
            color: white !important;
            text-shadow: 1px 1px 2px black;
        }
        .stTextInput > div > div,
        .stTextArea > div > div,
        .stDateInput > div > div {
            background-color: rgba(0, 0, 0, 0.5) !important;
            border-radius: 5px;
            padding: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

# Aplicando imagem de fundo e destaque
adicionar_fundo("fundo.jpg.jpg")
destacar_texto()

# Demais funções
def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def criar_veiculo(marca, modelo, combustivel, cor, renavam, placa, numero_do_chassi, data_fabricacao, data_apreensao, data_para_leilao, defeitos):
    return {
        'marca': marca,
        'modelo': modelo,
        'combustivel': combustivel,
        'cor': cor,
        'renavam': renavam,
        'placa': placa,
        'numero_do_chassi': numero_do_chassi,
        'data_fabricacao': str(data_fabricacao),
        'data_apreensao': str(data_apreensao),
        'data_para_leilao': str(data_para_leilao),
        'defeitos': defeitos
    }

def cadastra_veiculo():
    st.title('Cadastro de Motos para Leilão')
    marca = st.text_input('Marca do veículo')
    modelo = st.text_input('Modelo')
    combustivel = st.text_input('Combustível')
    cor = st.text_input('Cor')
    renavam = st.text_input('RENAVAM')
    placa = st.text_input('Placa')
    numeroch = st.text_input('Número do CHASSI')
    data_minima = datetime.date(1980, 1, 1)
    data_maxima = datetime.date.today()
    data_fabricacao = st.date_input('Data de Fabricação', min_value=data_minima, max_value=data_maxima)
    data_apreensao = st.date_input('Data de Apreensão', min_value=data_minima, max_value=data_maxima)
    data_para_leilao = st.date_input('Data para Leilão', min_value=data_minima, max_value=data_maxima)
    defeitos = st.text_area('Descreva os defeitos')

    if st.button('Salvar Veículo'):
        if not all([marca, modelo, combustivel, cor, renavam, placa, numeroch]):
            st.warning("Preencha todos os campos obrigatórios.")
            return
        dados = carregar_dados()
        if renavam in dados:
            st.warning("Já existe um veículo com esse RENAVAM.")
        else:
            novo_veiculo = criar_veiculo(marca, modelo, combustivel, cor, renavam, placa, numeroch, data_fabricacao, data_apreensao, data_para_leilao, defeitos)
            dados[renavam] = novo_veiculo
            salvar_dados(dados)
            st.success('Veículo cadastrado com sucesso!')

def listar_veiculo():
    st.title("Lista de Veículos Cadastrados")
    dados = carregar_dados()
    if not dados:
        st.info("Nenhum veículo cadastrado.")
    else:
        for renavam, veiculo in dados.items():
            st.subheader(f"RENAVAM: {renavam}")
            for chave, valor in veiculo.items():
                st.write(f"{chave.capitalize()}: {valor}")
            st.markdown("---")

def editar_veiculo():
    st.title("Editar Veículo")
    dados = carregar_dados()
    if not dados:
        st.info("Nenhum veículo cadastrado para editar.")
        return
    renavam_selecionado = st.selectbox("Selecione o RENAVAM para editar", list(dados.keys()))
    veiculo = dados.get(renavam_selecionado)
    if veiculo:
        marca = st.text_input('Marca', value=veiculo['marca'])
        modelo = st.text_input('Modelo', value=veiculo['modelo'])
        combustivel = st.text_input('Combustível', value=veiculo['combustivel'])
        cor = st.text_input('Cor', value=veiculo['cor'])
        placa = st.text_input('Placa', value=veiculo['placa'])
        numeroch = st.text_input('Número do CHASSI', value=veiculo['numero_do_chassi'])
        try:
            data_fabricacao = st.date_input('Data de Fabricação', value=datetime.date.fromisoformat(veiculo['data_fabricacao']))
            data_apreensao = st.date_input('Data de Apreensão', value=datetime.date.fromisoformat(veiculo['data_apreensao']))
            data_para_leilao = st.date_input('Data para Leilão', value=datetime.date.fromisoformat(veiculo['data_para_leilao']))
        except Exception:
            st.error("Erro ao converter datas. Verifique o formato no arquivo JSON.")
            return
        defeitos = st.text_area('Descreva os defeitos', value=veiculo['defeitos'])

        if st.button("Salvar Alterações"):
            veiculo_editado = criar_veiculo(marca, modelo, combustivel, cor, renavam_selecionado,
                                            placa, numeroch, data_fabricacao, data_apreensao, data_para_leilao, defeitos)
            dados[renavam_selecionado] = veiculo_editado
            salvar_dados(dados)
            st.success("Veículo atualizado com sucesso!")

def excluir_veiculo():
    st.title("Excluir Veículo")
    dados = carregar_dados()
    if not dados:
        st.info("Nenhum veículo cadastrado para excluir.")
        return
    renavam_selecionado = st.selectbox("Selecione o RENAVAM para excluir", list(dados.keys()))
    if st.button("Excluir Veículo"):
        if renavam_selecionado in dados:
            del dados[renavam_selecionado]
            salvar_dados(dados)
            st.success(f"Veículo com RENAVAM {renavam_selecionado} excluído com sucesso.")
        else:
            st.error("RENAVAM não encontrado.")

# Sidebar
st.sidebar.title('Menu')
opcao = st.sidebar.radio('Selecione uma opção:', ('Cadastra Veiculo', 'Listar Veiculo', 'Editar Veiculo', 'Excluir Veiculo'))

if opcao == "Cadastra Veiculo":
    cadastra_veiculo()
elif opcao == "Listar Veiculo":
    listar_veiculo()
elif opcao == "Editar Veiculo":
    editar_veiculo()
elif opcao == "Excluir Veiculo":
    excluir_veiculo()

st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvimento por Victor")
dados = carregar_dados()
st.sidebar.markdown(f"Total de Veículos: **{len(dados)}**")

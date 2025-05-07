import streamlit as st

# Título do aplicativo
st.title("Cadastro de Motos leilão")

# Formulário de cadastro
with st.form(key='cadastro_moto'):
    # Identificação do Veículo
    st.header("Identificação do Veículo")
    marca = st.text_input("Marca")
    modelo = st.text_input("Modelo")
    ano_fabricacao = st.number_input("Ano de Fabricação", min_value=1900, max_value=2025)
    cor = st.text_input("Cor")
    placa = st.text_input("Placa")
    chassi = st.text_input("Número do Chassi (VIN)")
    renavam = st.text_input("RENAVAM")

    # Especificações Técnicas
    st.header("Especificações Técnicas")
    cilindrada = st.number_input("Cilindrada (cc)", min_value=50, max_value=2000)
    potencia = st.number_input("Potência (cv)", min_value=1, max_value=200)
    combustivel = st.selectbox("Tipo de Combustível", ["Gasolina", "Etanol", "Elétrica", "Outro"])
    transmissao = st.selectbox("Tipo de Transmissão", ["Manual", "Automática", "Semi-automática"])

    # Histórico de Manutenção
    st.header("Histórico de Manutenção")
    revisao = st.text_area("Última Revisão Realizada")
    observacoes_manutencao = st.text_area("Observações Técnicas")

    # Documentação Legal
    st.header("Documentação Legal")
    licenciamento = st.date_input("Data do Licenciamento")
    ipva_pago = st.checkbox("IPVA Pago")
    dpvat_pago = st.checkbox("Seguro DPVAT Pago")
    multas = st.text_area("Multas e Infrações")

    # Dados do Antigo Proprietário
    st.header("Dados do Antigo Proprietário")
    nome_proprietario = st.text_area("Dados do propietario")

#streamlit run nomearquivo.py cria a pagina web

#primeiro comando chamar

import streamlit as st #st abreviação streamlit 
import datetime
st.title('Cadastro motos leilao')

st.write('Indentificação do veiculo!') #st.write subistitui print

data_minima = datetime.date(1900,1,1)
data_maxima = datetime.date(2100,12,31)


nome = st.text_input ('Marca veiculo') #subistitui input
nome = st.text_input ('Modelo')
nome = st.text_input('Combustivel')
nome = st.text_input('Cor')
nome = st.text_input('RENAVAM')
nome = st.text_input('Placa')
nome = st.text_input('Numero do CHASSI')
Dtnasc = st.date_input('Data de Fabricação', format="DD/MM/YYYY",min_value=data_minima, max_value=data_maxima)
dataapreensão = st.date_input('Data de apreensão', format="DD/MM/YYYY",min_value=data_minima, max_value=data_maxima)
dataparairparaleilão = st.date_input('Data para ir para leilão', format="DD/MM/YYYY",min_value=data_minima, max_value=data_maxima)



st.write('Defeitos apresentados')#(write) subistitui print
bio = st.text_area('descreva os defeitos')# st.text_area('') abre um escritor de texto 



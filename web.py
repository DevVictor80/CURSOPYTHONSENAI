#streamlit run nomearquivo.py cria a pagina web

#primeiro comando chamar

import streamlit as st #st abreviação streamlit 

st.title('ola mundo')

st.write('Hello World ! sou eu !') #subistitui print

nome = st.text_input ('Qual seu nome ?') #subistitui input
idade = st.number_input('idade?', step=1, value=0, format='%d')
Dtnasc = st.date_input('data de nascimento')
st.write(f'ola {nome} de {idade} anos!')

st.write('fale um pouco sobre você')
bio = st.text_area('')




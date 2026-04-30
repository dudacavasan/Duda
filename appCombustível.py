import streamlit as st
st.title('Calculadora de combustível')
# Quando vale a pena escolher etanol ao inves de gasolina
etanol = 0.1
gasolina = 0.1
etanol = st.number_input('Digite o valor do etanol', min_value = 0.0)
gasolina = st.number_input('Digite o valor da gasolina', min_value = 0.0)
if gasolina > 0:
  resultado = etanol/gasolina
  if resultado < 0.70:
    msg = 'Abasteça com etanol Chefe'
  else:
    msg = 'Abasteça com gasolina Chefe'
else:
   st.warning('Digite um valor acima de 0')
if st.button('Resolver'):
    st.success(msg)
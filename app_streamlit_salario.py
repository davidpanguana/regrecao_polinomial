import streamlit as sl
import json
import requests

sl.title("Modelo de Predição de Salário")

sl.write("A quanto tempo o proficional está na empresa?")
tempo_na_empresa = sl.slider("Meses", min_value=1, max_value=120, value=60, step=1)

sl.write("Qual é o nível do profissional na empresa?")
nivel_na_empresa = sl.slider("Meses", min_value=1, max_value=10, value=5, step=1)

# Preparar dados para API
input_features = {
    'tempo_na_empresa': tempo_na_empresa,
    'nivel_na_empresa': nivel_na_empresa
}

# Criar um botão e capturar um envento deste botão para desparar a API
if sl.button('Estimar Salário'):
    res = requests.post(url = "http://127.0.0.1:8000/predict", data=json.dumps(input_features))
    res_json = json.loads(res.text)
    salario =  round(res_json['salario_em_reais'],2)
    sl.subheader(f'O salario estimado é de USD {salario}')

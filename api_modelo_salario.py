from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

# Criar uma instâncaia do FastAPI
app = FastAPI()

# Criar uma classe com os dados de entreda que virão no request body com os tipos esperados
class request_body(BaseModel):
    tempo_na_empresa: int
    nivel_na_empresa: int

# Caregar Modelo para realizar a predicão
modelo_polinomial =joblib.load('./modelo_salario.pkl')

@app.post('/predict')
def predict(data: request_body):

    input_features = {
    'tempo_na_empresa': [data.tempo_na_empresa],
    'nivel_na_empresa': [data.nivel_na_empresa]
    }

    pred_df = pd.DataFrame(input_features)

    # Predicão
    y_pred = modelo_polinomial.predict(pred_df)[0].astype(float)

    return{'salario_em_reais': y_pred.tolist()}
import pandas as pd
from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI() # criando uma instância da classe FastAPI

@app.get("/verifica_plano/{id_cliente_servico}") 
def verifica_plano(id_cliente_servico):
    df_planos = pd.read_excel("planos.xlsx")
    
import pandas as pd
from fastapi import FastAPI
from query import *
from datetime import datetime, timedelta
from rotas import *
import os


app = FastAPI() # criando uma instância da classe FastAPI

@app.get("/apto_mudanca/{id_cliente_servico}") 
def verifica_apto_mudanca(id_cliente_servico):
    data_hoje = datetime.today().strftime('%Y-%m-%d')
    status_servico = pd.DataFrame(consulta_servico_habilitado(id_cliente_servico))
    status_cobranca = pd.DataFrame(consulta_cobranca_vencida(id_cliente_servico,data_hoje))
    if status_cobranca.empty and (status_servico['prefixo'] == 'servico_habilitado').any():
        datas_vencimento = datas_vencimentos_possiveis(id_cliente_servico)
        resposta = {
        "status": "success",
        "msg": "Não apto para mudança de vencimento",
        "datas": datas_vencimento 
        }
        return  resposta
    else:
        resposta = {
        "status": "success",
        "msg": "Não apto para mudança de vencimento",
        }
        return resposta


@app.get("/executa_mudanca/{id_cliente_servico}/{data_mudanca}") 
def executa_mudanca_definitivo(id_cliente_servico,data_mudanca):
    dados_rota = gera_dados_rota(id_cliente_servico,int(data_mudanca))
    resposta = executa_mudanca(id_cliente_servico, dados_rota)
    # data_atual = datetime.today()
    # data_faturamento = data_atual - timedelta(days=20)
    # if data_atual > data_faturamento:
    #     abrir_atendimento(id_cliente_servico,data_mudanca)
    if resposta.status_code == 200:
        resposta = {
        "status": "success",
        "msg": "Data de vencimento alterada com sucesso.",
        }
        return resposta
    else:
        resposta = {
        "status": "success",
        "msg": "Não foi possível alterar a data de vencimento.",
        }
        return resposta

def executa_mudanca(id_cliente_servico, dados_rota):  
    url = "https://api.testeallrede.hubsoft.com.br/api/v1/cliente/servico/{id_cliente_servico}".format(id_cliente_servico=id_cliente_servico)
    payload = json.dumps(dados_rota)
    token = os.getenv("TOKEN_TESTE")
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {token}'.format(token=token),
    'Cookie': 'hubsoft_session=nQmzXkwJCg8g2Fk3Y8mQl8KcY6bAuOCAksLD5Rhg'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    resposta = ''
    if response.status_code == 200:
        resposta = {
            "status": "success",
            "msg": "Data de vencimento alterada com sucesso.",
        }
    else:
        resposta = {
        "status": "success",
        "msg": "Não foi possível alterar a data de vencimento.",
        }
    
    return resposta

@app.get("/abre_atendimento/{id_cliente_servico}") 
def abrir_atendimento(id_cliente_servico,data_mudanca):
    dados = gera_dados_atendimento(id_cliente_servico, data_mudanca)
    status = abre_atendimento(dados)
    return status
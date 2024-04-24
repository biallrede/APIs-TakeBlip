import requests
from datetime import datetime, timedelta

def verificar_ultimo_atendimento(access_token,host):

    # Construir o URL da API
    api_url = f"{host}/api/v1/cliente/acesso/paginado/10?page=1"

    # Dados para enviar no corpo da requisição
    data = {
        "id_cliente_servico": 1604
    }

    # Configurar os headers com o token de acesso
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Fazer a solicitação POST com os dados no corpo
    response = requests.get(api_url, json=data, headers=headers)
    data_json = response.json()
    data_ult_atendimento = data_json['acessos_cliente']['data'][0]['data_cadastro']
    data_convertida = datetime.strptime(data_ult_atendimento, "%Y-%m-%d %H:%M:%S")
    dt_agora = datetime.now()
    dif = dt_agora - data_convertida
    tempo_limite = timedelta(minutes=15)
    if dif > tempo_limite:
        return 'inválido'
    else:
        return 'ok'
    
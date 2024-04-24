import requests
from ultimo_atendimento import verificar_ultimo_atendimento

# Credenciais
host = "https://api.testeallrede.hubsoft.com.br"
client_id = "108"
client_secret = "2vGFSalYQsK0o5H9NQ4Tk3OwW7s1jCUKRTeMLKMs"
username = "api@biallrede.com.br"
password = "zuUMxsWs8g7a27AP?#"
grant_type = "password"

# # Endpoint para obter token de acesso
# token_url = f"{host}/oauth/token"

# # Parâmetros para solicitação de token
# payload = {
#     "client_id": client_id,
#     "client_secret": client_secret,
#     "username": username,
#     "password": password,
#     "grant_type": grant_type
# }

# # Solicitar token de acesso
# response = requests.post(token_url, data=payload)

# # Verificar se a solicitação foi bem-sucedida
# if response.status_code == 200:
#     access_token = response.json()['access_token']
#     print("Token de acesso obtido com sucesso:", access_token)
# else:
#     print("Falha ao obter token de acesso. Código de status:", response.status_code)

access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijg3M2ZkNmJjZDIwOGI5ODUxOGI1MTkyYmFhOWZjMmQyOWQ3NzliOTFiYjI4MjVhNDk0MTQ0NjY2ODFkYTExNmQ0MmQ3MjdkOTZiNmVkYzBhIn0.eyJhdWQiOiI0IiwianRpIjoiODczZmQ2YmNkMjA4Yjk4NTE4YjUxOTJiYWE5ZmMyZDI5ZDc3OWI5MWJiMjgyNWE0OTQxNDQ2NjY4MWRhMTE2ZDQyZDcyN2Q5NmI2ZWRjMGEiLCJpYXQiOjE3MTI1Nzc5NTQsIm5iZiI6MTcxMjU3Nzk1NCwiZXhwIjoxODcwMzQ0MzUyLCJzdWIiOiIxNjU5Iiwic2NvcGVzIjpbXX0.WCyTtVPlSTGr8j1BbEk5lHGksz483zgMZ2MgDM8oZjqusvx7b8MzVUL8nHMt_NKdnTPaf2qxwLPeZunmDJib9lWpCmMd3j2gRuGNwLMZvNbfE88nmlPmY7YZkHwgFv2dWMs5LZrxo95Xv4cmQz_-PduidB-9OuTAJH_GjQ9G_RHFC-8XsbXFuXFSm0DtoLcDk-vBZccgRyao61-sOAx-p_Yj7rMWUJBsw7Y5FGaYVddPni8Ypvv_eo41GMUHzgT8dh3ICaeEm-sMtk_9RvEHNthi1OuCJCBJSZYPMtBZgKXwS8OhwPwzy0_au8D0l2HgCNcKyN6VodMxLFe6_BLO_SaxyXzDQBn7T3bSYHeQPj57Y8u6FBjQbnG3wF7xjFO2zuSjScDf17a-Q1wCFKWdJyfAGCI6CUEQqN5dE4qpgA11CU9PLCiwbWL4XdxKoevjrbknHbKoJQCtgBcAwjd75u4BFR59xvCQefDMN27ew-w5Q4mran_EdXgdncXweLeKtFSMYJm-Kv8AF-EclEzBd625khdtK-TjAkTHiYpcvaElAooq9vCPUhuVLZwiOmQow6bxKytaJhGuSfcs0GZl3bRaVp5Z_cV0Cm96ESHyvUQcDRG3__uSdUutXLiRCr80X6jaq4gHXwWCM-KNwHOE_gc-YWV5IGCTBko504HUubI'

# Exemplo de como usar o token de acesso para chamar a rota da API e passar id_cliente_serviço no corpo
if access_token:
    #verifica qual o dia e horário do último atendimento
    prosseguir_abertura = verificar_ultimo_atendimento(access_token,host)
    print(prosseguir_abertura)
    if prosseguir_abertura == 'ok':
        # Construir o URL da API
        api_url = f"{host}/api/v1/atendimento/iniciar"

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
        response = requests.post(api_url, json=data, headers=headers)

        # Verificar a resposta da API
        if response.status_code == 200:
            print("Requisição bem-sucedida.")
            print("Resposta da API:", response.json())
        else:
            print("Falha na requisição. Código de status:", response.status_code)

    else:
        print("Não é permitido abertura de atendimento para esse cliente.")
import pandas as pd 
from credentials import credenciais_banco

def consulta_cliente(cpf_cnpj,id_cliente_servico_parametro):
    conn = credenciais_banco()   
    query = '''
                select 
                a.id_cliente_servico, d.nome_razaosocial,
                case when b.descricao isnull then 'SEM TAG' else b.descricao end as nome_tag
                from cliente_servico_grupo a
                left join cliente_servico c on c.id_cliente_servico = a.id_cliente_servico
                left join cliente d on d.id_cliente = c.id_cliente
                left join grupo_cliente_servico b on b.id = a.id_grupo_cliente_servico
                where  b.ativo = true
                and d.cpf_cnpj = '{cpf_cnpj}'
                and c.data_cancelamento isnull 
                and a.id_cliente_servico = {id_cliente_servico_valor}

                    '''.format(cpf_cnpj=cpf_cnpj,id_cliente_servico_valor=id_cliente_servico_parametro)
        
    df = pd.read_sql(query,conn)
    return df
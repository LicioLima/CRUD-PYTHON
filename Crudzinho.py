import pyodbc


server = 'LINK'
database = 'POLITIQUE'
driver = '{SQL Server}'
# dados_conexao = (
#     "Driver={SQL Server};"
#     "Server=LINK;"
#     "Database=POLITIQUE;"
# )

dados_conexao = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

conexao = pyodbc.connect(dados_conexao)

print("Conexão Bem Sucedida")

cursor = conexao.cursor()

comando = """INSERT INTO tb_Embaixadores (ID_Embaixador, Nome, Data_Nascimento, Sexo, Data_Inicio, Matricula)
VALUES (6, 'Laisa', '2003-09-27','F', GETDATE(), 'E758050')"""

cursor.execute(comando)

cursor.commit()
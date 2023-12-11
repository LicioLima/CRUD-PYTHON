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
VALUES (5, 'Filispe', '1993-12-08','M', GETDATE(), 'E758040')"""

cursor.execute(comando)

cursor.commit()
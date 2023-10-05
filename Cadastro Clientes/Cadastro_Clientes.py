import sqlite3
from menu import menu

#Criação da função para conectar ao banco de dados
def conectar():
    try:
        global conn
        conn = sqlite3.connect("cadastro.db")
        global cursor 
        cursor = conn.cursor()
        print("Conexão realizada com sucesso!")
    except sqlite3.Error as erro:
        print("Erro de Conexão")

#Criação da tabela Cliente
conectar()
criar_tabela = "CREATE TABLE IF NOT EXISTS cliente(nome string, sobrenome string, idade integer, cpf integer, telefone integer, endereco string, cidade string, estado string)"
cursor.execute(criar_tabela)

#Criando uma função para coletar dados do cliente
def cadastrarCliente():
    try:
        conectar()
        nome  = input("Informe o seu Nome: ")
        sobrenome = input("Informe seu Sobrenome: ")
        idade = int(input("Informe sua Idade: "))
        cpf = int(input("Informe seu CPF: "))
        telefone = input("Informe seu Nº de Telefone: ")
        endereco = input("Informe seu Endereco: ")
        cidade = input("Informe a cidade: ")
        estado = input("Informe o Estado: ")

        inserir_cliente = "INSERT INTO cliente VALUES ('"+nome+"','"+sobrenome+"','"+str(idade)+"','"+str(cpf)+"','"+str(telefone)+"','"+endereco+"','"+cidade+"','"+estado+"')"
        cursor.execute(inserir_cliente)
        conn.commit()
        #conn.close()
        print("CLIENTE CADASTRADO COM SUCESSO")
    except sqlite3.Error as erro:
        print("Erro ao cadastrar Cliente",erro)

def exibirCliente():
    conectar()
    resultado = cursor.execute("SELECT * FROM cliente").fetchall()
    for result in resultado:
        print("##################################")
        print("Nome: ",result[0])
        print("Sobrenome: ",result[1])
        print("Idade: ",result[2])
        print("CPF: ",result[3])
        print("Telefone: ",result[4])
        print("Endereco: ",result[5])
        print("Cidade: ",result[6])
        print("Estado: ",result[7])
    #print(resultado,"\n")
    #conn.close()

def consultarCliente():
    cpf = input("Informe o CPF que deseja consultar: ")
    try:
        resultado ='''SELECT * FROM cliente WHERE cpf = ? ''',(cpf,)
        cursor.execute(resultado).fetchall()
        print("Cliente encontrado:\n",resultado)
    except sqlite3.Error as erro:
        print("Erro ao encontrar Cliente",erro)
    #conn.close()

def alterarDados():
    print("############# Alteração de dados #############")
    cpfPesquisar = consultarCliente()
    if(cpfPesquisar != 'NULL'):
        nome  = input("Informe o seu Nome: ")
        sobrenome = input("Informe seu Sobrenome: ")
        idade = int(input("Informe sua Idade: "))
        cpf = int(input("Informe seu CPF: "))
        telefone = input("Informe seu Nº de Telefone: ")
        endereco = input("Informe seu Endereco: ")
        cidade = input("Informe a cidade: ")
        estado = input("Informe o Estado: ")

        cursor.execute("UPDATE cliente SET VALUES ('"+nome+"','"+sobrenome+"','"+str(idade)+"','"+str(cpf)+"','"+str(telefone)+"','"+endereco+"','"+cidade+"','"+estado+"')")


opcao = menu()
while (opcao !='6'):
   
    if(opcao == '1'):
        cadastrarCliente()
    elif(opcao == '2'):
        exibirCliente()
    elif(opcao == '3'):
        consultarCliente()
    elif(opcao=='4'):
        alterarDados()
    opcao = menu()
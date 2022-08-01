from cadacliente import *

# ----------------------------------------- Bem vindos às funções financeiras ------------------------------------------#
# Nesta parte estão as funções de depósito em conta já cadastrada, saque, as vantagens de ser cliente BB, e o seu saldo!
# Explicarei passo a passo como eu pensei o cóigo por completo


def menusaque(): # De começo criei essa função para trazer o menu de opções
    os.system("cls")
    print("=="*39)
            # Neste menu estão linkadas todas as funções deste módulo
    print(''' 
    | ================================================ |
    | ---------- Bem vindos ao financeiro ------------ |
    | ---------- Depositar!           [1] ------------ |
    | ---------- Saque!               [2] ------------ |
    | ---------- Vantagens!           [3] ------------ |
    | ---------- Visualizar saldo     [4] ------------ |
    | ---------- Back main menu       [5] ------------ |
    | ================================================ |
            ''')
    print("=="*39)
    usuario = ' '
    usuario = input("Escolha uma opção: ") # aqui eu peço para o usuário escolher algumas das opções!
    if usuario == "1": # Se ele digitar 1, ele vai direto para a função de depósito bancário.
        deposibanco()
    elif usuario == "2": # Se ele digitar 2, ele irá direto para a função de saque bancário.
        saquebanco()
    elif usuario == "3": # Se ele digitar 3, vai aparecer na tela dele a função de vantagens.
        vantagens()
    elif usuario == "4": # se ele digitar 4, vai poder acessar o saldo em sua conta.
        saldo()
    else: # Caso ele digite qualquer outra coisa, irá aparecer uma mensagem de opção inválida.
        print('Opção inválida!')

dici = diciclientes






def deposibanco():
    os.system("cls")
    print("=="*50)
    print(''' 
    | ---------------------  Bem vindos ao depósito! -------------------------- |
    | ------- Se você está cadastrado no nosso sistema, poderá realizar seu depósito! ----------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        senha = input("Digite a senha já cadastrada em nosso sistema: ")
        if senha not in dici:
                print("Usuário não cadastrado!")
                break
        else:
            print("Usuário encontrado!")
            print(dici[senha])
            cliente = int(input("Digite o quanto você quer depositar: "))
            soma = dici[senha][4]
            soma1 = soma + cliente
            dici[senha][4] = soma1
            print('Valor depositado com sucesso!')
            
            print(f"Você depositou R${cliente} em sua conta!")
            gravclientes(diciclientes)
            break
        
            
   





def saquebanco():
    os.system("cls")
    print("=="*50)
    print(''' 
    | ---------------------  Bem vindos ao saque! -------------------------- |
    | ------- Se você está cadastrado no nosso sistema, poderá realizar seu saque! ----------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        cadastro = input("Digite a sua senha: ")
        if cadastro not in dici:
            print("Usuário não encontrado!")
            break
        else:
            print("Cliente encontrado!")
            print(dici[cadastro])
            valor = int(input('Qual o valor você quer sacar da sua conta: '))
            sub = dici[cadastro][4]
            sub1 = sub - valor 
            dici[cadastro][4] = sub1
            print('Valor sacado com sucesso!')
            print(f"Você sacou R${valor:.2f}")
            gravclientes(diciclientes)
            break
            

      
def saldo():
    os.system("cls")
    print("=="*50)
    print(''' 
    | ---------------------  Bem vindos às vantagens! -------------------------- |
    | ------- Se você está cadastrado no nosso sistema, poderá ver suas vantagens! ----------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        senha = input("Digite a senha de acesso: ")
        if senha not in dici:
            print('Usuário não encontrado!')
            break
        else:
            print("Usuário encontrado!")
            nome = dici[senha][0]
            saldo = dici[senha][4]
            print(f"Nome do usuário: {nome}")
            print(f"seu saldo é de R${saldo}")



def vantagens():
    while True:
        print(''' 
        |======================================================================================|
        |----------------------- Bem vindos às vantagens do BB --------------------------------|
        |--------------------------------------------------------------------------------------|
        |------- 1 - Nós temos as melhores taxas anuais para para empréstimos -----------------|
        |------- 2 - Nós temos as melhores facilidades para você financiar a sua casa, --------|
        |o seu carro, ou qualquer tipo de imóvel! ---------------------------------------------|
        |------- 3 - Temos as melhores linhas de crédito para micro e pequeno empreendedor ----|
        |------- 4 - Somente aqui no Banco do Brasil você consegue ter uma home broker, -------|
        |totalmente personalizada para você que quer começar os seus investimentos! -----------|
        |------- 5 - Então o que está esperando? venha logo fazer parte da família BB! --------|
        |======================================================================================|
        ''')
        input("Aperte qualquer tecla para sair: ")
        break
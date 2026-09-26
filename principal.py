import os
import sys
import platform

def teste1():
    print("\nexecutando o teste de letras...")
    print("\nabcdefghijklmnopqrstuvwxyz")
    print("\nteste executado! voltando")
def teste2():
    print("\nexecutando o teste de multiplas linhas...")
    print('''
    multiplas 
    linhas''')
    print("\nteste executado! voltando...")
def teste3():
    print("\nexecutando teste de numeros...")
    print("1234567890")
    print("\nteste executado! voltando...")
def teste4():
    print("\nexecutando o teste de numeros de multiplas linhas")
    print('''
    1234567890
    123456789
    12345678
    ...
    ''')
def exibir_menu():
    texto_menu = '''
    1 = teste de letras
    2 = teste de letras de multiplas linhas
    3 = teste de numeros
    4 = teste de numeros de multiplas linhas
    5 = sair
    '''
    print(texto_menu)

while True:
    exibir_menu()
    escolha = input("=> ")

    if escolha == "1":
        teste1()
    elif escolha == "2":
        teste2()
    elif escolha == "3":
        teste3()
    elif escolha == "4":
        teste4()
    elif escolha == "5":
        confirmacao = input("quer sair mesmo..? ;( (s/n): ")
        
        if confirmacao.upper() == "S":
            print("nãooooooooo")
            
            if platform.system() == "Windows":
                os.system("cls && exit") 
                sys.exit() 
            else:
                # linux e macOS
                os.system("exit")
                sys.exit()      
        elif confirmacao.upper() == "N":
            print("que bom que não quer sair, iremos continuar aqui!")
            input("\nenter para voltar ao menu!") 
            
    else:
        print("opção inválida, digite apenas os números indicados.")
        input("pressione enter para continuar...")

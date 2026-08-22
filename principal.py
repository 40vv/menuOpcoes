import os
import sys
import platform

def test():
    print("\nexecutando o teste 1...")
    print("\nteste executado! voltando...")
def test2():
    print("\nexecutando o teste 2...")
    print("\nteste executado! voltando...")
def exibir_menu():
    texto_menu = '''
    ===========================
    1 = teste 
    2 = testar outra opção
    3 = sair
    ===========================
    '''
    print(texto_menu)

while True:
    exibir_menu()
    escolha = input("=> ")

    if escolha == "1":
        test()
    elif escolha == "2":
        test2()
    elif escolha == "3":
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

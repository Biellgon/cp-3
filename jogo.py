# pedra, papel e tesoura
from random import choice

def opcao_jogador():
    jogador = input("\n\nEscolha pedra, papel ou tesoura: ") 
    jogador.lower()

    if jogador == "pedra":
        return  jogador
    
    elif jogador == "papel":
        return jogador
    
    elif jogador == "tesoura":
        return jogador
    else:
        print("\nOpção Invalida, tente novamente")
        opcao_jogador()

def opcao_maquina():
    maquina = choice(["pedra", "papel", "tesoura"])
    return maquina

        
def checar_resultado(jogador,maquina,resultado):
    if (jogador == "pedra") and (maquina == "tesoura")\
            or (jogador == "papel") and (maquina == "pedra")\
                or (jogador == "tesoura") and (maquina == "papel"):
            print(f"\nA maquina escolheu {maquina}, jogador venceu!")
            resultado [0] += 1
    elif jogador == maquina:
        print(f"\nA maquina escolheu{maquina}, Empate!")
    else:
        print(f"\nA maquina escolheu {maquina}, Maquina vaneceu!")
        resultado [1] += 1
    return resultado

def exibir_resultado(resultado):
    ("-"*30)
    print(f"Placar do jogador: {resultado[0]}") 
    print(f"placar da maquina: {resultado[1]}")                
    ("-"*30)
       
def menu():
    print("\ndeseja continuar jogando ?")
    while True:
        opcao = int(input("\n1-continuar jogando: \n2-encerrar o jogo: "))
        if opcao == 1 or opcao == 2:
            break
        else:
            print("\nopção invalida!")
    return opcao

resultado = [0,0]

while True:
    ("-"*30)
    jogador = opcao_jogador()
    maquina = opcao_maquina()
    ("-"*30)
    resultado = checar_resultado(jogador,maquina,resultado) 
    exibir_resultado(resultado)
    opcao = menu()
    if opcao == 2:
        break  

            
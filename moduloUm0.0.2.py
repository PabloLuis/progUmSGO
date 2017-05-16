def fecharOrdem():


    return None


def buscaOs(valor):
    #algoritmo de busca para encontrar ordens de serviço;
    ordens = []
    for indice in range(len(ordens)):
        if ordens[indice]!= valor:
            indice=+1
        else:
            return ordens[indice]


def getOptions():
    op1 = "Abrir Ordem"
    op2 = "Consultar Ordem"
    op3 = "Fechar ordem"
    op4 = "Exluir Ordem"
    return [op1,op2,op3,op4]

def getOptions2():
    #ordens = open("ordens.txt")
    chose2 = 0
    options = [0]*4
    options[0] = "TIC"
    options[1] = "EL"
    options[2] = "MEC"
    options[3] = "Voltar"
    print("Escolha uma opção de serviço","[1]",options[0],"[2]",options[1],"[3]",options[2],"[4]",options[3])
    chose2 = eval(input())
    if  chose2 == 1:
        print("Escolheu TIC")
        print("Digite a descrição:")
        desc = input("")
        print(criaOrdem(),desc)
    elif chose2 == 2:
        print("Escolheu EL")
        print("Digite a descrição:")
        desc2 = input("")
        print(criaOrdem(), desc2)
    elif chose2 == 3:
        print("Escolheu MEC")
        print("Digite a descrição:")
        desc3 = input("")
        print(criaOrdem(), desc3)
    elif chose2 == 4:
        getOptions()




def criaOrdem():
    from datetime import datetime
    now = datetime.now()
    print("Sua ordem de serviço é: ",now.minute,now.second )




def consultaOrdem():
    #ordens = open("ordens.txt")
    return None

def excuiOrdem():
    # ordens = open("ordens.txt")
    print("Deseja excluir uma ordem de serviço? [S] / [N]")
    snBool=input()
    if snBool == "S" or snBool == "s":
        print("As ordens são:")
        buscaOs()
        print("Deseja excluir qual OS?")
        excOs = int(input)
        #comparar o numero as OSs do Array.
    else:
        snBool == "n" or snBool == "N"
        print("Exibir opções ")

    return None



#PROGRAMA PRINCIPAL



print("Escolha a opção desejada: ",getOptions())
chose = int(input())

if chose == 1:
    getOptions2()
elif chose == 2:
    consultaOrdem()
elif chose == 3:
    fecharOrdem()#abrir o xml com as ordens
elif chose == 4:
    excuiOrdem() # excluir uma ordem do xml.
else:
    print("fim")








#Lucca Libanori
import re
#Inicializando váriaveis
constantes = ["T", "F"]
abreParen = "("
fechaParen = ")"
operador_unario = "\\neg"
operador_binario = ["\\lor", "\\land", "\\Rightarrow", "\\Leftrightarrow"]
parenteses = 0 
#Função para verificar a proposição.
def Proposicao(i):
    proposicao = re.search("[a-z]|[a-z]+[0-9]", expressao[i])
    if not proposicao:
        return False

    return True
#Função para identificar e conferir uma abertura de parentese.
def AbreParen(i):
    global parenteses
    parenteses += 1
#Condição criada para verificar posição da abertura do parentese.
    if (
            (i > tamanho - 1) or (expressao[i + 1] == operador_unario) or 
            (expressao[i + 1] in operador_binario) or (expressao[i + 1] == fechaParen)
    ):
        return False

    return True
#Função para identificar e conferir um fechamento de parentese.
def FechaParen(i):
    global parenteses
    parenteses -= 1
#Condição para verificar se existe uma abertura de parentese.
    if (parenteses < 0):
        return False

    return True
#Função para identificar um operador unário.
def FormulaUnaria(i):
#Condição para verificar a posição do operador.
    if (
            (i == tamanho) or (expressao[i + 1] == fechaParen) or (expressao[i + 1] in operador_binario)
    ):
        return False

    return True
#Função para identificar um operador binário.
def FormulaBinaria(i):
#Condições para verificar a posição do operador.
    if (
            (i == tamanho) or (expressao[i + 1] == fechaParen) or (expressao[i + 1] in operador_binario)
    ):
        return False

    if (
            (i == 0) or (expressao[i - 1] == abreParen) or (expressao[i - 1] == operador_unario) or
            (expressao[i - 1] in operador_binario)
    ):
        return False

    return True
#Função para verificar cada caracter da expressão.
def formula(i, funcao):
    if expressao[i] == abreParen:
        funcao = AbreParen(i)
    elif expressao[i] == fechaParen:
        funcao = FechaParen(i)
    elif expressao[i] == operador_unario:
        funcao = FormulaUnaria(i)
    elif expressao[i] in operador_binario:
        funcao = FormulaBinaria(i)
    elif expressao[i] not in constantes:
        funcao = Proposicao(i)

    if funcao and (i != tamanho):
        funcao = formula(i + 1, formula)

    return funcao
#Abre o arquivo de texto.
with open("expressao3.txt", "r") as arquivo:
    infos = arquivo.readlines()
#Le a primeira linha que informar a quantidade de expressões presentes.
    inteiro = int(infos[0])
    contador = 1
#Loop para limitar a entrada de expressões ao inteiro que foi passado 
#no arquivo de texto.
    while inteiro >= contador:
#Funcão strip utlizada para retirar o caracter especial \n.
        expressao = infos[contador].strip('\n').split()
#Váriavel para armazenar o tamanho da expressão.
        tamanho = len(expressao) - 1
#Chamando função do algoritmo
        funcao = formula(0, True)
        contador += 1
#Condição para verificar se a expressão é válida.
        if funcao and parenteses == 0:
            print('Válida')
        else:
            print('Inválida')
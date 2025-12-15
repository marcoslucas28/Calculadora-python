import os 
import time

continuar = True

def lerNumero(msg):
    while True:
        entrada = input(msg)
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida! Digite um número.")
            time.sleep(1)
            limparTerminal()


def adicao():
    n1 = lerNumero("Escolha o primeiro número: ")
    n2 = lerNumero("Escolha o segundo número: ")
    res = n1 + n2
    print("O resultado é: ", res)
    time.sleep(3)

def subtracao():
    n1 = lerNumero("Escolha o primeiro número: ")
    n2 = lerNumero("Escolha o segundo número: ")
    res = n1 - n2
    print("O resultado é: ", res)
    time.sleep(3)

def multiplicacao():
    n1 = lerNumero("Escolha o primeiro número: ")
    n2 = lerNumero("Escolha o segundo número: ")
    res = n1 * n2
    print("O resultado é: ", res)
    time.sleep(3)

def divisao():
    n1 = lerNumero("Escolha o primeiro número: ")
    while(1):
        n2 = lerNumero("Escolha o segundo número: ")
        if(n2 != 0): break;
        print("O divisor não pode ser 0")
        time.sleep(3)
        limparTerminal()

    res = n1 / n2
    print("O resultado é: ", res)
    time.sleep(3)

def limparTerminal():
    os.system("cls" if os.name == "nt" else "clear")

while(continuar):
    operacao = 0
    while(1):
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplição")
        print("4. Divisão")
        print("5. Sai")
        operacao = input("Qual operação você deseja realizar?: ")
        if operacao in ('1', '2', '3', '4', '5'):
            limparTerminal()
            break
        print("Por favor, digite uma opção valida")
        time.sleep(2)
        limparTerminal()
    
    if(operacao == '1'): adicao()
    if(operacao == '2'): subtracao()
    if(operacao == '3'): multiplicacao()
    if(operacao == '4'): divisao()
    if(operacao == '5'): 
        continuar = False
        continue
    limparTerminal()

print("Obrigado por usar a calculadora python!")
        


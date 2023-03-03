from time import sleep
import random 
from tqdm import tqdm

numeros = []
resultados = []

def carregamento():
    for i in tqdm(range(1000)):
        sleep(0.00007)

def menu():
    print('''
██       ██████  ████████ ███████ ██████  ██  █████  
██      ██    ██    ██    ██      ██   ██ ██ ██   ██ 
██      ██    ██    ██    █████   ██████  ██ ███████ 
██      ██    ██    ██    ██      ██   ██ ██ ██   ██ 
███████  ██████     ██    ███████ ██   ██ ██ ██   ██ 
                                                     
[1] Apostar

[2] Sair

    ''')
    opt = input("Opção: ")
    sleep(1)
    if opt == "1":
        print('''Escolha 5 numeros:
        
        1   2   3   4   5   6   7   8   9   10

        11  12  13  14  15  16  17  18  19  20

        21  22  23  24  25  26  27  28  29  30

        31  32  33  34  35  36  37  38  39  40

        41  42  43  44  45  46  47  48  49  50

        51  52  53  54  55  56  57  58  59  60        
        
         ''')
    elif opt == "2":
        print("Encerrando...")
        sleep(0.875)
        exit()
    
    elif opt != "1" or "2":
        print("Digite uma opção valida")
        menu()

    contador = 0
    while contador < 5:
        numipt = int(input("Digite um numero: "))
        if numipt > 60:
            print("Os numeros não podem ser maiores do que 60")
            menu()
        numeros.append(numipt)
        contador = contador + 1

    alt = 0
    contador = 0
    while contador < 5:
        alt = random.randrange(1,60)
        resultados.append(alt)
        contador = contador + 1

menu()

sumnum = sum(numeros)

sumres = sum(resultados)

sleep(1.2)
print("Aguarde estamos carregando os resultados")
carregamento()
sleep(0.4)

if sumnum == sumres:
    print("Parabéns você ganhou")
    sleep(2)
    menu()

elif sumnum != sumres:
    print(f"O resultado foi {resultados}")
    print("Não foi dessa vez, tente denovo no próximo sorteiro")
    sleep(1)
    menu()
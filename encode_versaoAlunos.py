
#importe as bibliotecas
from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import sys
from math import *

#funções a serem utilizadas
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)




def main():
    
   
    #********************************************instruções*********************************************** 
    # seu objetivo aqui é gerar duas senoides. Cada uma com frequencia corresposndente à tecla pressionada
    # então inicialmente peça ao usuário para digitar uma tecla do teclado numérico DTMF
    # agora, voce tem que gerar, por alguns segundos, suficiente para a outra aplicação gravar o audio, duas senoides com as frequencias corresposndentes à tecla pressionada, segundo a tabela DTMF
    # Essas senoides tem que ter taxa de amostragem de 44100 amostras por segundo, entao voce tera que gerar uma lista de tempo correspondente a isso e entao gerar as senoides
    # Lembre-se que a senoide pode ser construída com A*sin(2*pi*f*t)
    # O tamanho da lista tempo estará associada à duração do som. A intensidade é controlada pela constante A (amplitude da senoide). Construa com amplitude 1.
    # Some as senoides. A soma será o sinal a ser emitido.
    # Utilize a funcao da biblioteca sounddevice para reproduzir o som. Entenda seus argumento.
    # Grave o som com seu celular ou qualquer outro microfone. Cuidado, algumas placas de som não gravam sons gerados por elas mesmas. (Isso evita microfonia).
    
    # construa o gráfico do sinal emitido e o gráfico da transformada de Fourier. Cuidado. Como as frequencias sao relativamente altas, voce deve plotar apenas alguns pontos (alguns periodos) para conseguirmos ver o sinal  

    print("Inicializando encoder")
    print("Aguardando usuário")

    # num = int(input('Qual numero voce deseja transmitir de [0-9]: '))
    num = 8

    frequencias = {1 : (697, 1209), 2 : (697, 1336), 3 : (697, 1477), 'A' : (697, 1633),
            4 : (770, 1209), 5 : (770, 1336), 6 : (770, 1477), 'B' : (770, 1633),
            7 : (8552, 1209), 8 : (852, 1336), 9 : (852, 1477), 'C' : (852, 1633),
            'X' : (941, 1209), 0 : (941, 1336), '#' : (941, 1477), 'D' : (941, 1633) 
            }  

    frequencia = frequencias[num]

    taxa = 44100
    duracao = 5
    tempo = np.linspace(0, duracao, taxa*duracao)

    print(tempo)

    soma_senoides = []

    for i in tempo:
        sen1 = sin(2*pi*frequencia[0]*i)
        sen2 = sin(2*pi*frequencia[1]*i)
        soma = sen1 + sen2
        soma_senoides.append(soma)

    soma_senoides = np.array(soma_senoides)
    
    sd.play(soma_senoides, taxa)
    sd.wait()

    # plt.plot(tempo, soma_senoides)
    # plt.title('Frequências Somadas por Tempo')
    # plt.xlabel('tempo')
    # plt.ylabel('Frequencias somadas')

 
    # signal = signalMeu()
    # signal.plotFFT(soma_senoides, taxa)


if __name__ == "__main__":
    main()

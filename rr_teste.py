import os
import time
import signal
import collections 

def SIGINT_handler(sig_number, sig_stack):
    	print ("So pegando sinal de ctrl+c mesmo")

def getProcessos():
    tempo1 = int(input(" - Insira o tempo do dummy 1: "))
    tempo2 = int(input(" - Insira o tempo do dummy 2: "))
    d1 = ("dummy1.py", tempo1)
    d2 = ("dummy2.py", tempo2)
    return collections.deque([d1,d2])

def round_robin():

    quantum = float(input(" - Insira o valor do quantum: "))
    deque_processos = getProcessos()
    
    #falta ver como criar os processos e deixarem aguardando signal do escalonador
    #e pegar o tempo de entrada e em que o processo ficará em execução
    while deque_processos[0] != None:
        executavel = deque_processos[0][0]
        tempo_do_executavel = deque_processos[0][1]
        #comparar o tempo necessário para execução de cada processo com o tempo de quantum
        #executa tudo se for menor que o quantum, executa o tempo de quantum e vai pro fim da fila com o que sobrar
        pid_child = os.fork()
        if pid_child == 0:
            os.system("python3 "+executavel)
        else:
            if(tempo_do_executavel > quantum):
                time.sleep(quantum)
                deque_processos[0][1] -= quantum
            
            elif(tempo_do_executavel <= quantum):
                time.sleep(tempo_do_executavel)
                deque_processos[0][1] -= tempo_do_executavel
            
            os.kill(pid_child, signal.SIGINT)
            
            #usar rotate(-1) para mover primeiro elemento para ultima posicao
            if(deque_processos[0][1] == 0):
                deque_processos.popleft()
            else:
                deque_processos.rotate(-1)
    

def main():
    print ("Selecione o algoritmo de escalonamento\n (1) FIFO\n (2) Fair Share\n (3) Round Robin\n (0) Sair")
    
if __name__ == '__main__':
    main()
    
escolha = input ("\n - Escolha: ")

while escolha != "0":
    if escolha == "1":
            print("##### FIRST IN, FIRST OUT ########")
            print("***Algoritmo ainda não está implementado.\n")
            pass
    elif escolha == "2":
        print("########### FAIR SHARE ###########")
        print("***Algoritmo ainda não está implementado.\n")
        pass
    elif escolha == "3":
        print("\n########## ROUND ROBIN ###########")
        round_robin()
        pass
    else:
        print("\n***Escolha inválida! Tente novamente.")
        pass
    main()
    escolha = input ("\n - Escolha: ")    
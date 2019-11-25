import os
import time
import signal
import subprocess
import collections 
import queue

def getProcessos(estrutura):
    #tempo1 = int(input(" - Insira o tempo do dummy 1: "))
    #tempo2 = int(input(" - Insira o tempo do dummy 2: "))
    d1 = ("dummy1.py", 5)
    d2 = ("dummy2.py", 3)
    if(estrutura == "deque"):
        return collections.deque([d1,d2])
    elif(estrutura == "fila"):
        q = queue.Queue()
        q.put(d1)
        q.put(d2)
        return q

def first_in_first_out():
    fila_processos = getProcessos("fila")
    while not(fila_processos.empty()):
        executavel, t = fila_processos.get()
        print("\n-----------------------------------\n O processo", executavel, "está em execução \n-----------------------------------\n")
        
        proc = subprocess.Popen(['python', executavel])
        time.sleep(t)
        
        pass
        


def round_robin():

    quantum = float(input(" - Insira o valor do quantum: "))
    deque_processos = getProcessos("deque")
    
    #falta ver como criar os processos e deixarem aguardando signal do escalonador
    #e pegar o tempo de entrada e em que o processo ficará em execução
    while len(deque_processos) > 0:
        executavel = deque_processos[0][0]
        tempo_do_executavel = deque_processos[0][1]
        #comparar o tempo necessário para execução de cada processo com o tempo de quantum
        #executa tudo se for menor que o quantum, executa o tempo de quantum e vai pro fim da fila com o que sobrar
        """proc = executavel.Popen()
        try:
            outs, errs = proc.communicate(timeout=15)
        except TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()"""


        print("\n--------------------------------------------------------\n O processo", executavel, "está em execução\n--------------------------------------------------------\n")
        
        proc = subprocess.Popen(['python', executavel])
        pid = proc.pid

        #pid_child = os.fork()
        if(tempo_do_executavel > quantum):
            time.sleep(quantum)
            deque_processos[0] = (executavel, tempo_do_executavel-quantum)
        
        elif(tempo_do_executavel <= quantum):
            time.sleep(tempo_do_executavel)
            #executavel = deque_processos[0][0]
            #tempo_do_executavel = deque_processos[0][1]
            #print("oi ", deque_processos[0][1])
            deque_processos[0] = (executavel, 0) 
        
        os.kill(pid, signal.SIGINT)
        
        #usar rotate(-1) para mover primeiro elemento para ultima posicao
        if(deque_processos[0][1] == 0):
            os.kill(pid, signal.SIGKILL)
            deque_processos.popleft()
        else:
            deque_processos.rotate(-1)
    
    pass


def main():
    print ("\nSelecione o algoritmo de escalonamento\n (1) FIFO\n (2) Fair Share\n (3) Round Robin\n (0) Sair")
    escolha = input ("\n - Escolha: ")

    while escolha != "0":
        if escolha == "1":
                print("\n##### FIRST IN, FIRST OUT ########")
                first_in_first_out()
                pass
        elif escolha == "2":
            print("\n########### FAIR SHARE ###########")
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
    
if __name__ == '__main__':
    main()

import os
import time
import signal
import subprocess
import collections 
import queue

def getProcessos(estrutura):
    #tempo1 = int(input(" - Insira o tempo do dummy 1: "))
    #tempo2 = int(input(" - Insira o tempo do dummy 2: "))
    d1 = ("dummy1.py", 12)
    d2 = ("dummy2.py", 3)
    d3 = ("dummy3.py", 7)
    d4 = ("dummy4.py", 4)
    d5 = ("dummy5.py", 11)
    d6 = ("dummy6.py", 17)
    d7 = ("dummy7.py", 4)
    d8 = ("dummy8.py", 1)
    d9 = ("dummy9.py", 13)
    d10 = ("dummy10.py", 2)
    if(estrutura == "deque"):
        return collections.deque([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10])
    elif(estrutura == "fila"):
        q = queue.Queue()
        q.put(d1)
        q.put(d2)
        q.put(d3)
        q.put(d4)
        q.put(d5)
        q.put(d6)
        q.put(d7)
        q.put(d8)
        q.put(d9)
        q.put(d10)
        return q

def first_in_first_out():
    fila_processos = getProcessos("fila")
    while not(fila_processos.empty()):
        executavel, t = fila_processos.get()
        print("\n--------------------------------------------------------\n O processo", executavel, "está em execução\n--------------------------------------------------------\n")
        subprocess.Popen(['python', executavel])
        time.sleep(t)
        pass        

def fair_share():
    deque_processos = getProcessos("deque")
    #calcular tempo: 100% do tempo / n° de processos
    total_time = 0
    for dummy, time in deque_processos:
        total_time += time
    share_time = total_time / len(deque_processos)
    print("O valor do quantum utilizando fair share é ",share_time)
    round_robin(share_time)
    

def round_robin(quantum):
    deque_processos = getProcessos("deque")
    dict_proc = {}
    
    while len(deque_processos) > 0:
        executavel, tempo_do_executavel = deque_processos[0]
        
        print("\n--------------------------------------------------------\n O processo", executavel, "está em execução\n--------------------------------------------------------\n")
        
        if executavel in dict_proc:
            os.kill(dict_proc[executavel], signal.SIGCONT)
        else:
            proc = subprocess.Popen(['python ', executavel])
            dict_proc[executavel] = proc.pid
        
        if(tempo_do_executavel > quantum):
            time.sleep(quantum)
            deque_processos[0] = (executavel, tempo_do_executavel-quantum)
        
        elif(tempo_do_executavel <= quantum):
            time.sleep(tempo_do_executavel)
            deque_processos[0] = (executavel, 0) 
        
        os.kill(dict_proc[executavel], signal.SIGSTOP)
        
        #usar rotate(-1) para mover primeiro elemento para ultima posicao
        if(deque_processos[0][1] == 0):
            pid = dict_proc[executavel]
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
            fair_share()
            pass
        elif escolha == "3":
            print("\n########## ROUND ROBIN ###########")
            quantum = float(input("\n- Digite o valor do quantum: "))
            round_robin(quantum)
            pass
        else:
            print("\n***Escolha inválida! Tente novamente.")
            pass
        main()
        escolha = input ("\n - Escolha: ")
    return
    
if __name__ == '__main__':
    main()

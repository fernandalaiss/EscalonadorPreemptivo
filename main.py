import os
import time
import signal

def SIGINT_handler(sig_number, sig_stack):
    	print ("So pegando sinal de ctrl+c mesmo")

def round_robin():
    #tempo = int(input(" - Insira o tempo do dummy: "))
    dummy1 = "./dummy1.py"
    dummy2 = "./dummy2.py"
    lista_processos = [dummy1, dummy2]
    lista_tempos = []
    contador = 0
    aux = ""
    
    #falta ver como criar os processos e deixarem aguardando signal do escalonador
    #e pegar o tempo de entrada e em que o processo ficará em execução
    while lista_processos[0] != "":
        #print("O meu processo é ", processo, ".\n")
        os.system(lista_processos[0])
        while contador < quantum:
            print(lista_processos[0])
            time.sleep(1)
            contador += 1
        
        if contador == quantum:
            aux = lista_processos[0]
            lista_processos[0] = lista_processos[1]
            lista_processos[1] = aux
            contador = 0
            ##envia SIGNAL para interromper processo e o coloca no fim da fila
            #signal.signal(signal.SIGINT, SIGINT_handler)
  

def main():
    print ("Selecione o algoritmo de escalonamento\n (1) FIFO\n (2) Fair Share\n (3) Round Robin\n (0) Sair")
    
if __name__ == '__main__':
    main()
    
escolha = input (" - Escolha: ")

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
		quantum = float(input(" - Insira o valor do quantum: "))
		print("\n########## ROUND ROBIN ###########")
		round_robin()
		pass
	else:
		print("***Escolha inválida! Tente novamente.")
		pass
	main()
	escolha = input (" - Escolha: ")    
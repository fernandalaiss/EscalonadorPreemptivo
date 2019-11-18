import os
import time

def round_robin():
    print("")
    lista_processos = ["./dummy1.py", "./dummy2.py"]
    lista_tempos = []
    contador = 0
    
    #falta ver como criar os processos e deixarem aguardando signal do escalonador
    #e pegar o tempo de entrada e em que o processo ficará em execução
    for processo in lista_processos:
        #print("O meu processo é ", processo, ".\n")
        os.system(processo)
        while(contador < quantum):
            contador += 1
        
        if(contador == quantum):
            ##envia SIGNAL para interromper processo e o coloca no fim da fila
            print("já chega")    

def main():
    print ("Selecione o algoritmo de escalonamento\n (1) FIFO\n (2) Fair Share\n (3) Round Robin\n (0) Sair")
    
if __name__ == '__main__':
    main()
    
escolha = input (" - Escolha: ")
#ENQUANDO A ESCOLHA FOR DIFERENTE DE 0, EXECUTA O RESPECTIVO ALGORITMO, ABRE O GRÁFICO OU RETORNA COMANDO INVALIDO
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
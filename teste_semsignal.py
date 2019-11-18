
#FUNÇÃO DO ALGORITMO ROUND ROBIN
def rr ():
	entradas = list(tempoEntrada) #COPIA A LISTA DE ENTRADAS PARA UMA NOVA LISTA, QUE SERÁ ORDENADA
	tempos = list(tempoExecucao) # MESMA IDEIA DE CIMA
	contador = 0 
	processados = [0]*n  #CRIAMOS UMA LISTA ONDE A CADA EXECUÇÃO IREMOS INCREMENTAR O TEMPO QUE FOI EXECUTADO
	entraram = [0]*n  #CRIAMOS UMA LISTA DE 0/1 PARA SABER QUAIS PROCESSOS JA ENTRAM
	fila = [] #CRIAMOS UMA FILA, QUE IRÁ DETERMINAR QUAIS OS PROXIMOS PROCESSOS IRÃO EXECUTAR
	count = 0 
	soma = 0
	def entra():
		for x in range(0,n): #ADICIONA OS TEMPOS QUE NÃO ENTRARAM E MENORES OU IGUAL AO contador NA FILA
			if entradas[x] <= contador and entraram[x] == 0:
				#print "Entrou ", x
				entraram[x] = 1  # OS PROCESSOS QUE JÁ ENTRARAM, RECEBEM 1, ASSIM SÓ ENTRAM NOVAMENTE NA FILA EM CASO DE PREEPÇÃO
				fila.append(x)  #O PROCESSO É ADICIONADO AO FIM DA FILA
			pass
	entra()
	for processo in fila:
		#print "=====", processo, "======"
		falta = tempos[processo]-processados[processo]  #VARIÁVEL FALTA RECEBE O TEMPO DO PROCESSO - O QUE JÁ FOI PROCESSADO
		if falta > quantum: #SE FALTA MAIS QUE O QUANTUM ENTRA NO BLOCO
			contador+=quantum  #contador INCREMENTA O QUANTUM, POIS IRÁ EXECUTAR TODO O TEMPO DO QUANTUM
			entra() #VERIFICA SE ALGUM PROCESSO CHEGA DURANTE A EXECUÇÃO ATUAL
			processados[processo]+=quantum #INCREMENTA EM UM QUANTUM O QUE JÁ FOI PROCESSADO DO PROCESSO ATUAL
			#print "Executou ", processo, " até ", contador
			#print "Sobrecarga até ", contador+1
			#print processo, " foi pro fim da fila"
			fila.append(processo) #COMO O PROCESSO NÃO FOI EXECUTADO TOTALMENTE, ELE VOLTA PARA O FIM DA FILA DE EXECUÇÃO
			contador+=1 #ADIOCIONA AO contador O TEMPO DA SOBRECARGA
		elif falta <= quantum and falta > 0: #NESSE CASO VERIFICAMOS SE FALTA ALGUM TEMPO ENTRE 0 E O QUANTUM A SER EXECUTADO
			contador+=falta #INCREMENTA O RELÓGIO O TEMPO QUE FALTA
			entra() #VERIFICA SE ALGUM PROCESSO CHEGA DURANTE A EXECUÇÃO ATUAL
			processados[processo]+=falta #INCREMENTA O QUE FALTA AO QUE JÁ FOI PROCESSADO DO PROCESSO ATUAL
			soma+=contador-entradas[processo] #INCREMENTA A SOMA COM O TURNAROUND DO PROCESSO
	return float(soma/n) #RETORNA A MEDIA DOS TURNAROUND


#LEITURA DAS DEADLINES
def lerDeadlines():
	del deadlines[:] #ZERA A LISTA DE DEADLINES PARA A NOVA LEITURA
	for x in range(0,n):
		print ("Informe a Deadline do processo ", x+1, ": ")
		deadlines.append(input())
		pass

#LÊ A QUANTIDADE DE PROCESSOS E CRIA AS LISTAS DE TEMPO DE EXECUÇÃO E TEMPO DE ENTRADA PARA CADA PROCESSO
n = int(input ("Informe o numero de processos: "))
tempoExecucao = []
tempoEntrada = []
deadlines = []

#LÊ OS TEMPOS DE EXECUÇÃO E DE ENTRADA PARA CADA PROCESSO
for x in range(1,n+1):
	print ("Tempo de entrada do processo ", x, ": ")
	tempoEntrada.append(float(input()))
	print ("Tempo de execução do processo ", x, ": ")
	tempoExecucao.append(float(input()))

#SOLICITA AO USUARIO QUE INFORME O ALGORITMO DE ESCALONAMENTO DESEJADO
def menu():
	print ("Selecione o algoritmo de escalonamento\n (1) FIFO\n (2) Fair Share\n (3) Round Robin (Preemptivo)\n (0) Sair")

menu()
cmd = input ("Escolha: ")
#ENQUANDO A ESCOLHA FOR DIFERENTE DE 0, EXECUTA O RESPECTIVO ALGORITMO, ABRE O GRÁFICO OU RETORNA COMANDO INVALIDO
while cmd != "0":
	if cmd == "1":
            print("##### FIRST IN, FIRST OUT ########")
            print("Algoritmo ainda não está implementado. \n")
            pass
	elif cmd == "2":
		print("########### FAIR SHARE ###########")
		print("Algoritmo ainda não está implementado.\n")
		pass
	elif cmd == "3":
		quantum = float(input("Insira o valor do quantum: "))
		print("########## ROUND ROBIN ###########")
		print ("TURNAROUND MEDIO: ", rr())
		pass
	else:
		print("Escolha inválida! Tente novamente.")
		pass
	menu()
	cmd = input ("Escolha: ")
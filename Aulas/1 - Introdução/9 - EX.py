import os #biblioteca de comandos do terminal do sistema operacional

entrada = input('Deseja criar lista? [S][N] ')
lista = []

while entrada:
	
	if entrada == 'S' or entrada == 's':
		os.system('cls') #comando executado da biblioteca
		print('Selecione uma opção:')
		opcao = input('[I]nserir [A]pagar [L]istar ')

		if opcao == 'i' or opcao == 'I':
			for indice, nome in enumerate(lista):
						print(indice, nome)
			incluir = input('Insira um item: ')
			lista.append(incluir)
		elif opcao == 'a' or opcao == 'A':
			for indice, nome in enumerate(lista):
						print(indice, nome)
			n = input('Selecione um item numérico da lista: ')
			try:
				lista.pop(int(n))
			except:
				print('Não é um valor aceitável!')
		elif opcao == 'l' or opcao == 'L':
			if len(lista) == 0:
				print('Nada para listar!')
			else:
				for indice, nome in enumerate(lista):
					print(indice, nome)
		else:
			print('Opção inválida!')	

	elif entrada == 'N' or entrada == 'n':
		os.system('cls')
		print('Fim de lista!')
		for indice, nome in enumerate(lista):
					print(indice, nome)
		break
	else:
		os.system('cls')
		print('Opção inválida!')
	
	entrada = input('Deseja continuar na lista? [S][N] ')

# def - cria funções

def funcao(x,y):
	...

#recebem valores de parâmetros(nomes)
#servem para simplificar repetições
#retorna valores de acordo com o solicitado (None por padrão)

#argumentos podem ser nomeados ou não-nomeados(valor 'any', então recebe qualquer tipo de valor)
	# nomeados - tem nome com sinal de igual
	# não-nomeados - recebe apenas argumentos

def soma(x,y):
	print(f'{x = } y = {y} | x + y =', x + y)

soma(1, 2) # não-nomeados (posicionais)

def soma2(a,b):
	print(f'{a = } b = {b} | a + b =', a + b)

soma2(b = 'b', a = 'a') # nomeados (podem ser passados fora de ordem)
# sempre que um argumento anterior for nomeado(tanto funçaõ quanto chamada), o próximo também deve ser, ou executa ' keyword error'

#Refatorar == editar (-_-)

# Para situações em que seja necessária a criação de um parâmetro que possa ou não ser utilizado, pode-se utilizar o None

def soma3(x, y, z = None):
	if z is not None:
		print(f'{x = } {y = } {z =} |', x + y + z)
	else:
		print(f'{x = } {y = } |', x + y)

soma3(1, 2, 3)
soma3(4, 5)

'''
Escopo de funções
Escopo - local onde o código pode atingir.
Escopo local/global
local - escopo onde apenas nomes do mesmo local são alcançados (função)
global - escopo onde todo o código é alcançável (programa)
'''
# variaveis anteriores, seguindo a regra a da escrita, podem ser acessadas por funções posteriores, porém toda variavel interna a função é 'protegida' pelo escopo local

#variaveis internas tem prioridade a variaveis externas, caso sejam iguais

#variaveis externas não são modificadas por funções de variaveis internas, se forem iguais

x = 1

def escopo():
	x = 10
	def escopo2():
		y = 2
		print(x, y)
	escopo2()
	print(x)

print(x)
escopo()
print(x)

#para a modificação extrena de variaveis internamente na função, que tenham mesmo nome, se faz defindo o mesmo por 'global'

a = 2

print(a)

def globo():
	global a #definição de variavel global quando chamada a função
	a = 20
globo()

print(a)

# o escopo determina uma busca de informações do código, de dentro para fora
#call stack - visto em debug, sequencia logica em pilha para o fubncionamento do programa

#retorno (return) é o comando que define qual será o valor retornado dentro de uma função

def soma(x, y):
	return x + y #sempre finaliza a função

print(soma(1,2))

# caso não seja especificado, toda função retorna 'None'


#args - argumentos não nomeados
# * / *args (empacotamento / desempacotamento)

x, y, *resto = 1, 2, 3, 4 #empacotamento

print(x, y, *resto)

def funcao2(*args):
	print(args, type(args))
	total = 0
	for numero in args:
		total += numero
	return total

numeros = 1,2,3,4,5,6


funcao_soma1 = funcao2(1,2,3)
print(funcao_soma1)

funcao_soma2 = funcao2(4,5,6)
print(funcao_soma2)

funcao_soma_max = funcao2(*numeros) #desempacotamento
print(funcao_soma_max)

print(sum(numeros)) #sum - função padrão que executa a soma automaticamente, só podendo ser utilizado no máximo dois argumentos, e podendo também ser utilizado uma variavel de múltiplos argumentos

#Higher Order Function - Funções que podem receber e/ou retornar outras funções

#First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

def saudacao1(msg, nome):
	return f'{msg}, {nome}!'

def executa(funcao, *args):
	return funcao(*args) #LEMBRAR DE DESEMPACOTAR

print(executa(saudacao1, 'Bom dia', 'Talita'))
# Há possibilidade de executar chamada de função dentro de outra função

# Closure - aparentemente, uma função que cria outra função

def criar_saudacao(saudacao):
	def saudar(nome):
		return f'{saudacao}, {nome}!'
	return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

nomes = input('Insira nomes: ')
nomes = nomes.split()

for nome in nomes:
	print(falar_bom_dia(nome))
	print(falar_boa_noite(nome))

#A primeira função criada se torna "estática" e pré programada, sendo preparada para executar uma chamada para a segunda função, tornando editavel apenas nos pontos necessários

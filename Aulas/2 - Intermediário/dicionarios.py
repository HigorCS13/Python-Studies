#Keywords Arguments - argumentos utilizados de maneira chave/valor, em que se cria uma "chave" de chamada para acessar seu valor

# pessoa = dict(nome = 'Higor', sobrenome = 'Cunha Silva') - metodo possível
# dict - dicionários, que são formados por chaves e valores

pessoa = {
	'nome' : 'Higor',
	'sobrenome' : 'Cunha Silva',
	'idade' : 33,
	'altura' : 1.85,
	'endereço' : [
		{'rua' : 'lugar1', 'numero:' : 123},
		{'rua' : 'lugar2', 'numero:' : 456}
	]
}
# utiliza-se ":" para a divisão entre a criação da chave e o valor, e no método anterior, se utiliza "="

print(pessoa['nome'])
print(pessoa['sobrenome'])
print() # técninca para espaçamento

for chave in pessoa:
	print(chave, pessoa[chave])
print()

#chaves podem ser editadas

pessoa1 = {}

pessoa1['nome'] = 'Talita'
print(pessoa)

chave = 'nome'
pessoa1[chave] = 'Higor'

print(pessoa1)

'''
Métodos úteis em dicionários
	__len__() - quantas chaves existem
	keys() - retorna um iterável com as chaves
	values() - retorna um iterável com os valores de cada chave
	items() - retorna um iterável com chave/valor
	setdefalut(chave, valor) - adiciona chave/valor não existentes no dicionário
	copy() - executa uma cópia RASA (shallow copy) da determinada lista, sendo que, caso existam outras listas internas, será executado apenas o endereçamento
	copy.deepcopy() - executa cópia profunda (deep copy) do dicionário selecionado, deve ser usado junto a biblioteca 'copy'
	get() - obtem chave especificada, pode-se incluir um condicional de inexistência
	pop() - exclui chave e valor indicados
	popitem() - exclui de maneira orbigatória o ultimo item do dicionário
	update({...}) - método em que se pode alterar ou adicionar novas chave e valores para seu dicionário
'''

import copy #biblioteca deep copy


print(pessoa.__len__()) #também podendo ser len(pessoa)

print(list(pessoa.keys())) #pode ser convertido em tuplas, listas ou até impresso em for

print(tuple(pessoa.values())) #pode ser convertido em tuplas, listas ou até impresso em for

print(pessoa.items()) #pode ser convertido em tuplas, listas ou até impresso em for

pessoa.setdefault('cor_favorita', ['vermelho', 'preto'])
print(pessoa['cor_favorita'])
print()

pessoa1 = pessoa.copy()
pessoa1['cor_favorita'][1] = 'azul' #se feito com copia rasa, os dois são ser alterados
print(pessoa['cor_favorita'])
print(pessoa1['cor_favorita'])

pessoa1 = copy.deepcopy(pessoa)
pessoa['cor_favorita'][1] = 'preto' #se feito com copia profunda, apenas o item citado é alterado
print(pessoa['cor_favorita'])
print(pessoa1['cor_favorita'])

print(pessoa.get('nome', 'Não existe')) #exemplo com condicional de inexistência

pessoa1.pop('endereço')
print(pessoa1)

pessoa1.update({
	'nome' : 'Talita',
	'sobrenome' : 'Ribeiro',
	'idade': 25,
	'altura' : 1.73,
	'endereço' : [{'rua': 123}, {'casa': 456}]
})
# pode-se adicionar em formato de tuple ou list, em que caso seja uma alteração é necessário um virgula ao fim, caso não, apenas é feito a indicação
tupla = ('cor_favorita', 'roxo'),
pessoa1.update(tupla)
print(pessoa1)

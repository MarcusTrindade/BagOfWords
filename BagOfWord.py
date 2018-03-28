# -*- coding: utf-8 -*-
from __future__ import unicode_literals


gramatica = []
bagOfWords = []
tabelaSimilaridade = []

# Artigos definidos e indefinidos da lingua brasileira
artigos = [
	"o","a","os","as","ao","à","aos","às","do","da","dos","das","no",
	"na","nos","nas","pelo","pela","pelos","pelas","um","uma","uns",
	"umas","dum","duma","duns","dumas","num","numa","nuns","numas"
]

#Preposições da lingua brasileira
preposicoes = [
	"e","ou","a","ante","após","apos","até","ate","com","conforme","contra",
	"consoante","de","desde","durante","em","excepto","entre","mediante",
	"para","perante","por","salvo","sem","segundo","sob","sobre","trás","tras"
]

#Adicionando Artigos e Preposições na gramatica 
def addArtigoPrepo(): 
	for artigo in artigos:
		gramatica.append(artigo)
	for prepocicao in preposicoes:
		gramatica.append(prepocicao)
	return gramatica

# Abrir Arquivo, convertendo todas as palavras do arquivo para minusculo
def openFile(fileName):
	file = open(fileName,'r')
	textArq = file.readlines()
	lista = []
	for conteudo in textArq:
		lista.append(conteudo.lower())
	return lista

#Remover Artigos e preposições da gramatica
def removeAp(file):
	texto = file[0].split()
	for palavra in gramatica:
		if palavra in texto:
			texto.remove(palavra)
	return texto

#Remove artigos e preposições e adiciona na bagOfWords
def adicionarbagOfWords(file):	
	arquivo = removeAp(openFile(file + ".txt"))
	for word in arquivo:
		if word not in bagOfWords:
			bagOfWords.append(word)
	return arquivo		

#Calcular similaridade de dois textos
def similaridade(fileA,fileB):
	addArtigoPrepo()
	adicionarbagOfWords(fileA)
	adicionarbagOfWords(fileB)
	tamanhoA = len(fileA + ".txt")
	tamanhoB = len(fileB + ".txt")

		
	for i in range(0,tamanhoA):
		if i in bagOfWords:
			for j in range(0,tamanhoB):
				if j in bagOfWords:
					tabelaSimilaridade.append((i,j))
	return tabelaSimilaridade										
			
print(tabelaSimilaridade)			
print(similaridade("docA","docB"))
		


	

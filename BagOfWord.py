# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import math

gramatica = []
bagOfWords = []
tabelaSimilaridade = [[],[]]

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

#Adicionar Artigos e Preposições na gramatica 
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

#Remover artigos e preposições do arquivo texto
def adicionarbagOfWords(file):	
	arquivo = removeAp(openFile(file + ".txt"))
	for word in arquivo:
		if word not in bagOfWords:
			bagOfWords.append(word)
	return arquivo		

#Calcular similaridade de dois textos
def similaridade(fileA,fileB):
	addArtigoPrepo()
	array1 = adicionarbagOfWords(fileA)
	array2 = adicionarbagOfWords(fileB)							

	for i in range(0,len(bagOfWords)):
		if bagOfWords[i] in array1:
			tabelaSimilaridade[0].append(1)
		else:
			tabelaSimilaridade[0].append(0)

		if bagOfWords[i] in array2:
			tabelaSimilaridade[1].append(1)
		else:
			tabelaSimilaridade[1].append(0)	

similaridade("docA","docB")

def calcularSimilaridade():
	resultB = 0
	resultC = 0
	resultA = 0
	for i in range(0,len(tabelaSimilaridade)):
		if tabelaSimilaridade[0][i] == tabelaSimilaridade[1][i]:
			resultA += tabelaSimilaridade[0][i] * tabelaSimilaridade[1][i]
	for i in range(0,len(tabelaSimilaridade)+1):
		if tabelaSimilaridade[0][i] == 1 or tabelaSimilaridade[1][i] == 1:
			resultB += (tabelaSimilaridade[0][i] **2)
			resultC += (tabelaSimilaridade[1][i] **2)		 
	return  resultA / (math.sqrt(resultB) * math.sqrt(resultC))	

print("Resultado: " + str(calcularSimilaridade()))			
#!/usr/bin/env python

import os
import sys
import copy
import math
import numpy
import random

debug = False

phenotype_dict = {
	'a': 'amber',
	'b': 'bald',
	'c': 'conehead',
	'd': 'dumpy',
	'e': 'eyeless',
	'f': 'forked',
	'g': 'garnet',
	'h': 'hook',
	'i': 'indy',
	'j': 'jagged',
	'k': 'kidney',
	'l': 'lyra',
	'm': 'marula',
	'n': 'notch',
	'o': 'okra',
	'p': 'prickly',
	'q': 'quick',
	'r': 'rosy',
	's': 'scute',
	't': 'taxi',
	'u': 'upturned',
	'v': 'vestigial',
	'w': 'white',
	'x': 'xray',
	'y': 'yellow',
	'z': 'zipper',
}


def invertType(genotype, basetype):
	newtype = ''
	for i in range(3):
		if genotype[i] == '+':
			newtype += basetype[i]
		else:
			newtype += '+'
	return newtype

def flipGene(genotype, gene, basetype):
	newlist = list(genotype)
	for i in range(3):
		if basetype[i] == gene:
			if genotype[i] == '+':
				newlist[i] = basetype[i]
			else:
				newlist[i] = '+'
	newtype = ""
	for i in newlist:
		newtype += i
	return newtype

def getGeneOrder(basetype):
	basetype2 = basetype[0]+basetype[2]+basetype[1]
	basetype3 = basetype[1]+basetype[0]+basetype[2]

	#gene order
	if debug is True: print("selecting gene order")
	geneorder = random.choice([basetype, basetype2, basetype3])
	if debug is True: print(geneorder)
	return geneorder

def getDistances():
	if debug is True: print("determine gene distances")
	a = numpy.random.poisson(lam=12, size=7)
	a.sort()
	distances = [a[0], a[-1]]
	random.shuffle(distances)
	if debug is True: print(distances)
	return distances

def getProgenySize(distances):
	if debug is True: print("determine progeny size")
	gcd1 = math.gcd(distances[0], 100)
	gcd2 = math.gcd(distances[1], 100)
	gcdfinal = math.gcd(gcd1, gcd2)
	if debug is True: print("Final GCD", gcdfinal)
	progenybase = 100/gcdfinal
	minprogeny =  900/progenybase
	maxprogeny = 6000/progenybase
	progs = numpy.arange(minprogeny, maxprogeny+1, 1, dtype=numpy.float64)*progenybase
	#print(progs)
	numpy.random.shuffle(progs)
	#print(progs)
	bases = progs * distances[0] * distances[1] / 1e4
	#print(bases)
	devs = (bases - numpy.around(bases, 0))**2
	#print(devs)
	argmin = numpy.argmin(devs)
	progeny_size = int(progs[argmin])
	if debug is True: print(("total progeny: %d\n"%(progeny_size)))
	return progeny_size

def getPhenotype(genotype):
	if genotype == "+++":
		return '<I>wildtype</I>'
	phenotype_list = []
	for allele in genotype:
		if allele == '+':
			continue
		phenotype = phenotype_dict.get(allele)
		phenotype_list.append(phenotype)
	#print(phenotype_list)
	phenotype_string = ','.join(phenotype_list)
	return phenotype_string

def makeProgenyHtmlTable(typemap, progeny_size):
	alltypes = list(typemap.keys())
	alltypes.sort()
	td_extra = 'align="center" style="border: 1px solid black;"'
	table = '<table style="border-collaspe: collaspe; border: 1px solid black;">'
	table += '<tr>'
	table += '  <th colspan="3" {0}>Genotype</th>'.format(td_extra)
	table += '  <th {0}>Progeny<br/>Count</th>'.format(td_extra)
	table += '</tr>'
	for type in alltypes:
		phenotype_string = getPhenotype(type)
		table += '<tr>'
		table += ' <td {0}>{1}</td>'.format(td_extra, phenotype_string)
		table += ' <td {0}>{1}</td>'.format(td_extra, type[0])
		table += ' <td {0}>{1}</td>'.format(td_extra, type[1])
		table += ' <td {0}>{1}</td>'.format(td_extra, type[2])
		table += ' <td {0}>{1:d}</td>'.format(td_extra, typemap[type])
		table += '</tr>'
	table += '<tr>'
	table += '  <th colspan="3" align="right" style="border: 1px solid black;">TOTAL</th>'
	table += '  <td {0}>{1:d}</td>'.format(td_extra, progeny_size)
	table += '</tr>'
	table += '</table>'
	return table

def makeProgenyAsciiTable(typemap, progeny_size):
	alltypes = list(typemap.keys())
	alltypes.sort()
	table = ''
	for type in alltypes:
		phenotype_string = getPhenotype(type)
		table += ("{0}\t".format(type[0]))
		table += ("{0}\t".format(type[1]))
		table += ("{0}\t".format(type[2]))
		table += ("{0:d}\t".format(typemap[type]))
		table += ("{0}\t".format(phenotype_string))
		table += "\n"
	table +=  "\t\t\t-----\n"
	table +=  "\t\tTOTAL\t%d\n\n"%(progeny_size)
	return table

def generateProgenyData(types, type_counts, basetype):
	if debug is True: print("\n\ngenerate progeny data")
	typemap = {}
	for t in types:
		n = invertType(t, basetype)
		#rand = random.gauss(0.5, 0.01)
		try:
			count = type_counts[t]
		except KeyError:
			count = type_counts[n]
		tcount = 0
		ncount = 0
		for i in range(count):
			if random.random() > 0.5:
				tcount += 1
			else:
				ncount += 1
		sys.stderr.write(".")
		#typemap[t] = int(rand * count)
		#typemap[n] = count - typemap[t]
		typemap[t] = tcount
		typemap[n] = ncount
	sys.stderr.write("\n")
	return typemap

def generateTypeCounts(parental, doublecross, basetype):
	type_counts = {}
	if debug is True: print("determine double type")
	doubletype = flipGene(parental, geneorder[1], basetype)
	doublecount = int(round(doublecross*progeny_size/100.))
	if debug is True: print("  ", doubletype, invertType(doubletype, basetype), doublecount)
	type_counts[doubletype] = doublecount

	if debug is True: print("determine first flip")
	firsttype = flipGene(parental, geneorder[0], basetype)
	firstcount = int(round(distances[0]*progeny_size/100.)) - doublecount
	if debug is True: print("  ", firsttype, invertType(firsttype, basetype), firstcount)
	type_counts[firsttype] = firstcount

	if debug is True: print("determine second flip")
	secondtype = flipGene(parental, geneorder[2], basetype)
	secondcount = int(round(distances[1]*progeny_size/100.)) - doublecount
	if debug is True: print("  ", secondtype, invertType(secondtype, basetype), secondcount)
	type_counts[secondtype] = secondcount

	if debug is True: print("determine parental type count")
	parentcount = progeny_size - doublecount - firstcount - secondcount
	if debug is True: print("  ", parental, invertType(parental, basetype), parentcount)
	type_counts[parental] = parentcount

	return type_counts


def makeQuestion(basetype, geneorder, distances, progeny_size):
	if debug is True: print("------------")
	answerString = ("%s - %d - %s - %d - %s"
		%(geneorder[0], distances[0], geneorder[1], distances[1], geneorder[2]))
	print(answerString)
	if debug is True: print("------------")

	if debug is True: print("determine double crossovers")
	doublecross = distances[0]*distances[1]/100.
	if debug is True: print("doublecross", doublecross*10, 'per 1000')

	if debug is True: print("determine parental type")
	types = ['+++', '++'+basetype[2], '+'+basetype[1]+'+', '+'+basetype[1]+basetype[2]]
	parental = random.choice(types)
	if debug is True: print("  ", parental, invertType(parental, basetype))
	type_counts = generateTypeCounts(parental, doublecross, basetype)
	typemap = generateProgenyData(types, type_counts, basetype)
	return typemap

def questionText(basetype):
	question_string = '  '
	question_string += '<p>Complete these sentences: '
	question_string += 'the distance between genes {0} and {1} is [{0}{1}]'.format(basetype[0].upper(),basetype[1].upper())
	question_string += ', '
	question_string += 'the distance between genes {0} and {1} is [{0}{1}]'.format(basetype[0].upper(),basetype[2].upper())
	question_string += ', and '
	question_string += 'the distance between genes {0} and {1} is [{0}{1}]'.format(basetype[1].upper(),basetype[2].upper())
	question_string += '. '
	question_string += 'From this the correct order of the genes is [gene_order].</p>'
	return question_string

def getVariables(basetype):
	variable_list = []
	variable = '{0}{1}'.format(basetype[0].upper(),basetype[1].upper())
	variable_list.append(variable)
	variable = '{0}{1}'.format(basetype[0].upper(),basetype[2].upper())
	variable_list.append(variable)
	variable = '{0}{1}'.format(basetype[1].upper(),basetype[2].upper())
	variable_list.append(variable)
	variable = 'gene_order'
	variable_list.append(variable)
	return variable_list


def blackboardFormat(question_string, html_table, variable_list, geneorder, distances):

	#FIB_PLUS TAB question text TAB variable1 TAB answer1 TAB answer2 TAB TAB variable2 TAB answer3
	blackboard = 'FIB_PLUS\t'
	#blackboard += html_table
	blackboard += question_string
	for i in range(len(variable_list)-1):
		blackboard += '\t{0}\t{1}\t'.format(variable_list[i], distances[i])
	blackboard += '\tgene_order\t{0}\t{1}\n'.format(geneorder, geneorder.upper())
	return blackboard

if __name__ == "__main__":
	lowercase = "abcdefghijklmnopqrstuvwxyz"

	filename = "bbq-three_point_test_cross.txt"
	f = open(filename, "w")
	duplicates = 4
	for i in range(duplicates):
		basetype = lowercase[i:i+3]
		geneorder = getGeneOrder(basetype)
		distances = getDistances()
		distances.append(0)
		print(distances)
		progeny_size = getProgenySize(distances)
		typemap = makeQuestion(basetype, geneorder, distances, progeny_size)
		ascii_table = makeProgenyAsciiTable(typemap, progeny_size)
		print(ascii_table)
		html_table = makeProgenyHtmlTable(typemap, progeny_size)
		#print(html_table)
		question_string = questionText(basetype)
		variable_list = getVariables(geneorder)

		final_question = blackboardFormat(question_string, html_table, variable_list, geneorder, distances)
		print(final_question)

		f.write(final_question)
	f.close()







#THE END

#!/usr/bin/env python

import re
import sys
import math
import copy
import random
import pprint

def list2string(mylist, spacer=""):
	mystring = ""
	for letter in mylist:
		mystring += letter + spacer
	return mystring

def list2text(mylist):
	mystring = ""
	if len(mylist) > 2:
		sublist = mylist[:-1]
		for letter in sublist:
			mystring += letter+", "
		mystring += "and "+mylist[-1]
	elif len(mylist) == 2:
		mystring = mylist[0]+" and "+mylist[1]
	return mystring

num2word = {
	1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
	6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
	11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
	15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
	20: 'twenty',
}

def cutChromosome(chromolist, cut):
	chromosome_A = []
	chromosome_B = []
	count = 0
	for item in chromolist:
		count += 1
		if count <= cut:
			chromosome_A.append(item)
		else:
			chromosome_B.append(item)
	return chromosome_A, chromosome_B

def drawChromosomeCut(chromolist, cut):
	mystr = ""
	count = 0
	for item in chromolist:
		count += 1
		mystr += item
		if count == cut:
			mystr += "|"
	return mystr

#====================
if __name__ == '__main__':
	if len(sys.argv) >= 2:
		num_items = int(sys.argv[1])
	else:
		num_items = 7
	if num_items < 4:
		print("Sorry, you must have at least 4 genes for this program")
		sys.exit(1)
	if num_items > 20:
		print("Sorry, you must have less than 20 genes for this program")
		sys.exit(1)

	charlist = list("ABCDEFGHJKMPQRSTWXYZ")

	chromosome1_size = random.randint(4, num_items)
	chromosome1 = charlist[:chromosome1_size]

	chromosome2_size = random.randint(4, num_items)
	chromosome2_shift = random.randint(chromosome1_size+1, len(charlist)-chromosome2_size)
	chromosome2 = charlist[chromosome2_shift:chromosome2_shift+chromosome2_size]

	chromosome1_cut = random.randint(1, chromosome1_size-1)
	chromosome2_cut = random.randint(1, chromosome2_size-1)
	print chromosome1_cut, chromosome2_cut

	print chromosome1, chromosome2
	print drawChromosomeCut(chromosome1, chromosome1_cut)
	print drawChromosomeCut(chromosome2, chromosome2_cut)

	chromosome1_A, chromosome1_B = cutChromosome(chromosome1, chromosome1_cut)
	chromosome2_A, chromosome2_B = cutChromosome(chromosome2, chromosome2_cut)

	answers = []
	answers.append( chromosome1_A + chromosome2_B )
	answers.append( chromosome2_A + chromosome1_B )
	answers.append( chromosome1_A + chromosome2_A[::-1] )
	answers.append( chromosome1_B[::-1] + chromosome2_B )
	
	
	#so many wrong answer to choose from, want a short answer
	if len(chromosome1_A) < len(chromosome1_B):
		chromosome_piece1 = chromosome1_A
	else:
		#make sure telomeres are on the left
		chromosome_piece1 = chromosome1_B[::-1]
	if len(chromosome2_A) < len(chromosome2_B):
		chromosome_piece2 = chromosome2_A
	else:
		#make sure telomeres are on the left
		chromosome_piece2 = chromosome2_B[::-1]

	### SPEND A LOT OF TIME TO CREATE A WRONG ANSWER:
	#now merge pieces for a wrong answer
	if random.random() < 0.5:
		if random.random() < 0.5:
			wrong_answer = chromosome_piece1 + chromosome_piece2
		else:
			wrong_answer = chromosome_piece1[::-1] + chromosome_piece2
	else:
		if random.random() < 0.5:
			wrong_answer = chromosome_piece2 + chromosome_piece1
		else:
			wrong_answer = chromosome_piece2[::-1] + chromosome_piece1

	answers.append(wrong_answer)

	print ""


# Two chromosomes with the gene sequences A B C D E and Q R S T U undergo a reciprocal translocation after
# breaks in C D and R S.
# Which one of the following is NOT a possible product of this translocation?

	sys.stderr.write("\n")
	sys.stderr.write("XXX. Two chromosomes with the gene sequences ")
	sys.stderr.write(list2string(chromosome1, ""))
	sys.stderr.write(" and ")
	sys.stderr.write(list2string(chromosome2, ""))
	sys.stderr.write(" undergo a reciprocal translocation after breaks between ")
	sys.stderr.write(chromosome1_A[-1] + "|" + chromosome1_B[0])
	sys.stderr.write(" and ")
	sys.stderr.write(chromosome2_A[-1] + "|" + chromosome2_B[0])
	sys.stderr.write(". Which one of the following is NOT a possible product of this translocation?")
	sys.stderr.write("\n")
	
	random.shuffle(answers)
	for i,a in enumerate(answers):
		sys.stderr.write(charlist[i] + ". ")
		if random.random() < 0.5:
			sys.stderr.write(list2string(a, ""))
		else:
			sys.stderr.write(list2string(a[::-1], "") )
		sys.stderr.write("\n")

	sys.stderr.write("\n")
	sys.exit(1)

	sys.stderr.write(("A total of %s genes "%(num2word[len(origlist)]))
		+list2text(sortedlist)+" are closely linked in a single chromosome, but "
		+"their order is unknown. ")
	sys.stderr.write(("A total of %s deletions in the region are found "%(num2word[len(del_set)]))
		+"to uncover recessive alleles of the genes as follows: ")
	for i,deletion in enumerate(del_set):
		sys.stderr.write("Deletion #%d uncovers the %s genes %s; "%(i+1, num2word[len(deletion)], list2text(deletion)))
	sys.stderr.write("What the correct order for the %s genes? "%(num2word[len(origlist)]))
	sys.stderr.write("Hint: the first gene on the end is gene %s.\n"%(origlist[0]))

	sys.stderr.write("\n")
	sys.stderr.write("Answer: %s\n"%(list2string(origlist)))
	sys.stderr.write("\n")

	#sys.stdout.write("Which one of the following is the correct order for the genes?")

	sys.stderr.write("##########\n")


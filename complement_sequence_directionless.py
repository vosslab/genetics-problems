#!/usr/bin/env python

import sys
import copy
import random

def complement(seq):
	newseq = copy.copy(seq)
	newseq = newseq.replace('A', 'x')
	newseq = newseq.replace('T', 'A')
	newseq = newseq.replace('x', 'T')
	newseq = newseq.replace('G', 'x')
	newseq = newseq.replace('C', 'G')
	newseq = newseq.replace('x', 'C')
	return newseq

def flip(seq):
	newseq = copy.copy(seq)
	return newseq[::-1]

if __name__ == '__main__':
	if len(sys.argv) >= 2:
		seqlen = int(sys.argv[1])
	else:
		seqlen = 8

	choices = []
	seq = ""
	for i in range(seqlen):
		seq += random.choice('AGCT')
	#choices.append(seq)
	choices.append(flip(seq))
	
	print("1. Which one of the following sequences is complimentary to the direction-less sequence <span style='font-family: monospace;'>%s</span>?"%(seq))
	answer = complement(seq)
	choices.append(answer)
	half = int(seqlen//2)
	#print compl
	if seq == answer:
		print("oops")
		sys.exit(1)

	nube = answer[:half] + seq[half:]
	choices.append(nube)
	nube = seq[:half] + answer[half:]
	choices.append(nube)
	nube = flip(seq)[:half] + seq[half:]
	choices.append(nube)

	random.shuffle(choices)
	charlist = "ABCDEF"
	for i in range(len(choices)):
		choice_msg = choices[i]
		letter = charlist[i]
		prefix = ""
		if choice_msg == answer:
			prefix = "*"
		print("%s%s. <span style='font-family: monospace;'>%s</span>"%(prefix, letter, choice_msg))
		
		
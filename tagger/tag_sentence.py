import re
import os
import subprocess

def getTaggedString(sentence):
	sentence_file = open('sentence_file', 'w')
	sentence_file.write(sentence)
	sentence_file.close()
	tagged_string_file = tagSentenceStructure("sentence_file")

	tagged_string_file = open(tagged_string_file, 'r')
	tagged_string = ""

	for line in tagged_string_file.readlines():
		tagged_string = tagged_string + line

	tagged_string_file.close()
	print tagged_string

	regex_match = re.findall(r'(\S+)/(\S+)', tagged_string)
	if regex_match:
		words_and_types = process(regex_match)

		# check result
		for item in words_and_types.keys():
			print item
			print words_and_types[item]

	return words_and_types

def process(matched):
	words_and_types = {}
	for group in matched:
		word = group[0]
		tag = group[1]
		
		# check if words_and_types contains tag
		# if yes: add word to array
		# if no: create new key and array
		if (not(words_and_types.has_key(tag))):
			words_and_types[tag] = []		
		words_and_types[tag].append(word)

	return words_and_types


def tagSentenceStructure(sentence_file_name):
	f = open(r'output.txt', 'w')
	subprocess.call(["javac", "-cp", "stanford-postagger.jar", "TaggerDemo.java"])
	subprocess.call(["java", "-cp", """.:stanford-postagger.jar""", "TaggerDemo", "models/english-left3words-distsim.tagger", sentence_file_name], stdout = f)
	f.close()
	return 'output.txt'
	# print java_output.stdout




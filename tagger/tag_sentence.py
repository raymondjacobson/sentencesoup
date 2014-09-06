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
		process(regex_match)
	return 0

def process(matched):
	for group in matched:
		word = group[0]
		tag = group[1]
		print word + ", " + tag


def tagSentenceStructure(sentence_file_name):
	f = open(r'output.txt', 'w')
	subprocess.call(["javac", "-cp", "stanford-postagger.jar", "TaggerDemo.java"])
	subprocess.call(["java", "-cp", """.:stanford-postagger.jar""", "TaggerDemo", "models/english-left3words-distsim.tagger", "sample-input.txt"], stdout = f)
	f.close()
	return 'output.txt'
	# print java_output.stdout




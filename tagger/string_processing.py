import get_concepts
import tag_sentence
import subprocess

def setup():
	subprocess.call(["python", "alchemyapi.py", "60405a74657ccbaac0dd1663c86a2ce0fc143bb1"])

def processSentences(array_of_sentences):
	parts_of_sentences_names = [
		'conjunction',
		'preposition',
		'adjective',
		'noun',
		'pronoun',
		'adverb',
		'to',
		'interjection',
		'verb',
		'wh',
		'cardinal_number',
		'determiner',
		'symbol'
	]

	# Define types for each data structure
	parts_of_sentences_types_general = {
		'conjunction' : ["CC"],
		'preposition' : ["IN"],
		'adjective' : ["JJ", "JJR", "JJS"],
		'noun' : ["NN", "NNS", "NNP", "NNPS"],
		'pronoun' : ["PRP, PRP$"],
		'adverb' : ["RB", "RBR", "RBS"],
		'to' : ["TO"],
		'interjection' : ["UH"],
		'verb' : ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
		'wh' : ["WDT", "WP", "WP$", "WRB"],
		'cardinal_number' : ["CD"],
		'determiner' : ["DT"],
		'symbol' : ["SYM"]
	}

	# print parts_of_sentences_names

	# Define data structures
	parts_of_sentences = {}
	for i in  range(0, len(parts_of_sentences_names)):
		parts_of_sentences[parts_of_sentences_names[i]] = {}

	# print parts_of_sentences

	parts_of_sentences_types = {}
	for i in range(0, len(parts_of_sentences_names)):
		parts_of_sentences_types[parts_of_sentences_names[i]] = parts_of_sentences_types_general[parts_of_sentences_names[i]]
	# print parts_of_sentences_types

	# Get concepts of of each sentence 
	for sentence in array_of_sentences:
		concepts = get_concepts.getConceptOfString(sentence)

		# get concept of concepts
		array_of_concepts = []
		for concept in concepts:
			temp_array_of_concepts = get_concepts.getConceptOfString(concept)
			for item in temp_array_of_concepts:
				if (not(item in array_of_concepts) and not(item in concepts)):
					array_of_concepts.append(item)

		concepts += array_of_concepts

		print "concepts: "
		print concepts

		types_and_words = tag_sentence.getTaggedString(sentence)

		print "types_and_words: "
		print types_and_words

		# add words to correct type
		for concept in concepts:
			for sentence_type in parts_of_sentences.keys():
				for tag in parts_of_sentences_types[sentence_type]:
					if (types_and_words.has_key(tag)):
						if not(parts_of_sentences[sentence_type].has_key(concept)):
							parts_of_sentences[sentence_type][concept] = []
						parts_of_sentences[sentence_type][concept] += types_and_words[tag]


		print "parts_of_sentences: "
		for key in parts_of_sentences.keys():
			for concept in concepts:
				if parts_of_sentences[key].has_key(concept):
				# if len(parts_of_sentences[key][concept]) > 0:
					print key + ", " + concept
					print parts_of_sentences[key][concept]
				 



# main
two_sentences = ["the dog climbed a tree in the forest in africa"]
processSentences(two_sentences)

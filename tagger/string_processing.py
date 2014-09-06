import get_concepts
import tag_sentence

def processSentences(array_of_sentences):
	# Define data structures
	conjunction = {}
	preposition = {}
	adjective = {}
	noun = {}
	pronoun = {}
	adverb = {}
	to = {}
	interjection = {}
	verb = {}
	wh = {}
	other = {}
	cardinal_number = {}
	detiminer = {}
	symbol = {}


	# Get concepts of of each sentence 
	for sentence in array_of_sentences:
		concepts = get_concepts.getConceptOfString(sentence)

		print "concepts of " + sentence + " before: " 
		print concepts

		# get concept of concepts
		array_of_concepts = []
		for concept in concepts:
			temp_array_of_concepts = get_concepts.getConceptOfString(concept)
			for item in temp_array_of_concepts:
				if (not(item in array_of_concepts) and not(item in concepts)):
					array_of_concepts.append(item)

		concepts += array_of_concepts
		print "concepts of " + sentence + " after: " 
		print concepts

		# add new concepts to list of concepts
		# print concepts
		# for concept_list in array_of_concepts:
		# 	for concept_item in concept_list:
		# 		if (!concept_item in concepts):
		# 			print concept_item
		# 			concepts.append(concept_item)


# main
two_sentences = ["a dog went to the park", "a cat went up a tree", "go to the library to get a book about africa"]
processSentences(two_sentences)

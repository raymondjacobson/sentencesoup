import unirest
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()
import json

def getConceptOfSentence(sentence):
	concepts_of_sentence = []
	response = alchemyapi.concepts('text', sentence)
	if response['status'] == 'OK':
		for concept in response['concepts']:
			print concept['text']
			concepts_of_sentence.append(concept['text'].encode('ascii'))
	
	return concepts_of_sentence

#main
concepts_of_sentence = getConceptOfSentence("Go to the library to get a book")
print concepts_of_sentence
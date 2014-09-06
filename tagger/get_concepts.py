import unirest
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()
import json

def getConceptOfString(string):
	print "string in getConceptOfString: " + string
	concepts_of_string = []
	response = alchemyapi.concepts('text', string)
	if response['status'] == 'OK':
		for concept in response['concepts']:
			concepts_of_string.append(concept['text'].encode('ascii'))
	
	return concepts_of_string


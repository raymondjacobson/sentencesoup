from firebase import firebase
firebase = firebase.FirebaseApplication('https://sentencesoup.firebaseio.com', None)
result = firebase.post('/users', None, {'word': 'firstWord'});
print result
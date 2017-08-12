from firebase import firebase
import pickle
import json

url = "https://pyretest-458c7.firebaseio.com"
firebase = firebase.FirebaseApplication(url, None)

class Model:

	instanceVar = 4

	def __init__(self):
		raise NotImplementedError("Must use a subclass")

	def save(self):

		childName = "/" + self.__class__.__name__

		result = firebase.post(childName, self.getJson())
		print(result)

	def getJson(self):

		self.objects = {"helloString": "world", "otherInt": 5}

		d = dict()
		for name, value in self.objects.items():
			d[name] = pickle.dumps(value).decode('latin1')

		return json.dumps(d)

class Question(Model):

	def __init__(self):

		self.save()


if (__name__ == "__main__"):

	x = Question()

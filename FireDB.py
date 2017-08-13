import pickle
import pyrebase

config = {
  "apiKey": "AIzaSyDFlKD3vfQ0_K8HMqjRXactwlEmzSBdYys",
  "authDomain": "pyretest-458c7.firebaseapp.com",
  "databaseURL": "https://pyretest-458c7.firebaseio.com",
  "storageBucket": "pyretest-458c7.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

class Field:

	def __init__(self, **kwargs):
		self.setValue(None)

	def setValue(self, new):
		self.storedValue = new

	def getValue(self):
		return self.storedValue

class Model:

	def __init__(self, **kwargs):
		
		fields = self._getFieldDict()

		import pdb; pdb.set_trace()

		for name, value in kwargs.items():
			fields[name].setValue(value)

	def save(self):

		child = db.child(self.__class__.__name__)
		fields = self._getFieldDict()

		pickleAndDecode = lambda obj: pickle.dumps(obj).decode('latin1')
		unwrapAndPickle = lambda obj: pickleAndDecode(obj.getValue())

		pickleDict = { n : unwrapAndPickle(v) for n, v in fields.items() }
		res = child.set(pickleDict)

	def _getFieldDict(self):

		isField = lambda obj : (obj.__class__.__name__ == "Field")
		values = { v : getattr(self, v) for v in dir(self) }
		fields = { k : v for k, v in values.items() if isField(v) }




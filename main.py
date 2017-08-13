from models import Question

def main():

	x = Question(idee = "Hello", questionText = "World", answerText = "Russia")
	x.save()

main()
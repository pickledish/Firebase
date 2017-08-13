from FireDB import Model, Field

class Question(Model):

	idee = Field(null = False, default = 5)
	questionText = Field(null = False)
	answerText = Field()